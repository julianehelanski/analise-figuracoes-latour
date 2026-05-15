# Log de execucao - Etapa 2.6 final

Data: 2026-05-15.

Sessao de finalizacao da Etapa 2.6 (validacao amostral semantica), apos
preenchimento manual da planilha pela pesquisadora.

## Tarefas concluidas nesta sessao

1. **Correcao do bug de `id_kwic`**: a coluna estava reiniciada por
   camada (e.g. `actor_network#0000` aparecia tres vezes, uma por
   camada). Reescrita usando `<obra>#<campo>#pos_NNNNNN`, com NNNNNN =
   offset em caracteres no `.txt` normalizado, casado por
   `(grupo, termo_encontrado, contexto_antes, contexto_depois)` com o
   `kwic.csv` original. Casamento 82/82 confirmado.

2. **Correcao do bug de `pagina`**: a coluna estava fixa em "1". Sem
   marcadores `<<PG_VOL=N>>` no corpo dos `.txt`, mapeei a posicao
   absoluta de cada ocorrencia ao bloco de paragrafo correspondente
   no texto normalizado, e atribui a pagina citavel:
   - *Clarifications*: paginas 369-381 do Soziale Welt 47(4), uma por
     bloco-de-paragrafo do `.txt`.
   - *Recalling*: paginas 16, 18, 20, 22, 24 do volume Law & Hassard.

3. **Outputs analiticos da Etapa 2.6**:
   - `validacao_amostral_resultados.md`: 8 secoes com taxas por campo,
     por obra, por camada, mapa de polissemia, achado central sobre o
     registro metalinguistico do Recalling, validacao exaustiva do
     textil (15/16) e diagnostico da camada C.
   - `tabela_textil_topologico_refinada.tex`: tabela LaTeX para a tese,
     com Clarifications, Recalling e Science in Action; a taxa de
     figuralidade para SiA fica como pendente.
   - `log_execucao.md` (este arquivo).

4. **Candidatos metalinguistico retroativo nos livros** (TAREFA 4):
   `metalinguistico_retroativo_livros.csv` com ocorrencias dos campos
   `network` e `actor_network` nos tres livros que ativam gatilhos
   automaticos (`vocabulary`, `the word`, `the notion`, `the term`,
   `the expression of`, `let us abandon`, `coffin`, `so-called`,
   `misunderstanding`, `misrepresented`). Coluna `classificacao_manual`
   em branco; aguarda leitura da pesquisadora em Etapa 2-bis.

## Decisoes pequenas tomadas no caminho

- Subcategoria `definicao_operacional` cunhada pela pesquisadora durante
  o preenchimento (passagem `AT makes use of some of the simplest
  properties of nets`) aceita como sexta subcategoria valida, em coerencia
  com o registro etnografico do metodo.
- Pagina no Recalling: convencao do volume (16-24), nao do zip de OCR
  (1-11). A convencao do zip fica registrada implicitamente no id_kwic
  por offset.
- Validacao do textil em Clarifications tratada como exaustiva (15/16
  ocorrencias, cobertura 93,75%; variante nao amostrada: `fiber`).
- TAREFA 4 restrita ao gatilho metalinguistico em network e actor_network,
  como solicitado.

## Outputs gerados

- `outputs/etapa2_artigos/validacao_amostral_semantica_PREENCHIDA.csv`
  (intocada, classificacoes da pesquisadora).
- `outputs/etapa2_artigos/validacao_amostral_semantica_PREENCHIDA_CORRIGIDA.csv`.
- `outputs/etapa2_artigos/validacao_amostral_resultados.md`.
- `outputs/etapa2_artigos/tabela_textil_topologico_refinada.tex`.
- `outputs/etapa2_artigos/metalinguistico_retroativo_livros.csv`.
- `outputs/etapa2_artigos/log_execucao.md` (este arquivo).
- Atualizacao da secao Etapa 2 de `docs/decisoes_metodologicas.md` com a
  subsecao "Rendimento da validacao amostral A/B/C".

## Pendencias

- Validacao retroativa do protocolo A/B/C aos tres livros monograficos
  (Lab Life, Sci. in Action, Pandora). A taxa de figuralidade para
  Science in Action na tabela LaTeX fica como `pendente` ate la.
- Leitura manual dos candidatos metalinguisticos retroativos pela
  pesquisadora (Etapa 2-bis).
- PDF nativo do Recalling, se acessivel, para reanalise integral do
  artigo (pendencia aberta desde a Etapa 2.0).
