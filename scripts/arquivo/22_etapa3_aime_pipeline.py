"""Pipeline da Etapa 3 sobre AIME (Latour 2013).

Aplica em sequencia sobre corpus/txt_norm/latour_2013_aime_en.txt:

- Catalogo antigo (catalogo_termos.yaml + adicoes textil/topologia da
  Etapa 2): 19 campos figurativos.
- Catalogo novo (catalogo_termos_aime.yaml): 12 campos especificos de
  AIME, aplicado apenas nesta obra.

Gera kwic.csv e frequencias.csv para cada catalogo, plus tabela
comparativa 6 obras (estende tabela_comparativa_5_obras.tex com AIME)
e tabela do catalogo novo.

Uso:
    python scripts/22_etapa3_aime_pipeline.py
"""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
from _paths import obra_dir

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_TXT = REPO_ROOT / "corpus" / "txt_norm" / "latour_2013_aime_en.txt"
OUT_OBRA = REPO_ROOT / "outputs" / "etapa3" / "latour_2013_aime_en"
OUT_ETAPA3 = REPO_ROOT / "outputs" / "etapa3" / "consolidado"
CATALOGO_YAML = REPO_ROOT / "campos_lexicais" / "catalogo_termos.yaml"
CATALOGO_AIME = REPO_ROOT / "campos_lexicais" / "catalogo_termos_aime.yaml"
ADICOES = [
    REPO_ROOT / "campos_lexicais" / "latour_textil_en_etapa2_adicoes.txt",
    REPO_ROOT / "campos_lexicais" / "latour_topologia_en_etapa2_adicoes.txt",
]

# Carrega funcoes de 02_kwic.py
spec = importlib.util.spec_from_file_location(
    "kwic_mod", REPO_ROOT / "scripts" / "02_kwic.py"
)
kwic_mod = importlib.util.module_from_spec(spec)
sys.modules["kwic_mod"] = kwic_mod
spec.loader.exec_module(kwic_mod)

PALAVRAS_AIME = 194454  # contagem split pos-normalizacao (vide normalizacao_aplicada.md)


def carregar_catalogo_yaml(path: Path) -> list[kwic_mod.GrupoTermo]:
    import yaml
    dados = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    grupos: list[kwic_mod.GrupoTermo] = []
    for autor, conteudo in dados.items():
        if not isinstance(conteudo, dict):
            continue
        for grupo, meta in conteudo.items():
            termos = tuple(t.strip() for t in (meta.get("termos") or []) if t.strip())
            exclusoes = tuple(e.strip() for e in (meta.get("exclusoes") or []) if e.strip())
            nota = (meta.get("nota") or "").strip()
            if not termos:
                continue
            grupos.append(kwic_mod.GrupoTermo(
                autor=autor, grupo=grupo, termos=termos,
                exclusoes=exclusoes, nota=nota,
            ))
    return grupos


def kwic_aime(
    grupos: list[kwic_mod.GrupoTermo],
    saida_csv: Path,
    janela: int = 10,
) -> dict[str, int]:
    """Roda KWIC sobre AIME, com filtro de autor='latour'."""
    grupos = [g for g in grupos if g.autor == "latour"]
    texto = kwic_mod.ler_texto_sem_cabecalho(CORPUS_TXT)
    palavras = kwic_mod.localizar_palavras(texto)
    separadores = [m.start() for m in re.finditer(r"\f", texto)]

    saida_csv.parent.mkdir(parents=True, exist_ok=True)
    cabecalho = [
        "obra", "autor_yaml", "grupo", "termo_encontrado",
        "pagina", "posicao_no_texto",
        "contexto_antes", "trecho_central", "contexto_depois",
        "descartado_por_exclusao",
    ]
    n_grupo: dict[str, int] = {g.grupo: 0 for g in grupos}
    n_excl: dict[str, int] = {g.grupo: 0 for g in grupos}
    variantes_por_grupo: dict[str, Counter] = {g.grupo: Counter() for g in grupos}

    JANELA_EXCLUSAO = kwic_mod.JANELA_EXCLUSAO_PALAVRAS

    with saida_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cabecalho)
        w.writeheader()
        for grupo in grupos:
            padrao = kwic_mod.compilar_padrao(grupo.termos)
            padrao_exc = kwic_mod.compilar_exclusoes(grupo.exclusoes)
            for match in padrao.finditer(texto):
                antes, central, depois, _, _ = kwic_mod.janela_kwic(
                    texto, palavras, match.start(), match.end(), janela,
                )
                descartado = False
                if padrao_exc is not None:
                    idx_ini = kwic_mod._indice_palavra(palavras, match.start())
                    idx_fim = kwic_mod._indice_palavra(palavras, match.end() - 1)
                    janela_exc_antes = kwic_mod._trecho_palavras(
                        texto, palavras,
                        max(0, idx_ini - JANELA_EXCLUSAO), idx_ini,
                    )
                    janela_exc_depois = kwic_mod._trecho_palavras(
                        texto, palavras,
                        idx_fim + 1,
                        min(len(palavras), idx_fim + 1 + JANELA_EXCLUSAO),
                    )
                    janela_check = kwic_mod._normalizar(
                        f"{janela_exc_antes} {central} {janela_exc_depois}"
                    )
                    if padrao_exc.search(janela_check):
                        descartado = True
                        n_excl[grupo.grupo] += 1
                w.writerow({
                    "obra": "latour_2013_aime_en",
                    "autor_yaml": grupo.autor,
                    "grupo": grupo.grupo,
                    "termo_encontrado": central.lower(),
                    "pagina": kwic_mod.estimar_pagina(match.start(), separadores),
                    "posicao_no_texto": match.start(),
                    "contexto_antes": antes,
                    "trecho_central": central,
                    "contexto_depois": depois,
                    "descartado_por_exclusao": int(descartado),
                })
                if not descartado:
                    n_grupo[grupo.grupo] += 1
                    variantes_por_grupo[grupo.grupo][central.lower()] += 1

    return {
        "n_grupo": n_grupo,
        "n_excl": n_excl,
        "variantes_top": {g: variantes_por_grupo[g].most_common(5) for g in n_grupo},
    }


def gerar_frequencias_csv(
    saida_csv: Path,
    resultado: dict,
    palavras_total: int,
) -> None:
    saida_csv.parent.mkdir(parents=True, exist_ok=True)
    n_grupo = resultado["n_grupo"]
    n_excl = resultado["n_excl"]
    variantes_top = resultado["variantes_top"]
    with saida_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["grupo", "n_ocorrencias", "n_excluidas",
                    "frequencia_por_10k_palavras", "variantes_top"])
        for g in sorted(n_grupo, key=lambda x: -n_grupo[x]):
            n = n_grupo[g]
            freq = n / palavras_total * 10000 if palavras_total else 0
            var = ", ".join(f"{v}({k})" for v, k in variantes_top[g])
            w.writerow([g, n, n_excl.get(g, 0), f"{freq:.2f}", var])


def gerar_relatorio_md(catalogo_antigo: dict, catalogo_aime: dict) -> None:
    md = OUT_OBRA / "relatorios" / "frequencias.md"
    md.parent.mkdir(parents=True, exist_ok=True)
    linhas: list[str] = [
        "# Frequências figurativas em AIME (Latour, 2013)",
        "",
        f"Palavras totais (split, pós-normalização): **{PALAVRAS_AIME:,}**.".replace(",", "."),
        "Janela KWIC: ±10 palavras. Dois catálogos aplicados.",
        "",
        "## Catálogo antigo (19 campos das Etapas 1 e 2)",
        "",
        "| grupo | n | excl | freq./10k | variantes top |",
        "|---|---:|---:|---:|---|",
    ]
    n_grupo_a = catalogo_antigo["n_grupo"]
    n_excl_a = catalogo_antigo["n_excl"]
    var_a = catalogo_antigo["variantes_top"]
    for g in sorted(n_grupo_a, key=lambda x: -n_grupo_a[x]):
        n = n_grupo_a[g]
        e = n_excl_a.get(g, 0)
        freq = n / PALAVRAS_AIME * 10000
        var = ", ".join(f"`{v}` ({k})" for v, k in var_a[g][:4])
        linhas.append(f"| {g} | {n} | {e} | {freq:.2f} | {var} |")

    linhas += [
        "",
        "## Catálogo novo de AIME (12 campos específicos)",
        "",
        "| grupo | n | excl | freq./10k | variantes top |",
        "|---|---:|---:|---:|---|",
    ]
    n_grupo_b = catalogo_aime["n_grupo"]
    n_excl_b = catalogo_aime["n_excl"]
    var_b = catalogo_aime["variantes_top"]
    for g in sorted(n_grupo_b, key=lambda x: -n_grupo_b[x]):
        n = n_grupo_b[g]
        e = n_excl_b.get(g, 0)
        freq = n / PALAVRAS_AIME * 10000
        var = ", ".join(f"`{v}` ({k})" for v, k in var_b[g][:4])
        linhas.append(f"| {g} | {n} | {e} | {freq:.2f} | {var} |")
    md.write_text("\n".join(linhas), encoding="utf-8")
    print(f"  gravado: {md.relative_to(REPO_ROOT)}")


def gerar_tabela_6_obras(catalogo_antigo: dict) -> None:
    """Tabela LaTeX comparativa 6 obras x 19 campos."""
    ORDEM_OBRAS = [
        ("latour_woolgar_1986_lab_life_en", r"\emph{Lab Life} (1986)", 105749),
        ("latour_1987_science_action_en", r"\emph{Sci. Action} (1987)", 139861),
        ("latour_1999_pandora_en", r"\emph{Pandora} (1999)", 128001),
        ("latour_1996_clarifications_en", r"\emph{Clarifications} (1996)", 7848),
        ("latour_1999_recalling_bis", r"\emph{Recalling} (1999b)", 4825),
        ("latour_2013_aime_en", r"\emph{AIME} (2013)", PALAVRAS_AIME),
    ]
    ORDEM_GRUPOS = [
        "inscription", "immutable_mobile", "black_box", "centre_of_calculation",
        "actor_network", "translation", "trial_of_strength", "factish",
        "circulating_reference", "articulation", "construction", "proposition",
        "network", "agonistic", "enrollment", "spokesperson", "militar",
        "textil", "topologia",
    ]
    # Carrega frequencias.csv de cada obra
    contagens: dict[str, dict[str, int]] = {}
    for oid, _, _ in ORDEM_OBRAS:
        if oid == "latour_2013_aime_en":
            contagens[oid] = catalogo_antigo["n_grupo"]
            continue
        p = obra_dir(oid) /  "csv" / "frequencias.csv"
        c = {}
        if p.exists():
            with p.open(encoding="utf-8", newline="") as f:
                for row in csv.DictReader(f):
                    c[row["grupo"]] = int(row["n_ocorrencias"])
        contagens[oid] = c

    linhas = [
        r"% Tabela comparativa 6 obras (Etapa 3: AIME 2013 adicionado).",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Densidade dos 19 campos figurativos nas tres obras "
        r"monograficas, nos dois artigos metateoricos e em AIME 2013 "
        r"(ocorrencias por 10.000 palavras; contagem absoluta entre "
        r"parenteses). Recalling em versao bis (corpus integral) da Etapa "
        r"2-bis. AIME da Etapa 3.}",
        r"\label{tab:figuracoes_latour_6_obras}",
        r"\scriptsize",
        r"\begin{tabular}{l" + "r" * len(ORDEM_OBRAS) + r"}",
        r"\toprule",
    ]
    cab = [r"Campo"] + [rotulo for _, rotulo, _ in ORDEM_OBRAS]
    linhas.append(" & ".join(cab) + r" \\")
    linhas.append(r"\midrule")
    pal_linha = [r"\textit{Palavras}"]
    for _, _, pal in ORDEM_OBRAS:
        pal_linha.append(rf"\textit{{{pal:,}}}".replace(",", r"\,"))
    linhas.append(" & ".join(pal_linha) + r" \\")
    linhas.append(r"\midrule")
    for g in ORDEM_GRUPOS:
        celulas = [g.replace("_", r"\_")]
        for oid, _, pal in ORDEM_OBRAS:
            n = contagens[oid].get(g, 0)
            if n > 0:
                freq = n / pal * 10000
                celulas.append(rf"{freq:.2f} ({n})".replace(".", "{,}", 1))
            else:
                celulas.append(r"--")
        linhas.append(" & ".join(celulas) + r" \\")
    linhas += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]

    p_out = OUT_ETAPA3 / "tabela_comparativa_6_obras.tex"
    p_out.parent.mkdir(parents=True, exist_ok=True)
    p_out.write_text("\n".join(linhas), encoding="utf-8")
    print(f"  gravado: {p_out.relative_to(REPO_ROOT)}")


def gerar_tabela_aime_novo(catalogo_aime: dict) -> None:
    """Tabela LaTeX dos 12 campos novos em AIME."""
    n_grupo = catalogo_aime["n_grupo"]
    n_excl = catalogo_aime["n_excl"]

    linhas = [
        r"% Tabela dos 12 campos novos especificos de AIME (Etapa 3).",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Densidade dos 12 campos figurativos novos identificados "
        r"em AIME 2013 (catalogo aplicado apenas nesta obra). Ocorrencias "
        r"por 10.000 palavras em " + f"{PALAVRAS_AIME:,}".replace(",", r"\,") +
        r" palavras de corpo; contagem absoluta entre parenteses.}",
        r"\label{tab:aime_catalogo_novo}",
        r"\small",
        r"\begin{tabular}{lrr}",
        r"\toprule",
        r"Campo & $n$ & freq./10k \\",
        r"\midrule",
    ]
    for g in sorted(n_grupo, key=lambda x: -n_grupo[x]):
        n = n_grupo[g]
        freq = n / PALAVRAS_AIME * 10000
        linhas.append(rf"{g.replace('_', chr(92)+'_')} & {n} & {freq:.2f} \\".replace(".", "{,}", 1) if freq else
                      rf"{g.replace('_', chr(92)+'_')} & {n} & --")
    linhas += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]

    p_out = OUT_ETAPA3 / "tabela_aime_catalogo_novo.tex"
    p_out.parent.mkdir(parents=True, exist_ok=True)
    p_out.write_text("\n".join(linhas), encoding="utf-8")
    print(f"  gravado: {p_out.relative_to(REPO_ROOT)}")


def main() -> None:
    print("== Etapa 3 passo 4: contagem bruta em AIME ==\n")

    # Catalogo antigo + adicoes textil/topologia
    grupos_antigo = kwic_mod.carregar_catalogo()
    grupos_antigo = grupos_antigo + kwic_mod.carregar_adicoes(ADICOES)
    print(f"Catalogo antigo: {len(grupos_antigo)} grupos (catalogo_termos.yaml + adicoes).")
    kwic_csv_antigo = OUT_OBRA / "csv" / "kwic_catalogo_antigo.csv"
    res_antigo = kwic_aime(grupos_antigo, kwic_csv_antigo)
    print(f"  gravado: {kwic_csv_antigo.relative_to(REPO_ROOT)} "
          f"({sum(res_antigo['n_grupo'].values())} ocorrencias)")
    freq_csv_antigo = OUT_OBRA / "csv" / "frequencias_catalogo_antigo.csv"
    gerar_frequencias_csv(freq_csv_antigo, res_antigo, PALAVRAS_AIME)
    print(f"  gravado: {freq_csv_antigo.relative_to(REPO_ROOT)}")

    # Catalogo novo de AIME
    print()
    grupos_aime = carregar_catalogo_yaml(CATALOGO_AIME)
    print(f"Catalogo AIME: {len(grupos_aime)} grupos (catalogo_termos_aime.yaml).")
    kwic_csv_aime = OUT_OBRA / "csv" / "kwic_catalogo_aime.csv"
    res_aime = kwic_aime(grupos_aime, kwic_csv_aime)
    print(f"  gravado: {kwic_csv_aime.relative_to(REPO_ROOT)} "
          f"({sum(res_aime['n_grupo'].values())} ocorrencias)")
    freq_csv_aime = OUT_OBRA / "csv" / "frequencias_catalogo_aime.csv"
    gerar_frequencias_csv(freq_csv_aime, res_aime, PALAVRAS_AIME)
    print(f"  gravado: {freq_csv_aime.relative_to(REPO_ROOT)}")

    # Relatorio MD e tabelas
    print()
    gerar_relatorio_md(res_antigo, res_aime)
    gerar_tabela_6_obras(res_antigo)
    gerar_tabela_aime_novo(res_aime)


if __name__ == "__main__":
    main()
