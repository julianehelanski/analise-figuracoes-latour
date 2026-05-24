"""Matriz de cocorrência e rede figural por obra.

Para cada obra em escopo, lê `outputs/etapa<N>/<obra_id>/csv/kwic.csv` (ocorrências
válidas) e constrói matriz de cocorrência entre grupos figurativos com
janela configurável (default: 200 palavras).

Outputs:
- `outputs/etapa<N>/<obra_id>/csv/cocorrencia.csv`: matriz simétrica grupo × grupo.
- `outputs/etapa<N>/<obra_id>/figuras/rede_cocorrencia.png`: grafo (NetworkX).
- `outputs/etapa<N>/<obra_id>/relatorios/cocorrencia.md`: lista de pares com maior
  força de cocorrência.

Comunidades por Louvain ficam comentadas: se `python-louvain` estiver
instalado, são detectadas e impressas; senão, é pulado sem erro.

Uso:
    python scripts/05_cooccurrence.py
    python scripts/05_cooccurrence.py --janela 200 --only latour_1987
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from itertools import combinations
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
METADATA_CSV = REPO_ROOT / "corpus" / "metadata.csv"
from _paths import OUTPUTS_DIR, obra_dir
CORPUS_TXT_DIR = REPO_ROOT / "corpus" / "txt_norm"


def obras_em_escopo(escopo: str = "etapa1") -> list[dict[str, str]]:
    """Filtra metadata.csv por `escopo_etapa1`, `escopo_etapa2` ou ambos."""
    with METADATA_CSV.open(encoding="utf-8", newline="") as f:
        linhas = list(csv.DictReader(f))
    def _mark(r: dict[str, str], col: str) -> bool:
        return r.get(col, "").strip().lower() == "sim"
    if escopo == "etapa1":
        return [r for r in linhas if _mark(r, "escopo_etapa1")]
    if escopo == "etapa2":
        return [r for r in linhas if _mark(r, "escopo_etapa2")]
    if escopo == "etapa2bis":
        return [r for r in linhas if _mark(r, "escopo_etapa2bis")]
    if escopo == "etapa3":
        return [r for r in linhas if _mark(r, "escopo_etapa3")]
    if escopo == "todos":
        return [r for r in linhas if _mark(r, "escopo_etapa1") or _mark(r, "escopo_etapa2")]
    raise SystemExit(f"escopo desconhecido '{escopo}'.")


# Obras cuja cocorrência cruza mais de um arquivo kwic (catálogos paralelos
# aplicados sobre o mesmo texto). A AIME (Etapa 3) aplica o catálogo antigo
# (19 campos) e o catálogo novo (12 campos) em paralelo, com um kwic cada.
KWIC_FILES_MULTIPLOS: dict[str, list[str]] = {
    "latour_2013_aime_en": ["kwic_catalogo_antigo.csv", "kwic_catalogo_aime.csv"],
}


def kwic_files_de(obra_id: str) -> list[str]:
    """Arquivos kwic a ler para uma obra (default: um único kwic.csv)."""
    return KWIC_FILES_MULTIPLOS.get(obra_id, ["kwic.csv"])


def carregar_ocorrencias(
    obra_id: str, kwic_filenames: list[str] | None = None
) -> list[tuple[str, int]]:
    """Lê um ou mais kwic.csv da obra e concatena as ocorrências válidas.

    Para a maioria das obras `kwic_filenames` é `["kwic.csv"]`. A AIME
    (Etapa 3) tem dois kwic (`kwic_catalogo_antigo.csv` e
    `kwic_catalogo_aime.csv`), concatenados aqui para que a cocorrência
    cruze os dois catálogos.
    """
    if kwic_filenames is None:
        kwic_filenames = ["kwic.csv"]
    ocs: list[tuple[str, int]] = []
    for nome in kwic_filenames:
        p = obra_dir(obra_id) / "csv" / nome
        if not p.exists():
            continue
        with p.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row.get("descartado_por_exclusao", "0") != "0":
                    continue
                try:
                    ocs.append((row["grupo"], int(row["posicao_no_texto"])))
                except (KeyError, ValueError):
                    continue
    return ocs


def cocorrencia_por_janela(
    ocs: list[tuple[str, int]],
    janela_palavras: int,
    media_chars_por_palavra: float = 5.5,
) -> dict[tuple[str, str], int]:
    """Conta pares de grupos cujas ocorrências caem em janela de N palavras.

    A janela é aproximada por `janela_palavras * media_chars_por_palavra` em
    caracteres, suficiente para a Etapa 1.
    """
    janela_chars = int(janela_palavras * media_chars_por_palavra)
    ocs_ord = sorted(ocs, key=lambda x: x[1])
    pares: dict[tuple[str, str], int] = defaultdict(int)
    n = len(ocs_ord)
    for i in range(n):
        grupo_i, pos_i = ocs_ord[i]
        for j in range(i + 1, n):
            grupo_j, pos_j = ocs_ord[j]
            if pos_j - pos_i > janela_chars:
                break
            if grupo_i == grupo_j:
                continue
            chave = tuple(sorted([grupo_i, grupo_j]))
            pares[chave] += 1
    return pares


def gerar_outputs(
    obra_id: str, janela: int, sufixo: str = "",
    kwic_filenames: list[str] | None = None,
    reportar_sobreposicao: bool = False,
) -> None:
    if kwic_filenames is None:
        kwic_filenames = ["kwic.csv"]
    ocs = carregar_ocorrencias(obra_id, kwic_filenames)
    if not ocs:
        print(f"  [pular] sem ocorrências válidas para {obra_id}.")
        return
    grupos = sorted({g for g, _ in ocs})
    pares = cocorrencia_por_janela(ocs, janela)
    sufixo_arquivo = f"_{sufixo}" if sufixo else ""

    # Sobreposição de termos: posições contadas por mais de um campo. Ocorre ao
    # concatenar catálogos paralelos (AIME: `trajectory` conta em `topologia` e
    # em `trajectory_pass`) ou quando um termo pertence a mais de um campo do
    # mesmo catálogo (Etapa 1: `circulating` conta em `circulating_reference` e
    # em `topologia`). Reportado quando há catálogos múltiplos ou quando o flag
    # `--reportar-sobreposicao` é passado. A contagem não é deduplicada.
    multiplos = len(kwic_filenames) > 1
    reportar = multiplos or reportar_sobreposicao
    overlap_pares: dict[tuple[str, str], int] = {}
    overlap_total = 0
    if reportar:
        pos_grupos: dict[int, set[str]] = defaultdict(set)
        for g, pos in ocs:
            pos_grupos[pos].add(g)
        contador: dict[tuple[str, str], int] = defaultdict(int)
        for gs in pos_grupos.values():
            if len(gs) > 1:
                overlap_total += 1
                for a, b in combinations(sorted(gs), 2):
                    contador[(a, b)] += 1
        overlap_pares = dict(contador)
        print(f"  sobreposição: {overlap_total} posições contadas por mais de um campo")
        for (a, b), n in sorted(overlap_pares.items(), key=lambda x: -x[1]):
            print(f"    {a}–{b}: {n} posições")

    csv_dir = obra_dir(obra_id) / "csv"
    csv_dir.mkdir(parents=True, exist_ok=True)
    matriz = csv_dir / f"cocorrencia{sufixo_arquivo}.csv"
    with matriz.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([""] + grupos)
        for g in grupos:
            linha = [g]
            for h in grupos:
                if g == h:
                    linha.append(0)
                else:
                    chave = tuple(sorted([g, h]))
                    linha.append(pares.get(chave, 0))
            escritor.writerow(linha)

    md = obra_dir(obra_id) / "relatorios" / f"cocorrencia{sufixo_arquivo}.md"
    md.parent.mkdir(parents=True, exist_ok=True)
    linhas: list[str] = [
        f"# Cocorrência figural: {obra_id}",
        "",
        f"Janela: {janela} palavras (aproximada por caracteres).",
        f"Pares válidos: {len(pares)}.",
        "",
        "## Top 20 pares por força de cocorrência",
        "",
        "| grupo A | grupo B | n |",
        "|---|---|---:|",
    ]
    for (a, b), n in sorted(pares.items(), key=lambda x: -x[1])[:20]:
        linhas.append(f"| {a} | {b} | {n} |")
    if reportar and overlap_total > 0:
        if multiplos:
            titulo = "## Sobreposição de termos entre catálogos"
            intro = (
                f"Posições contadas por mais de um campo: **{overlap_total}**. "
                "Ocorre quando um termo pertence a dois catálogos aplicados em "
                "paralelo sobre o mesmo texto; cada par abaixo soma pares de "
                "distância zero à cocorrência, embutidos na contagem por decisão "
                "de reprodução fiel (sem deduplicação)."
            )
        else:
            titulo = "## Sobreposição de termos entre campos do catálogo"
            intro = (
                f"Posições contadas por mais de um campo: **{overlap_total}**. "
                "Ocorre quando um termo pertence a mais de um campo do catálogo; "
                "cada par abaixo soma pares de distância zero à cocorrência, "
                "mantidos sem deduplicação."
            )
        linhas += [
            "", titulo, "", intro, "",
            "| campo A | campo B | posições compartilhadas |",
            "|---|---|---:|",
        ]
        for (a, b), n in sorted(overlap_pares.items(), key=lambda x: -x[1]):
            linhas.append(f"| {a} | {b} | {n} |")
    md.write_text("\n".join(linhas), encoding="utf-8")

    # Figura: NetworkX -----------------------------------------------------
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import networkx as nx
    except ImportError:
        print("  (matplotlib/networkx ausentes; pulei a figura).")
        return

    G = nx.Graph()
    contagem_grupo: dict[str, int] = defaultdict(int)
    for g, _ in ocs:
        contagem_grupo[g] += 1
    for g in grupos:
        G.add_node(g, freq=contagem_grupo[g])
    for (a, b), n in pares.items():
        if n > 0:
            G.add_edge(a, b, weight=n)

    if G.number_of_edges() == 0:
        print("  (nenhuma cocorrência detectada; sem figura).")
        return

    fig_dir = obra_dir(obra_id) / "figuras"
    fig_dir.mkdir(parents=True, exist_ok=True)
    pos = nx.spring_layout(G, seed=42, weight="weight")
    fig, ax = plt.subplots(figsize=(9, 7))
    tamanhos = [200 + 80 * G.nodes[n]["freq"] ** 0.5 for n in G.nodes()]
    larguras = [0.4 + 0.3 * G.edges[e]["weight"] ** 0.5 for e in G.edges()]
    nx.draw_networkx_nodes(G, pos, node_size=tamanhos, node_color="#4c72b0",
                           edgecolors="white", linewidths=1.5, ax=ax)
    nx.draw_networkx_edges(G, pos, width=larguras, alpha=0.45, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=8, ax=ax)
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(fig_dir / f"rede_cocorrencia{sufixo_arquivo}.png", dpi=300)
    fig.savefig(fig_dir / f"rede_cocorrencia{sufixo_arquivo}.svg")
    plt.close(fig)

    # Louvain opcional
    try:
        import community as community_louvain  # python-louvain
        particao = community_louvain.best_partition(G, weight="weight", random_state=42)
        clusters: dict[int, list[str]] = defaultdict(list)
        for node, cid in particao.items():
            clusters[cid].append(node)
        with (md.parent / f"cocorrencia_clusters{sufixo_arquivo}.md").open("w", encoding="utf-8") as f:
            f.write(f"# Clusters Louvain: {obra_id}\n\n")
            for cid, nodes in sorted(clusters.items()):
                f.write(f"## Cluster {cid} (n={len(nodes)})\n\n")
                for n in sorted(nodes):
                    f.write(f"- {n}\n")
                f.write("\n")
    except ImportError:
        pass

    print(f"  gravado: outputs/{obra_id}/csv/cocorrencia{sufixo_arquivo}.csv")
    print(f"  gravado: outputs/{obra_id}/figuras/rede_cocorrencia{sufixo_arquivo}.png")
    print(f"  gravado: outputs/{obra_id}/relatorios/cocorrencia{sufixo_arquivo}.md")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", help="filtra obras por substring de id.")
    parser.add_argument("--janela", type=int, default=200,
                        help="janela em palavras para cocorrência (default: 200).")
    parser.add_argument("--escopo", default="etapa1",
                        choices=["etapa1", "etapa2", "etapa2bis", "etapa3", "todos"],
                        help="filtro de obras: etapa1 (default), etapa2, "
                             "etapa2bis, etapa3 (AIME, dois catálogos) ou todos.")
    parser.add_argument("--sufixo", default="",
                        help="sufixo nos nomes de arquivo de saída "
                             "(default: vazio, sobrescreve cocorrencia.csv).")
    parser.add_argument("--reportar-sobreposicao", action="store_true",
                        help="reporta posições contadas por mais de um campo "
                             "(stdout e .md), mesmo com kwic único. Catálogos "
                             "múltiplos já reportam automaticamente.")
    args = parser.parse_args()

    obras = obras_em_escopo(args.escopo)
    if args.only:
        obras = [o for o in obras if args.only.lower() in o["id"].lower()]
    for obra in obras:
        print(f"\n[{obra['id']}]")
        gerar_outputs(obra["id"], args.janela, args.sufixo,
                      kwic_files_de(obra["id"]),
                      reportar_sobreposicao=args.reportar_sobreposicao)


if __name__ == "__main__":
    main()
