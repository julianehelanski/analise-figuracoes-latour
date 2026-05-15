"""Tabela comparativa das 5 obras com Recalling em versao bis.

Substitui a coluna 'Recalling 1999' da Tabela tab:figuracoes_latour_5_obras
da Etapa 2 original pela contagem da Etapa 2-bis (corpus integral, 4.825
palavras), mantendo as demais colunas inalteradas. Genera tambem versoes
em CSV.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = REPO_ROOT / "outputs"
ETAPA2BIS_DIR = OUTPUTS_DIR / "etapa2bis_artigos"

ORDEM_OBRAS = [
    ("latour_woolgar_1986_lab_life_en", "Lab Life 1986", r"\emph{Laboratory Life} (1986)", 105749),
    ("latour_1987_science_action_en", "Sci. in Action 1987", r"\emph{Science in Action} (1987)", 139861),
    ("latour_1999_pandora_en", "Pandora 1999", r"\emph{Pandora's Hope} (1999)", 128001),
    ("latour_1996_clarifications_en", "Clarifications 1996", r"\emph{Clarifications} (1996)", 7848),
    ("latour_1999_recalling_bis", "Recalling 1999 (bis)", r"\emph{Recalling ANT} (1999, bis)", 4825),
]

ORDEM_GRUPOS = [
    "inscription", "immutable_mobile", "black_box", "centre_of_calculation",
    "actor_network", "translation", "trial_of_strength", "factish",
    "circulating_reference", "articulation", "construction", "proposition",
    "network", "agonistic", "enrollment", "spokesperson", "militar",
    "textil", "topologia",
]


def carregar_freq(obra_id: str) -> dict[str, int]:
    p = OUTPUTS_DIR / obra_id / "csv" / "frequencias.csv"
    cont: dict[str, int] = {}
    if not p.exists():
        return cont
    with p.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            cont[row["grupo"]] = int(row["n_ocorrencias"])
    return cont


def main() -> None:
    ETAPA2BIS_DIR.mkdir(parents=True, exist_ok=True)
    contagens = {oid: carregar_freq(oid) for oid, _, _, _ in ORDEM_OBRAS}

    # CSV absoluto
    csv_n = ETAPA2BIS_DIR / "tabela_comparativa_5_obras_bis_n.csv"
    with csv_n.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["obra", "palavras_total"] + ORDEM_GRUPOS)
        for oid, _, _, pal in ORDEM_OBRAS:
            w.writerow([oid, pal] + [contagens[oid].get(g, 0) for g in ORDEM_GRUPOS])
    print(f"  gravado: {csv_n.relative_to(REPO_ROOT)}")

    # CSV densidade
    csv_f = ETAPA2BIS_DIR / "tabela_comparativa_5_obras_bis_freq.csv"
    with csv_f.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["obra", "palavras_total"] + ORDEM_GRUPOS)
        for oid, _, _, pal in ORDEM_OBRAS:
            linha = [oid, pal]
            for g in ORDEM_GRUPOS:
                n = contagens[oid].get(g, 0)
                linha.append(f"{n/pal*10000:.2f}")
            w.writerow(linha)
    print(f"  gravado: {csv_f.relative_to(REPO_ROOT)}")

    # LaTeX
    tex_p = ETAPA2BIS_DIR / "tabela_comparativa_5_obras_bis.tex"
    linhas = [
        r"% Tabela comparativa 5 obras com Recalling em versao bis (Etapa 2-bis).",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Densidade dos campos figurativos nas tres obras monograficas "
        r"e nos dois artigos metateoricos de Latour (Etapa 2-bis: Recalling em "
        r"corpus integral de 4.825 palavras). Densidade por 10.000 palavras; "
        r"contagem absoluta entre parenteses.}",
        r"\label{tab:figuracoes_latour_5_obras_bis}",
        r"\small",
        r"\begin{tabular}{l" + "r" * len(ORDEM_OBRAS) + r"}",
        r"\toprule",
    ]
    cab = [r"Campo figurativo"] + [rotulo.replace("_", r"\_")
                                    for _, _, rotulo, _ in ORDEM_OBRAS]
    linhas.append(" & ".join(cab) + r" \\")
    linhas.append(r"\midrule")
    pal_linha = [r"\textit{Palavras totais}"]
    for _, _, _, pal in ORDEM_OBRAS:
        pal_linha.append(rf"\textit{{{pal:,}}}".replace(",", r"\,"))
    linhas.append(" & ".join(pal_linha) + r" \\")
    linhas.append(r"\midrule")
    for g in ORDEM_GRUPOS:
        celulas = [g.replace("_", r"\_")]
        for oid, _, _, pal in ORDEM_OBRAS:
            n = contagens[oid].get(g, 0)
            if n > 0:
                freq = n / pal * 10000
                celulas.append(rf"{freq:.2f} ({n})".replace(".", "{,}", 1))
            else:
                celulas.append(r"--")
        linhas.append(" & ".join(celulas) + r" \\")
    linhas += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex_p.write_text("\n".join(linhas), encoding="utf-8")
    print(f"  gravado: {tex_p.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
