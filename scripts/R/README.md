# scripts/R

Camada em R do pipeline. Hoje contém apenas a análise Reinert + AFC sobre as três obras de Latour da Etapa 1.

## Pré-requisitos (Windows + RStudio + R via Anaconda)

No Anaconda Prompt:

```bash
conda create -n latour-r -c conda-forge ^
    r-base r-essentials r-quanteda r-factominer r-factoextra ^
    r-tidyverse r-ggrepel
conda activate latour-r
```

Pacotes que ficam mais atualizados via CRAN, instalados dentro do R:

```r
install.packages(c("rainette", "udpipe"),
                 repos = "https://cloud.r-project.org")
```

No RStudio, apontar para o R do env conda em `Tools > Global Options > General > R version`. O executável fica em `C:\Users\<seu_usuario>\anaconda3\envs\latour-r\Lib\R\bin\x64\R.exe`.

## Como rodar

1. Abrir o projeto no RStudio (`File > Open Project` no `.Rproj` da raiz; se ainda não existir, basta abrir a pasta e usar `Session > Set Working Directory > Choose Directory` apontando para a raiz do repositório).
2. Abrir `scripts/R/10_reinert_afc.R`.
3. Executar o script inteiro (`Ctrl+Shift+Enter` ou `Source`).

Na primeira execução o script baixa o modelo udpipe `english-ewt` (cerca de 15 MB) para `udpipe_models/` e gera os arquivos lematizados em `corpus/txt_lemma_en/`. Execuções subsequentes reaproveitam ambos.

## O que o script faz

1. Lê os três `corpus/txt_norm/*.txt` em escopo da Etapa 1.
2. Lematiza via `udpipe` (english-ewt), descartando pontuação, numerais e símbolos. Lemas em caixa baixa.
3. Constrói o corpus no `quanteda` e segmenta em STs de cerca de 40 ocorrências, replicando o padrão IRaMuTeQ.
4. Roda a Reinert (CHD) via `rainette` com k = 6 classes.
5. Salva o dendrograma com os 20 lemas mais característicos de cada classe (`reinert_dendrograma.png`).
6. Roda duas AFCs via `FactoMineR::CA`:
   - lema x classe Reinert (`afc_classes_reinert.png`)
   - lema x obra (`afc_obras.png`), que é a AFC mais próxima do argumento do capítulo 2 sobre a trajetória 1986-1999.
7. Exporta perfis de classe, coordenadas fatoriais e distribuição de classes por obra em CSV.

## Saídas

Todas em `outputs/etapa1/reinert_afc/`:

- `reinert_dendrograma.png`
- `afc_classes_reinert.png`
- `afc_obras.png`
- `perfis_classe_NN.csv` (um por classe Reinert)
- `afc_classes_coordenadas_lemas.csv`
- `afc_classes_coordenadas_classes.csv`
- `afc_obras_coordenadas_lemas.csv`
- `afc_obras_coordenadas_obras.csv`
- `distribuicao_classes_por_obra.csv`

## Observações metodológicas

- Seed fixa em 42 (CLAUDE.md).
- Stopwords inglesas removidas via `quanteda::stopwords("en")`, lemas com menos de 3 caracteres descartados.
- Termos presentes em menos de 3 STs descartados (`min_docfreq = 3`) para estabilizar a Reinert.
- STs vazios após filtragem são removidos antes da CHD.
- AFC visual limitada aos 250 lemas com maior frequência total, para gráfico legível. As coordenadas completas saem nos CSVs.
