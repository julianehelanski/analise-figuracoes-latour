# Inventário de figuras da análise

Referência aberta para escolha e redação de legendas. Cada entrada lista o nome do arquivo, o que a figura mostra (tipo de gráfico, obras representadas, campos figurativos exibidos) e a pasta do repositório.

Versão LaTeX com blocos `\begin{figure}` prontos: `outputs/latex/inventario_figuras.tex`.

Total de figuras únicas: **29**, presentes em PNG e SVG no diretório canônico, e em PNG (com nomes desambiguados) no espelho `outputs/consolidado/figuras/`. Quando há espelho, indico o nome correspondente abaixo.

Catálogo de campos figurativos: `campos_lexicais/catalogo_termos.yaml`.

---

## Convenções

- **Obras** (siglas usadas abaixo):
  - **LL86** = *Laboratory Life* (Latour e Woolgar, 1986, ed. Princeton). 105.749 palavras.
  - **SIA87** = *Science in Action* (Latour, 1987). 139.861 palavras.
  - **PAN99** = *Pandora's Hope* (Latour, 1999). 128.001 palavras.
  - **CLA96** = *On Actor-Network Theory: A Few Clarifications* (Latour, 1996, *Soziale Welt*). 7.848 palavras.
  - **REC99** = *On Recalling ANT* (Latour, 1999, eds. Law e Hassard). 1.241 palavras na Etapa 2 (corpus parcial, 25,3% de cobertura); 4.825 palavras na Etapa 2-bis (corpus integral).
  - **AIME13** = *An Inquiry into Modes of Existence* (Latour, 2013). 194.454 palavras.

- **Tipos de gráfico recorrentes**:
  - *Ranking de frequência por campo*: barras horizontais ou verticais, contagem absoluta dos campos figurativos com ocorrência na obra, ordenados por n.
  - *Densidade ao longo do texto*: histograma empilhado (30 bins) com a posição relativa de cada ocorrência no eixo horizontal (0 início, 1 fim), uma cor por campo.
  - *Rede de cocorrência*: grafo não direcionado em que os nós são campos figurativos e as arestas têm espessura proporcional à contagem de pares coocorrentes na janela `j`.
  - *Painel comparativo*: três sub-figuras lado a lado, uma por obra, com escala vertical comum.
  - *Dendrograma Reinert*: árvore da classificação hierárquica descendente sobre lemas normalizados.
  - *Biplot AFC*: projeção fatorial dos lemas e das classes (ou das obras) nos dois primeiros eixos.

- **Janela KWIC**: $\pm$10 palavras para detecção e contagem; janelas de cocorrência (`j200`, `j157`, `j025`, `jprop`) parametrizam o cálculo do par e estão indicadas no nome do arquivo.

---

## Etapa 1, três obras de Latour em inglês original

### `latour_woolgar_1986_lab_life_en/figuras/`

Pasta canônica: `outputs/etapa1/latour_woolgar_1986_lab_life_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking de frequência por campo, barras | LL86 | 12 campos com ocorrência | Ordem do ranking: `construction` (204), `topologia` (146), `inscription` (125), `network` (45), `militar` (39), `agonistic` (32), `textil` (13), `black_box` (10), `proposition` (5), `translation` (3), `enrollment` (1), `spokesperson` (1). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 30 bins, eixo x = posição relativa 0--1 | LL86 | os mesmos 12 campos do ranking, uma cor por campo (paleta tab20) | Distribuição das ocorrências ao longo da obra; visualiza concentração de `inscription` nos capítulos centrais e dispersão de `construction`. |
| `rede_cocorrencia.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | LL86 | nós: campos coocorrentes; arestas top: `construction`--`inscription` (90), `construction`--`network` (51), `agonistic`--`construction` (46), `inscription`--`network` (20), `construction`--`militar` (15) | 15 pares válidos. |

Espelhos em `outputs/consolidado/figuras/`: `frequencia_grupos_lab_life.png`, `densidade_lab_life.png`, `rede_cocorrencia_lab_life.png`.

### `latour_1987_science_action_en/figuras/`

Pasta canônica: `outputs/etapa1/latour_1987_science_action_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking de frequência por campo, barras | SIA87 | 16 campos com ocorrência | Ordem: `topologia` (485), `militar` (374), `black_box` (134), `network` (127), `textil` (111), `translation` (78), `inscription` (62), `construction` (53), `spokesperson` (46), `enrollment` (44), `trial_of_strength` (20), `centre_of_calculation` (19), `actor_network` (17), `proposition` (5), `immutable_mobile` (4), `articulation` (4). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 30 bins | SIA87 | mesmos 16 campos | Adensamento do campo `militar` no terço central (capítulos sobre *trials of strength* e *from short to longer networks*). |
| `rede_cocorrencia.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | SIA87 | 62 pares válidos; topo: `black_box`--`militar` (152), `militar`--`network` (98), `inscription`--`militar` (72), `militar`--`translation` (71), `construction`--`militar` (59), `militar`--`spokesperson` (55), `enrollment`--`militar` (52), `militar`--`trial_of_strength` (39) | Campo `militar` aparece em quase todos os pares de maior densidade (articulador semântico). |

Espelhos em `outputs/consolidado/figuras/`: `frequencia_grupos_sia.png`, `densidade_sia.png`, `rede_cocorrencia_sia.png`.

### `latour_1999_pandora_en/figuras/`

Pasta canônica: `outputs/etapa1/latour_1999_pandora_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking de frequência por campo, barras | PAN99 | 16 campos com ocorrência | Ordem (contagem bruta, antes da desambiguação de `war`/`wars`): `topologia` (353), `militar` (212), `textil` (105), `translation` (70), `construction` (62), `factish` (53), `articulation` (53), `proposition` (41), `network` (35), `actor_network` (31), `circulating_reference` (18), `black_box` (17), `inscription` (14), `enrollment` (12), `centre_of_calculation` (4), `immutable_mobile` (3). |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 30 bins | PAN99 | mesmos 16 campos | Dois picos do campo `militar`: capítulo sobre Joliot (Segunda Guerra Mundial) e bloco final sobre *Science Wars*. |
| `rede_cocorrencia.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | PAN99 | 64 pares válidos; topo: `articulation`--`proposition` (64), `construction`--`militar` (47), `construction`--`factish` (37), `militar`--`translation` (32), `factish`--`militar` (30), `articulation`--`translation` (22), `militar`--`network` (21), `actor_network`--`black_box` (21), `actor_network`--`militar` (20) | Par `articulation`--`proposition` lidera, refletindo guinada conceitual de 1999 para *articulating propositions*. |

Espelhos em `outputs/consolidado/figuras/`: `frequencia_grupos_pandora.png`, `densidade_pandora.png`, `rede_cocorrencia_pandora.png`.

---

## Etapa 1, passo 4: consolidação das três obras e refinamento de `war`/`wars`

Pasta canônica: `outputs/etapa1/passo4/figuras/`.

| Arquivo | Tipo de gráfico | Obras | Campos | Conteúdo |
|---|---|---|---|---|
| `comparacao_frequencias_tres_obras.png` (+ `.svg`) | barras agrupadas por campo, três cores (uma por obra), eixo y = freq./10k palavras | LL86 + SIA87 + PAN99 | 17 campos do catálogo, em paralelo | Visualiza salto militar de 1986 (3,69) para 1987 (26,74), recuo em 1999 (16,56 bruto). |
| `frequencia_grupos_tres_obras_painel.png` (+ `.svg`) | painel de três sub-figuras lado a lado, ranking por obra, mesma escala vertical | LL86 + SIA87 + PAN99 | todos os campos com ocorrência por obra | Leitura sinóptica da trajetória conceitual: do par `construction`--`inscription` em 1986 ao par `topologia`--`militar` em 1987 e 1999. |
| `densidade_militar_sia_pandora.png` (+ `.svg`) | sub-figuras lado a lado, densidade de um único campo ao longo do texto | SIA87 + PAN99 | apenas `militar` | Compara distribuição do campo militar nas duas monografias solo (uniforme em SIA87 com pico central; bimodal em PAN99 com adensamentos em Joliot e *Science Wars*). |
| `frequencia_grupos_sia_refinada.png` (+ `.svg`) | ranking de frequência por campo, barras | SIA87 | 16 campos, com `militar` refinado | Versão de `frequencia_grupos.png` de SIA87 após desambiguação de `war`/`wars`: `militar` cai de n=374 para n=364 (-2,7%); ranking inalterado. |
| `frequencia_grupos_pandora_refinada.png` (+ `.svg`) | ranking de frequência por campo, barras | PAN99 | 16 campos, com `militar` refinado | Versão de `frequencia_grupos.png` de PAN99 após desambiguação: `militar` cai de n=212 para n=156 (-26,4%); ranking reordenado, com `militar` aproximando-se de `textil`. |
| `rede_cocorrencia_sia.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras, layout uniformizado | SIA87 | mesmos campos de `rede_cocorrencia.png` de SIA87 | Reapresentação visual em layout consistente com as demais redes do passo 4; conteúdo idêntico ao da Etapa 1 por obra. |

Espelhos em `outputs/consolidado/figuras/`: `comparacao_frequencias_tres_obras.png`, `frequencia_grupos_tres_obras_painel.png`, `densidade_militar_sia_pandora.png`, `frequencia_grupos_sia_refinada.png`, `frequencia_grupos_pandora_refinada.png`, `rede_cocorrencia_sia_passo4.png`.

Tabela LaTeX correspondente (não é figura, mas alimenta o argumento): `outputs/etapa1/refinamento/tabela_militar_refinada.tex` e `outputs/latex/trajetoria_latour_1986_1999.tex`.

---

## Etapa 1, Reinert/AFC: lexicometria estilo IRaMuTeQ

Pasta canônica: `outputs/etapa1/reinert_afc/`.

Status em 2026-05-23: figuras ainda **a gerar** pela execução local de `scripts/R/10_reinert_afc.R` em RStudio sobre R do Anaconda (pendência do passo 6 do refinamento atual). Os arquivos PNG abaixo já existem no repositório como saída anterior; rodar o script atualiza.

| Arquivo | Tipo de gráfico | Obras | Campos / classes | Conteúdo |
|---|---|---|---|---|
| `reinert_dendrograma.png` | dendrograma da classificação hierárquica descendente (CHD) | LL86 + SIA87 + PAN99 (corpus consolidado) | 6 classes lexicais identificadas pelo algoritmo `rainette` sobre lemas normalizados | Folhas rotuladas pelas classes; perfis correspondentes em `perfis_classe_01.csv` a `perfis_classe_06.csv`. |
| `afc_classes_reinert.png` | biplot AFC, dois primeiros eixos | LL86 + SIA87 + PAN99 | 6 classes da CHD + lemas característicos | Posição relativa das classes no plano fatorial. Coordenadas em `afc_classes_coordenadas_classes.csv` e `afc_classes_coordenadas_lemas.csv`. |
| `afc_obras.png` | biplot AFC, dois primeiros eixos | LL86 + SIA87 + PAN99 como pontos suplementares | lemas mais característicos por obra | Distância semântica entre as três obras no espaço lexical conjunto. Coordenadas em `afc_obras_coordenadas_obras.csv` e `afc_obras_coordenadas_lemas.csv`. |

CSVs auxiliares no mesmo diretório: `distribuicao_classes_por_obra.csv`.

---

## Etapa 2: artigos metateóricos, corpus parcial

### `latour_1996_clarifications_en/figuras/`

Pasta canônica: `outputs/etapa2/latour_1996_clarifications_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | CLA96 | 22 pares válidos; topo: `network`--`topologia` (783), `textil`--`topologia` (222), `actor_network`--`network` (162), `network`--`textil` (130), `actor_network`--`topologia` (102) | Dominância do par têxtil-topológico; `militar` em conexão marginal (`militar`--`network`: 10). |
| `rede_cocorrencia_j157.png` (+ `.svg`) | grafo de cocorrência, janela 157 palavras (proporcional aos livros) | CLA96 | 21 pares válidos; topo: `network`--`topologia` (616), `textil`--`topologia` (171), `actor_network`--`network` (138), `network`--`textil` (101), `actor_network`--`topologia` (84) | Controle de sensibilidade da janela; topologia da rede permanece estável. |

Espelhos em `outputs/consolidado/figuras/`: `rede_cocorrencia_clarifications_j200.png`, `rede_cocorrencia_clarifications_j157.png`.

### `latour_1999_recalling_en/figuras/` (corpus parcial, 1.241 palavras)

Pasta canônica: `outputs/etapa2/latour_1999_recalling_en/figuras/`.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | REC99 corpus parcial | 6 pares válidos: `network`--`topologia` (20), `actor_network`--`network` (6), `militar`--`topologia` (5), `construction`--`topologia` (5), `construction`--`militar` (1), `construction`--`network` (1) | Rede pequena dado o tamanho do corpus parcial. |
| `rede_cocorrencia_j025.png` (+ `.svg`) | grafo de cocorrência, janela 25 palavras (adjacência próxima) | REC99 corpus parcial | 3 pares válidos: `actor_network`--`network` (2), `network`--`topologia` (2), `militar`--`topologia` (1) | Controle de sensibilidade com janela curta. |

Espelhos em `outputs/consolidado/figuras/`: `rede_cocorrencia_recalling_etapa2_j200.png`, `rede_cocorrencia_recalling_etapa2_j025.png`.

---

## Etapa 2-bis: reanálise do *Recalling ANT* sobre TXT integral

Pasta canônica: `outputs/etapa2bis/latour_1999_recalling_bis/figuras/`.

Corpus: 4.825 palavras (cobertura de 100% das páginas 15--25 do volume), substitui o corpus parcial da Etapa 2 como leitura definitiva.

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | REC99 integral | 24 pares válidos; topo: `network`--`topologia` (79), `actor_network`--`network` (28), `actor_network`--`topologia` (23), `circulating_reference`--`topologia` (17), `construction`--`topologia` (10), `network`--`translation` (9), `articulation`--`topologia` (8), `textil`--`topologia` (7), `militar`--`topologia` (7) | Reaparecem os campos antes ausentes do corpus parcial (`translation`, `circulating_reference`, `inscription`, `articulation`, `textil`). |
| `rede_cocorrencia_jprop.png` (+ `.svg`) | grafo de cocorrência, janela proporcional 97 palavras | REC99 integral | 19 pares válidos; topo: `network`--`topologia` (38), `actor_network`--`network` (23), `actor_network`--`topologia` (10), `circulating_reference`--`topologia` (9), `textil`--`topologia` (6), `network`--`translation` (3), `militar`--`topologia` (3) | Controle de sensibilidade em escala proporcional aos livros. |

Espelhos em `outputs/consolidado/figuras/`: `rede_cocorrencia_recalling_etapa2bis_j200.png`, `rede_cocorrencia_recalling_etapa2bis_jprop.png`.

---

## Etapa 3: *An Inquiry into Modes of Existence* (2013)

Pasta canônica: `outputs/etapa3/latour_2013_aime_en/figuras/`.

Catálogo duplo: catálogo antigo (Etapas 1--2, 19 campos) + catálogo novo da Etapa 3 (12 campos específicos de AIME identificados por leitura qualitativa).

| Arquivo | Tipo de gráfico | Obra | Campos | Conteúdo |
|---|---|---|---|---|
| `frequencia_grupos.png` (+ `.svg`) | ranking de frequência por campo, barras coloridas por proveniência (azul: catálogo antigo, laranja: catálogo novo) | AIME13 | 26 campos com ocorrência (14 do antigo, 12 do novo) | Total: 1.343 ocorrências do catálogo antigo + 2.214 do novo = 3.557. Catálogo antigo top: `topologia` (514), `network` (255), `textil` (201), `militar` (129), `construction` (74), `articulation` (56), `translation` (40), `inscription` (20), `immutable_mobile` (20), `actor_network` (17). Catálogo novo top: `trajetoria_passe` (433), `modernos` (397), `categorias_dominio` (281), `experiencia` (276), `instituicao` (227), `modos_existencia` (167), `alteracao` (112), `felicidade` (92), `diplomacia` etc. |
| `densidade_ao_longo_do_texto.png` (+ `.svg`) | histograma empilhado, 30 bins, **12 campos mais frequentes** | AIME13 | `topologia`, `trajetoria_passe`, `modernos`, `categorias_dominio`, `experiencia`, `network`, `instituicao`, `textil`, `modos_existencia`, `militar`, `alteracao`, `felicidade` | Visualiza alternância das três camadas figurativas: catálogo antigo dominante (topologia/network/textil/militar) + catálogo novo (trajetoria_passe/modernos/categorias_dominio/etc.). No `legendas_figuras.tex` da Etapa 3, esse arquivo aparece referenciado como `aime_densidade_top12.png`. |
| `densidade_ao_longo_do_texto_todos.png` (+ `.svg`) | histograma empilhado, 30 bins, **todos os 26 campos com ocorrência** | AIME13 | os 26 campos (14 antigos + 12 novos) | Versão completa da figura anterior, para auditoria. Campos do catálogo antigo sem ocorrências em AIME (`centre_of_calculation`, `trial_of_strength`, `factish`, `circulating_reference`, `spokesperson`) não aparecem. No `legendas_figuras.tex` da Etapa 3, referenciado como `aime_densidade_todos.png`. |
| `rede_cocorrencia_j200.png` (+ `.svg`) | grafo de cocorrência, janela 200 palavras | AIME13 | 242 pares válidos; topo: `topologia`--`trajetoria_passe` (584), `network`--`topologia` (379), `network`--`trajetoria_passe` (301), `categorias_dominio`--`topologia` (285), `categorias_dominio`--`trajetoria_passe` (276), `categorias_dominio`--`network` (264), `experiencia`--`modernos` (243), `network`--`textil` (236), `instituicao`--`modernos` (212), `modernos`--`topologia` (201), `textil`--`topologia` (197), `militar`--`modernos` (144) | Continuidade do par têxtil-topológico desde a Etapa 2; campo `militar` em registro residual articulado aos `moderns`. |
| `rede_cocorrencia_jprop.png` (+ `.svg`) | grafo de cocorrência, janela proporcional 39 palavras | AIME13 | 180 pares válidos; topo: `topologia`--`trajetoria_passe` (205), `network`--`textil` (93), `network`--`topologia` (91), `categorias_dominio`--`network` (70), `experiencia`--`modernos` (56), `network`--`trajetoria_passe` (54), `categorias_dominio`--`topologia` (53), `instituicao`--`modernos` (48) | Sob janela curta, `network`--`textil` passa à frente de `network`--`topologia`. |

Não há espelho no `consolidado/figuras/` para os arquivos de AIME (Etapa 3 mais recente; integração consolidada cross-etapas pendente).

Arquivo LaTeX preexistente com três legendas (alternativa, em estilo próprio): `outputs/etapa3/consolidado/legendas_figuras.tex`.

---

## Como usar este inventário

1. Para escolher uma figura para a tese, identifique a obra, o tipo de gráfico e o(s) campo(s) que interessam, e localize a linha correspondente.
2. Anote o caminho da pasta canônica (PNG e SVG juntos) e, quando disponível, o espelho com nome desambiguado em `outputs/consolidado/figuras/`.
3. O bloco LaTeX correspondente (com `\begin{figure}`, `\caption[]{}`, `\label{}`) está em `outputs/latex/inventario_figuras.tex`, na seção da mesma etapa.
4. Os números nas células \enquote{Conteúdo} vêm dos CSVs em `outputs/<etapa>/<obra>/csv/` e dos relatórios em `outputs/<etapa>/<obra>/relatorios/`.

## Pendências

- Gerar/atualizar as três figuras da pasta `etapa1/reinert_afc/` rodando `scripts/R/10_reinert_afc.R` localmente (passo 6 do refinamento atual).
- Renomear/copiar os arquivos de AIME para o padrão `aime_*.png` usado em `outputs/etapa3/consolidado/legendas_figuras.tex` (ou ajustar os paths das legendas), para coerência interna.
- Espelhar as figuras de AIME em `outputs/consolidado/figuras/` quando a Etapa 3 entrar no consolidado cross-etapas.
