"""Passo versionado: desambiguação war/wars do campo militar (Etapa 1).

Aplica a classificação manual já registrada (coluna `categoria_final` dos
CSVs `outputs/etapa1/refinamento/war_<obra>_classificacao.csv`) sobre o
campo `militar` das três obras da Etapa 1 e verifica que a contagem
refinada reproduz os valores fixos da tese: Laboratory Life 37, Science in
Action 363, Pandora's Hope 156.

Este passo não recomputa a camada manual: lê `categoria_final` e a aplica
por casamento de assinatura contra o `kwic.csv`. As figuras de frequência
e densidade (`scripts/04_visualizations.py` e
`scripts/arquivo/24_freq_densidade_por_obra.py`) importam o mesmo módulo
`_desambiguar_war`, de modo que figura e contagem partilham uma única
fonte de verdade.

Uso:
    python scripts/09_desambiguar_war.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _desambiguar_war import (  # noqa: E402
    REFINADO_ESPERADO,
    WAR_CLASSIFICACAO,
    carregar_descritivos,
    is_descritivo,
)
from _paths import obra_dir  # noqa: E402


def militar_validos(obra_id: str) -> list[dict]:
    """Ocorrências válidas do campo militar no kwic.csv da obra."""
    caminho = obra_dir(obra_id) / "csv" / "kwic.csv"
    with caminho.open(encoding="utf-8", newline="") as f:
        return [
            r for r in csv.DictReader(f)
            if r["grupo"] == "militar" and r.get("descartado_por_exclusao", "0") == "0"
        ]


def main() -> int:
    print("Desambiguação war/wars do campo militar (Etapa 1)\n")
    print(f"{'obra':40s} {'bruto':>6s} {'descr.':>7s} {'refinado':>9s} {'alvo':>5s}  ok")
    falhas = 0
    for obra_id in WAR_CLASSIFICACAO:
        militares = militar_validos(obra_id)
        descritivos = carregar_descritivos(obra_id)
        removidos = sum(1 for r in militares if is_descritivo(r, descritivos))
        bruto = len(militares)
        refinado = bruto - removidos
        alvo = REFINADO_ESPERADO[obra_id]
        ok = refinado == alvo
        falhas += 0 if ok else 1
        print(
            f"{obra_id:40s} {bruto:6d} {removidos:7d} {refinado:9d} {alvo:5d}  "
            f"{'OK' if ok else 'FALHA'}"
        )
    print()
    if falhas:
        print(
            f"VERIFICAÇÃO FALHOU em {falhas} obra(s): a contagem refinada "
            "divergiu do alvo. Não use as figuras regeradas; revise a "
            "classificação manual antes de prosseguir."
        )
        return 1
    print("Verificação OK: a contagem refinada reproduz os valores fixos da tese.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
