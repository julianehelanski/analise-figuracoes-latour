"""Normalização pré-KWIC dos textos extraídos.

Implementa o Adendo 1 (14/05/2026) das decisões metodológicas. Lê as
extrações cruas em `corpus/txt/<id>.txt` e grava versão normalizada em
`corpus/txt_norm/<id>.txt`. Regenera `corpus/paginas/<id>.csv` e
`corpus/qualidade_extracao.csv` a partir da versão normalizada usando as
mesmas heurísticas de `01_extract_text.py`.

Operações, na ordem:

1. Remoção de soft hyphen U+00AD (afeta sobretudo Pandora's Hope).
2. De-hifenização de fim de linha (`infor-\\nmation` -> `information`).
3. Remoção de marcadores ((NN)) injetados pelo conversor (afeta Science
   in Action).
4. Descarte de linhas com cabeçalho de letras espaçadas (afeta Pandora).
5. NFKC e mapeamento de aspas tipográficas/travessões para ASCII.
6. Substituição de replacement chars (\\ufffd) por espaço.

O separador de página \\f é preservado em todas as operações.

Uso:
    python scripts/01b_normalize_text.py
    python scripts/01b_normalize_text.py --only latour_1987
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
METADATA_CSV = REPO_ROOT / "corpus" / "metadata.csv"
CORPUS_TXT_DIR = REPO_ROOT / "corpus" / "txt"
CORPUS_TXT_NORM_DIR = REPO_ROOT / "corpus" / "txt_norm"
PAGINAS_DIR = REPO_ROOT / "corpus" / "paginas"
QUALIDADE_CSV = REPO_ROOT / "corpus" / "qualidade_extracao.csv"

# Regexes principais ---------------------------------------------------------- #

_RE_SOFT_HYPHEN = re.compile("­")
_RE_HYPH_EOL = re.compile(r"-\n(?=[a-zA-Z])")
_RE_PARENS_MARKER = re.compile(r"\(\(\d+\)\)")
# Linha de cabeçalho com letras únicas separadas por espaço, e.g.:
# "P A N D O R A ' S   H O P E" — exige pelo menos 6 caracteres únicos em sequência.
_RE_HEADER_SPACED = re.compile(
    r"^\s*(?:[A-Za-z'’]\s+){5,}[A-Za-z'’]\s*$", re.MULTILINE,
)

_MAP_PONTUACAO = str.maketrans({
    "‘": "'", "’": "'",  # aspas simples tipográficas
    "“": '"', "”": '"',  # aspas duplas tipográficas
    "–": "-", "—": "-",  # en-dash, em-dash
    "�": " ",                 # replacement char -> espaço
})

# Heurísticas de classificação por página (copiadas de 01_extract_text.py) ---- #

_RE_INICIO_CAPITULO = re.compile(
    r"^\s*(chapter|capítulo|capitulo|chapitre|part|parte)\s+(\d+|[ivxlcdm]+)\b",
    re.IGNORECASE | re.MULTILINE,
)
_RE_NOTAS_FIM = re.compile(
    r"^\s*(notes|notas)\s*$", re.IGNORECASE | re.MULTILINE,
)
_RE_PARATEXTO = re.compile(
    r"^\s*(bibliography|references|bibliografia|index|índice|indice|"
    r"acknowledgements|acknowledgments|agradecimentos|appendix|apêndice|apendice|"
    r"contents|sumário|sumario)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def normalizar_texto(texto: str) -> tuple[str, dict[str, int]]:
    """Aplica as seis operações e retorna texto normalizado + estatísticas."""
    estats: dict[str, int] = {}

    # 1. Soft hyphen
    estats["soft_hyphen_removidos"] = len(_RE_SOFT_HYPHEN.findall(texto))
    texto = _RE_SOFT_HYPHEN.sub("", texto)

    # 2. De-hifenização de fim de linha
    estats["hyph_eol_juntados"] = len(_RE_HYPH_EOL.findall(texto))
    texto = _RE_HYPH_EOL.sub("", texto)

    # 3. Marcadores ((NN))
    estats["marcadores_parens_removidos"] = len(_RE_PARENS_MARKER.findall(texto))
    texto = _RE_PARENS_MARKER.sub(" ", texto)

    # 4. Cabeçalho espaçado (linha inteira). Aplica linha a linha. Se a linha
    # contém \f (separador de página), preserva o \f mesmo descartando o resto.
    n_header_removidas = 0
    novas_linhas: list[str] = []
    for linha in texto.split("\n"):
        linha_sem_ff = linha.replace("\f", "")
        if _RE_HEADER_SPACED.match(linha_sem_ff):
            n_header_removidas += 1
            n_ff = linha.count("\f")
            if n_ff:
                novas_linhas.append("\f" * n_ff)
            continue
        novas_linhas.append(linha)
    texto = "\n".join(novas_linhas)
    estats["linhas_cabecalho_descartadas"] = n_header_removidas

    # 5. NFKC + map de pontuação. NFKC pode quebrar ligaduras unicode em letras
    # simples (ﬁ -> fi), o que é desejável para o casamento de termos. Aplica-se
    # antes do map para que travessões/aspas decompostas também sejam pegas.
    texto_nfkc = unicodedata.normalize("NFKC", texto)
    estats["chars_nfkc_alterados"] = sum(1 for a, b in zip(texto, texto_nfkc) if a != b)
    texto = texto_nfkc

    # 6. Replacement chars (� já está no _MAP_PONTUACAO) e demais
    # mapeamentos de pontuação.
    estats["replacement_chars"] = texto.count("�")
    texto = texto.translate(_MAP_PONTUACAO)

    return texto, estats


# Classificação de páginas (idêntica a 01_extract_text.py) -------------------- #

def avaliar_qualidade_pagina(texto: str) -> str:
    if not texto.strip():
        return "baixa"
    total = len(texto)
    estranhos = sum(
        1 for c in texto
        if not (c.isalnum() or c.isspace() or c in ".,;:!?\"'()[]-—–…/\\&%$#@*+=<>")
    )
    prop_estranhos = estranhos / total
    linhas = [line for line in texto.splitlines() if line.strip()]
    if not linhas:
        return "baixa"
    curtas = sum(1 for line in linhas if len(line) < 10)
    prop_curtas = curtas / len(linhas)
    if prop_estranhos > 0.05 or prop_curtas > 0.5:
        return "baixa"
    if prop_estranhos > 0.02 or prop_curtas > 0.3:
        return "media"
    return "boa"


_ESTADO_INICIAL = "corpo"


def classificar_paginas(texto: str) -> list[dict[str, object]]:
    paginas = texto.split("\f")
    classificacao: list[dict[str, object]] = []
    estado = _ESTADO_INICIAL
    for numero, conteudo in enumerate(paginas, start=1):
        qualidade = avaliar_qualidade_pagina(conteudo)
        if qualidade == "baixa":
            classe = "qualidade_baixa"
        elif _RE_PARATEXTO.search(conteudo):
            classe = "paratexto"
            estado = "paratexto"
        elif _RE_NOTAS_FIM.search(conteudo) and estado != "paratexto":
            classe = "notas_fim"
            estado = "notas_fim"
        elif (
            _RE_INICIO_CAPITULO.search(conteudo)
            and estado not in ("notas_fim", "paratexto")
        ):
            classe = "inicio_capitulo"
            estado = "corpo"
        else:
            classe = estado if estado in ("notas_fim", "paratexto") else "corpo"

        classificacao.append({
            "pagina": numero,
            "classe": classe,
            "n_chars": len(conteudo),
            "n_palavras": sum(1 for tok in re.split(r"\s+", conteudo) if tok),
            "qualidade_pagina": qualidade,
        })
    return classificacao


def salvar_paginas_csv(obra_id: str, paginas: list[dict[str, object]]) -> None:
    PAGINAS_DIR.mkdir(parents=True, exist_ok=True)
    saida = PAGINAS_DIR / f"{obra_id}.csv"
    cabecalho = ["pagina", "classe", "n_chars", "n_palavras", "qualidade_pagina"]
    with saida.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=cabecalho)
        escritor.writeheader()
        escritor.writerows(paginas)


def atualizar_qualidade_extracao(
    obra_id: str,
    obra: dict[str, str],
    paginas: list[dict[str, object]],
) -> dict[str, object]:
    QUALIDADE_CSV.parent.mkdir(parents=True, exist_ok=True)
    cabecalho = [
        "id", "autor", "titulo", "ano_edicao", "idioma",
        "paginas_total", "palavras_total",
        "paginas_corpo", "paginas_inicio_capitulo", "paginas_notas_fim",
        "paginas_paratexto", "paginas_qualidade_baixa",
        "taxa_qualidade_boa", "taxa_qualidade_baixa",
        "qualidade_global",
    ]
    n_total = len(paginas)
    n_palavras = sum(int(p["n_palavras"]) for p in paginas)
    contagem_classes = {c: sum(1 for p in paginas if p["classe"] == c) for c in (
        "corpo", "inicio_capitulo", "notas_fim", "paratexto", "qualidade_baixa",
    )}
    contagem_q = {q: sum(1 for p in paginas if p["qualidade_pagina"] == q) for q in (
        "boa", "media", "baixa",
    )}
    taxa_boa = contagem_q["boa"] / n_total if n_total else 0
    taxa_baixa = contagem_q["baixa"] / n_total if n_total else 0
    qualidade_global = (
        "boa" if taxa_boa >= 0.8 and taxa_baixa <= 0.05
        else "media" if taxa_boa >= 0.6 and taxa_baixa <= 0.15
        else "baixa"
    )
    linha = {
        "id": obra_id,
        "autor": obra.get("autor", ""),
        "titulo": obra.get("titulo", ""),
        "ano_edicao": obra.get("ano_edicao", ""),
        "idioma": obra.get("idioma", ""),
        "paginas_total": n_total,
        "palavras_total": n_palavras,
        "paginas_corpo": contagem_classes["corpo"],
        "paginas_inicio_capitulo": contagem_classes["inicio_capitulo"],
        "paginas_notas_fim": contagem_classes["notas_fim"],
        "paginas_paratexto": contagem_classes["paratexto"],
        "paginas_qualidade_baixa": contagem_classes["qualidade_baixa"],
        "taxa_qualidade_boa": f"{taxa_boa:.3f}",
        "taxa_qualidade_baixa": f"{taxa_baixa:.3f}",
        "qualidade_global": qualidade_global,
    }
    existentes: dict[str, dict[str, str]] = {}
    if QUALIDADE_CSV.exists():
        with QUALIDADE_CSV.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                existentes[row["id"]] = row
    existentes[obra_id] = {k: str(v) for k, v in linha.items()}
    with QUALIDADE_CSV.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=cabecalho)
        escritor.writeheader()
        for _, row in sorted(existentes.items()):
            escritor.writerow(row)
    return linha


def obras_em_escopo() -> list[dict[str, str]]:
    if not METADATA_CSV.exists():
        sys.exit(f"ERRO: {METADATA_CSV} não existe.")
    with METADATA_CSV.open(encoding="utf-8", newline="") as f:
        rows = [row for row in csv.DictReader(f)
                if row.get("escopo_etapa1", "").strip().lower() == "sim"]
    if not rows:
        sys.exit("ERRO: nenhuma obra com escopo_etapa1 == 'sim' em metadata.csv.")
    return rows


def processar(obra: dict[str, str]) -> tuple[dict[str, object], dict[str, int]] | None:
    obra_id = obra["id"]
    bruto = CORPUS_TXT_DIR / f"{obra_id}.txt"
    if not bruto.exists():
        print(f"  ERRO: {bruto} nao existe; rode antes scripts/01_extract_text.py "
              "ou comite o txt no main.")
        return None
    texto = bruto.read_text(encoding="utf-8", errors="replace")
    normalizado, estats = normalizar_texto(texto)

    CORPUS_TXT_NORM_DIR.mkdir(parents=True, exist_ok=True)
    saida = CORPUS_TXT_NORM_DIR / f"{obra_id}.txt"
    saida.write_text(normalizado, encoding="utf-8")

    paginas = classificar_paginas(normalizado)
    salvar_paginas_csv(obra_id, paginas)
    linha_q = atualizar_qualidade_extracao(obra_id, obra, paginas)
    print(
        f"  ok: paginas={linha_q['paginas_total']}, "
        f"palavras={linha_q['palavras_total']}, "
        f"qualidade_global={linha_q['qualidade_global']}"
    )
    print(
        f"     normalizacoes: soft_hyphen={estats['soft_hyphen_removidos']}, "
        f"hyph_eol={estats['hyph_eol_juntados']}, "
        f"marcadores=({estats['marcadores_parens_removidos']}), "
        f"cabecalhos={estats['linhas_cabecalho_descartadas']}, "
        f"replacement={estats['replacement_chars']}"
    )
    return linha_q, estats


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", help="filtra obras por substring de id.")
    args = parser.parse_args()

    obras = obras_em_escopo()
    if args.only:
        obras = [o for o in obras if args.only.lower() in o["id"].lower()]
        if not obras:
            sys.exit(f"Nenhuma obra em escopo casa com --only='{args.only}'.")

    print(f"Obras a normalizar: {len(obras)}")
    resumo: list[tuple[dict[str, object], dict[str, int]]] = []
    for obra in obras:
        print(f"\n[{obra['id']}]")
        r = processar(obra)
        if r is not None:
            resumo.append(r)

    print("\nResumo da normalização (por obra):")
    print(
        f"  {'id':<45s} {'pgs':>5s} {'palavras':>10s} "
        f"{'soft_hy':>8s} {'hyph_eol':>9s} {'((NN))':>7s} "
        f"{'header':>7s} {'repl':>6s}"
    )
    for linha, e in resumo:
        print(
            f"  {linha['id']:<45s} {linha['paginas_total']:>5} "
            f"{linha['palavras_total']:>10} "
            f"{e['soft_hyphen_removidos']:>8} "
            f"{e['hyph_eol_juntados']:>9} "
            f"{e['marcadores_parens_removidos']:>7} "
            f"{e['linhas_cabecalho_descartadas']:>7} "
            f"{e['replacement_chars']:>6}"
        )


if __name__ == "__main__":
    main()
