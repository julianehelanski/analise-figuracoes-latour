"""Mapeamento centralizado de obras para etapas e construção de caminhos.

Importado pelos scripts do pipeline para resolver `outputs/etapa<N>/<obra_id>/`
sem hardcoding da etapa em cada script. Mantém o acoplamento obra → etapa em
um único local, em coerência com a reorganização do diretório `outputs/` em
sub-pastas por etapa.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = REPO_ROOT / "outputs"

ETAPA_DE_OBRA: dict[str, str] = {
    "latour_woolgar_1986_lab_life_en": "etapa1",
    "latour_1987_science_action_en": "etapa1",
    "latour_1999_pandora_en": "etapa1",
    "latour_1996_clarifications_en": "etapa2",
    "latour_1999_recalling_en": "etapa2",
    "latour_1999_recalling_bis": "etapa2bis",
    "latour_2013_aime_en": "etapa3",
}


def obra_dir(obra_id: str) -> Path:
    """Retorna o diretório de outputs de uma obra na hierarquia por etapa."""
    etapa = ETAPA_DE_OBRA.get(obra_id)
    if etapa is None:
        raise KeyError(
            f"Obra {obra_id!r} não está no mapeamento ETAPA_DE_OBRA. "
            "Adicione em scripts/_paths.py."
        )
    return OUTPUTS_DIR / etapa / obra_id


def consolidado_dir(etapa: str) -> Path:
    """Retorna o diretório consolidado de uma etapa."""
    return OUTPUTS_DIR / etapa / "consolidado"
