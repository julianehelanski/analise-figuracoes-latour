"""Gera as versões públicas, sem contexto, dos arquivos KWIC.

Os arquivos `kwic*.csv` gerados por `scripts/02_kwic.py` (e, para AIME, por
`scripts/arquivo/22_etapa3_aime_pipeline.py`) guardam ±10 palavras de contexto
antes e depois de cada ocorrência. Somadas, essas janelas reproduzem de 11% a
45% do texto de cada obra, o que excede a citação admitida pela Lei 9.610/98.
Por isso, desde 09/10/2026, os `kwic*.csv` completos ficam apenas na cópia
local de trabalho (estão no `.gitignore`) e continuam sendo lidos pelo
pipeline, em particular pela desambiguação de `war`/`wars`, que casa as
ocorrências pelo contexto.

Este script escreve, ao lado de cada `kwic*.csv`, um `kwic*_publico.csv` com
as mesmas linhas e todas as colunas exceto `contexto_antes` e
`contexto_depois`. A versão pública é a versionada: ela preserva a contagem
auditável (obra, grupo, termo, posição no texto, exclusão), e quem tiver o
texto reconstrói o contexto a partir de `posicao_no_texto`.

Uso:
    python scripts/12_kwic_publico.py
"""

from __future__ import annotations

import csv
from pathlib import Path

from _paths import OUTPUTS_DIR

COLUNAS_RETIRADAS: tuple[str, ...] = ("contexto_antes", "contexto_depois")


def caminho_publico(caminho_kwic: Path) -> Path:
    """Retorna o caminho da versão pública de um arquivo KWIC."""
    return caminho_kwic.with_name(f"{caminho_kwic.stem}_publico.csv")


def escrever_publico(caminho_kwic: Path) -> int:
    """Escreve a versão pública de um KWIC e retorna o número de linhas."""
    with caminho_kwic.open(encoding="utf-8", newline="") as f:
        leitor = csv.DictReader(f)
        colunas = [c for c in (leitor.fieldnames or []) if c not in COLUNAS_RETIRADAS]
        linhas = [{c: row[c] for c in colunas} for row in leitor]
    with caminho_publico(caminho_kwic).open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(linhas)
    return len(linhas)


def main() -> None:
    """Gera a versão pública de todos os KWIC por obra em `outputs/`."""
    arquivos = sorted(
        p for p in OUTPUTS_DIR.glob("etapa*/*/csv/kwic*.csv") if not p.stem.endswith("_publico")
    )
    if not arquivos:
        print("Nenhum kwic*.csv encontrado; rode antes scripts/02_kwic.py.")
        return
    for caminho in arquivos:
        n = escrever_publico(caminho)
        print(f"  {caminho_publico(caminho).relative_to(OUTPUTS_DIR)}: {n} linhas")


if __name__ == "__main__":
    main()
