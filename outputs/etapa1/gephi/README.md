# Rede de coocorrência de lemas para Gephi

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
