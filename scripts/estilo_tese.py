# -*- coding: utf-8 -*-
"""Identidade visual compartilhada das figuras da tese (lexicometria Latour).

Espelha a paleta-mestra adotada nas figuras bibliométricas do capítulo 2
(repositório bibliometria-ia-humanas): categórico Okabe-Ito (à prova de
daltonismo), sequencial viridis, marcador "bolinha" com borda branca, dot
plot de Cleveland e estilo editorial (sem molduras/grade), além da notação
numérica em português brasileiro (milhar com ponto, decimal com vírgula).

Mantido autônomo (sem dependência externa) para o repo continuar
reproduzível por conta própria.
"""
from __future__ import annotations

import matplotlib.pyplot as plt

# --- Paleta categórica Okabe-Ito -------------------------------------------
OKABE_ITO = {
    "preto": "#000000", "laranja": "#E69F00", "azul_claro": "#56B4E9",
    "verde": "#009E73", "amarelo": "#F0E442", "azul": "#0072B2",
    "vermelho": "#D55E00", "roxo": "#CC79A7", "cinza": "#999999",
}
# Cor-assinatura dos campos figurativos nesta análise (azul Okabe-Ito) e
# destaque magenta para o campo em foco analítico (militar).
COR_CAMPO = "#0072B2"        # azul: campos figurativos em geral
COR_DESTAQUE = "#CC79A7"     # magenta: campo em foco (militar)
COR_TEXTIL = "#009E73"       # verde: campo têxtil (contraponto haraway)
COR_NEUTRO = "#999999"       # cinza
# Catálogo duplo (AIME): proveniência antiga vs nova.
COR_CAT_ANTIGO = "#0072B2"   # azul: catálogo antigo (Etapas 1--2)
COR_CAT_NOVO = "#E69F00"     # laranja: catálogo novo (Etapa 3)
CMAP_SEQUENCIAL = "viridis"

GUIA_COR = "#e9eef2"
# Texto em cinza escuro suave (nada de preto puro), sem negrito; notas e
# secundário em cinza médio. Sem título embutido (a legenda do LaTeX titula).
_TXT = "#404040"
_TXT_FRACO = "#8a8a8a"
FONTE = "DejaVu Sans"
PONTO_S = 150

# Ordem perceptual para quando há mais categorias que o Okabe-Ito comporta
# (densidade empilhada, com 16--20 campos): começa pelo Okabe-Ito e estende
# com tons intermediários distinguíveis, evitando o arco-íris saturado.
_EXTENSAO = [
    "#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#D55E00",
    "#F0E442", "#999999", "#3a5fa0", "#b5651d", "#1b7a5a", "#8e4585",
    "#7fb2d6", "#a04000", "#c9b037", "#5a5a5a", "#264f78", "#d98c5f",
    "#2e8b57", "#b76e9b",
]


def cor_categorica(n: int) -> list[str]:
    """Devolve ``n`` cores categóricas, partindo do Okabe-Ito.

    Para ``n`` até 8, usa o núcleo Okabe-Ito; acima disso, estende com tons
    adicionais distinguíveis (sem cair no arco-íris). Cicla se ``n`` passar
    do tamanho da extensão.
    """
    if n <= 0:
        return []
    return [_EXTENSAO[i % len(_EXTENSAO)] for i in range(n)]


def num_ptbr(valor) -> str:
    """Inteiro pt-BR: ponto como separador de milhar (5284 -> "5.284")."""
    return f"{int(round(valor)):,}".replace(",", ".")


def pct_ptbr(valor, casas: int = 1) -> str:
    """Número pt-BR com vírgula decimal (40.66 -> "40,7"), sem o '%'."""
    return f"{valor:,.{casas}f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def _tick_ptbr(x, pos=None) -> str:
    if float(x).is_integer():
        return num_ptbr(int(round(x)))
    return f"{x:g}".replace(".", ",")


def eixo_ptbr(ax, eixo: str = "x") -> None:
    """Notação pt-BR nos ticks de um eixo NUMÉRICO (x, y ou ambos)."""
    from matplotlib.ticker import FuncFormatter
    fmt = FuncFormatter(_tick_ptbr)
    if eixo in ("x", "ambos"):
        ax.xaxis.set_major_formatter(fmt)
    if eixo in ("y", "ambos"):
        ax.yaxis.set_major_formatter(fmt)


def aplicar_rcparams() -> None:
    """rcParams editoriais: fundo branco, fontes sóbrias, sem molduras top/dir."""
    plt.rcParams.update({
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "figure.dpi": 100,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "font.size": 10,
        "font.family": "DejaVu Sans",
    })


def estilo_editorial(ax) -> None:
    """Remove molduras, grade e ticks (para dot plots e painéis limpos)."""
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(left=False, bottom=False)
    ax.grid(False)


def dotplot(ax, labels, vals, cores, rotulos=None) -> None:
    """Dot plot de Cleveland com linha-guia e marcador-identidade (bolinha).

    labels: categorias (eixo Y, do menor para o maior). vals: valores.
    cores: cor por ponto (lista) ou cor única (str). rotulos: rótulo já
    formatado por ponto; se None, usa ``num_ptbr(val)``. O número fica à
    direita da bolinha com folga fixa em pontos (não encosta no marcador).
    """
    n = len(labels)
    y = list(range(n))
    mx = max(vals) if vals else 1
    if isinstance(cores, str):
        cores = [cores] * n
    for i, v in enumerate(vals):
        ax.plot([0, v], [i, i], color=GUIA_COR, linewidth=1.2, zorder=1)
    ax.scatter(vals, y, s=PONTO_S, color=cores, zorder=3, edgecolors="white",
               linewidths=1.4)
    for i, v in enumerate(vals):
        txt = rotulos[i] if rotulos is not None else num_ptbr(v)
        ax.annotate(txt, xy=(v, i), xytext=(11, 0), textcoords="offset points",
                    va="center", ha="left", fontsize=9.5, color=_TXT)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9, color=_TXT)
    ax.set_xticks([])
    ax.set_xlim(0, mx * 1.42)
    ax.set_ylim(-0.6, n - 0.4)
    estilo_editorial(ax)


def dumbbell(ax, labels, series, cores) -> None:
    """Dumbbell: por categoria, um ponto por série ligado por linha-guia.

    labels: categorias (eixo Y). series: dict {nome: [valores]}. cores:
    dict {nome: cor}. Mantém grade vertical sutil e remove molduras.
    """
    n = len(labels)
    y = list(range(n))
    nomes = list(series.keys())
    todos = [v for s in series.values() for v in s]
    mx = max(todos) if todos else 1
    for i in range(n):
        pontos = [series[nm][i] for nm in nomes]
        ax.plot([min(pontos), max(pontos)], [i, i], color=GUIA_COR,
                linewidth=2.4, zorder=1, solid_capstyle="round")
    for nm in nomes:
        ax.scatter(series[nm], y, s=150, color=cores[nm], zorder=3,
                   edgecolors="white", linewidths=1.4, label=nm)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9, color=_TXT)
    ax.set_xlim(0, mx * 1.12)
    ax.set_ylim(-0.6, n - 0.4)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(left=False, bottom=False)
    ax.grid(axis="x", linestyle=":", linewidth=0.6, color="#dddddd", zorder=0)
