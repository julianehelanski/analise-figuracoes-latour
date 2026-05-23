"""Versão simétrica de densidade_militar_sia_pandora.

A figura `densidade_militar_sia_pandora.png` gerada por
`11_passo4_graficos.py` aplica a desambiguação de `war`/`wars` apenas
em Pandora (via `war_pandora_classificacao.csv`); em SIA, os hits são
brutos. Este script:

1. Classifica as 18 ocorrências válidas de `war`/`wars` no campo
   `militar` de Science in Action 1987, escrevendo
   `outputs/etapa1/refinamento/war_sia_classificacao.csv` com o mesmo
   schema do CSV de Pandora.
2. Gera a versão **simétrica** da figura, com hits refinados
   (descritivos removidos) nas duas obras, em
   `outputs/etapa1/passo4/figuras/densidade_militar_sia_pandora_simetrica.{png,svg}`.
3. Espelha em `outputs/consolidado/figuras/`.

A figura assimétrica original fica preservada para comparação histórica
e como objeto de decisão metodológica (registrada em
`docs/decisoes_metodologicas.md`).
"""
from __future__ import annotations

import bisect
import csv
import re
import shutil
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
from _paths import obra_dir

REPO = Path(__file__).resolve().parents[2]
OUT_FIG_DIR = REPO / "outputs" / "etapa1" / "passo4" / "figuras"
OUT_REF_DIR = REPO / "outputs" / "etapa1" / "refinamento"
OUT_CONS_DIR = REPO / "outputs" / "consolidado" / "figuras"

OBRA_SIA = "latour_1987_science_action_en"
OBRA_PAN = "latour_1999_pandora_en"

# Classificação manual das 18 ocorrências válidas de war/wars no campo
# militar de Science in Action 1987 (Latour 1987). Chave: posicao_no_texto
# do kwic.csv. Mesma rubrica aplicada em PAN: descritivos são ocorrências
# que nomeiam objeto histórico, referência bibliográfica ou instituição;
# figurativos são tropos conceituais e analogias.
CLASSIFICACAO_SIA: dict[int, dict[str, str]] = {
    145556: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'in war' analogia entre texto científico e enumeração bélica"},
    200936: {"final": "descritivo", "auto": "descritivo_historico", "gatilho": "World",
             "justif": "automatico: gatilho 'World' — 'Second World Wars'"},
    292408: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'God in not-so-ancient wars' analogia conceitual Natureza/divindade"},
    342229: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'waging war'"},
    342668: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'win the war'"},
    342759: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'win a war'"},
    342766: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'a war in its usual rendering'"},
    342872: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'win the war meaning now a new atomic'"},
    343072: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'war machine' em narrativa histórica"},
    343548: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'wage a nuclear war'"},
    345424: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "capítulo Szilard/Pentagon WWII — 'Pentagon wishes to win the war'"},
    349716: {"final": "descritivo", "auto": "descritivo_historico", "gatilho": "Franco-Prussian",
             "justif": "automatico: gatilho 'Franco-Prussian'"},
    519389: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'war machine' tropo conceitual sobre technoscience"},
    519451: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'link between war and technoscience' tropo conceitual"},
    575572: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'war cries' analogia para fórmulas matemáticas como intimidação"},
    579039: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'situation of war' exemplo filosófico-categorial sobre homicídio"},
    579282: {"final": "figurativo", "auto": "ambiguo", "gatilho": "",
             "justif": "'situation of war' como categoria abstrata; Nuremberg citado como exceção"},
    816909: {"final": "descritivo", "auto": "ambiguo", "gatilho": "",
             "justif": "referência bibliográfica Tolstoi 'War and Peace'"},
}


def carregar_militar_war_hits(obra_id: str) -> list[dict]:
    """Lê do kwic.csv as ocorrências válidas de war/wars no campo militar."""
    hits: list[dict] = []
    with (obra_dir(obra_id) / "csv" / "kwic.csv").open() as f:
        for row in csv.DictReader(f):
            if row["grupo"] != "militar":
                continue
            if row["termo_encontrado"].lower() not in ("war", "wars"):
                continue
            if row.get("descartado_por_exclusao", "0") != "0":
                continue
            hits.append({
                "pagina": int(row["pagina"]),
                "pos_char": int(row["posicao_no_texto"]),
                "termo": row["termo_encontrado"],
                "contexto_antes": row["contexto_antes"],
                "contexto_depois": row["contexto_depois"],
            })
    return hits


def carregar_militar_hits(obra_id: str) -> list[dict]:
    """Lê do kwic.csv todas as ocorrências válidas do campo militar."""
    hits: list[dict] = []
    with (obra_dir(obra_id) / "csv" / "kwic.csv").open() as f:
        for row in csv.DictReader(f):
            if row["grupo"] != "militar":
                continue
            if row.get("descartado_por_exclusao", "0") != "0":
                continue
            hits.append({
                "pagina": int(row["pagina"]),
                "pos_char": int(row["posicao_no_texto"]),
                "termo": row["termo_encontrado"],
                "contexto_antes": row["contexto_antes"],
                "contexto_depois": row["contexto_depois"],
            })
    return hits


def escrever_csv_classificacao_sia() -> Path:
    """Escreve war_sia_classificacao.csv aplicando CLASSIFICACAO_SIA."""
    hits = carregar_militar_war_hits(OBRA_SIA)
    if len(hits) != len(CLASSIFICACAO_SIA):
        raise RuntimeError(
            f"Esperava {len(CLASSIFICACAO_SIA)} hits classificados em "
            f"CLASSIFICACAO_SIA, mas o kwic.csv tem {len(hits)} hits válidos. "
            f"Posições no kwic: {sorted(h['pos_char'] for h in hits)}; "
            f"posições classificadas: {sorted(CLASSIFICACAO_SIA.keys())}."
        )
    posicoes_kwic = {h["pos_char"] for h in hits}
    faltando = set(CLASSIFICACAO_SIA) - posicoes_kwic
    sobrando = posicoes_kwic - set(CLASSIFICACAO_SIA)
    if faltando or sobrando:
        raise RuntimeError(
            f"Mismatch de posições entre kwic.csv e CLASSIFICACAO_SIA. "
            f"Faltando no kwic: {faltando}. Sobrando no kwic: {sobrando}."
        )

    OUT_REF_DIR.mkdir(parents=True, exist_ok=True)
    caminho = OUT_REF_DIR / "war_sia_classificacao.csv"
    with caminho.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([
            "pagina", "termo", "categoria_auto", "gatilho_detectado",
            "contexto_antes", "trecho_central", "contexto_depois",
            "categoria_final", "justificativa",
        ])
        for h in sorted(hits, key=lambda x: x["pos_char"]):
            cls = CLASSIFICACAO_SIA[h["pos_char"]]
            escritor.writerow([
                h["pagina"],
                h["termo"],
                cls["auto"],
                cls["gatilho"],
                h["contexto_antes"],
                h["termo"],
                h["contexto_depois"],
                cls["final"],
                cls["justif"],
            ])
    return caminho


def filtrar_war_descritivos(hits: list[dict], caminho_csv: Path) -> list[dict]:
    """Remove ocorrências de war/wars classificadas como descritivo.

    Cruza por assinatura (termo, sufixo do contexto_antes, prefixo do
    contexto_depois). O campo `pagina` foi removido da assinatura porque
    o `kwic.csv` em uso na 2026-05-23 grava todas as ocorrências com
    `pagina=1` (extração em bloco único), enquanto os CSVs de
    classificação preservam páginas reais. A assinatura por contexto é
    suficiente para identificar a ocorrência univocamente; as 18 (SIA)
    e 85 (PAN) ocorrências de war/wars no campo militar têm contextos
    distintos entre si.
    """
    descritivos: set[tuple] = set()
    with caminho_csv.open() as f:
        for row in csv.DictReader(f):
            if row["categoria_final"] != "descritivo":
                continue
            assinatura = (
                row["termo"].lower(),
                row["contexto_antes"][-30:].strip().lower(),
                row["contexto_depois"][:30].strip().lower(),
            )
            descritivos.add(assinatura)

    def is_descritivo(h: dict) -> bool:
        if h["termo"].lower() not in ("war", "wars"):
            return False
        sig = (
            h["termo"].lower(),
            h["contexto_antes"][-30:].strip().lower(),
            h["contexto_depois"][:30].strip().lower(),
        )
        return sig in descritivos

    return [h for h in hits if not is_descritivo(h)]


def converter_char_para_palavra(txt: str, hits: list[dict]) -> tuple[list[int], int]:
    """Converte posições de char (kwic) em índices de palavra do txt_norm."""
    offsets_palavras = [m.start() for m in re.finditer(r"\S+", txt)]
    total = len(offsets_palavras)
    indices: list[int] = []
    for h in hits:
        idx = bisect.bisect_right(offsets_palavras, h["pos_char"]) - 1
        if idx < 0:
            idx = 0
        indices.append(idx)
    return indices, total


def estilo_matplotlib() -> None:
    plt.rcParams.update({
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "grid.alpha": 0.3,
        "grid.linewidth": 0.5,
        "figure.dpi": 100,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "font.size": 10,
        "font.family": "DejaVu Sans",
    })


def figura_densidade_simetrica() -> tuple[int, int]:
    """Gera a versão simétrica da densidade militar em SIA e PAN.

    Retorna (n_sia_refinado, n_pan_refinado) para o relatório.
    """
    janela = 1000
    passo = 200

    paineis = [
        (OBRA_SIA, "Science in Action, 1987",
         OUT_REF_DIR / "war_sia_classificacao.csv"),
        (OBRA_PAN, "Pandora's Hope, 1999",
         OUT_REF_DIR / "war_pandora_classificacao.csv"),
    ]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    if not isinstance(axes, np.ndarray):
        axes = np.array([axes])

    contagens_refinadas: list[int] = []
    for ax, (obra_id, rotulo, csv_class) in zip(axes, paineis):
        txt = (REPO / "corpus" / "txt_norm" / f"{obra_id}.txt").read_text(
            encoding="utf-8"
        )
        hits = carregar_militar_hits(obra_id)
        hits = filtrar_war_descritivos(hits, csv_class)
        contagens_refinadas.append(len(hits))
        word_indices, total_palavras = converter_char_para_palavra(txt, hits)
        word_indices.sort()

        starts = list(range(0, max(total_palavras - janela, 1), passo))
        xs: list[float] = []
        ys: list[int] = []
        for start in starts:
            end = start + janela
            lo = bisect.bisect_left(word_indices, start)
            hi = bisect.bisect_left(word_indices, end)
            xs.append((start + end) / 2 / 1000)
            ys.append(hi - lo)

        ax.plot(xs, ys, color="#B22222", linewidth=1.5)
        ax.fill_between(xs, 0, ys, color="#B22222", alpha=0.2)
        ax.set_ylabel(
            "Ocorrências do campo militar\n(janela de 1.000 palavras)",
            fontsize=9,
        )
        ax.set_xlim(0, total_palavras / 1000)
        ax.set_ylim(bottom=0)
        ax.text(
            0.01, 0.95,
            f"{rotulo}  (n refinado = {len(hits)})",
            transform=ax.transAxes,
            fontsize=10, va="top", ha="left",
            color="#303030", fontweight="bold",
        )
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="x", alpha=0.3, linewidth=0.5)
        ax.set_axisbelow(True)

    axes[-1].set_xlabel(
        "Posição no texto (milhares de palavras)", fontsize=10
    )

    # Anotação no canto inferior direito da figura, deixando explícito
    # que esta é a versão simétrica (ambas as obras com war/wars
    # descritivos filtrados).
    fig.text(
        0.99, 0.005,
        "Versão simétrica: war/wars descritivos removidos em ambas as obras "
        "(classificação em refinamento/war_{sia,pandora}_classificacao.csv).",
        ha="right", va="bottom", fontsize=8, color="#606060",
    )

    fig.tight_layout(rect=(0, 0.02, 1, 1))

    OUT_FIG_DIR.mkdir(parents=True, exist_ok=True)
    png = OUT_FIG_DIR / "densidade_militar_sia_pandora_simetrica.png"
    svg = OUT_FIG_DIR / "densidade_militar_sia_pandora_simetrica.svg"
    fig.savefig(png, dpi=300, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    OUT_CONS_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(png, OUT_CONS_DIR / png.name)

    return tuple(contagens_refinadas)  # type: ignore[return-value]


def main() -> None:
    estilo_matplotlib()
    print("Escrevendo war_sia_classificacao.csv ...")
    caminho_sia = escrever_csv_classificacao_sia()
    print(f"  gravado: {caminho_sia.relative_to(REPO)}")

    print("Gerando figura simétrica ...")
    n_sia, n_pan = figura_densidade_simetrica()
    print(f"  n militar SIA refinado: {n_sia}")
    print(f"  n militar PAN refinado: {n_pan}")
    print(f"  gravado: outputs/etapa1/passo4/figuras/"
          f"densidade_militar_sia_pandora_simetrica.png")
    print(f"  espelhado: outputs/consolidado/figuras/"
          f"densidade_militar_sia_pandora_simetrica.png")


if __name__ == "__main__":
    main()
