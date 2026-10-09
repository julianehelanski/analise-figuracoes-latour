"""
Passo 4 do refinamento, gráficos comparativos para o capítulo 2 da tese.

Gera três figuras que sustentam visualmente a subseção sobre figuração
militar nas três obras de Latour:

1. comparacao_frequencias_tres_obras.{png,svg}: densidade dos 17 campos
   figurativos nas três obras, em barras agrupadas horizontais. Campo
   militar destacado em vermelho ferrugem; valores refinados pela
   desambiguação de war/wars no campo militar (passo 1 do refinamento)
   substituem a contagem bruta do frequencias.csv.

2. densidade_militar_sia_pandora.{png,svg}: distribuição da densidade
   do campo militar ao longo dos textos de Science in Action 1987 e
   Pandora's Hope 1999, em janelas deslizantes de 1.000 palavras com
   passo de 200. Versão simétrica de 2026-05-23: nas duas obras as
   ocorrências de war/wars classificadas como descritivas são excluídas
   antes da contagem, via cruzamento com refinamento/war_sia_classificacao.csv
   (SIA) e war_pandora_classificacao.csv (PAN).

3. rede_cocorrencia_sia.{png,svg}: grafo de cocorrências entre campos
   figurativos em Science in Action, recalculado a partir do kwic.csv
   em janela de 100 palavras (o cocorrencia.csv versionado usa 200; a
   janela menor é exigida pelo briefing). Limiar mínimo de 5
   cocorrências por aresta. Campo militar como nó em destaque.

Saídas em outputs/etapa1/passo4/figuras/, em PNG (300 dpi) e SVG.
"""

from __future__ import annotations

import bisect
import csv
import re
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import yaml
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
from _paths import obra_dir
from estilo_tese import (  # noqa: E402
    OKABE_ITO, aplicar_rcparams, dumbbell, pct_ptbr,
)

REPO = Path(__file__).resolve().parents[2]
OUT_DIR = REPO / "outputs" / "etapa1" / "passo4" / "figuras"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OBRAS_ANO = [
    ("latour_woolgar_1986_lab_life_en", "1986"),
    ("latour_1987_science_action_en", "1987"),
    ("latour_1999_pandora_en", "1999"),
]

# Valores refinados do campo militar (passo 1 do refinamento). Tabela
# refinamento/tabela_militar_refinada.tex. Atualização simétrica de
# 2026-05-23: SIA passa de n=364 (agregado anterior) para n=363, pela
# classificação por ocorrência registrada em
# refinamento/war_sia_classificacao.csv (11 descritivos sobre 18
# ocorrências de war/wars no campo militar de SIA).
MILITAR_REFINADO = {
    "latour_woolgar_1986_lab_life_en": {"n": 37, "freq_10k": 3.50},
    "latour_1987_science_action_en": {"n": 363, "freq_10k": 25.95},
    "latour_1999_pandora_en": {"n": 156, "freq_10k": 12.19},
}

# CSVs de classificação war/wars por ocorrência para SIA e PAN,
# carregados em figura_2_densidade_militar (tratamento simétrico).
WAR_CLASSIFICACAO = {
    "latour_1987_science_action_en": "war_sia_classificacao.csv",
    "latour_1999_pandora_en": "war_pandora_classificacao.csv",
}

# Paleta. O vermelho ferrugem (#B22222) é o destaque do campo militar.
# Variantes mais clara e mais escura indicam cronologia. Os demais
# campos seguem a mesma lógica em escala de cinza.
COR_MILITAR = {"1986": "#E08570", "1987": "#B22222", "1999": "#7A1A1A"}
COR_BASE = {"1986": "#D4D4D4", "1987": "#808080", "1999": "#404040"}


def estilo_matplotlib() -> None:
    """Aplica defaults sóbrios: sem spines top/direita, grid leve no X."""
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


def salvar(fig, nome: str) -> None:
    """Salva a figura em PNG 300 dpi e SVG."""
    fig.savefig(OUT_DIR / f"{nome}.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT_DIR / f"{nome}.svg", bbox_inches="tight")
    plt.close(fig)


def carregar_campos_catalogo() -> list[str]:
    """Lê os 17 campos do catálogo, na ordem do arquivo."""
    with open(REPO / "campos_lexicais" / "catalogo_termos.yaml") as f:
        cat = yaml.safe_load(f)
    return list(cat["latour"].keys())


def carregar_frequencias(obra_id: str) -> dict[str, float]:
    """Retorna mapa campo -> frequência por 10k palavras."""
    freq: dict[str, float] = {}
    with open(obra_dir(obra_id) /  "csv" / "frequencias.csv") as f:
        for row in csv.DictReader(f):
            freq[row["grupo"]] = float(row["frequencia_por_10k_palavras"])
    return freq


def carregar_n_absoluto(obra_id: str) -> dict[str, int]:
    """Retorna mapa campo -> ocorrências absolutas."""
    n: dict[str, int] = {}
    with open(obra_dir(obra_id) /  "csv" / "frequencias.csv") as f:
        for row in csv.DictReader(f):
            n[row["grupo"]] = int(row["n_ocorrencias"])
    return n


def figura_1_comparacao_frequencias() -> None:
    """Dumbbell dos 17 campos × 3 obras: frequência por 10k palavras.

    Cada campo é uma linha; os três pontos (Laboratory Life 1986, Science
    in Action 1987, Pandora's Hope 1999) ligados pela linha-guia mostram a
    dispersão da figuração ao longo do tempo. O campo militar aparece com a
    maior amplitude (3,5 -> 26,0 -> 12,2)."""
    campos = carregar_campos_catalogo()
    freq_por_obra = {
        ano: carregar_frequencias(obra_id) for obra_id, ano in OBRAS_ANO
    }
    # Substitui o militar pela contagem refinada do passo 1
    for obra_id, ano in OBRAS_ANO:
        freq_por_obra[ano]["militar"] = MILITAR_REFINADO[obra_id]["freq_10k"]

    # Ordena os campos por densidade decrescente em SIA (1987). Quem
    # estiver ausente em SIA cai para o fim, mantendo ordem do catálogo.
    def chave_ord(campo: str) -> tuple[float, int]:
        return (-freq_por_obra["1987"].get(campo, 0.0), campos.index(campo))

    # Dumbbell desenha do menor (base) ao maior (topo): inverte a ordem.
    campos_ord = sorted(campos, key=chave_ord)[::-1]

    nomes = {
        "1986": "Laboratory Life (1986)",
        "1987": "Science in Action (1987)",
        "1999": "Pandora's Hope (1999)",
    }
    cores = {
        nomes["1986"]: OKABE_ITO["azul_claro"],
        nomes["1987"]: OKABE_ITO["azul"],
        nomes["1999"]: OKABE_ITO["vermelho"],
    }
    series = {
        nomes[ano]: [freq_por_obra[ano].get(c, 0.0) for c in campos_ord]
        for ano in ("1986", "1987", "1999")
    }

    fig, ax = plt.subplots(figsize=(12, 10))
    dumbbell(ax, campos_ord, series, cores)
    ax.set_xlabel("frequência por 10.000 palavras", fontsize=10, color="#6b6b6b")
    ax.legend(loc="lower right", frameon=False, fontsize=10)

    # Rótulo do militar (campo em foco) em cada obra, para leitura direta
    # da amplitude que sustenta o argumento.
    i_mil = campos_ord.index("militar")
    for ano in ("1986", "1987", "1999"):
        val = freq_por_obra[ano]["militar"]
        ax.annotate(pct_ptbr(val, 1), xy=(val, i_mil), xytext=(0, 9),
                    textcoords="offset points", ha="center", fontsize=8,
                    color="#404040")

    salvar(fig, "comparacao_frequencias_tres_obras")
    print(f"  figura 1 salva: {OUT_DIR / 'comparacao_frequencias_tres_obras.png'}")


def carregar_militar_hits(obra_id: str) -> list[dict]:
    """Lê do kwic.csv as ocorrências válidas do campo militar."""
    hits: list[dict] = []
    with open(obra_dir(obra_id) /  "csv" / "kwic.csv") as f:
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


def filtrar_war_descritivos(hits: list[dict], obra_id: str) -> list[dict]:
    """Remove ocorrências de war/wars classificadas como descritivo.

    Cruza por assinatura (termo, sufixo do contexto_antes, prefixo do
    contexto_depois). O campo pagina foi removido da assinatura porque
    o kwic.csv em uso na 2026-05-23 grava todas as ocorrências com
    pagina=1 (extração em bloco único), enquanto os CSVs de classificação
    preservam páginas reais. A assinatura por contexto é suficiente para
    identificar ocorrências univocamente.

    A classificação por obra está em refinamento/war_<obra>_classificacao.csv
    (SIA e PAN). LL86 não tem CSV de classificação porque a contagem
    refinada é tratada apenas no agregado (subtração de 2 ocorrências
    descritivas em MILITAR_REFINADO).
    """
    nome_csv = WAR_CLASSIFICACAO.get(obra_id)
    if nome_csv is None:
        return hits

    caminho = REPO / "outputs" / "etapa1" / "refinamento" / nome_csv
    descritivos: set[tuple] = set()
    with open(caminho) as f:
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


def figura_2_densidade_militar() -> None:
    """Curva de densidade do campo militar ao longo de SIA e Pandora."""
    janela = 1000
    passo = 200

    paineis = [
        ("latour_1987_science_action_en", "Science in Action"),
        ("latour_1999_pandora_en", "Pandora's Hope"),
    ]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    if not isinstance(axes, np.ndarray):
        axes = np.array([axes])

    for ax, (obra_id, rotulo) in zip(axes, paineis):
        txt = (REPO / "corpus" / "txt_norm" / f"{obra_id}.txt").read_text(encoding="utf-8")
        hits = carregar_militar_hits(obra_id)
        hits = filtrar_war_descritivos(hits, obra_id)
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
            0.01,
            0.95,
            rotulo,
            transform=ax.transAxes,
            fontsize=10,
            va="top",
            ha="left",
            color="#303030",
            fontweight="bold",
        )
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="x", alpha=0.3, linewidth=0.5)
        ax.set_axisbelow(True)

    axes[-1].set_xlabel("Posição no texto (milhares de palavras)", fontsize=10)

    fig.text(
        0.99, 0.005,
        "Versão simétrica: war/wars descritivos removidos em ambas as obras "
        "(refinamento/war_{sia,pandora}_classificacao.csv).",
        ha="right", va="bottom", fontsize=8, color="#606060",
    )

    fig.tight_layout(rect=(0, 0.02, 1, 1))
    salvar(fig, "densidade_militar_sia_pandora")
    print(f"  figura 2 salva: {OUT_DIR / 'densidade_militar_sia_pandora.png'}")


def recomputar_cocorrencia_sia(janela_palavras: int = 100) -> dict[tuple[str, str], int]:
    """Recalcula cocorrência a partir do kwic.csv em janela menor.

    Mesma heurística de scripts/05_cooccurrence.py: aproxima a janela
    em palavras pelo número de caracteres, usando média de 5,5
    chars/palavra. O cocorrencia.csv versionado é gerado em janela 200;
    aqui uso 100 por exigência do briefing.
    """
    media_chars = 5.5
    janela_chars = int(janela_palavras * media_chars)

    ocs: list[tuple[str, int]] = []
    caminho = obra_dir("latour_1987_science_action_en") / "csv" / "kwic.csv"
    with open(caminho) as f:
        for row in csv.DictReader(f):
            if row.get("descartado_por_exclusao", "0") != "0":
                continue
            try:
                ocs.append((row["grupo"], int(row["posicao_no_texto"])))
            except (KeyError, ValueError):
                continue
    ocs.sort(key=lambda x: x[1])

    pares: dict[tuple[str, str], int] = defaultdict(int)
    for i, (gi, pi) in enumerate(ocs):
        for j in range(i + 1, len(ocs)):
            gj, pj = ocs[j]
            if pj - pi > janela_chars:
                break
            if gi == gj:
                continue
            chave = tuple(sorted([gi, gj]))
            pares[chave] += 1
    return pares


def figura_3_rede_cocorrencia() -> None:
    """Grafo de cocorrências em SIA 1987 com militar como nó destacado."""
    pares = recomputar_cocorrencia_sia(janela_palavras=100)
    n_absoluto = carregar_n_absoluto("latour_1987_science_action_en")
    n_absoluto["militar"] = MILITAR_REFINADO["latour_1987_science_action_en"]["n"]

    limiar = 5
    G = nx.Graph()
    for (a, b), w in pares.items():
        if w >= limiar:
            G.add_edge(a, b, weight=w)

    if "militar" not in G.nodes():
        raise RuntimeError("nó 'militar' ausente do grafo; revisar dados de entrada")

    # Layout: spring com militar fixo no centro para evitar que o nó
    # mais conectado fique deslocado pela inicialização aleatória.
    pos_inicial = {n: (np.cos(2 * np.pi * i / len(G)) * 0.5,
                       np.sin(2 * np.pi * i / len(G)) * 0.5)
                   for i, n in enumerate(G.nodes())}
    pos_inicial["militar"] = (0.0, 0.0)
    pos = nx.spring_layout(
        G,
        pos=pos_inicial,
        fixed=["militar"],
        seed=42,
        k=1.2,
        iterations=200,
    )

    fig, ax = plt.subplots(figsize=(12, 10))

    pesos = np.array([G[u][v]["weight"] for u, v in G.edges()])
    peso_max = pesos.max() if len(pesos) else 1
    larguras = 0.4 + 4.0 * (pesos / peso_max)
    cores_arestas = [
        plt.cm.Greys(0.35 + 0.5 * (w / peso_max)) for w in pesos
    ]
    nx.draw_networkx_edges(
        G, pos, ax=ax,
        width=larguras,
        edge_color=cores_arestas,
        alpha=0.85,
    )

    # Tamanho do nó proporcional à frequência absoluta em SIA. Aplico
    # raiz para comprimir a escala (militar é muito maior que os outros).
    freqs = np.array([n_absoluto.get(node, 1) for node in G.nodes()])
    sizes = 80 + 60 * np.sqrt(freqs)
    cores_nos = [
        "#B22222" if node == "militar" else "#808080"
        for node in G.nodes()
    ]
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_size=sizes,
        node_color=cores_nos,
        edgecolors="#303030",
        linewidths=0.8,
    )

    # Rótulos com caixa branca semitransparente para reduzir sobreposição
    labels = {n: n for n in G.nodes()}
    label_options = dict(
        font_size=9,
        font_family="DejaVu Sans",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.75, pad=1.2),
    )
    nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, **label_options)

    ax.set_axis_off()
    ax.text(
        0.99, 0.01,
        f"Arestas: limiar mínimo de {limiar} cocorrências. Janela: 100 palavras.",
        transform=ax.transAxes,
        ha="right", va="bottom",
        fontsize=8, color="#505050",
    )

    salvar(fig, "rede_cocorrencia_sia")
    print(f"  figura 3 salva: {OUT_DIR / 'rede_cocorrencia_sia.png'}")


# -------------------------------------------------------------------
# Figuras 4-6: ranking absoluto por obra com contagem refinada do
# campo militar e destaque cromático em vermelho ferrugem.
# As figuras 4 e 5 substituem B4 e B7 do inventário; a figura 6 é o
# painel combinado das três obras (B1 + B4 + B7).
# -------------------------------------------------------------------

OBRAS_ROTULO = {
    "latour_woolgar_1986_lab_life_en": "Laboratory Life",
    "latour_1987_science_action_en": "Science in Action",
    "latour_1999_pandora_en": "Pandora's Hope",
}


def desenhar_ranking_absoluto(ax, obra_id: str, mostrar_xlabel: bool = True) -> None:
    """Plota barras horizontais com n_ocorrencias por campo na obra.

    A barra do campo militar usa a contagem refinada do passo 1
    (Lab Life 37, SIA 364, Pandora 156) e cor vermelho ferrugem.
    Os demais campos ficam em cinza médio. Ordenação decrescente
    por contagem dentro de cada obra. Anotações inline à direita
    das barras com o valor absoluto.
    """
    n_abs = carregar_n_absoluto(obra_id)
    n_abs["militar"] = MILITAR_REFINADO[obra_id]["n"]

    campos = sorted(n_abs.keys(), key=lambda g: -n_abs[g])
    valores = [n_abs[g] for g in campos]
    cores = ["#B22222" if g == "militar" else "#808080" for g in campos]

    y = np.arange(len(campos))
    ax.barh(y, valores, color=cores, edgecolor="white", linewidth=0.3)
    ax.set_yticks(y)
    ax.set_yticklabels(campos, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, max(valores) * 1.12)
    if mostrar_xlabel:
        ax.set_xlabel("Ocorrências válidas (após exclusões)", fontsize=10)
    ax.grid(axis="x", alpha=0.3, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for i, v in enumerate(valores):
        ax.text(
            v + max(valores) * 0.01,
            i,
            f" {v}",
            va="center",
            ha="left",
            fontsize=8,
            color="#303030",
            fontweight="bold" if campos[i] == "militar" else "normal",
        )

    ax.text(
        0.99, 0.02,
        OBRAS_ROTULO[obra_id],
        transform=ax.transAxes,
        ha="right", va="bottom",
        fontsize=10, color="#303030",
        fontweight="bold",
    )


def figura_4_frequencia_sia_refinada() -> None:
    """B4 refinada: ranking absoluto em SIA, militar em vermelho ferrugem."""
    fig, ax = plt.subplots(figsize=(10, 7))
    desenhar_ranking_absoluto(ax, "latour_1987_science_action_en")
    salvar(fig, "frequencia_grupos_sia_refinada")
    print(f"  figura 4 salva: {OUT_DIR / 'frequencia_grupos_sia_refinada.png'}")


def figura_5_frequencia_pandora_refinada() -> None:
    """B7 refinada: ranking absoluto em Pandora, militar em vermelho ferrugem."""
    fig, ax = plt.subplots(figsize=(10, 7))
    desenhar_ranking_absoluto(ax, "latour_1999_pandora_en")
    salvar(fig, "frequencia_grupos_pandora_refinada")
    print(f"  figura 5 salva: {OUT_DIR / 'frequencia_grupos_pandora_refinada.png'}")


def figura_6_painel_tres_obras() -> None:
    """Painel combinado: rankings absolutos das três obras (B1 + B4 + B7).

    Três painéis empilhados verticalmente, cada um com a sua ordenação
    própria. Eixo X independente por painel (escalas absolutas diferem
    bastante entre as obras). Militar refinado em vermelho ferrugem.
    """
    fig, axes = plt.subplots(3, 1, figsize=(11, 14))
    for ax, (obra_id, _ano) in zip(axes, OBRAS_ANO):
        desenhar_ranking_absoluto(ax, obra_id, mostrar_xlabel=False)
    axes[-1].set_xlabel("Ocorrências válidas (após exclusões)", fontsize=10)
    fig.tight_layout()
    salvar(fig, "frequencia_grupos_tres_obras_painel")
    print(f"  figura 6 salva: {OUT_DIR / 'frequencia_grupos_tres_obras_painel.png'}")


if __name__ == "__main__":
    estilo_matplotlib()
    print("Gerando figura 1 (comparação 17 campos × 3 obras)")
    figura_1_comparacao_frequencias()
    print("Gerando figura 2 (densidade militar ao longo dos textos)")
    figura_2_densidade_militar()
    print("Gerando figura 3 (rede de cocorrência em SIA)")
    figura_3_rede_cocorrencia()
    print("Gerando figura 4 (ranking absoluto SIA com militar refinado)")
    figura_4_frequencia_sia_refinada()
    print("Gerando figura 5 (ranking absoluto Pandora com militar refinado)")
    figura_5_frequencia_pandora_refinada()
    print("Gerando figura 6 (painel das três obras, rankings absolutos)")
    figura_6_painel_tres_obras()
    print(f"Gráficos salvos em {OUT_DIR}")
