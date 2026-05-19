"""Migra classificacoes manuais da Etapa 2.6 para a planilha bis do Recalling.

Para a Etapa 2-bis, refaz a amostragem A/B/C dos quatro campos (textil,
topologia, network, actor_network) sobre o corpus integral do Recalling.
Como ha agora muito mais ocorrencias do que na Etapa 2 original (96 vs
22 no Recalling), o protocolo A/B/C completo aplica-se aos campos com
mais de 15 ocorrencias; os demais ficam exaustivos.

Para cada ocorrencia nova:
- Se for a mesma ocorrencia (mesmo termo + mesmo trecho_central) que ja
  existia na Etapa 2.6 e foi classificada, migra a classificacao.
- Caso contrario, deixa em branco para preenchimento manual futuro.

A planilha original PREENCHIDA da Etapa 2.6 fica intocada.
"""

from __future__ import annotations

import csv
import random
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = REPO_ROOT / "outputs"
ETAPA2BIS_DIR = OUTPUTS_DIR / "etapa2bis" / "consolidado"
ETAPA2BIS_RECALLING = OUTPUTS_DIR / "etapa2bis" / "recalling_extras"

PREENCHIDA_2_6 = OUTPUTS_DIR / "etapa2" / "consolidado" / "validacao_amostral_semantica_PREENCHIDA_CORRIGIDA.csv"
KWIC_BIS = OUTPUTS_DIR / "etapa2bis" / "latour_1999_recalling_bis" / "csv" / "kwic.csv"

CAMPOS = ["textil", "topologia", "network", "actor_network"]
N_POR_CAMADA = 5
SEED = 42

CABECALHO = [
    "obra", "campo", "camada", "id_kwic",
    "pagina", "termo_encontrado",
    "contexto_antes", "trecho_central", "contexto_depois",
    "uso_figural", "subcategoria", "comentario",
]


def carregar_classificacoes_existentes() -> dict[tuple[str, str, str], dict[str, str]]:
    """Indexa as classificacoes preenchidas da Etapa 2.6 por
    (campo, termo_encontrado_lower, trecho_central_lower)."""
    idx: dict[tuple[str, str, str], dict[str, str]] = {}
    if not PREENCHIDA_2_6.exists():
        return idx
    with PREENCHIDA_2_6.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if "recalling" not in row["obra"]:
                continue
            chave = (
                row["campo"],
                row["termo_encontrado"].strip().lower(),
                row["trecho_central"].strip().lower(),
            )
            idx[chave] = row
    return idx


def carregar_kwic_bis(campo: str) -> list[dict[str, str]]:
    saida: list[dict[str, str]] = []
    with KWIC_BIS.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("grupo") != campo:
                continue
            if row.get("descartado_por_exclusao") == "1":
                continue
            saida.append(row)
    return saida


def densidade(row: dict[str, str], todos: set[str]) -> int:
    janela = (
        f"{row['contexto_antes']} {row['trecho_central']} {row['contexto_depois']}"
    ).lower()
    return sum(1 for t in todos if t in janela)


def amostrar(ocs: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    if len(ocs) < 3 * N_POR_CAMADA:
        return {"exaustiva": list(ocs)}
    todos = {r["termo_encontrado"].lower() for r in ocs}
    por_densidade = sorted(ocs, key=lambda r: -densidade(r, todos))
    a = por_densidade[:N_POR_CAMADA]
    rng = random.Random(SEED)
    cand_b = [r for r in ocs if r not in a]
    b = rng.sample(cand_b, min(N_POR_CAMADA, len(cand_b)))
    freq = Counter(r["termo_encontrado"].lower() for r in ocs)
    raras = sorted(freq.items(), key=lambda x: x[1])
    variantes_raras = {v for v, _ in raras[:max(1, len(raras) // 3)]}
    cand_c = [r for r in ocs if r["termo_encontrado"].lower() in variantes_raras
              and r not in a and r not in b]
    if len(cand_c) < N_POR_CAMADA:
        extras = [r for r in ocs if r not in a and r not in b and r not in cand_c]
        extras = sorted(extras, key=lambda r: freq[r["termo_encontrado"].lower()])
        cand_c = cand_c + extras
    c = cand_c[:N_POR_CAMADA]
    return {"A_top_densidade": a, "B_aleatoria": b, "C_variantes_raras": c}


def main() -> None:
    ETAPA2BIS_DIR.mkdir(parents=True, exist_ok=True)
    ETAPA2BIS_RECALLING.mkdir(parents=True, exist_ok=True)

    idx_existentes = carregar_classificacoes_existentes()

    saida: list[dict[str, str]] = []
    contagens_migracao: dict[str, int] = {"migradas": 0, "novas": 0}

    for campo in CAMPOS:
        ocs = carregar_kwic_bis(campo)
        amostra = amostrar(ocs)
        for camada, rows in amostra.items():
            for i, row in enumerate(rows):
                offset = int(row["posicao_no_texto"])
                id_kwic = f"latour_1999_recalling_bis#{campo}#pos_{offset:06d}"
                # Casamento por (campo, termo, trecho central) com Etapa 2.6
                chave = (campo, row["termo_encontrado"].strip().lower(),
                         row["trecho_central"].strip().lower())
                ja = idx_existentes.get(chave)
                if ja:
                    contagens_migracao["migradas"] += 1
                    uso_figural = ja.get("uso_figural", "")
                    subcategoria = ja.get("subcategoria", "")
                    comentario = (ja.get("comentario", "") +
                                  " [migrado da Etapa 2.6]").strip()
                else:
                    contagens_migracao["novas"] += 1
                    uso_figural = ""
                    subcategoria = ""
                    comentario = ""
                saida.append({
                    "obra": "latour_1999_recalling_bis",
                    "campo": campo,
                    "camada": camada,
                    "id_kwic": id_kwic,
                    "pagina": row.get("pagina", ""),
                    "termo_encontrado": row.get("termo_encontrado", ""),
                    "contexto_antes": row.get("contexto_antes", ""),
                    "trecho_central": row.get("trecho_central", ""),
                    "contexto_depois": row.get("contexto_depois", ""),
                    "uso_figural": uso_figural,
                    "subcategoria": subcategoria,
                    "comentario": comentario,
                })

    p = ETAPA2BIS_RECALLING / "validacao_amostral_semantica.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CABECALHO)
        w.writeheader()
        w.writerows(saida)
    print(f"gravado: {p.relative_to(REPO_ROOT)} ({len(saida)} linhas)")
    print(f"  migradas da Etapa 2.6: {contagens_migracao['migradas']}")
    print(f"  novas (em branco): {contagens_migracao['novas']}")

    # Relatorio side-by-side
    md = ETAPA2BIS_DIR / "validacao_amostral_migracao.md"
    linhas = [
        "# Migração da validação amostral A/B/C: Etapa 2.6 → Etapa 2-bis",
        "",
        "Data: 2026-05-15.",
        "",
        f"Total de linhas na nova planilha: **{len(saida)}**.",
        f"- Linhas migradas da Etapa 2.6 (mesma ocorrência, mesma classificação): **{contagens_migracao['migradas']}**.",
        f"- Linhas novas (ficam em branco para preenchimento manual): **{contagens_migracao['novas']}**.",
        "",
        "## Distribuição por campo e camada",
        "",
        "| Campo | Camada | n na 2-bis | migradas | novas |",
        "|---|---|---:|---:|---:|",
    ]
    por_camada: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for r in saida:
        por_camada[(r["campo"], r["camada"])].append(r)
    for (campo, camada), rows in sorted(por_camada.items()):
        n = len(rows)
        n_mig = sum(1 for r in rows if r["uso_figural"])
        n_nov = n - n_mig
        linhas.append(f"| {campo} | {camada} | {n} | {n_mig} | {n_nov} |")

    linhas += [
        "",
        "## Procedimento de casamento",
        "",
        "O casamento entre ocorrência da Etapa 2.6 e ocorrência da Etapa 2-bis "
        "foi feito pela chave composta (`campo` + `termo_encontrado` + "
        "`trecho_central`), normalizados a minúsculas. O casamento por offset "
        "absoluto seria mais preciso mas inaplicável aqui, porque o `.txt` "
        "normalizado mudou (passou de 1.241 para 4.825 palavras), o que altera "
        "todos os offsets em caracteres. A chave por trecho central é estável a "
        "essa renormalização.",
        "",
        "## Pendência",
        "",
        f"As **{contagens_migracao['novas']} linhas novas** ficam com colunas "
        "`uso_figural`, `subcategoria` e `comentario` em branco. Aguardam "
        "preenchimento manual da pesquisadora em sessão futura. Após o "
        "preenchimento, regerar `validacao_amostral_resultados.md` "
        "consolidando a Etapa 2-bis.",
    ]
    md.write_text("\n".join(linhas), encoding="utf-8")
    print(f"gravado: {md.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
