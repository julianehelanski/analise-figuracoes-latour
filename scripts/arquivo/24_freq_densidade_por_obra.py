"""Figura combinada frequência + densidade, uma por obra (6 obras no total).

Para cada uma das seis obras do corpus (Laboratory Life 1986, Science
in Action 1987, Clarifications 1996, Pandora's Hope 1999, Recalling
ANT 1999 integral, AIME 2013), gera uma figura única em layout
1 linha × 2 colunas:

- Coluna esquerda: ranking de campos figurativos por frequência por
  10.000 palavras (barras horizontais, paleta viridis para obras de
  catálogo único; para AIME, azul/laranja por proveniência do catálogo).
- Coluna direita: densidade empilhada das ocorrências ao longo do
  texto (histograma de 30 bins, paleta tab20, eixo X = posição
  relativa 0--1).

Para Recalling, uso o corpus integral da Etapa 2-bis (4.825 palavras).
Para AIME, combino catálogo antigo + catálogo novo (26 campos com
ocorrência) com cor distinta por proveniência.

Saídas (PNG 300 dpi + SVG):
- outputs/consolidado/figuras/freq_densidade_<obra>.{png,svg}
- outputs/figuras/etapa<N>_<obra>_freq_e_densidade.{png,svg}
"""
from __future__ import annotations

import csv
import random
import shutil
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _desambiguar_war import filtrar_militar_refinado  # noqa: E402
from estilo_tese import (  # noqa: E402
    COR_CAMPO, COR_DESTAQUE, COR_TEXTIL, COR_CAT_ANTIGO, COR_CAT_NOVO,
    aplicar_rcparams, dotplot, eixo_ptbr, pct_ptbr,
)

REPO = Path(__file__).resolve().parents[2]
OUT_CONSOL = REPO / "outputs" / "consolidado" / "figuras"
OUT_PASTA = REPO / "outputs" / "figuras"

GRUPOS_ANTIGOS = {
    "inscription", "immutable_mobile", "black_box", "centre_of_calculation",
    "actor_network", "translation", "trial_of_strength", "factish",
    "circulating_reference", "articulation", "construction", "proposition",
    "network", "agonistic", "enrollment", "spokesperson", "militar",
    "textil", "topologia",
}

# Configuração das 6 obras. Para AIME, `kwic_filenames` lista os dois
# CSVs do catálogo duplo; para as outras, lista única com `kwic.csv`.
OBRAS = [
    {
        "id": "latour_woolgar_1986_lab_life_en",
        "slug_curto": "lab_life",
        "slug_pasta": "etapa1_lab_life",
        "rotulo": "Laboratory Life, 1986",
        "titulo_obra": "Laboratory Life",
        "palavras": 105_749,
        "txt": "latour_woolgar_1986_lab_life_en.txt",
        "etapa_dir": "etapa1",
        "kwic_filenames": ["kwic.csv"],
        "catalogo_duplo": False,
    },
    {
        "id": "latour_1987_science_action_en",
        "slug_curto": "sia",
        "slug_pasta": "etapa1_sia",
        "rotulo": "Science in Action, 1987",
        "titulo_obra": "Science in Action",
        "palavras": 139_861,
        "txt": "latour_1987_science_action_en.txt",
        "etapa_dir": "etapa1",
        "kwic_filenames": ["kwic.csv"],
        "catalogo_duplo": False,
    },
    {
        "id": "latour_1996_clarifications_en",
        "slug_curto": "clarifications",
        "slug_pasta": "etapa2_clarifications",
        "rotulo": "Clarifications, 1996",
        "titulo_obra": "On Actor-Network Theory",
        "palavras": 7_848,
        "txt": "latour_1996_clarifications_en.txt",
        "etapa_dir": "etapa2",
        "kwic_filenames": ["kwic.csv"],
        "catalogo_duplo": False,
        # As 3 ocorrências brutas do campo militar (allies, enemies,
        # alliance) são todas metalinguísticas ou bibliográficas
        # (Latour citando para criticar; título de Prigogine+Stengers).
        # Nenhuma é uso figural latouriano do vocabulário militar para
        # a prática científica, conforme relatório consolidado da
        # Etapa 2 (outputs/etapa2/consolidado/relatorio_etapa2.md, § 1).
        # Refinado figural = 0.
        "militar_zero": True,
    },
    {
        "id": "latour_1999_pandora_en",
        "slug_curto": "pandora",
        "slug_pasta": "etapa1_pandora",
        "rotulo": "Pandora's Hope, 1999",
        "titulo_obra": "Pandora's Hope",
        "palavras": 128_001,
        "txt": "latour_1999_pandora_en.txt",
        "etapa_dir": "etapa1",
        "kwic_filenames": ["kwic.csv"],
        "catalogo_duplo": False,
    },
    {
        "id": "latour_1999_recalling_bis",
        "slug_curto": "recalling_integral",
        "slug_pasta": "etapa2bis_recalling_integral",
        "rotulo": "Recalling ANT, 1999 (integral)",
        "titulo_obra": "On Recalling ANT",
        "palavras": 4_825,
        "txt": "latour_1999_recalling_bis.txt",
        "etapa_dir": "etapa2bis",
        "kwic_filenames": ["kwic.csv"],
        "catalogo_duplo": False,
        # As 2 ocorrências brutas do campo militar (alliance, wars) são
        # respectivamente metalinguística (Latour listando vocabulário
        # ANT que ele mesmo critica) e descritivo-histórica (Science
        # Wars como objeto público). Nenhuma é uso figural latouriano,
        # conforme relatório da Etapa 2-bis
        # (outputs/etapa2bis/consolidado/relatorio_etapa2bis.md, § 3).
        # Refinado figural = 0.
        "militar_zero": True,
    },
    {
        "id": "latour_2013_aime_en",
        "slug_curto": "aime",
        "slug_pasta": "etapa3_aime",
        "rotulo": "AIME, 2013",
        "titulo_obra": "An Inquiry into Modes of Existence",
        "palavras": 194_454,
        "txt": "latour_2013_aime_en.txt",
        "etapa_dir": "etapa3",
        "kwic_filenames": ["kwic_catalogo_antigo.csv", "kwic_catalogo_aime.csv"],
        "catalogo_duplo": True,
    },
]


def carregar_kwic_valido(obra: dict) -> list[dict[str, str]]:
    """Carrega kwic.csv(s) da obra, mantendo só ocorrências válidas.

    Aplica a desambiguação war/wars do campo militar (módulo
    `_desambiguar_war`): para as três obras da Etapa 1 com classificação
    registrada, remove as ocorrências de `war`/`wars` lidas como
    descritivo-históricas, deixando o militar na contagem refinada
    (Laboratory Life 37, Science in Action 363, Pandora's Hope 156).

    Quando `militar_zero` é True na config da obra, remove todas as
    ocorrências do campo `militar` antes de devolver, refletindo a
    leitura figural de que o militar nos artigos metateóricos é zero
    (todas as ocorrências brutas são metalinguísticas, bibliográficas
    ou descritivo-históricas).
    """
    base = REPO / "outputs" / obra["etapa_dir"] / obra["id"] / "csv"
    todas: list[dict[str, str]] = []
    for nome in obra["kwic_filenames"]:
        caminho = base / nome
        if not caminho.exists():
            raise FileNotFoundError(f"kwic não encontrado: {caminho}")
        with caminho.open(encoding="utf-8", newline="") as f:
            todas.extend([row for row in csv.DictReader(f)
                          if row.get("descartado_por_exclusao", "0") == "0"])
    # Campo militar refinado: remove as ocorrências war/wars descritivas
    # conforme a classificação manual da obra (no-op para obras sem CSV,
    # como os artigos metateóricos e a AIME).
    todas = filtrar_militar_refinado(todas, obra["id"])
    if obra.get("militar_zero"):
        todas = [r for r in todas if r["grupo"] != "militar"]
    return todas


def estilo_matplotlib() -> None:
    aplicar_rcparams()


def _cor_campo(grupo: str, catalogo_duplo: bool) -> str:
    """Cor-assinatura por campo figurativo (identidade visual da tese).

    militar em magenta (foco analítico), têxtil em verde (contraponto
    haraway), demais campos em azul. No catálogo duplo da AIME, a cor
    marca a proveniência (antigo vs novo)."""
    if catalogo_duplo:
        return COR_CAT_ANTIGO if grupo in GRUPOS_ANTIGOS else COR_CAT_NOVO
    if grupo == "militar":
        return COR_DESTAQUE
    if grupo == "textil":
        return COR_TEXTIL
    return COR_CAMPO


def ordenar_campos(ocs: list[dict], catalogo_duplo: bool):
    """Ordena os campos por frequência (ascendente: mais frequente no topo)
    e devolve (grupos, contagem, cores) para os dois painéis usarem a mesma
    ordem e as mesmas cores-assinatura."""
    contagem: dict[str, int] = defaultdict(int)
    for row in ocs:
        contagem[row["grupo"]] += 1
    grupos = sorted(contagem, key=contagem.get)
    cores = [_cor_campo(g, catalogo_duplo) for g in grupos]
    return grupos, contagem, cores


def plot_freq(ax, grupos, contagem, cores, palavras, catalogo_duplo) -> None:
    """Dot plot de Cleveland: frequência por 10k palavras por campo."""
    if not grupos:
        ax.text(0.5, 0.5, "(sem ocorrências)", ha="center", va="center",
                transform=ax.transAxes, color="#909090", fontsize=10)
        ax.set_axis_off()
        return
    freqs = [contagem[g] / palavras * 10_000 for g in grupos]
    rotulos = [f"{pct_ptbr(f)}" for f in freqs]

    dotplot(ax, grupos, freqs, cores, rotulos=rotulos)
    ax.set_xlabel("frequência por 10.000 palavras", fontsize=9, color="#6b6b6b")

    if catalogo_duplo:
        legenda = [
            Patch(facecolor=COR_CAT_ANTIGO, label="catálogo antigo (Etapas 1--2)"),
            Patch(facecolor=COR_CAT_NOVO, label="catálogo novo (Etapa 3)"),
        ]
        ax.legend(handles=legenda, loc="lower right", fontsize=8, frameon=False)


def plot_densidade(ax, ocs, txt_path, grupos, cores) -> None:
    """Strip plot da posição das ocorrências ao longo do texto.

    Cada campo é uma faixa horizontal (mesma ordem e cor do painel de
    frequência); cada ocorrência é uma bolinha na sua posição relativa
    (0 = início, 1 = fim). O eixo Y nomeia os campos, então a figura
    dispensa legenda. Um leve deslocamento vertical (jitter) revela a
    concentração quando muitas ocorrências caem perto."""
    if not txt_path.exists() or not grupos:
        ax.text(0.5, 0.5, "(sem dados de posição)", ha="center", va="center",
                transform=ax.transAxes, color="#909090", fontsize=10)
        ax.set_axis_off()
        return
    n_chars = txt_path.stat().st_size or 1
    posicoes_por_grupo: dict[str, list[float]] = defaultdict(list)
    for row in ocs:
        try:
            posicoes_por_grupo[row["grupo"]].append(
                int(row["posicao_no_texto"]) / n_chars
            )
        except (ValueError, KeyError):
            continue

    jit = random.Random(42)
    for i, g in enumerate(grupos):
        xs = posicoes_por_grupo.get(g, [])
        if not xs:
            continue
        ys = [i + (jit.random() - 0.5) * 0.55 for _ in xs]
        ax.scatter(xs, ys, s=12, color=cores[i], alpha=0.45,
                   edgecolors="none", zorder=3)
    ax.set_xlabel("posição relativa no texto (0 = início, 1 = fim)",
                  fontsize=9, color="#6b6b6b")
    ax.set_xlim(-0.02, 1.02)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    eixo_ptbr(ax, "x")
    ax.tick_params(axis="x", labelsize=8)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(left=False)
    ax.grid(axis="x", linestyle=":", linewidth=0.6, color="#e3e3e3", zorder=0)


def gerar_uma_figura(obra: dict) -> tuple[Path, Path]:
    ocs = carregar_kwic_valido(obra)

    grupos, contagem, cores = ordenar_campos(ocs, obra["catalogo_duplo"])

    fig, (ax_freq, ax_dens) = plt.subplots(
        nrows=1, ncols=2, sharey=True,
        figsize=(15, max(4.5, 0.34 * max(1, len(grupos)) + 2.5)),
        gridspec_kw={"width_ratios": [1.0, 1.6], "wspace": 0.06},
    )

    plot_freq(ax_freq, grupos, contagem, cores, obra["palavras"],
              obra["catalogo_duplo"])
    plot_densidade(ax_dens, ocs, REPO / "corpus" / "txt_norm" / obra["txt"],
                   grupos, cores)

    # Sem título embutido: o nome da obra, ano, contagem de palavras e nota
    # de catálogo duplo ficam na legenda (caption) do LaTeX
    # (outputs/latex/inventario_figuras.tex).
    fig.tight_layout()

    OUT_CONSOL.mkdir(parents=True, exist_ok=True)
    OUT_PASTA.mkdir(parents=True, exist_ok=True)
    nome_consol = f"freq_densidade_{obra['slug_curto']}"
    nome_pasta = f"{obra['slug_pasta']}_freq_e_densidade"
    png_consol = OUT_CONSOL / f"{nome_consol}.png"
    svg_consol = OUT_CONSOL / f"{nome_consol}.svg"
    fig.savefig(png_consol, dpi=300, bbox_inches="tight")
    fig.savefig(svg_consol, bbox_inches="tight")
    plt.close(fig)

    shutil.copy2(png_consol, OUT_PASTA / f"{nome_pasta}.png")
    shutil.copy2(svg_consol, OUT_PASTA / f"{nome_pasta}.svg")
    return png_consol, OUT_PASTA / f"{nome_pasta}.png"


def main() -> None:
    estilo_matplotlib()
    print("Gerando 6 figuras combinadas (frequência + densidade), uma por obra ...")
    for obra in OBRAS:
        c, p = gerar_uma_figura(obra)
        print(f"  [{obra['slug_curto']}] gravado: {c.relative_to(REPO)}")
        print(f"                espelho: {p.relative_to(REPO)}")


if __name__ == "__main__":
    main()
