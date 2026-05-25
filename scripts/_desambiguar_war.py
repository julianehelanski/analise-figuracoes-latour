"""Desambiguação war/wars do campo militar (Etapa 1), reproduzível.

Lê a classificação por ocorrência registrada em
`outputs/etapa1/refinamento/war_<obra>_classificacao.csv` e aplica a
coluna `categoria_final` para remover do campo `militar` as ocorrências
de `war`/`wars` classificadas como descritivo-históricas.

A camada manual NÃO é recomputada por este módulo: ele lê `categoria_final`
(palavra final da pesquisadora) e a aplica. A camada automática por
gatilhos, que sugeriu `categoria_auto`, está documentada em
`scripts/arquivo/15_etapa2_desambiguar_militar.py` e em
`docs/decisoes_metodologicas.md`; aqui ela não é reexecutada.

O casamento entre cada linha de classificação e a ocorrência no `kwic.csv`
usa a assinatura (termo, sufixo de `contexto_antes`, prefixo de
`contexto_depois`). O campo `pagina` fica fora da assinatura porque o
`kwic.csv` grava todas as ocorrências com pagina=1, enquanto os CSVs de
classificação podem preservar páginas reais.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REFINAMENTO_DIR = REPO_ROOT / "outputs" / "etapa1" / "refinamento"

# Obra -> CSV de classificação war/wars (camada manual fixa).
WAR_CLASSIFICACAO: dict[str, str] = {
    "latour_woolgar_1986_lab_life_en": "war_lab_life_classificacao.csv",
    "latour_1987_science_action_en": "war_sia_classificacao.csv",
    "latour_1999_pandora_en": "war_pandora_classificacao.csv",
}

# Contagem refinada esperada do campo militar (alvo fixo da tese).
REFINADO_ESPERADO: dict[str, int] = {
    "latour_woolgar_1986_lab_life_en": 37,
    "latour_1987_science_action_en": 363,
    "latour_1999_pandora_en": 156,
}


def _assinatura(termo: str, antes: str, depois: str) -> tuple[str, str, str]:
    """Assinatura de uma ocorrência, estável entre kwic e CSV de classificação."""
    return (termo.lower(), antes[-30:].strip().lower(), depois[:30].strip().lower())


def carregar_descritivos(obra_id: str) -> set[tuple[str, str, str]]:
    """Assinaturas das ocorrências war/wars marcadas como `descritivo`.

    Lê `categoria_final == 'descritivo'` do CSV de classificação da obra.
    Devolve conjunto vazio para obras sem CSV mapeado.
    """
    nome = WAR_CLASSIFICACAO.get(obra_id)
    if nome is None:
        return set()
    caminho = REFINAMENTO_DIR / nome
    if not caminho.exists():
        raise FileNotFoundError(
            f"CSV de classificação war/wars não encontrado: {caminho}"
        )
    descritivos: set[tuple[str, str, str]] = set()
    with caminho.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row["categoria_final"].strip().lower() != "descritivo":
                continue
            descritivos.add(
                _assinatura(row["termo"], row["contexto_antes"], row["contexto_depois"])
            )
    return descritivos


def _termo_da_linha(row: dict) -> str:
    """Termo central, tolerando o nome de coluna do kwic ou do CSV de classificação."""
    return row.get("termo_encontrado") or row.get("termo") or ""


def is_descritivo(row: dict, descritivos: set[tuple[str, str, str]]) -> bool:
    """True se a linha de kwic é uma ocorrência war/wars classificada como descritivo."""
    termo = _termo_da_linha(row)
    if termo.lower() not in ("war", "wars"):
        return False
    sig = _assinatura(termo, row.get("contexto_antes", ""), row.get("contexto_depois", ""))
    return sig in descritivos


def filtrar_militar_refinado(rows: list[dict], obra_id: str) -> list[dict]:
    """Remove de `rows` (linhas de kwic) as ocorrências war/wars descritivas do militar.

    Aplica a classificação manual da obra ao campo `militar`. Obras sem CSV
    mapeado retornam `rows` inalterado.
    """
    descritivos = carregar_descritivos(obra_id)
    if not descritivos:
        return rows
    return [
        r for r in rows
        if not (r.get("grupo") == "militar" and is_descritivo(r, descritivos))
    ]
