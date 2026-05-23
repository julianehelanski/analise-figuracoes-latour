# Inventário de figuras da análise

Referência aberta para escolha e redação de legendas. Cada entrada lista o nome do arquivo, o que a figura mostra (tipo de gráfico, obras representadas, campos figurativos exibidos, parâmetros visuais relevantes) e a pasta do repositório.

Versão LaTeX com blocos `\begin{figure}` prontos: `outputs/latex/inventario_figuras.tex`.

Total de figuras únicas inventariadas: **29 existentes no repo + 1 prevista pelo script Reinert/AFC, ainda não gerada** = 30. PNG e SVG no diretório canônico; PNG com nomes desambiguados no espelho `outputs/consolidado/figuras/` quando aplicável.

Catálogo de campos figurativos: `campos_lexicais/catalogo_termos.yaml`.

Auditoria de 2026-05-23: cada entrada foi verificada contra o script gerador. Discrepâncias entre versão anterior e o que os scripts efetivamente produzem foram corrigidas; pontos onde a figura difere do que se esperaria pelo nome do arquivo estão sinalizados com **ATENÇÃO**.

---

## Convenções

### Obras (siglas usadas abaixo)

- **LL86** = *Laboratory Life* (Latour e Woolgar, 1986, ed. Princeton). 105.749 palavras.
- **SIA87** = *Science in Action* (Latour, 1987). 139.861 palavras.
- **PAN99** = *Pandora's Hope* (Latour, 1999). 128.001 palavras.
- **CLA96** = *On Actor-Network Theory: A Few Clarifications* (Latour, 1996, *Soziale Welt*). 7.848 palavras.
- **REC99** = *On Recalling ANT* (Latour, 1999, eds. Law e Hassard). 1.241 palavras na Etapa 2 (corpus parcial, 25,3% de cobertura); 4.825 palavras na Etapa 2-bis (corpus integral).
- **AIME13** = *An Inquiry into Modes of Existence* (Latour, 2013). 194.454 palavras.

### Tipos de gráfico

Tipos canônicos da Etapa 1 por obra (gerados por `scripts/04_visualizations.py` e `scripts/05_cooccurrence.py`):

- *Ranking de frequência por campo*: barras **horizontais**, eixo X = **ocorrências válidas após exclusões (n absoluto, não freq/10k)**, ordenação ascendente para leitura do topo, paleta **viridis**, anotação numérica à direita de cada barra.
- *Densidade ao longo do texto*: histograma **empilhado, 20 bins**, eixo X = posição relativa no texto (0 início, 1 fim, calculada como `posicao_no_texto / n_chars` do arquivo `corpus/txt_norm/<obra>.txt`), uma cor por campo (paleta viridis), legenda no canto superior direito.
- *Rede de cocorrência*: grafo não direcionado, nós como campos figurativos em **cor uniforme `#4c72b0` (azul)**, tamanho do nó proporcional à raiz quadrada da frequência absoluta do campo, arestas com **largura ∝ √(peso)**, alpha 0,45, layout `spring_layout` com `seed=42`. Janela de cocorrência expressa em palavras e aproximada por caracteres na implementação (5,5 chars/palavra).

Tipos do passo 4 (gerados por `scripts/arquivo/11_passo4_graficos.py`) têm paleta própria: campo `militar` em **vermelho ferrugem `#B22222`** (variantes mais claras e mais escuras quando há cronologia, `#E08570/#B22222/#7A1A1A` para 1986/1987/1999), demais campos em escala de **cinza** (`#D4D4D4/#808080/#404040`). Estilo `matplotlib` com spines top/direita removidos e grid no eixo X em alpha 0,3.

Tipos da Etapa 3 sobre AIME (gerados por `scripts/arquivo/23_etapa3_aime_visualizacoes.py`): paleta dupla por proveniência do catálogo (azul `#4c72b0` antigo, laranja `#dd8452` novo); densidade com **30 bins, paleta tab20**.

### Janela KWIC

$\pm$10 palavras para detecção e contagem (`scripts/02_kwic.py`). Para curadoria de passagens citáveis (passo 4), janela ampliada de $\pm$50. Para cocorrência, janela parametrizável em palavras, indicada no sufixo do nome do arquivo (`j025`, `j100`, `j157`, `j200`, `jprop` para proporcional ~2% das palavras totais da obra).

---

## Etapa 1, três obras de Latour em inglês original

### `latour_woolgar_1986_lab_life_en/figuras/`

Pasta canônica: `outputs/etapa1/latour_woolgar_1986_lab_life_en/figuras/`. Gerador: `scripts/04_visualizations.py` (freq + densidade) e `scripts/05_cooccurrence.py` (rede).

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking, barras horizontais, eixo X = n absoluto, paleta viridis | LL86 | 12 campos com ocorrência | Ordem do ranking por n: `construction` (204), `topologia` (146), `inscription` (125), `network` (45), `militar` (39), `agonistic` (32), `textil` (13), `black_box` (10), `proposition` (5), `translation` (3), `enrollment` (1), `spokesperson` (1). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 20 bins, eixo X = posição relativa 0--1 por bytes do txt_norm, paleta viridis | LL86 | os 12 campos do ranking, uma cor por campo | Distribuição das ocorrências ao longo da obra; concentração de `inscription` nos capítulos centrais e dispersão de `construction`. |
| `rede_cocorrencia.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras (1100 chars), nós azul `#4c72b0`, largura ∝ √peso, spring_layout seed=42 | LL86 | nós: campos coocorrentes; arestas top: `construction`--`inscription` (90), `construction`--`network` (51), `agonistic`--`construction` (46), `inscription`--`network` (20), `construction`--`militar` (15) | 15 pares válidos. |

Espelhos em `outputs/consolidado/figuras/`: `frequencia_grupos_lab_life.png`, `densidade_lab_life.png`, `rede_cocorrencia_lab_life.png`.

### `latour_1987_science_action_en/figuras/`

Pasta canônica: `outputs/etapa1/latour_1987_science_action_en/figuras/`. Mesmos geradores.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking, barras horizontais, n absoluto, viridis | SIA87 | 16 campos com ocorrência | Ordem: `topologia` (485), `militar` (374), `black_box` (134), `network` (127), `textil` (111), `translation` (78), `inscription` (62), `construction` (53), `spokesperson` (46), `enrollment` (44), `trial_of_strength` (20), `centre_of_calculation` (19), `actor_network` (17), `proposition` (5), `immutable_mobile` (4), `articulation` (4). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 20 bins, posição relativa 0--1, viridis | SIA87 | mesmos 16 campos | Adensamento do campo `militar` no terço central (capítulos sobre *trials of strength* e *from short to longer networks*). |
| `rede_cocorrencia.png` (+ `.svg`) | grafo, janela 200 palavras, nós azuis uniformes, largura ∝ √peso | SIA87 | 62 pares válidos; topo: `black_box`--`militar` (152), `militar`--`network` (98), `inscription`--`militar` (72), `militar`--`translation` (71), `construction`--`militar` (59), `militar`--`spokesperson` (55), `enrollment`--`militar` (52), `militar`--`trial_of_strength` (39) | Campo `militar` aparece em quase todos os pares de maior densidade. Contagem do campo militar é **bruta** (374) tanto no tamanho do nó quanto nas cocorrências. |

Espelhos: `frequencia_grupos_sia.png`, `densidade_sia.png`, `rede_cocorrencia_sia.png`.

### `latour_1999_pandora_en/figuras/`

Pasta canônica: `outputs/etapa1/latour_1999_pandora_en/figuras/`. Mesmos geradores.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking, barras horizontais, n absoluto, viridis | PAN99 | 16 campos com ocorrência | Ordem (contagem **bruta**, antes da desambiguação de `war`/`wars`): `topologia` (353), `militar` (212), `textil` (105), `translation` (70), `construction` (62), `factish` (53), `articulation` (53), `proposition` (41), `network` (35), `actor_network` (31), `circulating_reference` (18), `black_box` (17), `inscription` (14), `enrollment` (12), `centre_of_calculation` (4), `immutable_mobile` (3). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 20 bins, posição relativa 0--1, viridis | PAN99 | mesmos 16 campos | Dois picos do campo `militar` (em contagem bruta): capítulo sobre Joliot (Segunda Guerra Mundial) e bloco final sobre *Science Wars*. |
| `rede_cocorrencia.png` (+ `.svg`) | grafo, janela 200 palavras, nós azuis uniformes, largura ∝ √peso | PAN99 | 64 pares válidos; topo: `articulation`--`proposition` (64), `construction`--`militar` (47), `construction`--`factish` (37), `militar`--`translation` (32), `factish`--`militar` (30), `articulation`--`translation` (22), `militar`--`network` (21), `actor_network`--`black_box` (21), `actor_network`--`militar` (20) | Par `articulation`--`proposition` lidera, refletindo guinada conceitual de 1999 para *articulating propositions*. Cocorrências envolvendo `militar` são **brutas** (não refinadas). |

Espelhos: `frequencia_grupos_pandora.png`, `densidade_pandora.png`, `rede_cocorrencia_pandora.png`.

---

## Etapa 1, passo 4: consolidação das três obras e refinamento de `war`/`wars`

Pasta canônica: `outputs/etapa1/passo4/figuras/`. Gerador: `scripts/arquivo/11_passo4_graficos.py`. Paleta: vermelho ferrugem `#B22222` (com variantes claras/escuras para cronologia) para o campo `militar`, cinza para os demais.

| Arquivo | Tipo de gráfico | Obras | Campos | Conteúdo |
|---|---|---|---|---|
| `comparacao_frequencias_tres_obras.png` (+ `.svg`) | barras horizontais agrupadas por campo, 3 cores por obra (cinza claro/médio/escuro para 1986/1987/1999 nos campos gerais; vermelho ferrugem claro/médio/escuro no campo `militar`), eixo X = freq./10k palavras, ordenação por densidade decrescente em SIA 1987 | LL86 + SIA87 + PAN99 | 17 campos do catálogo, todos exibidos | **Campo `militar` plotado em contagem refinada** pós-desambiguação simétrica de `war`/`wars` em SIA e PAN (LL86 3,50; SIA87 **25,95**; PAN99 12,19 por 10.000 palavras), com **anotação numérica in-line dos três valores** ao lado da barra militar. Os demais 16 campos seguem a contagem bruta de `frequencias.csv`. |
| `frequencia_grupos_tres_obras_painel.png` (+ `.svg`) | **3 painéis empilhados verticalmente** (1 por obra), barras horizontais com eixo X = **n absoluto** ("Ocorrências válidas após exclusões"), **escalas X independentes** entre painéis (cada obra tem max próprio), militar em vermelho ferrugem, demais campos em cinza médio | LL86 + SIA87 + PAN99 | todos os campos com ocorrência por obra | Cada painel ordenado por n decrescente, com rótulo da obra no canto inferior direito. **Militar refinado simétrico** (LL86 n=37, SIA87 n=**363**, PAN99 n=156). Anotação numérica à direita de cada barra; o valor do militar fica em negrito. **ATENÇÃO**: as escalas X diferem muito entre obras, comparação direta entre painéis exige cuidado. |
| `densidade_militar_sia_pandora.png` (+ `.svg`) | **curva de linha + área preenchida** (NÃO histograma) em vermelho ferrugem `#B22222`, com janela deslizante de **1.000 palavras** e passo de 200, painel **vertical em 2 linhas**, eixo X = posição no texto em milhares de palavras, rótulo de painel exibindo o **n refinado** e anotação no canto inferior da figura: \enquote{Versão simétrica: war/wars descritivos removidos em ambas as obras} | SIA87 + PAN99 (sem LL86) | apenas `militar` | **Versão simétrica** (canônica desde 2026-05-23): hits refinados em ambas as obras. SIA87 n=**363** (em 374 brutos, 11 descritivos removidos: `Second World Wars`, oito ocorrências no capítulo Szilard/Pentagon sobre WWII, `Franco-Prussian war`, referência bibliográfica Tolstoi `War and Peace`); PAN99 n=**156**, mesma classificação de `war_pandora_classificacao.csv`. Refinamento SIA registrado em `outputs/etapa1/refinamento/war_sia_classificacao.csv`, schema idêntico ao de PAN. A versão assimétrica anterior (SIA bruto, PAN refinado) fica disponível no histórico do git. |
| `frequencia_grupos_sia_refinada.png` (+ `.svg`) | ranking, barras horizontais, **eixo X = n absoluto** (não freq/10k), militar em vermelho ferrugem `#B22222`, demais campos em cinza médio `#808080`, ordenação por n decrescente, rótulo da obra no canto inferior direito | SIA87 | 16 campos, com `militar` refinado | Versão refinada do ranking SIA: militar plotado com n=**363** (bruta era 374, -2,9% pela classificação simétrica em `war_sia_classificacao.csv`); ordem por n decrescente fica praticamente igual à da figura `frequencia_grupos.png` da Etapa 1 base. Anotações numéricas à direita de cada barra; valor do militar em negrito. |
| `frequencia_grupos_pandora_refinada.png` (+ `.svg`) | mesmo esquema da SIA refinada | PAN99 | 16 campos, com `militar` refinado | Versão refinada do ranking Pandora: militar plotado com n=156 (bruta era 212, -26,4%); na ordem por n decrescente o militar cai duas posições, ficando próximo de `textil` (105) e `translation` (70). |
| `rede_cocorrencia_sia.png` (+ `.svg`) | grafo de cocorrência, **janela 100 palavras** (não 200, recomputada do kwic.csv), **limiar mínimo de 5 cocorrências por aresta**, militar fixo no centro do layout (vermelho ferrugem `#B22222`), demais nós em cinza `#808080`, tamanho do nó ∝ √(n_absoluto), largura da aresta ∝ peso/peso_max, cor da aresta em escala de cinzas `Greys`. Texto no canto inferior direito: \enquote{Arestas: limiar mínimo de 5 cocorrências. Janela: 100 palavras.} | SIA87 | mesmos campos da rede da Etapa 1 base, mas filtrados por limiar 5 | **ATENÇÃO**: não é a mesma rede de `rede_cocorrencia.png` da Etapa 1 base (janela 200, sem limiar). Esta é recomputada com parâmetros novos para destacar visualmente a posição articuladora do campo militar. Tamanho do nó militar usa **n=363 refinado simétrico**. |

Espelhos em `outputs/consolidado/figuras/`: `comparacao_frequencias_tres_obras.png`, `frequencia_grupos_tres_obras_painel.png`, `densidade_militar_sia_pandora.png`, `frequencia_grupos_sia_refinada.png`, `frequencia_grupos_pandora_refinada.png`, `rede_cocorrencia_sia_passo4.png`.

Tabela LaTeX correspondente: `outputs/etapa1/refinamento/tabela_militar_refinada.tex`.

---

## Etapa 1, Reinert/AFC: lexicometria estilo IRaMuTeQ

Pasta canônica: `outputs/etapa1/reinert_afc/`. Gerador: `scripts/R/10_reinert_afc.R`. Pipeline: lematização via **udpipe** (modelo `english-ewt`, filtrando por upos e descartando PUNCT, NUM, SYM, X) $\rightarrow$ segmentação em STs de **40 tokens** via `rainette::split_segments` $\rightarrow$ dfm com remoção de stopwords inglesas e `min_docfreq=3` $\rightarrow$ CHD Reinert com `k=6` e `min_segment_size=10` $\rightarrow$ AFC sobre **top 250 lemas** via `FactoMineR::CA`. Seed=42.

Status em 2026-05-23: três figuras já existem no repo (saída anterior); rodar o script atualiza. **Uma quarta figura prevista pelo script ainda não existe no repo**.

| Arquivo | Tipo de gráfico | Obras | Campos / classes | Conteúdo |
|---|---|---|---|---|
| `reinert_dendrograma.png` | dendrograma da CHD via `plot()` direto sobre objeto rainette/hclust, `hang=-1` | LL86 + SIA87 + PAN99 (corpus consolidado, lematizado) | 6 classes lexicais identificadas pelo algoritmo | Folhas correspondem às classes; eixo Y = distância qui². Tamanho da imagem 1600×900 px, 150 dpi. Perfis em `perfis_classe_01.csv` a `perfis_classe_06.csv`. |
| `afc_classes_reinert.png` | biplot AFC via `FactoMineR::CA` + `ggplot2` + `ggrepel`, dois primeiros eixos fatoriais | LL86 + SIA87 + PAN99 (consolidado) | **top 250 lemas** (pontos com rótulo) × **6 classes** (labels pretos centrais) | Lemas coloridos pela **classe dominante** (índice da maior contribuição em `res_ca$row$contrib`, via `which.max`). Eixos com porcentagem de inércia explicada. Linhas guia em x=0 e y=0. Coordenadas em `afc_classes_coordenadas_classes.csv` e `afc_classes_coordenadas_lemas.csv`. |
| `afc_obras.png` | biplot AFC via FactoMineR + ggplot2 + ggrepel, dois primeiros eixos | LL86 + SIA87 + PAN99 (como rótulos vermelhos `firebrick`) | top 250 lemas × 3 obras | Obras em labels vermelhos centrais; lemas em cinza com `geom_text_repel`. Eixos com porcentagem de inércia. Coordenadas em `afc_obras_coordenadas_obras.csv` e `afc_obras_coordenadas_lemas.csv`. |
| `reinert_perfis_classes.png` **(ainda não gerada)** | barplot facetado via `ggplot2` + `facet_wrap`, 6 facetas (uma por classe), barras horizontais em `steelblue`, eixo X = chi², eixo Y = lema | mesmo corpus | os 15 lemas mais característicos por classe (top 15 por chi² nos `perfis_classe_0N.csv`) | Visualização complementar dos perfis de classe. Tamanho 14×9 polegadas, 150 dpi. Pendente: rodar o script localmente para gerar; nenhum PNG `reinert_perfis_classes.png` existe ainda em `outputs/etapa1/reinert_afc/`. |

CSVs auxiliares no mesmo diretório: `distribuicao_classes_por_obra.csv`.

---

## Etapa 2: artigos metateóricos, corpus parcial

Gerador das redes: `scripts/05_cooccurrence.py` com `--sufixo j<N>` (mesmo estilo visual das redes da Etapa 1 base: nó azul `#4c72b0` uniforme, largura ∝ √peso, spring_layout seed=42).

### `latour_1996_clarifications_en/figuras/`

Pasta canônica: `outputs/etapa2/latour_1996_clarifications_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras (controle, comparável à Etapa 1) | CLA96 | 22 pares válidos; topo: `network`--`topologia` (783), `textil`--`topologia` (222), `actor_network`--`network` (162), `network`--`textil` (130), `actor_network`--`topologia` (102) | Dominância do par têxtil-topológico; `militar` em conexão marginal (`militar`--`network`: 10). |
| `rede_cocorrencia_j157.png` (+ `.svg`) | grafo de cocorrência, **janela 157 palavras (~2% das palavras totais do artigo, proporção análoga à de uma janela de 200 num livro)** | CLA96 | 21 pares válidos; topo: `network`--`topologia` (616), `textil`--`topologia` (171), `actor_network`--`network` (138), `network`--`textil` (101), `actor_network`--`topologia` (84) | Janela proporcional sugerida em `outputs/etapa2/consolidado/cocorrencia_comparacao.md` como configuração principal para a tese; janela 200 fica como controle. Topologia da rede permanece estável. |

Espelhos: `rede_cocorrencia_clarifications_j200.png`, `rede_cocorrencia_clarifications_j157.png`.

### `latour_1999_recalling_en/figuras/` (corpus parcial Etapa 2, 1.241 palavras)

Pasta canônica: `outputs/etapa2/latour_1999_recalling_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo, janela 200 palavras (controle) | REC99 corpus parcial | 6 pares válidos: `network`--`topologia` (20), `actor_network`--`network` (6), `militar`--`topologia` (5), `construction`--`topologia` (5), `construction`--`militar` (1), `construction`--`network` (1) | Rede pequena dado o tamanho do corpus parcial. |
| `rede_cocorrencia_j025.png` (+ `.svg`) | grafo, **janela 25 palavras (~2% das 1.241 palavras do corpus parcial)** | REC99 corpus parcial | 3 pares válidos: `actor_network`--`network` (2), `network`--`topologia` (2), `militar`--`topologia` (1) | Janela proporcional ao corpus parcial. A leitura definitiva está nas figuras da Etapa 2-bis sobre corpus integral. |

Espelhos: `rede_cocorrencia_recalling_etapa2_j200.png`, `rede_cocorrencia_recalling_etapa2_j025.png`.

---

## Etapa 2-bis: reanálise do *Recalling ANT* sobre TXT integral

Pasta canônica: `outputs/etapa2bis/latour_1999_recalling_bis/figuras/`. Mesmo gerador `05_cooccurrence.py` com `--sufixo`.

Corpus: 4.825 palavras (cobertura de 100% das páginas 15--25 do volume), substitui o corpus parcial da Etapa 2 como leitura definitiva.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo, janela 200 palavras (controle, comparável aos livros) | REC99 integral | 24 pares válidos; topo: `network`--`topologia` (79), `actor_network`--`network` (28), `actor_network`--`topologia` (23), `circulating_reference`--`topologia` (17), `construction`--`topologia` (10), `network`--`translation` (9), `articulation`--`topologia` (8), `textil`--`topologia` (7), `militar`--`topologia` (7) | Reaparecem os campos antes ausentes do corpus parcial (`translation`, `circulating_reference`, `inscription`, `articulation`, `textil`). |
| `rede_cocorrencia_jprop.png` (+ `.svg`) | grafo, **janela proporcional 97 palavras (~2% das 4.825 palavras do corpus integral)** | REC99 integral | 19 pares válidos; topo: `network`--`topologia` (38), `actor_network`--`network` (23), `actor_network`--`topologia` (10), `circulating_reference`--`topologia` (9), `textil`--`topologia` (6), `network`--`translation` (3), `militar`--`topologia` (3) | Janela proporcional, comparável à `j157` de CLA96 em escala equivalente. |

Espelhos: `rede_cocorrencia_recalling_etapa2bis_j200.png`, `rede_cocorrencia_recalling_etapa2bis_jprop.png`.

---

## Etapa 3: *An Inquiry into Modes of Existence* (2013)

Pasta canônica: `outputs/etapa3/latour_2013_aime_en/figuras/`. Geradores: `scripts/arquivo/23_etapa3_aime_visualizacoes.py` (freq + densidades) e `scripts/05_cooccurrence.py` com `--sufixo` (redes).

Catálogo duplo: catálogo antigo (Etapas 1--2, 19 campos) + catálogo novo da Etapa 3 (12 campos específicos de AIME identificados por leitura qualitativa).

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking, **barras horizontais, eixo X = n absoluto** ("Ocorrências válidas após exclusões"), coloridas por proveniência: azul `#4c72b0` catálogo antigo, laranja `#dd8452` catálogo novo, legenda manual no canto inferior direito | AIME13 | 26 campos com ocorrência (14 do antigo, 12 do novo) | Total: 1.343 ocorrências do catálogo antigo + 2.214 do novo = 3.557. Catálogo antigo top: `topologia` (514), `network` (255), `textil` (201), `militar` (129), `construction` (74), `articulation` (56), `translation` (40), `inscription` (20), `immutable_mobile` (20), `actor_network` (17). Catálogo novo top: `trajetoria_passe` (433), `modernos` (397), `categorias_dominio` (281), `experiencia` (276), `instituicao` (227), `modos_existencia` (167), `alteracao` (112), `felicidade` (92). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, **30 bins, paleta tab20**, eixo X = posição relativa 0--1 por bytes, **restrito aos 12 campos mais densos** para legibilidade | AIME13 | `topologia`, `trajetoria_passe`, `modernos`, `categorias_dominio`, `experiencia`, `network`, `instituicao`, `textil`, `modos_existencia`, `militar`, `alteracao`, `felicidade` | Visualiza alternância das três camadas figurativas: catálogo antigo dominante (topologia/network/textil/militar) + catálogo novo (trajetoria_passe/modernos/categorias_dominio/etc.). **ATENÇÃO**: no `legendas_figuras.tex` da Etapa 3, este arquivo está referenciado como `aime_densidade_top12.png` (path divergente do nome real). |
| `densidade_ao_longo_do_texto_todos.png` (+ `.svg`) | histograma empilhado, 30 bins, tab20, **todos os 26 campos com ocorrência** (versão poluída para auditoria) | AIME13 | os 26 campos (14 antigos + 12 novos) | Versão completa da figura anterior. Campos do catálogo antigo sem ocorrências em AIME (`centre_of_calculation`, `trial_of_strength`, `factish`, `circulating_reference`, `spokesperson`) não aparecem. No `legendas_figuras.tex` da Etapa 3 referenciado como `aime_densidade_todos.png`. |
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo, janela 200 palavras, mesmo estilo `05_cooccurrence.py` (nós azul `#4c72b0` uniforme, largura ∝ √peso, spring seed=42) | AIME13 | 242 pares válidos; topo: `topologia`--`trajetoria_passe` (584), `network`--`topologia` (379), `network`--`trajetoria_passe` (301), `categorias_dominio`--`topologia` (285), `categorias_dominio`--`trajetoria_passe` (276), `categorias_dominio`--`network` (264), `experiencia`--`modernos` (243), `network`--`textil` (236), `instituicao`--`modernos` (212), `modernos`--`topologia` (201), `textil`--`topologia` (197), `militar`--`modernos` (144) | Continuidade do par têxtil-topológico desde a Etapa 2; campo `militar` em registro residual articulado aos `moderns`. |
| `rede_cocorrencia_jprop.png` (+ `.svg`) | grafo, **janela proporcional 39 palavras (~2% das 194.454 palavras de AIME)** | AIME13 | 180 pares válidos; topo: `topologia`--`trajetoria_passe` (205), `network`--`textil` (93), `network`--`topologia` (91), `categorias_dominio`--`network` (70), `experiencia`--`modernos` (56), `network`--`trajetoria_passe` (54), `categorias_dominio`--`topologia` (53), `instituicao`--`modernos` (48) | Sob janela curta, `network`--`textil` passa à frente de `network`--`topologia`. |

Não há espelho em `outputs/consolidado/figuras/` para os arquivos de AIME (Etapa 3 mais recente; integração consolidada cross-etapas pendente).

Arquivo LaTeX preexistente com três legendas (alternativa, em estilo próprio, com paths apontando para nomes `aime_*.png`): `outputs/etapa3/consolidado/legendas_figuras.tex`.

---

## Como usar este inventário

1. Para escolher uma figura para a tese, identifique a obra, o tipo de gráfico e o(s) campo(s) que interessam, e localize a linha correspondente.
2. Anote o caminho da pasta canônica (PNG e SVG juntos) e, quando disponível, o espelho com nome desambiguado em `outputs/consolidado/figuras/`.
3. Os blocos LaTeX correspondentes (com `\begin{figure}`, `\caption[]{}`, `\label{}`) estão em `outputs/latex/inventario_figuras.tex`, na seção da mesma etapa.
4. Os números nas células \enquote{Conteúdo} vêm dos CSVs em `outputs/<etapa>/<obra>/csv/` e dos relatórios em `outputs/<etapa>/<obra>/relatorios/`.
5. Onde a figura mistura contagens (parte bruta, parte refinada) ou tem nome de arquivo divergente do path nominal em LaTeX, o aviso fica explícito em **ATENÇÃO** na coluna \enquote{Conteúdo}.

## Pendências

- Rodar `scripts/R/10_reinert_afc.R` localmente em RStudio para regenerar as 3 figuras de `etapa1/reinert_afc/` e produzir a 4ª (`reinert_perfis_classes.png`, ainda inexistente no repo).
- Padronizar os nomes dos arquivos PNG de AIME para o padrão `aime_*.png` usado em `outputs/etapa3/consolidado/legendas_figuras.tex` (ou ajustar os paths nas legendas).
- Espelhar as figuras de AIME em `outputs/consolidado/figuras/` quando a Etapa 3 entrar no consolidado cross-etapas.
- A assimetria de tratamento em `densidade_militar_sia_pandora.png` (SIA bruto, PAN refinado) foi resolvida em 2026-05-23: o script `scripts/arquivo/11_passo4_graficos.py` foi atualizado para aplicar a filtragem simétrica em SIA e PAN via `war_sia_classificacao.csv` e `war_pandora_classificacao.csv`. `MILITAR_REFINADO[SIA]` passou de n=364 (agregado anterior) para n=363 (classificação por ocorrência), e as 6 figuras do passo 4 foram regeradas com os novos valores. A figura assimétrica anterior fica preservada no histórico do git.
