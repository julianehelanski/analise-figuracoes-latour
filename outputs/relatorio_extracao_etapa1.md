# Relatório de extração e qualidade — Etapa 1

Consolidação técnica da etapa de preparação textual antes do KWIC. Gerado por `scripts/01b_normalize_text.py` (normalização) e contadores subsequentes. Os arquivos crus em `corpus/txt/` permanecem como artefato auditável; a análise opera sobre `corpus/txt_norm/`.

## 1. Volume e qualidade global por obra

| Obra | Páginas | Palavras | Qualidade global | Taxa qualidade boa | Taxa qualidade baixa |
|---|---:|---:|:---:|---:|---:|
| `latour_woolgar_1986_lab_life_en` | 296 | 105.749 | boa | 0,949 | 0,034 |
| `latour_1987_science_action_en` | 314 | 139.861 | boa | 0,990 | 0,006 |
| `latour_1999_pandora_en` | 337 | 128.001 | boa | 0,979 | 0,018 |
| **Total** | **947** | **373.611** |  |  |  |

Métrica `qualidade_pagina` por página avalia proporção de caracteres estranhos e de linhas curtas. Critérios herdados de `scripts/01_extract_text.py`: qualidade global "boa" exige ≥80% das páginas como qualidade `boa` e ≤5% como `baixa`. As três obras passam.

## 2. Operações de normalização aplicadas

Detalhes em `docs/decisoes_metodologicas.md`, Adendo 1 (14/05/2026). Contagem por operação:

| Obra | Soft hyphen | Hifenização EOL | Marcadores `((NN))` | Cabeçalhos espaçados | Replacement `�` |
|---|---:|---:|---:|---:|---:|
| `latour_woolgar_1986_lab_life_en` | 0 | 500 | 0 | 0 | 0 |
| `latour_1987_science_action_en` | 0 | 55 | 276 | 0 | 0 |
| `latour_1999_pandora_en` | 2.367 | 18 | 0 | 6 | 220 |

Notas:

- O grosso da normalização em Pandora foi remoção de soft hyphens U+00AD internos a palavras (`per­formed` → `performed`), problema sistemático da extração via leitor de PDF.
- Em Lab Life o ganho foi reconstruir 500 palavras quebradas no fim de linha por `pdftotext -layout`.
- Em Science in Action o ganho foi retirar 276 marcadores `((NN))` que o conversor injetou no corpo.
- O cabeçalho espaçado `P A N D O R A ' S H O P E` em Pandora ocorre nas variantes (com letras coladas, com palavras intermediárias, etc.) que escapam ao regex conservador; o impacto sobre o KWIC é nulo porque tokens de letra única não casam termos do catálogo.

## 3. Classificação por estado da página (limitação conhecida)

A heurística de classificação por estado em `scripts/01_extract_text.py` (replicada em `01b_normalize_text.py`) classifica cada página em uma das cinco classes `inicio_capitulo`, `corpo`, `notas_fim`, `paratexto`, `qualidade_baixa`. A distribuição produzida é fortemente enviesada:

| Obra | inicio_capitulo | corpo | notas_fim | paratexto | qualidade_baixa |
|---|---:|---:|---:|---:|---:|
| `latour_woolgar_1986_lab_life_en` | 0 | 4 | 0 | 282 | 10 |
| `latour_1987_science_action_en` | 1 | 2 | 0 | 309 | 2 |
| `latour_1999_pandora_en` | 0 | 3 | 0 | 328 | 6 |

Diagnóstico: o estado `paratexto` é sticky e a primeira página de cada obra contém "Contents"/"Sumário", o que dispara `paratexto` no início e nunca sai. A heurística atual transita `corpo → paratexto` ao casar regex de back matter, mas trata `front matter` (TOC, copyright) com a mesma regex, sem distinguir `front` de `back`. Consequência: o restante do livro fica preso em `paratexto`.

Esse viés impede uma amostra estratificada balanceada (passo 6 abaixo). O KWIC, as frequências, a cocorrência e a trajetória **não** dependem dessa classificação e seus números seguem corretos, calculados sobre o texto integral.

Decisão pendente da Juliane: ajustar a heurística antes da Etapa 2 (validação amostral), separando `front matter` de `back matter` e tornando reversível a entrada em `paratexto`. Proposta detalhada acompanha o relatório de amostra (item 6).

## 4. Tabela de frequências preliminar (consolidada)

Frequência absoluta e por 10 000 palavras, por grupo figurativo, por obra. Fonte: `outputs/<id>/csv/frequencias.csv` (gerada por `scripts/03_frequencies.py`).

| Grupo | 1986 lab_life | 1987 science_action | 1999 pandora | Obras |
|---|---|---|---|---:|
| `inscription` | 11,82 (125) | 4,43 (62) | 1,09 (14) | 3/3 |
| `construction` | 19,29 (204) | 3,79 (53) | 4,84 (62) | 3/3 |
| `network` | 4,26 (45) | 9,08 (127) | 2,73 (35) | 3/3 |
| `translation` | 0,28 (3) | 5,58 (78) | 5,47 (70) | 3/3 |
| `black_box` | 0,95 (10) | 9,58 (134) | 1,33 (17) | 3/3 |
| `enrollment` | 0,09 (1) | 3,15 (44) | 0,94 (12) | 3/3 |
| `proposition` | 0,47 (5) | 0,36 (5) | 3,20 (41) | 3/3 |
| `actor_network` | 0 | 1,22 (17) | 2,42 (31) | 2/3 |
| `immutable_mobile` | 0 | 0,29 (4) | 0,23 (3) | 2/3 |
| `centre_of_calculation` | 0 | 1,36 (19) | 0,31 (4) | 2/3 |
| `spokesperson` | 0,09 (1) | 3,29 (46) | 0 | 2/3 |
| `articulation` | 0 | 0,29 (4) | 4,14 (53) | 2/3 |
| `trial_of_strength` | 0 | 1,43 (20) | 0 | 1/3 |
| `factish` | 0 | 0 | 4,14 (53) | 1/3 |
| `circulating_reference` | 0 | 0 | 1,41 (18) | 1/3 |
| `agonistic` | 3,03 (32) | 0 | 0 | 1/3 |

Total de ocorrências válidas por obra (após exclusões): 426 (1986), 613 (1987), 413 (1999). Total geral: 1.452.

## 5. Outputs gerados na Etapa 1

Por obra (em `outputs/<id>/`):

- `csv/kwic.csv` — uma linha por ocorrência, com janela ±10 palavras, página, posição e flag de exclusão.
- `csv/frequencias.csv` — contagem por grupo, com frequência por 10k palavras.
- `csv/cocorrencia.csv` — matriz grupo × grupo com pesos por janela de 200 palavras.
- `csv/amostra_validacao.csv` — amostra estratificada para validação manual (com colunas vazias prontas para codificação).
- `figuras/frequencia_grupos.png` — ranking visual de grupos.
- `figuras/densidade_ao_longo_do_texto.png` — histograma da posição relativa das ocorrências.
- `figuras/rede_cocorrencia.png` — grafo de cocorrência figural.
- `relatorios/frequencias.md` — ranking + exemplos top-3.
- `relatorios/cocorrencia.md` — top 20 pares por força de cocorrência.
- `relatorios/validacao_amostral_etapa1.md` — guia de leitura da amostra.

Consolidados (em `outputs/`):

- `trajetoria_latour_1986_1999.csv` — matriz grupo × obra com perfil de trajetória.
- `trajetoria_latour_1986_1999.md` — relatório textual da trajetória 1986-1999.
- `amostra_validacao_etapa1.csv` — 26 linhas (limitação descrita em §3).

## 6. Status da amostra estratificada (passo 6 do plano)

A decisão de 13/05/2026 previu 45 páginas (15 por obra, 5 estratos de 3). Por causa do viés da heurística descrito em §3, a amostra efetiva tem **26 páginas**, distribuídas:

- `latour_woolgar_1986_lab_life_en`: 9 páginas (3 `corpo`, 3 `paratexto`, 3 `qualidade_baixa`).
- `latour_1987_science_action_en`: 8 páginas (1 `inicio_capitulo`, 2 `corpo`, 3 `paratexto`, 2 `qualidade_baixa`).
- `latour_1999_pandora_en`: 9 páginas (3 `corpo`, 3 `paratexto`, 3 `qualidade_baixa`).

Os estratos `notas_fim` e `inicio_capitulo` estão sub-representados em todas as obras. Para chegar a 45 páginas balanceadas, a heurística precisa ser corrigida. Proposta de correção:

1. Separar `front_matter` (Contents, copyright, half-title) de `back_matter` (Bibliography, Index, References, Notes).
2. Tornar `front_matter` não-sticky (permitir saída para `corpo` ao casar pattern de capítulo).
3. Manter `back_matter` sticky (uma vez na bibliografia, fica nela).
4. Refinar detecção de início de capítulo para casar variantes em maiúsculas tipo `CHAPTER 1` ou números isolados seguidos de título em caixa alta (padrão de Lab Life e Pandora).

A correção é simples (~40 linhas de alteração em `01_extract_text.py` e replicação em `01b_normalize_text.py`), mas é decisão analítica: define o que conta como "corpo" para fins de validação amostral. **Aguardo aprovação antes de implementar e reprocessar.**

---

**Resumo executivo**: extração e normalização concluídas com qualidade boa nas três obras (947 páginas, 373.611 palavras, 1.452 ocorrências válidas no catálogo). KWIC, frequências, visualizações, cocorrência e trajetória entregues e consistentes com leitura qualitativa esperada (Lab Life concentra `inscription`/`construction`; Science in Action consolida `black_box`/`network`/`translation`; Pandora introduz `factish` e `circulating_reference`). Amostra estratificada incompleta (26/45) por viés da heurística de classificação de páginas; correção proposta e parada para aprovação antes de avançar à Etapa 2.
