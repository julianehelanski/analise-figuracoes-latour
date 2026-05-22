"""Exporta rede de coocorrência de lemas para Gephi.

Ramo paralelo experimental do pipeline da Etapa 1.

Constrói uma rede não dirigida em que:
- nós são lemas (cada lema é um nó único, com sua frequência total);
- arestas conectam dois lemas que aparecem juntos no mesmo ST
  (segmento de texto de 40 lemas, igual ao padrão IRaMuTeQ usado
  pelo `scripts/R/10_reinert_afc.R`);
- peso da aresta é o número de STs em que os dois lemas coocorrem.

Cada nó recebe atributos adicionais úteis para o Gephi:
- `Obra_dominante`: obra em que o lema tem maior frequência relativa;
- `Classe_reinert`: classe Reinert mais associada ao lema, lida dos
  CSVs `perfis_classe_XX.csv` gerados pelo script R. Lemas que não
  aparecem em nenhum perfil ficam com `Classe_reinert = "outro"`.

Saídas:
- `outputs/etapa1/gephi/nodes.csv`
- `outputs/etapa1/gephi/edges.csv`
- `outputs/etapa1/gephi/README.md` (instruções de importação)

Filtros padrão (suficientes para uma rede com cerca de 250 nós,
tratável no Gephi sem prejuízo de leitura):
- top 250 lemas por frequência total;
- mínimo de 3 coocorrências por aresta;
- stopwords inglesas removidas, lemas com menos de 3 caracteres
  descartados (replica o filtro do dfm do R).

Uso:
    python scripts/11_export_gephi.py
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path

import pandas as pd

SEED = 42
TAMANHO_ST = 40
TOP_LEMAS = 250
MIN_PESO_ARESTA = 3

RAIZ = Path(__file__).resolve().parent.parent
DIR_LEMMA = RAIZ / "corpus" / "txt_lemma_en"
DIR_PERFIS = RAIZ / "outputs" / "etapa1" / "reinert_afc"
DIR_SAIDA = RAIZ / "outputs" / "etapa1" / "gephi"

OBRAS = {
    "lab_life_1986": "latour_woolgar_1986_lab_life_en_lemma.txt",
    "science_1987": "latour_1987_science_action_en_lemma.txt",
    "pandora_1999": "latour_1999_pandora_en_lemma.txt",
}

# Lista enxuta de stopwords inglesas, alinhada com quanteda::stopwords("en").
# Mantida inline para evitar dependência de download em runtime.
STOPWORDS_EN: frozenset[str] = frozenset({
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
    "your", "yours", "yourself", "yourselves", "he", "him", "his",
    "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which",
    "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having",
    "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while", "of", "at", "by", "for",
    "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further",
    "then", "once", "here", "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more", "most", "other", "some",
    "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should",
    "now", "would", "could", "should", "ought", "may", "might", "must",
    "shall", "also", "let", "us", "yes", "even", "still", "well", "thus",
    "however", "therefore", "hence",
})


def segmentar(lemas: list[str], tamanho: int = TAMANHO_ST) -> list[list[str]]:
    """Divide uma lista de lemas em STs de tamanho fixo."""
    return [lemas[i : i + tamanho] for i in range(0, len(lemas), tamanho)]


def carregar_lemas_obra(caminho: Path) -> list[str]:
    """Lê um arquivo de lemas e devolve a lista após filtros básicos."""
    texto = caminho.read_text(encoding="utf-8")
    lemas = [
        lema for lema in texto.split()
        if len(lema) >= 3
        and lema.isalpha()
        and lema not in STOPWORDS_EN
    ]
    return lemas


def carregar_perfis_reinert(dir_perfis: Path) -> dict[str, str]:
    """Lê os 6 perfis_classe_XX.csv e devolve mapeamento lema -> classe.

    Quando um lema aparece em mais de uma classe (raro, dado o chi²
    do Reinert), prevalece a classe em que tem maior chi².
    """
    melhor_chi2: dict[str, tuple[float, str]] = {}
    for i in range(1, 7):
        caminho = dir_perfis / f"perfis_classe_{i:02d}.csv"
        if not caminho.exists():
            continue
        df = pd.read_csv(caminho)
        classe = f"Classe {i}"
        for _, linha in df.iterrows():
            lema = str(linha["feature"])
            chi2 = float(linha["chi2"])
            anterior = melhor_chi2.get(lema)
            if anterior is None or chi2 > anterior[0]:
                melhor_chi2[lema] = (chi2, classe)
    return {lema: classe for lema, (_, classe) in melhor_chi2.items()}


def main() -> None:
    DIR_SAIDA.mkdir(parents=True, exist_ok=True)

    # 1. Carrega lemas por obra e segmenta em STs.
    sts: list[tuple[str, list[str]]] = []
    freq_por_obra: dict[str, Counter[str]] = {obra: Counter() for obra in OBRAS}

    for obra, arquivo in OBRAS.items():
        lemas = carregar_lemas_obra(DIR_LEMMA / arquivo)
        freq_por_obra[obra].update(lemas)
        for st in segmentar(lemas):
            sts.append((obra, st))

    print(f"Total de STs: {len(sts)}")

    # 2. Frequência total e seleção dos top N lemas.
    freq_total: Counter[str] = Counter()
    for cnt in freq_por_obra.values():
        freq_total.update(cnt)

    top_lemas = {lema for lema, _ in freq_total.most_common(TOP_LEMAS)}
    print(f"Top lemas selecionados: {len(top_lemas)}")

    # 3. Coocorrência: para cada ST, todos os pares de lemas em top_lemas.
    coocorrencia: Counter[tuple[str, str]] = Counter()
    for _obra, st in sts:
        lemas_st = sorted(set(st) & top_lemas)
        for a, b in combinations(lemas_st, 2):
            coocorrencia[(a, b)] += 1

    # Filtra arestas por peso mínimo.
    arestas = [
        (a, b, peso)
        for (a, b), peso in coocorrencia.items()
        if peso >= MIN_PESO_ARESTA
    ]
    print(f"Arestas após filtro (peso >= {MIN_PESO_ARESTA}): {len(arestas)}")

    # 4. Classe Reinert por lema.
    classe_por_lema = carregar_perfis_reinert(DIR_PERFIS)

    # 5. Obra dominante por lema (maior frequência absoluta na obra).
    obra_dominante: dict[str, str] = {}
    for lema in top_lemas:
        contagens = {
            obra: freq_por_obra[obra].get(lema, 0) for obra in OBRAS
        }
        obra_dominante[lema] = max(contagens, key=lambda o: contagens[o])

    # 6. Escreve nodes.csv.
    df_nodes = pd.DataFrame({
        "Id": sorted(top_lemas),
        "Label": sorted(top_lemas),
    })
    df_nodes["Frequency"] = df_nodes["Id"].map(freq_total)
    df_nodes["Obra_dominante"] = df_nodes["Id"].map(obra_dominante)
    df_nodes["Classe_reinert"] = df_nodes["Id"].map(
        lambda lema: classe_por_lema.get(lema, "outro")
    )
    df_nodes.to_csv(DIR_SAIDA / "nodes.csv", index=False)
    print(f"Escrito: {DIR_SAIDA / 'nodes.csv'} ({len(df_nodes)} nós)")

    # 7. Escreve edges.csv.
    df_edges = pd.DataFrame(arestas, columns=["Source", "Target", "Weight"])
    df_edges["Type"] = "Undirected"
    df_edges = df_edges[["Source", "Target", "Type", "Weight"]]
    df_edges.to_csv(DIR_SAIDA / "edges.csv", index=False)
    print(f"Escrito: {DIR_SAIDA / 'edges.csv'} ({len(df_edges)} arestas)")

    # 8. README com instruções de importação no Gephi.
    readme = DIR_SAIDA / "README.md"
    readme.write_text(GEPHI_README, encoding="utf-8")
    print(f"Escrito: {readme}")


GEPHI_README = """# Rede de coocorrência de lemas para Gephi

Arquivos prontos para importação no Gephi 0.10+.

## Como importar

1. Abrir Gephi e criar um novo projeto.
2. Em `File > Import spreadsheet`, importar primeiro `nodes.csv`
   como tabela de nós.
3. Em seguida, importar `edges.csv` como tabela de arestas
   (`Source` e `Target` correspondem ao `Id` dos nós).
4. Quando perguntar, deixar marcado `Append to existing workspace`.

## Sugestões de análise

- **Layout**: ForceAtlas2 com `Prevent Overlap = true` e
  `Scaling = 10`. Deixar rodar até estabilizar.
- **Modularidade**: rodar `Statistics > Modularity` para detectar
  comunidades lexicais. Comparar com `Classe_reinert` para checar
  convergência entre os dois métodos (modularidade do Gephi vs. CHD
  do rainette).
- **Cor dos nós**: por `Classe_reinert` ou por `Obra_dominante`.
- **Tamanho dos nós**: proporcional a `Frequency`.

## Parâmetros usados na geração

- Tamanho de ST: 40 lemas.
- Top lemas por frequência total: 250.
- Peso mínimo da aresta: 3 coocorrências.
- Stopwords inglesas removidas; lemas com menos de 3 caracteres
  descartados.

Para regenerar com outros parâmetros, editar as constantes no topo
de `scripts/11_export_gephi.py`.
"""


if __name__ == "__main__":
    main()
