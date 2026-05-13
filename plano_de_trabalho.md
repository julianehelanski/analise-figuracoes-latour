# Plano de trabalho: análise textual de figurações em Latour e Haraway

Este plano detalha as oito etapas da análise, adaptado para execução com Claude Code sobre repositório GitHub. Leitura obrigatória antes da execução: `README.md` (visão geral) e `CLAUDE.md` (princípios de trabalho e estado atual).

---

## Visão geral

| Etapa | Densidade | Output | Tempo estimado |
|-------|-----------|--------|----------------|
| 0 | Preparação | Estrutura de pastas, conversão PDFs → texto | 1 dia |
| 1 | Lexicometria mínima | CSV KWIC, 2 livros, 10 termos por autor | 1 dia |
| 2 | Validação amostral | Relatório de precisão e refinamento de campos | 1 dia |
| 3 | Lexicometria expandida | CSVs do corpus completo | 2-3 dias |
| 4 | Frequências comparadas | Tabelas e gráficos | 2 dias |
| 5 | Cocorrências e redes | Grafos de proximidade textual | 2-3 dias |
| 6 | Anotação manual amostral | 50 passagens codificadas por autor | 3-4 dias |
| 7 | Leitura interpretativa | Síntese por capítulo, validada | 1-2 semanas |
| 8 | Consolidação | Apêndice metodológico para a tese | 1 semana |

Total estimado: 4 a 6 semanas em ritmo de pesquisa, com pausas entre etapas para validação.

---

## Etapa 0: Preparação do ambiente e do corpus

### Objetivo

Ter a infraestrutura mínima para que tudo o que vem depois seja reproduzível, com repositório git limpo, ambiente Python configurado, pasta Drive sincronizada localmente e acessível via `.env`.

### Tarefas

1. **Verificar estrutura de pastas** (já criada pelo template; só validar):
   ```
   corpus/{txt}/, campos_lexicais/, scripts/, outputs/{csv,figuras,relatorios,latex}/, docs/
   ```
   Nota: **não há pasta `corpus/pdf/`**. Os PDFs ficam em pasta Drive sincronizada localmente, fora do repositório.

2. **Verificar `.gitignore`**: confirmar que inclui `.env`, qualquer `*.pdf` no repositório, `__pycache__/`, `.venv/`, modelos spaCy, e outputs intermediários.

3. **Verificar `.env`**: o arquivo `.env` (não versionado) deve conter `CORPUS_PDF_PATH` apontando para a pasta Drive sincronizada localmente. Se o arquivo não existir, copiar de `.env.example` e pedir à Juliane que preencha.

4. **Validar acesso à pasta Drive**:
   - Ler `CORPUS_PDF_PATH` do `.env` via `python-dotenv`.
   - Confirmar que o caminho existe, é diretório, e tem permissão de leitura.
   - Listar PDFs presentes na pasta (extensões `.pdf` e `.PDF`).
   - **Se a pasta estiver vazia ou inacessível**, parar e reportar à Juliane com mensagem clara, sugerindo as causas mais prováveis (Drive não sincronizado, Drive pausado, caminho errado em `.env`, permissão negada). Não improvisar.

5. **Cruzar PDFs presentes com a lista esperada em `corpus/README.md`**. Reportar à Juliane:
   - Quais obras estão presentes.
   - Quais obras esperadas estão faltando.
   - Quais arquivos presentes não correspondem ao padrão de nomenclatura.

6. **Extrair texto** de cada PDF presente (a partir do caminho Drive), salvando em `corpus/txt/<id>.txt`:
   ```python
   import subprocess
   from pathlib import Path
   
   pdf_path = Path(corpus_pdf_path) / "latour_1987_science_in_action.pdf"
   txt_path = Path("corpus/txt/latour_1987.txt")
   subprocess.run(["pdftotext", "-layout", str(pdf_path), str(txt_path)], check=True)
   ```
   Atenção a caminhos com espaços (especialmente macOS): usar `str(Path)` em vez de string concatenada.

7. **Para cada texto extraído**:
   - Contar páginas e palavras totais.
   - Identificar automaticamente onde começa o corpo do texto: primeira ocorrência de "Chapter 1", "Capítulo 1", "Chapitre 1" ou "Introduction" como cabeçalho de seção.
   - Identificar onde termina: primeira ocorrência de "Bibliography", "References", "Bibliografia", "Notes" como cabeçalho de seção pós-corpo.
   - Verificar qualidade da extração: abrir 3 trechos aleatórios e checar se há quebras absurdas, palavras coladas, caracteres especiais corrompidos. Se a qualidade estiver baixa, considerar OCR (com `tesseract`) e reportar à Juliane.

8. **Preencher `corpus/metadata.csv`** com colunas:
   ```
   id, autor, titulo, ano, idioma, edicao, paginas_total,
   pagina_inicio_corpo, pagina_fim_corpo, palavras_corpo, qualidade_extracao
   ```

9. **Documentar tudo em `docs/decisoes_metodologicas.md`**, incluindo o caminho local da pasta Drive (campo `Quem decidiu`: Juliane), decisões sobre extração e qualquer ajuste manual feito.

### Gate de revisão

Juliane confere:
- Estrutura de pastas e `.gitignore`.
- `.env` configurado e funcionando (Claude Code consegue ler PDFs do Drive sincronizado).
- Qualidade da extração (lê 3 trechos por livro).
- Tabela `metadata.csv`.
- Anotações em `decisoes_metodologicas.md`.

### Prompt-base para Claude Code

```
Leia README.md, CLAUDE.md e plano_de_trabalho.md.
Execute a Etapa 0 conforme especificação.

Antes de qualquer extração, valide o acesso à pasta Drive sincronizada
lendo CORPUS_PDF_PATH do .env. Se o caminho não existe ou está vazio,
pare e reporte o problema com mensagem clara, sem improvisar.

Depois reporte: PDFs presentes, PDFs esperados ausentes, qualidade da
extração, e decisões metodológicas tomadas. Aguarde minha confirmação
antes de avançar para a Etapa 1.
```

### Commit esperado ao final da etapa

```
git add corpus/txt/ corpus/metadata.csv docs/decisoes_metodologicas.md
git commit -m "Etapa 0: extração de texto dos PDFs sincronizados via Drive"
```

---


## Etapa 1: Lexicometria mínima (prova de conceito)

### Objetivo

Validar que o pipeline funciona, antes de escalar. Trabalho com 10 termos por autor e dois livros apenas.

### Corpus inicial (sugerido; ajustar se necessário)

- **Latour:** *Science in Action* (1987, inglês original).
- **Haraway:** *Staying with the Trouble* (Duke 2016, inglês).

Se outro corpus inicial fizer mais sentido para Juliane, ajustar e registrar a decisão em `docs/decisoes_metodologicas.md`.

### Campos lexicais iniciais

**Latour, campo militar-industrial (`campos_lexicais/latour_militar_en.txt`):**
- ally, allies, alliance
- enroll, enrolment, recruit
- enemy, adversary, opponent
- trial of strength, trial, force
- army, troops, soldier
- battle, battlefield, war
- conquer, victory, defeat
- weapon, arsenal, weaponry
- mobilize, mobilization
- network (controle: termo neutro frequente)

**Haraway, campo têxtil-feminista (`campos_lexicais/haraway_textil_en.txt`):**
- string figure, cat's cradle
- thread, threading
- weave, weaving, woven
- knot, knotted
- tangle, tangled
- compost, composting
- tentacle, tentacular
- sympoiesis, sympoietic
- kin, kinship, make kin
- holobiont (controle: termo biológico frequente)

### Tarefas

1. **Implementar `scripts/02_kwic.py`** com as funções:
   - Carregamento de texto e campo lexical.
   - Busca de termos com variantes morfológicas (regex simples por sufixos comuns na Etapa 1; lemmatização entra na Etapa 3).
   - Extração de janela KWIC (50 palavras antes, 50 depois, configurável).
   - Saída CSV com colunas: `termo_buscado, termo_encontrado, obra, pagina_aproximada, posicao_no_texto, contexto_antes, trecho_central, contexto_depois`.
   - Tratamento de notas de rodapé: marcar e excluir quando detectáveis.

2. **Executar pipeline** para 2 livros × 2 campos lexicais (4 combinações).

3. **Gerar relatório-resumo** em `outputs/relatorios/etapa1_resumo.md`:
   - Total de ocorrências por termo, por par autor × campo.
   - As 3 passagens com maior densidade lexical por par (concentração de termos do campo lexical em janela próxima).
   - Indicadores de qualidade: termos com zero ocorrências, termos com mais de 100 ocorrências (suspeita de ruído alto).

### Gate de revisão

Juliane abre os CSVs em planilha, lê 20 ocorrências aleatórias por par autor × campo, e responde:
- O trecho central é uso significativo do termo?
- O contexto antes/depois é informativo (50 palavras é suficiente, demais, de menos)?
- Há falsos positivos óbvios?

### Prompt-base para Claude Code

```
Execute a Etapa 1. Implemente scripts/02_kwic.py conforme especificação,
processe Latour 1987 e Haraway 2016 com os campos lexicais em
campos_lexicais/, gere os CSVs em outputs/csv/etapa1/ e o relatório
em outputs/relatorios/etapa1_resumo.md. Documente decisões em
docs/decisoes_metodologicas.md. Aguarde minha revisão.
```

### Commit esperado

```
git add scripts/02_kwic.py campos_lexicais/ outputs/csv/etapa1/ \
        outputs/relatorios/etapa1_resumo.md docs/decisoes_metodologicas.md
git commit -m "Etapa 1: pipeline KWIC, 2 livros, 10 termos por autor"
```

---

## Etapa 2: Validação amostral

### Objetivo

Medir a qualidade do output da Etapa 1 antes de escalar, e refinar os campos lexicais.

### Tarefas

1. **Implementar `scripts/06_sampling.py`** para amostragem aleatória com seed fixa (`seed=42` por padrão).

2. **Sortear 30 ocorrências por par autor × campo** (total 120 ocorrências). Exportar em CSV com colunas pré-preenchidas e colunas em branco para codificação manual da Juliane:
   ```
   id, termo_buscado, trecho_central, contexto, [colunas_juliane:]
   uso_figural (sim/nao), marcacao (ironica/citacional/convicta/tecnica/casual),
   densidade_co_ocorrente, comentario
   ```

3. **Pausar e aguardar codificação da Juliane**. Esta é responsabilidade dela, não automatizável nesta etapa.

4. **Quando Juliane devolver o CSV codificado**, calcular:
   - **Precisão por termo**: % de ocorrências com `uso_figural = sim`. Corte sugerido: 70% para validar o termo. Abaixo disso, o termo é ruidoso e exige filtro contextual ou exclusão.
   - **Distribuição por marcação**: % de usos por categoria (irônico, citacional, etc.).
   - **Falsos positivos sistemáticos**: termos cuja precisão é baixa, com diagnóstico do tipo de erro.

5. **Falsos negativos**: pedir à Juliane que leia 5 páginas de cada livro à mão e identifique passagens figurais que o pipeline deixou passar. Acrescentar termos faltantes aos campos lexicais.

6. **Gerar `outputs/relatorios/etapa2_validacao.md`** com:
   - Métricas de precisão por termo.
   - Lista de termos a manter, retirar, acrescentar.
   - Filtros contextuais sugeridos (ex.: excluir `trial` quando próximo de `court`, `lawsuit`, `judge`).
   - Decisões finais aprovadas pela Juliane.

7. **Atualizar campos lexicais** em `campos_lexicais/` à luz das decisões.

### Gate de revisão

Juliane valida as métricas e aprova os refinamentos. **Esta é a etapa onde a pesquisadora codifica pessoalmente**; Claude Code só pré-processa e calcula métricas. A codificação qualitativa é responsabilidade humana.

### Prompt-base para Claude Code

```
Execute a Etapa 2. Sorteie 30 ocorrências por par autor × campo
(seed 42) e exporte CSV pré-preenchido em
outputs/csv/etapa2/amostra_validacao.csv com colunas em branco para
minha codificação. Aguarde meu retorno com o CSV codificado, e em
seguida calcule as métricas e produza o relatório de refinamento.
Documente cada decisão em docs/decisoes_metodologicas.md.
```

### Commit esperado

```
git add outputs/csv/etapa2/ outputs/relatorios/etapa2_validacao.md \
        campos_lexicais/ docs/decisoes_metodologicas.md
git commit -m "Etapa 2: validação amostral e refinamento de campos lexicais"
```

---

## Etapa 3: Lexicometria expandida sobre todo o corpus

### Objetivo

Aplicar o pipeline validado ao corpus completo, com campos lexicais refinados e lemmatização.

### Corpus completo

**Latour:**
- *Pasteur: guerre et paix des microbes* (1984, francês).
- *Science in Action* (1987, inglês).
- *Pandora's Hope* (1999, inglês).
- *Reassembling the Social* (2005, inglês).
- *On recalling ANT* (1999, artigo).
- *On actor-network theory: a few clarifications* (1996, artigo).

**Haraway:**
- *A Cyborg Manifesto* (1985, ensaio).
- *Situated Knowledges* (1988, artigo).
- *The Promises of Monsters* (1992, ensaio).
- *Modest_Witness@Second_Millennium* (1997).
- *The Companion Species Manifesto* (2003).
- *When Species Meet* (2008).
- *Staying with the Trouble* (2016).

**Stengers e Ingold** entram em escala reduzida (apenas dois livros principais por autor), ou ficam para a Etapa 7.

### Tarefas

1. **Verificar PDFs na pasta Drive sincronizada** (`CORPUS_PDF_PATH`) e reportar à Juliane quais obras esperadas ainda faltam.

2. **Extrair texto** para todos os PDFs presentes na pasta Drive, salvando em `corpus/txt/`.

3. **Atualizar campos lexicais por idioma**:
   - `campos_lexicais/latour_militar_fr.txt`: allié, recruter, ennemi, armée, victoire, mobiliser, bataille, conquérir, guerre, etc.
   - `campos_lexicais/latour_militar_pt.txt`: aliado, recrutar, inimigo, exército, vitória, mobilizar, batalha, conquistar, guerra, etc.
   - Demais autores: análogo.

4. **Implementar lemmatização** em `scripts/02_kwic.py` (versão refinada), usando spaCy:
   ```python
   import spacy
   nlp_en = spacy.load("en_core_web_sm")
   nlp_fr = spacy.load("fr_core_news_sm")
   nlp_pt = spacy.load("pt_core_news_sm")
   ```

5. **Executar pipeline KWIC** sobre corpus completo. Gerar CSV consolidado em `outputs/csv/etapa3/corpus_completo.csv`, com coluna adicional `idioma`.

6. **Gerar relatório** em `outputs/relatorios/etapa3_corpus.md`:
   - Total de ocorrências por termo, por obra, por autor.
   - Mapa de calor de densidade lexical ao longo de cada livro.
   - Comparação entre versões em línguas diferentes do mesmo autor (Latour francês vs. inglês vs. português, quando aplicável).

### Gate de revisão

Juliane olha o CSV consolidado, amostra 10 passagens densas por autor para conferência rápida da qualidade em escala.

### Prompt-base para Claude Code

```
Execute a Etapa 3. Processe o corpus completo conforme listado, aplique
lemmatização com spaCy, use campos lexicais refinados por idioma. Gere
CSV consolidado e relatório com mapas de calor de densidade. Documente
o tratamento de cada idioma e quaisquer ajustes em
docs/decisoes_metodologicas.md.
```

### Commit esperado

```
git add corpus/txt/ scripts/02_kwic.py campos_lexicais/ \
        outputs/csv/etapa3/ outputs/relatorios/etapa3_corpus.md \
        docs/decisoes_metodologicas.md
git commit -m "Etapa 3: lexicometria expandida sobre corpus completo"
```

---

## Etapa 4: Frequências comparadas e visualizações

### Objetivo

Transformar a tabela de ocorrências em material visual citável.

### Tarefas

1. **Implementar `scripts/04_visualizations.py`** com funções para:
   - Tabela de frequências absolutas e relativas (ocorrências por 10.000 palavras).
   - Gráfico temporal de evolução por autor.
   - Comparação cruzada Latour × Haraway por década.
   - Distribuição interna por livro (janela móvel).

2. **Gerar tabelas em LaTeX** em `outputs/latex/etapa4/`, com pacote `booktabs` se disponível, ou tabular padrão da SKILL.md da tese. Cada tabela com `\label{}` no padrão `tab:figuracoes_<descricao>`.

3. **Gerar gráficos** em `outputs/figuras/etapa4/`, em PNG (300 dpi) e SVG. Paleta acessível (sem vermelho/verde puros para daltonismo), fontes serifadas compatíveis com o estilo da tese (idealmente serifada padrão LaTeX).

4. **Relatório** em `outputs/relatorios/etapa4_analise.md` com observações sobre os 3 padrões mais salientes identificados.

### Variações analíticas a explorar

- Filtrar só ocorrências em capítulos onde há discussão explícita de método.
- Agregar termos por subcategoria (ex.: subcampo militar vs. subcampo agonístico geral).
- Comparar densidade em prefácios, introduções, capítulos centrais e conclusões.

### Gate de revisão

Juliane olha as tabelas e gráficos, identifica padrões, pede variações que façam sentido analítico.

### Prompt-base para Claude Code

```
Execute a Etapa 4. Use matplotlib (estilo limpo, paleta acessível) para
gráficos, e tabular do LaTeX para tabelas. Salve outputs em
outputs/figuras/etapa4/ e outputs/latex/etapa4/. Produza relatório
com observações sobre os padrões mais salientes.
```

### Commit esperado

```
git add scripts/04_visualizations.py outputs/figuras/etapa4/ \
        outputs/latex/etapa4/ outputs/relatorios/etapa4_analise.md \
        docs/decisoes_metodologicas.md
git commit -m "Etapa 4: frequências comparadas, tabelas e gráficos"
```

---

## Etapa 5: Cocorrências e redes figurais

### Objetivo

Mapear quais termos figurais aparecem juntos e construir a topologia de cada vocabulário.

### Tarefas

1. **Implementar `scripts/05_cooccurrence.py`** com:
   - Matriz de cocorrência (testar janelas de 100, 200, 500 palavras).
   - Conversão em grafo via NetworkX.
   - Detecção de comunidades com Louvain (`python-louvain`).
   - Visualização com matplotlib + NetworkX (nó dimensionado por frequência, aresta dimensionada por força de cocorrência, layout *force-directed*).

2. **Gerar redes** lado a lado para Latour e Haraway, em PNG e SVG.

3. **Identificar clusters** (comunidades detectadas) e **termos-ponte** (que aparecem em múltiplos clusters).

4. **Relatório** em `outputs/relatorios/etapa5_redes.md` com:
   - Listagem dos clusters identificados por autor.
   - Comparação topológica entre os autores.
   - Termos-ponte e sua função argumentativa.
   - Decisão sobre janela ótima (a documentar).

### Gate de revisão

Juliane olha as redes, valida se os clusters fazem sentido conceitual, decide quais visualizações entram na tese.

### Prompt-base para Claude Code

```
Execute a Etapa 5. Use NetworkX e python-louvain. Teste 3 janelas
(100, 200, 500 palavras) e reporte qual produz redes mais informativas.
Gere visualizações em PNG e SVG, com nós e arestas dimensionados.
Produza relatório com clusters e termos-ponte. Documente decisão sobre
janela em docs/decisoes_metodologicas.md.
```

### Commit esperado

```
git add scripts/05_cooccurrence.py outputs/figuras/etapa5/ \
        outputs/relatorios/etapa5_redes.md docs/decisoes_metodologicas.md
git commit -m "Etapa 5: cocorrências e redes figurais"
```

---

## Etapa 6: Anotação manual amostral

### Objetivo

Produzir dado qualitativo denso sobre uma amostra significativa, para sustentar interpretação na Etapa 7.

### Tarefas

1. **Selecionar 50 passagens por autor**: 25 das passagens com maior densidade lexical (top 25 da Etapa 4) + 25 aleatórias do restante para evitar viés. Seed fixa.

2. **Schema de codificação qualitativa** (CSV com colunas):
   ```
   id, autor, obra, pagina, passagem_completa_200_palavras,
   tipo_figuracao (militar/textil/organica/arquitetural/cartografica/outra),
   funcao_argumentativa (inaugural/recorrente/subordinada/ironica_citacional),
   articulacao_outras_figuracoes (campo aberto),
   densidade_conceitual (1-5),
   citacao_na_tese (sim/talvez/nao),
   justificativa_citacao,
   comentario_livre,
   [colunas_juliane:]
   concordo_claude (sim/parcial/nao),
   minha_codificacao_se_diferente,
   anotacao_metodologica
   ```

3. **Claude Code pré-anota** cada passagem com justificativa em 2-3 linhas.

4. **Juliane revisa cada passagem**, marca concordância ou discordância, registra discordâncias como dado metodológico.

5. **Relatório** em `outputs/relatorios/etapa6_anotacao.md` com:
   - Taxa de concordância pesquisadora vs. modelo.
   - Tipos de discordância (modelo classifica diferente, modelo erra detecção do tipo, modelo erra a função argumentativa, etc.).
   - Passagens marcadas para citação na tese.

### Princípio crítico

Esta é a etapa onde "o método é parte do argumento" se concretiza. As **discordâncias** entre Juliane e Claude Code são registradas como **dado etnográfico** sobre o que significa trabalhar com um modelo de linguagem, e vão alimentar o apêndice metodológico.

### Gate de revisão

Juliane valida a coerência da própria codificação, identifica tendências interpretativas que vai querer desenvolver na Etapa 7.

### Prompt-base para Claude Code

```
Execute a Etapa 6. Selecione 50 passagens por autor (25 top-densidade
+ 25 aleatórias com seed 42). Pré-anote cada uma com justificativa em
2-3 linhas. Salve CSV em outputs/csv/etapa6/anotacao_amostral.csv
com colunas para minha revisão. Após minha revisão, calcule taxa de
concordância e classifique tipos de discordância, em
outputs/relatorios/etapa6_anotacao.md.
```

### Commit esperado

```
git add scripts/06_sampling.py outputs/csv/etapa6/ \
        outputs/relatorios/etapa6_anotacao.md docs/decisoes_metodologicas.md
git commit -m "Etapa 6: anotação amostral, 50 passagens por autor"
```

---

## Etapa 7: Leitura interpretativa assistida

### Objetivo

Produzir cartografia figural por capítulo, com Claude Code como leitor assistente.

### Tarefas

1. **Por livro, por capítulo**, Claude Code produz síntese de 300-500 palavras respondendo:
   - Quais figurações organizam este capítulo?
   - Qual a função argumentativa de cada uma?
   - Há tensões ou contrastes entre figurações dentro do capítulo?
   - Há passagens que dialogam diretamente com o outro autor?
   - Quais passagens são candidatas a citação na tese?

2. **Cada afirmação** com citação direta de página entre aspas. Afirmações sem citação direta marcadas com `[INFERÊNCIA]`.

3. **Juliane valida por amostragem**: lê 3 capítulos por livro em paralelo e compara com a síntese do Claude Code.

4. **Mapa figural por livro**: representação visual da progressão de figurações ao longo dos capítulos, em diagrama Mermaid (em coerência com o resto da tese).

5. **Síntese comparativa Latour × Haraway**: documento de 5-10 páginas em que **Juliane redige** a interpretação final, usando os outputs do Claude Code como insumo. Esse documento é responsabilidade da pesquisadora; Claude Code só organiza o material.

### Caveat crítico

Esta é a etapa mais sujeita a alucinação. A revisão amostral não é opcional, é estrutural. Discordâncias importantes entre leitura de Juliane e do modelo devem ser registradas como dado metodológico, não corrigidas silenciosamente.

### Gate de revisão

Juliane valida sínteses por capítulo, pede refinos onde necessário, e escreve a síntese comparativa final.

### Prompt-base para Claude Code

```
Execute a Etapa 7. Para cada livro do corpus, produza síntese por
capítulo conforme especificação. Use apenas passagens dos próprios
livros como evidência, com citação literal entre aspas e indicação
de página. Marque com [INFERÊNCIA] qualquer afirmação que não tenha
citação direta como base. Salve em outputs/relatorios/etapa7/. Gere
mapa figural Mermaid. Não produza a síntese comparativa final.
```

### Commit esperado

```
git add outputs/relatorios/etapa7/ outputs/figuras/etapa7/ \
        docs/decisoes_metodologicas.md
git commit -m "Etapa 7: leitura interpretativa por capítulo"
```

---

## Etapa 8: Consolidação para a tese

### Objetivo

Transformar o trabalho acumulado em material citável e em apêndice metodológico da tese.

### Tarefas

1. **Apêndice metodológico** em `docs/apendice_tese.md` e `outputs/latex/apendice_metodologico.tex` (10-15 páginas):
   - Descrição do método.
   - Apresentação do corpus.
   - Decisões tomadas e suas justificativas.
   - Limitações declaradas.
   - Achados.
   - Descrição etnográfica da cadeia mim → Claude Code → minha revisão, em coerência com a tese sobre mediação técnica.

2. **Tabelas e figuras para o capítulo 2 da tese**:
   - Selecionar 2-3 figuras das Etapas 4 e 5.
   - Selecionar 1-2 tabelas de frequências comparadas.
   - Exportar em LaTeX pronto para `\input{}` no master da tese.

3. **Banco de citações** em `outputs/csv/etapa8/citacoes_selecionadas.csv`:
   - 15-20 passagens prontas para incorporação.
   - Cada uma com referência ABNT completa, contexto, função argumentativa na tese, capítulo da tese onde encaixa.

4. **Limpeza final do repositório**:
   - Remover arquivos intermediários grandes que não precisam ser versionados.
   - Atualizar `README.md` com estado final.
   - Verificar que todas as decisões estão documentadas em `docs/decisoes_metodologicas.md`.

5. **Tag de versão**:
   ```bash
   git tag -a v1.0-tese -m "Versão consolidada para incorporação à tese"
   git push origin v1.0-tese
   ```

### Gate final

Revisão integrada de tudo, com olhar editorial.

### Prompt-base para Claude Code

```
Execute a Etapa 8. Produza apêndice metodológico em Markdown e LaTeX,
exporte figuras e tabelas selecionadas para outputs/latex/, monte
banco de citações em CSV. Atualize README com estado final. Aguarde
minha revisão e a tag de versão.
```

### Commit esperado

```
git add docs/apendice_tese.md outputs/latex/ outputs/csv/etapa8/ README.md
git commit -m "Etapa 8: consolidação para a tese"
git tag -a v1.0-tese -m "Versão consolidada"
```

---

## Princípios transversais

1. **Cada etapa é fechada**: produz artefato próprio, usável mesmo se a etapa seguinte não for executada.

2. **Reprodutibilidade**: seeds fixos, scripts versionados, decisões documentadas. Outra pesquisadora deve poder reexecutar e obter os mesmos resultados.

3. **Validação humana é estrutural**: Claude Code propõe, Juliane valida. Discordâncias são registradas, não silenciadas.

4. **O método é parte do argumento**: a cadeia mim → Claude Code → minha revisão é descrita no apêndice em registro etnográfico.

5. **Pluralidade linguística é parte do dado**: traduções viram camadas de mediação a explicitar.

6. **Limites declarados**: lexicometria detecta presença, não nuances de uso. Os limites são parte da honestidade epistêmica.

7. **Erro como dado**: falsos positivos e negativos viram seção do apêndice, não problema a esconder.

---

## O que NÃO está neste plano (escopo)

- Análise de discurso fina, reconstrução de argumento em sentido filosófico denso.
- Comparação com toda a tradição STS (Pinch, Bijker, Collins, Forsythe). Pode-se acrescentar Forsythe e Collins na Etapa 3 como controle externo.
- Adensamento de Ingold, Stengers, Mol como autores centrais.
- Análise de imagens (capas, diagramas internos).

---

## Decisões pendentes da Juliane antes do início

1. Confirmar corpus inicial da Etapa 1 (Latour 1987 + Haraway 2016?).
2. Confirmar quais PDFs já tem e quais ainda precisa adquirir.
3. Decidir idioma de trabalho preferencial: originais sempre, ou também comparar com traduções brasileiras?
4. Confirmar que a janela KWIC inicial é 50 palavras de cada lado.
5. Confirmar a estrutura de pastas e o nome do repositório no GitHub.

Documentar as respostas em `CLAUDE.md` antes de iniciar a Etapa 0.

---

## Como Claude Code deve operar (resumo)

1. Não avançar entre etapas sem confirmação explícita da Juliane.
2. Documentar cada decisão em `docs/decisoes_metodologicas.md`.
3. Marcar `[INFERÊNCIA]` em afirmações sem citação direta.
4. Seeds fixos em qualquer processo estocástico.
5. Scripts em Python 3.11+, PEP 8, comentários em português.
6. Outputs em CSV (aberto) e LaTeX (para a tese) quando aplicável.
7. Em ambiguidade metodológica, parar e perguntar, em vez de decidir sozinho.
8. Traduções como camada de mediação, sem mesclar idiomas no mesmo CSV sem coluna `idioma`.
