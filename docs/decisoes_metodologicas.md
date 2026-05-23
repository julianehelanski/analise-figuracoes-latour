# Decisões metodológicas — projeto `analise_figuracoes`

Este documento registra as decisões metodológicas tomadas para cada etapa da análise computacional do corpus teórico mobilizado na tese. Cada decisão é datada, justificada e revisável. Alterações posteriores devem ser registradas em adendo, com data e razão, sem sobrescrever a decisão anterior.

---

## Etapa 1 — Análise de trajetória conceitual em três obras de Bruno Latour (1986, 1987, 1999)

Data da decisão: 13 de maio de 2026.

### Objetivo analítico

A Etapa 1 rastreia o vocabulário figurativo de Bruno Latour em três obras publicadas ao longo de duas décadas, com objetivo de mapear continuidades, deslocamentos e introduções conceituais ao longo da trajetória do autor. A escolha de três obras do mesmo autor (em vez de uma) permite análise de trajetória que análise de obra única não oferece: como conceitos como *inscription*, *black box*, *immutable mobile* aparecem, persistem ou são reformulados ao longo do tempo, e quais figurações são introduzidas em momentos específicos da obra (por exemplo, *factish* em 1999).

A primeira obra do corpus, *Laboratory Life* (1986), tem coautoria com Steve Woolgar. Esse fato é registrado no metadata e considerado na análise: o vocabulário figurativo do livro é coautoral, e a comparação com as obras subsequentes (de Latour solo) permite observar quais figurações persistem após a parceria.

### 1. Corpus inicial

**Decisão**: a Etapa 1 processa três obras, todas em inglês:

- `latour_woolgar_1986_lab_life_en` — Latour e Woolgar, *Laboratory Life: The Construction of Scientific Facts*, Princeton University Press, 1986 (segunda edição).
- `latour_1987_science_action_en` — Bruno Latour, *Science in Action: How to Follow Scientists and Engineers through Society*, Harvard University Press, 1987.
- `latour_1999_pandora_en` — Bruno Latour, *Pandora's Hope: Essays on the Reality of Science Studies*, Harvard University Press, 1999.

**Justificativa**: as três obras compõem a trajetória de Latour entre o estudo etnográfico inicial do laboratório (com Woolgar), a sistematização da teoria ator-rede como programa de pesquisa, e a reflexão posterior sobre realismo científico e mediação. O vocabulário figurativo de cada obra é parcialmente herdeiro do anterior e parcialmente novo. Mapear esses três momentos permite produzir resultados que dialogam diretamente com a tese, em que Latour é mobilizado em todos os capítulos.

**Escolha da edição de *Laboratory Life***: a edição de 1986 (Princeton) substitui a de 1979 (Sage). A diferença não é trivial: a edição de 1986 remove a palavra "Social" do subtítulo (de *The Social Construction of Scientific Facts* para *The Construction of Scientific Facts*) e inclui um pós-escrito em que os autores justificam essa remoção. O pós-escrito é, ele mesmo, registro de deslocamento figurativo. A edição 1986 contém o texto da edição 1979 acrescido do pós-escrito, e é a edição mais citada na literatura subsequente.

### 2. Idioma de trabalho

**Decisão**: inglês. Modelo spaCy a carregar: `en_core_web_sm`.

**Justificativa**: as três obras são originais em inglês. Latour é francês e parte da sua obra é publicada originalmente em francês, mas as três obras desta etapa foram escritas e publicadas em inglês como textos originais (não como traduções). A análise se faz na língua de publicação original. Traduções para o português entram em rodadas posteriores, com pergunta analítica distinta.

### 3. Janela KWIC

**Decisão**: janela de ±10 palavras (10 palavras antes do termo-alvo e 10 palavras depois).

**Justificativa**: 5 palavras (padrão `nltk` e CLAWS) trunca a unidade argumentativa na prosa teórica densa de Latour, em que conceitos como *immutable mobile* ou *centre of calculation* costumam vir acompanhados de elaboração extensa. Janelas de 15 ou mais palavras geram contexto longo demais para leitura rápida durante validação amostral. 10 palavras é o ponto onde a unidade argumentativa fecha sem produzir excesso. A janela é parâmetro revisável: se a validação amostral mostrar que casos específicos exigem janela maior, o ajuste pode ser feito por termo, com adendo abaixo.

### 4. Catálogo único de termos em YAML

**Decisão**: aceita. O catálogo de termos a rastrear será mantido em arquivo único `campos_lexicais/catalogo_termos.yaml`, com hierarquia autor → campo figurativo → termos, e metadados por termo (variantes, lematização, exclusões, nota analítica).

**Justificativa**: arquivo único é mais auditável que múltiplos `.txt` plano. YAML permite registrar variantes, exclusões e notas que em `.txt` virariam ruído. O catálogo torna-se artefato citável: pode integrar o apêndice metodológico da tese, documentando exatamente quais termos foram rastreados e com que critérios.

**Estrutura inicial do catálogo para a Etapa 1 (Latour)**:

```yaml
latour:
  inscription:
    termos: ["inscription", "inscriptions", "inscription device", "inscription devices", "literary inscription"]
    nota: "Conceito presente desde Laboratory Life. Verificar continuidade nas tres obras."
  immutable_mobile:
    termos: ["immutable mobile", "immutable mobiles"]
    nota: "Aparece em Science in Action. Rastrear se ha precursor em Laboratory Life."
  black_box:
    termos: ["black box", "black-box", "black boxes", "blackbox", "blackboxing", "black-boxing"]
    nota: "Verificar primeira ocorrencia entre as tres obras."
  centre_of_calculation:
    termos: ["centre of calculation", "center of calculation", "centres of calculation", "centers of calculation"]
    nota: "Variantes ortograficas britanica e americana."
  actor_network:
    termos: ["actor-network", "actor network", "actant", "actants"]
    nota: "Em Laboratory Life o termo 'actant' ja aparece. Em Science in Action a expressao actor-network se consolida."
  translation:
    termos: ["translation", "translations", "translate", "translates", "translated"]
    exclusoes: ["translation of", "english translation", "french translation"]
    nota: "Atencao a falsos positivos: 'translation' em sentido linguistico trivial precisa ser separado do sentido conceitual."
  trial_of_strength:
    termos: ["trial of strength", "trials of strength"]
    nota: "Conceito de Science in Action."
  factish:
    termos: ["factish", "factishes"]
    nota: "Neologismo de Pandora's Hope. Verificar se ha precursores."
  circulating_reference:
    termos: ["circulating reference", "circulating references"]
    nota: "Pandora's Hope."
  articulation:
    termos: ["articulation", "articulations", "articulate", "articulated"]
    nota: "Conceito reformulado em Pandora's Hope. Possivel ruido por usos triviais do termo."
  construction:
    termos: ["construction", "constructed", "constructing", "social construction"]
    nota: "Conceito central em Laboratory Life. O pos-escrito de 1986 discute a polissemia do termo."
  proposition:
    termos: ["proposition", "propositions"]
    nota: "Reformulacao em Pandora's Hope. Atencao a usos logicos triviais."
  network:
    termos: ["network", "networks", "networking"]
    exclusoes: ["telephone network", "computer network"]
    nota: "Termo polissemico. Validacao amostral cuidadosa."
  agonistic:
    termos: ["agonistic", "agonistics", "agonistic field"]
    nota: "Science in Action."
  enrollment:
    termos: ["enrollment", "enrolment", "enroll", "enrol", "enrolled"]
    nota: "Variantes ortograficas britanica e americana."
  spokesperson:
    termos: ["spokesperson", "spokespersons", "spokesman", "spokesmen", "spokeswoman"]
    nota: "Traducao do frances 'porte-parole'."
```

### 5. Validação amostral das heurísticas de detecção de corpo e de qualidade

**Decisão**: validação por amostra estratificada de 15 páginas por obra (45 páginas no total para as três obras), distribuídas em cinco categorias de 3 páginas cada.

**Justificativa**: a validação estratificada garante representatividade dos contextos onde a heurística pode falhar. A redução de 25 para 15 páginas por obra é compensada pela triplicação do número de obras: 45 páginas no total cobre proporcionalmente mais diversidade de layouts editoriais e padrões de extração do que 25 páginas de uma obra única. Se durante a revisão a taxa de erro em uma categoria ultrapassar 20%, a amostra naquela categoria é ampliada e a heurística correspondente é ajustada.

**Distribuição da amostra (por obra)**:

- 3 páginas marcadas pelo algoritmo como início de capítulo
- 3 páginas marcadas como corpo de capítulo
- 3 páginas marcadas como notas de fim
- 3 páginas marcadas como bibliografia, índice remissivo ou outros paratextos
- 3 páginas com aviso automático de qualidade baixa (caracteres corrompidos, falhas de OCR, ligaduras mal extraídas)

Resultado da validação fica registrado em três arquivos:

- `outputs/etapa1/latour_woolgar_1986_lab_life_en/relatorios/validacao_amostral_etapa1.md`
- `outputs/etapa1/latour_1987_science_action_en/relatorios/validacao_amostral_etapa1.md`
- `outputs/etapa1/latour_1999_pandora_en/relatorios/validacao_amostral_etapa1.md`

### 6. Estrutura do relatório final da Etapa 1

**Decisão**: o relatório final da Etapa 1 é organizado em dois níveis: relatório por obra (três arquivos) e relatório de trajetória (um arquivo consolidado).

**Por obra**: cada obra recebe seu próprio diretório de outputs em `outputs/etapa<N>/<id_da_obra>/`, com KWIC, tabelas de frequência, visualizações e relatório descritivo.

**Trajetória consolidada**: o arquivo `outputs/etapa1/trajetoria_latour_1986_1999.md` agrega resultados das três obras com foco em três perguntas:

1. Quais figurações aparecem em todas as três obras? Com que frequência relativa?
2. Quais figurações são introduzidas em uma obra e desaparecem ou persistem nas seguintes?
3. Como o vocabulário coautoral de *Laboratory Life* (Latour-Woolgar) se relaciona com o vocabulário das obras posteriores de Latour solo?

A estrutura comparativa do relatório de trajetória é o que torna a Etapa 1 analiticamente distinta de três análises independentes empilhadas.

---

## Adendos

### Adendo 1 (14 de maio de 2026): pipeline de normalização pré-KWIC

Decisão tomada após a primeira inspeção amostral dos três `corpus/txt/<id>.txt`. Inspeção registrou três artefatos sistemáticos de extração que, sem tratamento, contaminam a tokenização e o casamento de termos do catálogo:

- `latour_woolgar_1986_lab_life_en.txt`: 578 hifenizações de fim de linha (`infor-\nmation`).
- `latour_1987_science_action_en.txt`: 276 marcadores `((NN))` injetados no corpo pelo conversor (formato `((1))`, `((2))`, ...).
- `latour_1999_pandora_en.txt`: cerca de 2.500 caracteres não-ASCII dominados por soft hyphens U+00AD dentro de palavras (`per­formed`, `tech­nology`, `philoso­phers`); 220 replacement chars `�`; cabeçalhos com letras espaçadas (`P A N D O R A ' S H O P E`) repetidos no topo de muitas páginas.

Para preservar os textos crus como artefato auditável e operar a análise sobre versão normalizada, fica decidido:

1. Os arquivos em `corpus/txt/<id>.txt` permanecem intocados como extrações cruas. São o registro daquilo que o conversor entregou.
2. O script `scripts/01b_normalize_text.py` aplica seis operações de normalização e grava o resultado em `corpus/txt_norm/<id>.txt`. As operações, em ordem:
   1. Soft hyphen U+00AD removido.
   2. De-hifenização de fim de linha: `r"-\n(?=[a-z])"` substituído por `""`, juntando palavras quebradas pelo layout. Hifens médios (`actor-network`) ficam intactos.
   3. Marcadores `((NN))` substituídos por espaço.
   4. Linhas que casam o padrão de cabeçalho espaçado (sequências de caracteres únicos separados por espaço) descartadas.
   5. NFKC e mapeamento de aspas tipográficas (`‘’“”`) para ASCII; travessões longos (`–—`) para `-`.
   6. Replacement chars `�` substituídos por espaço (preserva separação de tokens; o caso reaparece na validação amostral da Etapa 2).
3. Os scripts seguintes (02 a 06) lêem a partir de `corpus/txt_norm/<id>.txt`. A tabela de páginas `corpus/paginas/<id>.csv` é regenerada a partir da versão normalizada, mantendo a heurística de classificação de `01_extract_text.py`. `corpus/qualidade_extracao.csv` é atualizado a partir das contagens da versão normalizada.
4. Nenhum parâmetro analítico da Etapa 1 muda. Janela KWIC continua ±10 palavras. Catálogo continua o mesmo. Amostra estratificada continua 15 páginas por obra. A normalização é preparação técnica.

Justificativa: sem essas seis operações, o KWIC perde casamentos óbvios em Pandora (`per­formed` não casa `performed`) e produz tokens espúrios em Science in Action (`((103))` virando token). Tratar de forma uniforme as três obras é o que permite que a comparação de trajetória produza números comparáveis.

### Adendo 2 (14 de maio de 2026): correção da heurística de classificação de páginas

Decisão tomada após a primeira rodada da amostra estratificada. A heurística original em `scripts/01_extract_text.py` tratava `paratexto` como estado único e sticky. Como toda obra começa com `Contents` ou `Sumário`, o estado entrava em `paratexto` na primeira página e nunca saía. Consequência: 282/296 (Lab Life), 309/314 (Science in Action) e 328/337 (Pandora) páginas classificadas como `paratexto`, com `corpo` colapsado para 4, 2 e 3 páginas respectivamente. A amostra estratificada, que pede 3 páginas por estrato, ficou inviável: 26 páginas em vez de 45.

Correção:

1. A regex `_RE_PARATEXTO` é decomposta em duas. `_RE_FRONT_MATTER` casa `contents`, `table of contents`, `sumário`, `sumario`, `acknowledgements`, `acknowledgments`, `agradecimentos`, `preface`, `prefácio`, `prefacio`, `dedication`, `introduction`, `foreword`. `_RE_BACK_MATTER` casa `bibliography`, `references`, `additional references`, `bibliografia`, `index`, `índice`, `indice`, `appendix`, `apêndice`, `apendice`.
2. O estado interno passa a ter três valores: `front_matter` (inicial, não-sticky), `corpo`, `back_matter` (sticky). `notas_fim` continua sendo classe de transição entre `corpo` e `back_matter`.
3. Detecção de início de capítulo (`Chapter N`, `CHAPTER N`, `Capítulo N`) passa a transitar para `corpo` mesmo se o estado atual for `front_matter`. Esse é o ponto que destrava o algoritmo: a primeira ocorrência de `Chapter 1` (Lab Life pg16, Science in Action pg25, Pandora — variantes) sai do front matter e começa a contar o corpo do livro.
4. `back_matter` continua sticky: uma vez em `Bibliography`, `Index`, etc., não se volta para `corpo`.
5. A classe registrada em `corpus/paginas/<id>.csv` permanece com cinco valores (`inicio_capitulo`, `corpo`, `notas_fim`, `paratexto`, `qualidade_baixa`) para preservar a estrutura dos estratos da decisão original. O front matter e o back matter ambos rotulam como `paratexto`; o estado interno apenas controla a transição.

A correção é replicada em `scripts/01_extract_text.py` (para quando a extração for refeita a partir do PDF) e em `scripts/01b_normalize_text.py` (para a regeneração imediata sobre os textos já normalizados). O catálogo de termos, a janela KWIC e a amostra estratificada (15 páginas por obra, 5 estratos de 3) permanecem inalterados. Os arquivos de KWIC, frequência, cocorrência e trajetória já gerados **não** são afetados, porque essas análises operam sobre o texto integral e não dependem da classificação por estado.

### Adendo 3 (14 de maio de 2026): refinamentos posteriores na heurística de página

Após a primeira rodada do Adendo 2, dois ajustes adicionais foram necessários para acomodar diferenças tipográficas entre as três obras:

1. **Início de capítulo detectado só no topo da página** (5 primeiras linhas, `_LINHAS_TOPO_INICIO_CAPITULO = 5`). Motivo: a página de abertura da seção de notas de Science in Action (pg282) começa com `Notes` seguido de `Introduction` e depois `Chapter 1` como subtítulo do agrupamento de notas por capítulo. A regex original casava `Chapter 1` em qualquer lugar da página e classificava erroneamente esta página como `inicio_capitulo`. Restringir a detecção ao topo da página resolve esse falso positivo sem sacrificar a detecção de capítulos reais, que sempre aparecem como cabeçalho na primeira linha não-vazia da página.

2. **Variantes tipográficas adicionais para início de capítulo**. A regex `_RE_INICIO_CAPITULO` foi estendida com três alternativas:
   - `^\s*(chapter|capítulo|capitulo|chapitre|part|parte)\s+(\d+|[ivxlcdm]+)\b` — padrão canônico (Lab Life, Science in Action).
   - `^\s*C\s+H\s+A\s+P\s+T\s+E\s+R\b` — letras espaçadas (Pandora's Hope, que tipografa cabeçalhos como `C H A P T E R   O N E`).
   - `^\s*chapter\s+(one|two|three|four|five|six|seven|eight|nine|ten)\b` — ordinal por extenso (também usado em Pandora).

Distribuição final de páginas por classe:

| Obra | inicio_capitulo | corpo | notas_fim | paratexto | qualidade_baixa |
|---|---:|---:|---:|---:|---:|
| `latour_woolgar_1986_lab_life_en` | 7 | 200 | 33 | 46 | 10 |
| `latour_1987_science_action_en` | 4 | 277 | 4 | 27 | 2 |
| `latour_1999_pandora_en` | 3 | 297 | 0 | 31 | 6 |

A amostra estratificada subsequente produz 41/45 páginas. As 4 páginas faltantes correspondem a estratos onde o livro não oferece material: 1 em `qualidade_baixa` de Science in Action (livro com extração quase perfeita) e 3 em `notas_fim` de Pandora (cuja seção de notas é absorvida pelo back matter sem cabeçalho `Notes` isolado).

---

## Etapa 2 — Validação amostral

Data da execução: 14 de maio de 2026.

### Procedimento

A validação amostral aplica critérios uniformes sobre o texto normalizado em `corpus/txt_norm/<obra>.txt` para cada uma das 41 páginas amostradas. Implementação em `scripts/08_validate_sample.py`. Cada página recebe três campos preenchidos automaticamente:

- `estrato_correto` (`sim`, `parcial`, `nao`): se o estrato predito é confirmado pelo conteúdo da página.
- `erro_extracao`: descrição curta de problemas visíveis na página (replacement chars, letras espaçadas, linhas com excesso de caracteres não-alfa, soft hyphens residuais).
- `decisao_metodologica`: justificativa em uma linha; recebe prefixo `[INFERÊNCIA]` quando a decisão depende do estado de vizinhança e não de marcador objetivo na própria página.

A leitura final cabe à pesquisadora. Casos `parcial` ficam registrados para revisão manual antes de virarem citação na tese.

### Critérios automáticos por estrato

- `inicio_capitulo` confirmado quando `_RE_INICIO_CAPITULO` casa nas 5 primeiras linhas da página.
- `corpo` confirmado quando a página tem ≥150 palavras de prosa contínua, sem cabeçalho de front/back matter, sem dominância de notas numeradas.
- `notas_fim` confirmado quando há cabeçalho `Notes`/`Notas` no topo ou ≥4 linhas com padrão `^\d+\s+[A-Z]` (notas numeradas).
- `paratexto` confirmado quando há cabeçalho de front ou back matter, ≥3 entradas de índice (`palavra N, N, N`) ou ≥3 linhas de TOC (linha terminando em número de página).
- `qualidade_baixa` confirmado quando a página tem <10 palavras, replacement chars, ou >5% caracteres não-padrão.

### Resultado

| Estrato | n | sim | parcial | nao | taxa de confirmação |
|---|---:|---:|---:|---:|---:|
| `inicio_capitulo` | 9 | 9 | 0 | 0 | 100% |
| `corpo` | 9 | 9 | 0 | 0 | 100% |
| `notas_fim` | 6 | 3 | 3 | 0 | 50% |
| `paratexto` | 9 | 6 | 3 | 0 | 67% |
| `qualidade_baixa` | 8 | 8 | 0 | 0 | 100% |

Taxa de erro confirmado (`nao`): 0/41 = 0%, abaixo da tolerância de 20% prevista na decisão de 13/05/2026 (Etapa 1, seção 5). A heurística de classificação atende à regra.

### Casos `parcial` para revisão manual

Os seis casos `parcial` decorrem de páginas onde a heurística predisse pelo estado da vizinhança, sem marcador objetivo na própria página:

- Lab Life pg94, pg96, pg102: páginas com placeholder `Image Not Available NN` referentes ao Photograph File (pg91--104). Classificadas como `notas_fim` por herança do estado (Notes do capítulo 2 termina em pg88). Ajuste futuro: a heurística poderia reconhecer páginas de figura como classe própria (`figura`), mas o ganho analítico é baixo porque essas páginas têm 4 palavras cada.
- Lab Life pg284: segunda página do **Postscript da 2ª edição**, classificada como `paratexto` por herança de back matter. Esse é um caso metodologicamente sensível: o Postscript é o conteúdo distintivo da edição de 1986 (justifica a remoção de "Social" do subtítulo) e contém prosa argumentativa, não paratexto. As análises de KWIC, frequência e cocorrência **operam sobre o texto integral** e portanto incluem o Postscript no cálculo das figurações; apenas a estratificação da amostra registra o conteúdo erroneamente. Para a Etapa 1, o efeito é nulo. Para análises futuras que dependam da estratificação, considerar regex específica para `^\s*POSTSCRIPT\s*$` antes de back matter.
- Science in Action pg294: continuação da bibliografia (entradas Dauben, Dubos...) sem cabeçalho `References` na própria página. Caso esperado e benigno.
- Pandora pg7: página de Acknowledgments com cabeçalho tipografado em letras espaçadas (`A C K N O W L E D G M E NT S`). A heurística de front matter não casa esse padrão. Análoga ao tratamento dado a `C H A P T E R` no Adendo 3; ajuste similar seria viável se o ganho justificasse.

### Outputs

- `outputs/etapa1/amostra_validacao_etapa1.csv` (consolidado, 41 linhas com campos preenchidos).
- `outputs/etapa<N>/<id_obra>/csv/amostra_validacao.csv` (por obra).
- `outputs/etapa<N>/<id_obra>/relatorios/validacao_amostral_etapa1.md` (relatório por obra).
- `outputs/etapa1/validacao_amostral_etapa1.md` (relatório consolidado).

---

## Etapa 3 — Lexicometria expandida (rodada parcial sobre o corpus de Etapa 1)

Data da execução: 14 de maio de 2026.

A Etapa 3 plena prevista no `plano_de_trabalho.md` (linhas 254-328) requer a inclusão de obras adicionais de Latour (*Pasteur 1984* em francês, *Reassembling 2005*, *On recalling ANT 1999*, *Clarifications 1996*), das obras centrais de Haraway (*Cyborg Manifesto*, *Situated Knowledges*, *Modest_Witness*, *Companion Species*, *When Species Meet*, *Staying with the Trouble*) e de Stengers e Ingold em escala reduzida. Como esses textos ainda não foram extraídos para `corpus/txt/`, a Etapa 3 é executada aqui em rodada parcial sobre as três obras de Latour da Etapa 1, com expansão do catálogo e dependências instaladas para suportar o corpus completo quando ele chegar.

### 1. Expansão do catálogo: campo `militar`

Decisão: o catálogo `campos_lexicais/catalogo_termos.yaml` recebe um novo grupo `militar` sob o autor Latour, com 64 variantes em inglês cobrindo o vocabulário militar-industrial que minha tese argumenta ser característico de Latour. Termos: `ally`/`allies`/`alliance`/`alliances`; `enemy`/`enemies`/`enmity`; `recruit` e flexões; `mobilise`/`mobilize` e flexões (variantes britânica e americana); `battle`/`battles`/`battlefield`/`embattled`; `war`/`wars`/`warfare`/`warlike`; `conquer` e flexões; `victory`/`victories`/`victorious`; `defeat` e flexões; `troops`; `attack` e flexões; `defend`/`defends`/`defended`/`defensive`/`defence`/`defenses`/`defenders`; `fortress`/`fortresses`/`fortified`/`fortify`/`citadel`/`citadels`; `weapon`/`weapons`/`weaponry`/`arsenal`/`arsenals`; `soldier`/`soldiers`; `siege`/`besieged`/`besieging`.

Exclusões definidas para descartar usos metafóricos triviais e termos médicos: `best ally`, `natural ally`, `first attack`, `asthma attack`, `heart attack`, `panic attack`, `battle of ideas`.

Justificativa: o campo militar é o eixo empírico da tensão figural que minha tese sustenta. Sem um grupo dedicado, esse vocabulário aparece dispersamente em outros grupos (`enrollment`, `mobilise`, `trial_of_strength` etc.) e a leitura quantitativa fica fragmentada. A consolidação em um único campo permite leitura de densidade total.

### 2. Resultado quantitativo

Contagem absoluta e frequência por 10.000 palavras, com janela KWIC de ±10:

| Obra | n | freq/10k |
|---|---:|---:|
| `latour_woolgar_1986_lab_life_en` | 39 | 3,69 |
| `latour_1987_science_action_en` | 374 | 26,74 |
| `latour_1999_pandora_en` | 212 | 16,56 |

O pico de 374 ocorrências em \emph{Science in Action} é a maior densidade do livro inteiro entre os dezessete campos figurativos do catálogo, ultrapassando `black_box` (9,58/10k), `network` (9,08/10k) e `translation` (5,58/10k). Variantes top em 1987: `allies` (92), `mobilisation` (28), `mobilised` (24), `alliances` (22), `ally` (21), `war` (16), `defence` (15). Em 1999, predominância de `war`/`wars` (85 conjuntas).

### 3. Decisão sobre lematização

A Etapa 3 prevê lematização com spaCy para neutralizar variações flexionais (`mobilise`/`mobilised`/`mobilising` viram um lema único). Instalei `spacy==3.8.14` e o modelo `en_core_web_sm` no ambiente, mas optei por **manter o casamento literal de variantes** nesta rodada parcial, por três razões:

1. Auditabilidade: a lista de variantes literais é inspecionável no YAML; lematização é caixa-preta.
2. Robustez: para inglês acadêmico, variantes flexionais regulares são poucas; listei explicitamente as principais para cada lema do campo militar.
3. Custo de oportunidade: a lematização só se torna necessária quando entram obras em francês ou português, onde a flexão é mais rica. Para essa rodada (3 obras em inglês), o casamento literal é suficiente.

A integração da lematização fica para a Etapa 3 plena, junto com a entrada de \emph{Pasteur 1984} em francês.

### 4. Scripts e outputs atualizados

Os scripts da Etapa 1 (02_kwic, 03_frequencies, 04_visualizations, 05_cooccurrence, 07_trajectory) foram re-executados sobre o catálogo expandido. Outputs por obra (`outputs/etapa<N>/<obra>/csv/`, `outputs/etapa<N>/<obra>/relatorios/`, `outputs/etapa<N>/<obra>/figuras/`) e o consolidado (`outputs/etapa1/trajetoria_latour_1986_1999.md` e `.csv`) refletem a inclusão do campo militar. A seção 4.3.a do relatório de trajetória traz a leitura interpretativa específica.

### 5. Pendências para a Etapa 3 plena

- Subir os `.txt` das obras adicionais do plano de trabalho.
- Implementar lematização efetiva no `02_kwic.py` (flag `--lematizar`) para suportar francês e português.
- Adicionar campos lexicais correspondentes para Haraway (têxtil-feminista: companheirismo, parentesco, fiação, tecitura, costura, tecelagem) e para Stengers/Ingold conforme o plano.
- Comparação cruzada autor por autor, com matriz idioma × autor × campo.

---

## Etapa 2 — Extensão da análise lexicométrica aos artigos teóricos de Latour

Data da decisão: 15 de maio de 2026.

A Etapa 2 (no sentido do `briefing_etapa2_artigos_latour.md`, v2) estende a instrumentação lexicométrica da Etapa 1 a dois artigos metateóricos de Latour, com o objetivo de submeter à mesma contagem sistemática a hipótese qualitativa de divisão de trabalho metafórico por gênero textual: vocabulário militar-industrial dominante nos livros monográficos (já documentado pela Etapa 1) e vocabulário têxtil-topológico ocupando o terreno nos artigos metateóricos.

### 1. Corpus

Adiciono ao `metadata.csv` (marcados com `escopo_etapa2 = sim`):

- `latour_1996_clarifications_en` — Bruno Latour, *On Actor-Network Theory: A Few Clarifications*, *Soziale Welt*, vol. 47, n. 4, pp. 369-381, 1996.
- `latour_1999_recalling_en` — Bruno Latour, *On Recalling ANT*, in Law e Hassard (orgs.), *Actor Network Theory and After*, Blackwell, Oxford, pp. 15-25, 1999.

O slug do segundo artigo foi unificado a partir do registro anterior `latour_1999_recalling_ant_en` para `latour_1999_recalling_en`, alinhando-se à convenção do briefing e dos caminhos de output (`outputs/etapa<N>/<slug>/...`).

### 2. Origem dos `.txt` e cadeia de mediação

Os dois arquivos vieram já normalizados, em sessão de chat anterior com o Claude, fora do pipeline canônico `scripts/01_extract_text.py` → `scripts/01b_normalize_text.py`. A normalização externa foi registrada nos próprios cabeçalhos `#` dos `.txt`, com referência a `scripts/12_etapa2_extrair_ocr_zips.py` (script de extração fora deste repositório). Os arquivos foram depositados em `corpus/txt_norm/` por upload direto à sessão remota, sem passar pelo Drive sincronizado, dado que a sessão remota não tem acesso ao Drive da pesquisadora.

A cadeia mim → chat → Claude Code → repositório é registrada como dado etnográfico, em coerência com o tratamento que a tese dá às demais cadeias de mediação técnica.

### 3. Restrição de cobertura do *Recalling*

O OCR de origem (zip de 11 páginas) entregou texto principal limpo apenas para as páginas pares do zip (2, 4, 6, 8, 10), que cobrem as páginas 16, 18, 20, 22 e 24 do volume. As páginas ímpares do zip estavam severamente truncadas no início das linhas e foram excluídas, conforme nota de estrutura no cabeçalho do `.txt`. As páginas 15 (abertura + abstract) e 25 (final + bibliografia) do volume não estão integralmente representadas.

Consequências:

- A contagem do *Recalling* opera sobre 1.344 palavras de corpo, equivalente a cerca de 80% do artigo original.
- A passagem-chave dos pp. 19-20 sobre a contaminação do vocabulário (`vocabulary has contaminated our ability to let the actors build their own space`) está integralmente preservada no corpus. Confirmação por sanity check em `scripts/13_audit_articles_etapa2.py`.
- A limitação enfraquece a quantificação absoluta do artigo mas não compromete o argumento comparativo, que opera por ordem de grandeza (3 a 7 vezes menor que *Science in Action*).
- Fica registrada como pendência para uma eventual Etapa 2-bis a reanálise com PDF nativo do *Recalling*, caso adquirido.

### 4. Saneamento de OCR adicional no momento da leitura

A auditoria dos dois `.txt` registrou caracteres de controle ASCII residuais (12 ocorrências de `\x02` no *Recalling*, 11 no *Clarifications*) que funcionam, na maior parte das ocorrências, como soft hyphens não resolvidos pelo OCR. Exemplos: `actor\x02network`, `abil\x02ity`, `micro\x02distinction`, `non\x02existing`.

Decisão: ao invés de reescrever os `.txt` (que ficariam menos auditáveis), `ler_texto_sem_cabecalho` em `scripts/02_kwic.py` substitui `\x02` (e demais caracteres de controle ASCII de baixa ordem `\x00`-`\x08`, `\x0b`-`\x1f`, `\x7f`) por espaço durante a leitura, preservando offsets. O tratamento é análogo ao Adendo 1 das decisões da Etapa 1 (soft hyphen U+00AD nos livros) e mantém os `.txt` como artefato auditável intacto. A regex do catálogo já tolera ausência de hífen (`[-\s]?` em `compilar_padrao`), de modo que `actor\x02network` casa o termo `actor-network` mesmo após a substituição por espaço.

Limitação registrada: no *Recalling*, 11 candidatos a colagem de OCR (tokens com mais de 18 letras consecutivas sem espaço, do tipo `havealternatedbetweentwo`, `stochasticcomposition`, `intersubjectiveencounter`) permanecem no corpus como sub-recobrimento esperado. O efeito sobre a contagem do campo militar é marginal (a estimativa preliminar do briefing já contempla `n = 1`); o efeito sobre os campos têxtil e topologia será aferido na contagem da Etapa 2.1.

### 5. Catálogos têxtil e topologia (sem alterar o YAML)

O catálogo `campos_lexicais/catalogo_termos.yaml` permanece intacto, em coerência com o princípio da Etapa 2 de usar instrumento idêntico à Etapa 1 para tornar o contraste defensável. Os campos têxtil e topologia, exigidos pela hipótese de divisão de trabalho metafórico, entram como arquivos de adição separados:

- `campos_lexicais/latour_textil_en_etapa2_adicoes.txt` (61 variantes literais: `thread`, `weave`, `knot`, `tangle`, `fiber`, `fibrous`, `filament`, `string`, `wire`, `rope`, `lace`, `plait`, `twist`, `net`, `fabric`, `texture`, `capillary` e flexões).
- `campos_lexicais/latour_topologia_en_etapa2_adicoes.txt` (43 variantes literais: `fluid`, `surface`, `node`, `connection`, `topology`, `flat`, `fold`, `locus`, `trajectory`, `flow`, `circulation`, `path`, `grid`, `mesh`, `boundary`, `inside`, `outside`, `proximity`, `scale`, `plane` e flexões; `network` permanece no grupo homônimo do YAML para não duplicar).

A consolidação dos termos têxteis e topológicos em grupos do `catalogo_termos.yaml` fica pendente até a aprovação dos resultados da Etapa 2.1. Enquanto isso, os arquivos `.txt` de adição são tratados como suplemento auditável.

### 6. Categorias novas de desambiguação do campo militar

A desambiguação automática + manual aplicada na Etapa 1 (gatilhos lexicais para *Science Wars*, *World War*, *Cold War*, *Franco-Prussian War*, *Ministry of War*, *phony war*, *War and Peace*, etc.) ganha três categorias novas específicas para os artigos metateóricos:

- `metalinguistico`: ocorrências em que Latour cita o próprio vocabulário da TAR (como em `vocabulary association, translation, alliance, obligatory passage point`). Gatilho automático implementado: ≥2 aspas curvas/retas na janela junto a ≥1 termo do vocabulário próprio da TAR (`association`, `translation`, `passage point`, `actor-network`, `enrollment`, `actant`, `network` e variantes), ou indicador citacional explícito (`vocabulary`, `term`, `notion`, `so-called`, `the way AT is`) com ≥2 termos da TAR.
- `descritivo_bibliografico`: ocorrências em referências bibliográficas e em títulos de obras citadas (`La nouvelle alliance` de Prigogine e Stengers). Gatilho automático implementado: ≥2 sinais entre ano em parênteses, editora conhecida (`Routledge`, `Blackwell`, `Harvard`, `Gallimard`, `Bantam` etc.) e nomes próprios sequenciais com `and`/`et`.
- `conceitual_debate`: ocorrências em que o termo militar descreve polêmica entre escolas teóricas (`pre-relativist enemies`, `Reflexivists`, etc.). Gatilho automático: ≥2 palavras terminadas em `-ist`, `-ists`, `-ism`, `-isms` na janela. Categoria registrada como distinta do uso figural da prática científica, em coerência com a leitura do briefing § 2.

A implementação está em `scripts/15_etapa2_desambiguar_militar.py`. A planilha de classificação `outputs/etapa2/consolidado/militar_classificacao_automatica.csv` segue o formato de `refinamento/war_pandora_classificacao.csv`.

**Achado da Etapa 2.2**: cobertura automática de 4/4 ocorrências militares dos artigos. Todas caem em categorias não-figurais. A contagem refinada figural do campo militar nos artigos cai para zero, sustentando empiricamente a hipótese de divisão de trabalho metafórico por gênero textual proposta pelo briefing.

**Ressalva sobre a citação prevista no briefing § 2 que não está no corpus**: a passagem metalinguística `vocabulary association, translation, alliance, obligatory passage point` (que motivou a categoria `metalinguistico`) não aparece nas pp. 16-24 do *Recalling* incluídas no corpus. A inferência mais provável é que esteja em uma das páginas excluídas (15 ou 25 do volume). A única ocorrência militar efetiva no corpus do *Recalling* é `wars` em `Science Wars` (`descritivo_historico`). O argumento comparativo permanece sustentado: o `wars` de `Science Wars` também é não-figural, e a refinada figural do *Recalling* permanece zero.

### 7. Janela de cocorrência

A janela de cocorrência de 200 palavras, calibrada para os livros, corresponde a cerca de 15% do *Recalling* (1.241 palavras na convenção `split`) e a 2,5% do *Clarifications* (7.848 palavras), o que distorce a comparabilidade. Decisão: na Etapa 2.4, gerar duas versões da matriz de cocorrência para os artigos, uma com janela 200 (controle direto para comparação com os livros) e outra com janela proporcional (2% do total, arredondada para 25 palavras no *Recalling* e 157 no *Clarifications*).

O briefing § 3.4 antecipava 27 e 159 com base na convenção `\b\w+\b`; os valores aplicados (25 e 157) refletem a convenção `split` registrada em `corpus/qualidade_extracao.csv`, que é a convenção da Etapa 1.

Implementação: `scripts/05_cooccurrence.py` ganhou o argumento `--sufixo`, que sufixa os nomes dos arquivos de saída (CSV, MD e figuras) para que as duas configurações coexistam sem sobrescrita. `scripts/16_etapa2_cocorrencia_comparacao.py` consolida as duas matrizes lado a lado em `outputs/etapa2/consolidado/cocorrencia_comparacao.md`.

**Achado da Etapa 2.4**: o ranking dos pares principais é consistente entre as duas janelas em ambos os artigos. Em *Clarifications*, `network`–`topologia` lidera com 783 (j=200) e 616 (j=157); o par envolvendo `militar` mais forte é `militar`–`network` com 10/8, cerca de 77 vezes menor. Em *Recalling*, `network`–`topologia` lidera com 20/2. A malha argumentativa central dos artigos é estruturada por `network`–`topologia`, `actor_network` e `textil`; o vocabulário militar ocupa posição periférica.

A decisão final sobre qual versão entra na tese cabe à pesquisadora após o Gate 2.4. A recomendação registrada em `outputs/etapa2/consolidado/cocorrencia_comparacao.md` é apresentar a janela proporcional como configuração principal, com a janela 200 em nota como controle.

### 8. Mudanças no código aplicadas para suportar a Etapa 2

- Coluna `escopo_etapa2` adicionada a `corpus/metadata.csv` (e à cópia em `metadata.csv` na raiz). Marcada `sim` para os dois artigos e `nao` para as demais 31 obras.
- Slug `latour_1999_recalling_ant_en` renomeado para `latour_1999_recalling_en` (referência cruzada com os caminhos `outputs/etapa<N>/<slug>/...` do briefing).
- `scripts/02_kwic.py`, `scripts/03_frequencies.py`, `scripts/04_visualizations.py` e `scripts/05_cooccurrence.py` ganharam o argumento `--escopo etapa1|etapa2|todos` (default: `etapa1` para preservar comportamento prévio).
- `scripts/02_kwic.py` ganhou `ler_texto_sem_cabecalho` que descarta linhas iniciadas por `#` e substitui caracteres de controle ASCII por espaço, preservando offsets para o casamento com a matriz de cocorrência.
- `scripts/13_audit_articles_etapa2.py` é o novo script de sanity check para os `.txt` da Etapa 2: reporta linhas de cabeçalho, palavras de corpo, candidatos de colagem de OCR, caracteres de controle residuais e presença de passagens-chave por slug.
- `corpus/qualidade_extracao.csv` recebeu duas linhas para os artigos, com `palavras_total` e `qualidade_global` (`boa_com_pequenos_artefatos_de_ocr` para o *Clarifications*; `parcial_com_colagem_de_ocr` para o *Recalling*).

### 9. Convenção de contagem de palavras

A Etapa 1 contabiliza `palavras_total` em `corpus/qualidade_extracao.csv` via `re.split(r"\s+", conteudo)` (`scripts/01_extract_text.py:255`), que divide o texto por whitespace e conta tokens. A inspeção exploratória registrada no `briefing_etapa2_artigos_latour.md` § 2 usou a convenção alternativa `\b\w+\b` (regex de borda de palavra), que conta também separadores internos como hifens e apóstrofos como fronteira, produzindo um número marginalmente maior.

Decisão: registro em `corpus/qualidade_extracao.csv` os valores em convenção `split` para garantir comparabilidade direta com os livros, da seguinte forma:

| Slug | Convenção `split` (registrado) | Convenção `\b\w+\b` (preliminar do briefing) | Diferença |
|---|---:|---:|---:|
| `latour_1996_clarifications_en` | 7.848 | 7.934 | +86 (1,1%) |
| `latour_1999_recalling_en` | 1.241 | 1.344 | +103 (8,3%) |

A diferença maior no *Recalling* é consequência do OCR colado discutido na seção 4 desta entrada: tokens como `havealternatedbetweentwo` contam como uma só palavra em ambas as convenções, mas o número total cai porque a tokenização absorve tudo em torno desses tokens. As densidades por 10.000 palavras na Etapa 2.1 e seguintes operam sobre os valores `split` (7.848 e 1.241). A leitura interpretativa pode mencionar os dois números quando convier para sustentar a ordem de grandeza do achado.

### 10. Outputs comparativos consolidados (Etapa 2.5)

Os outputs finais para incorporação ao capítulo 2 da tese estão em `outputs/etapa2/consolidado/`, gerados por `scripts/17_etapa2_tabelas_finais.py` ao final da Etapa 2.5. Três cortes tabulares respondem ao briefing § 4.2:

1. **Comparativa geral** das 5 obras × 19 grupos figurativos: `tabela_comparativa_5_obras.tex` (LaTeX), `tabela_comparativa_5_obras_n.csv` (contagem absoluta) e `tabela_comparativa_5_obras_freq.csv` (densidade por 10k). Gerada na Etapa 2.1, mantida sem alteração.
2. **Campo militar refinado** das 5 obras: duas versões LaTeX. `tabela_militar_refinada_5_obras.tex` (Etapa 2.2, enxuta com bruta vs. refinada figural) para o capítulo 2. `tabela_militar_refinado_5_obras_detalhada.tex` (Etapa 2.5, breakdown por categoria) para o apêndice metodológico. CSV equivalente em `tabela_militar_refinado_5_obras.csv`. As três categorias de desambiguação aplicadas apenas aos artigos (descritivo-bibliográfica, metalinguística, polêmica conceitual) ficam como `--` nos livros, em coerência com o escopo da Etapa 1.
3. **Têxtil e topologia** das 5 obras: `tabela_textil_topologico_5_obras.{csv,tex}`. A coluna `textil_variantes_top` do CSV registra as quatro variantes mais frequentes por obra, base para a depuração da Etapa 2.6 (polissemia esperada em `tie`, `net`, `string`).

A leitura sintética dos contrastes está em `outputs/etapa2/consolidado/relatorio_etapa2.md`. A redação da subseção do capítulo 2 que mobiliza esses resultados é responsabilidade da pesquisadora.

### 11. Protocolo A/B/C da validação amostral semântica (Etapa 2.6)

O briefing § 3.6 indica que a Etapa 2.6 aplica "a mesma validação amostral" em três camadas (A/B/C) usada na Etapa 1, mas a Etapa 1 do repositório não tinha implementação prévia desse protocolo (o `scripts/08_validate_sample.py` valida classificação de página, não classificação semântica de ocorrências figurativas). Defino aqui o protocolo aplicado à Etapa 2.6:

- **Camada A — top-densidade**: cinco ocorrências por campo cuja janela KWIC tem o maior número de termos do mesmo campo lexical na vizinhança imediata. Heurística: passagens onde o campo aparece de modo concentrado são candidatas a uso central e a citação na tese. Em *Clarifications*, a camada A do campo `textil` recuperou a sequência canônica `fibrous, thread-like, wiry, stringy, ropy, capillary` na primeira página.
- **Camada B — aleatória**: cinco ocorrências aleatórias por campo, com `seed=42`. Representa o "fundo" do campo, sem viés de densidade.
- **Camada C — variantes raras**: cinco ocorrências por campo cuja variante (`termo_encontrado`) é das menos frequentes no campo. Heurística: ocorrências em variantes raras são as mais suspeitas de polissemia ou uso periférico (`tie` como verbo em vez de laço, `net` como rede de computadores em vez de tessitura, etc.).

Quando o campo tem menos de 15 ocorrências, a amostra é exaustiva, com a camada rotulada como `exaustiva`. Caso do *Recalling* (22 ocorrências totais nos campos validados: 13 `topologia` + 7 `network` + 2 `actor_network` + 0 `textil`).

Campos validados: `textil`, `topologia`, `network`, `actor_network`. São os quatro campos centrais do argumento têxtil-topológico da Etapa 2. O campo `militar` está fora desta amostra porque já foi 100% desambiguado na Etapa 2.2 (cobertura 4/4).

Implementação em `scripts/18_etapa2_validacao_amostral.py`. Outputs:

- `outputs/etapa<N>/<artigo>/csv/validacao_amostral_semantica.csv` (60 linhas em *Clarifications*, 22 em *Recalling*).
- `outputs/etapa2/consolidado/validacao_amostral_semantica.csv` (consolidado, 82 linhas).
- `outputs/etapa2/consolidado/validacao_amostral_instrucoes.md` (instruções de preenchimento para a pesquisadora).

A planilha tem colunas pré-preenchidas (`obra`, `campo`, `camada`, `id_kwic`, `pagina`, `termo_encontrado`, `contexto_antes`, `trecho_central`, `contexto_depois`) e colunas em branco para preenchimento manual: `uso_figural` (`sim`/`parcial`/`nao`), `subcategoria` (texto livre, sugestões: `tecnico`, `polissemia`, `descritivo`, `metalinguistico`), `comentario` (texto livre, registro etnográfico).

Após o preenchimento, gero `outputs/etapa2/consolidado/validacao_amostral_resultados.md` com taxa de uso figural por campo e por camada, mapa de polissemia, e densidade refinada figural para `textil` e `topologia` (bruta × taxa de figuralidade aferida).

Pendência: a Etapa 1 prevê a mesma validação A/B/C para os livros (passo 2 do refinamento mencionado no `CLAUDE.md`). Quando essa validação for executada, a Etapa 2 pode rodar comparação cruzada de figuralidade entre livros e artigos no mesmo protocolo. Esta etapa fica fora do escopo da 2.6.

### 12. Rendimento da validação amostral A/B/C

Recebi a planilha preenchida pela pesquisadora com as 82 classificações em 15 de maio de 2026. Apliquei correções de pipeline e gerei os outputs analíticos finais nesta sessão.

Distribuição final das classificações: 62 `sim` (75,6%), 9 `parcial` (11,0%), 11 `nao` (13,4%). Taxa de figuralidade ponderada `(sim + 0,5·parcial) / total` igual a 0,815 sobre o conjunto.

Por obra:

| Obra | n | tx. figural |
|---|---:|---:|
| *Clarifications* 1996 | 60 | 0,875 |
| *Recalling ANT* 1999 | 22 | 0,636 |

Por campo:

| Campo | n | tx. figural |
|---|---:|---:|
| textil | 15 | 0,967 |
| topologia | 28 | 0,964 |
| actor_network | 17 | 0,794 |
| network | 22 | 0,523 |

O contraste entre obras (0,875 vs. 0,636) e a taxa baixa do campo `network` (0,523) decorrem ambos do registro autocrítico-metalinguístico do *Recalling*. Dos 11 `nao` no corpus validado, 9 são da subcategoria `metalinguistico`, e 8 desses 9 estão no *Recalling*. As passagens em causa são as do gesto autocrítico em que Latour cita seu próprio vocabulário para suspendê-lo (`let us abandon the words actor and network`, `the very expression of actor-network invites this reaction`, `the third nail in the coffin`).

Esse achado adiciona uma divisão de segundo nível à hipótese de divisão de trabalho metafórico por gênero textual: dentro do gênero metateórico, *Clarifications* opera em regime expositivo-figural e *Recalling* em regime autocrítico-metalinguístico. Esse resultado entra na seção do capítulo 2 que mobiliza a tabela `tab:textil-topologico-refinado`.

**Bugs do pipeline da 2.6 corrigidos nesta sessão:**

1. **`id_kwic` reiniciado por camada**: a coluna estava reiniciada por camada A/B/C, produzindo identificadores duplicados (e.g. `actor_network#0000` aparecia três vezes, uma por camada). Reescrevi cada `id_kwic` como `<obra>#<campo>#pos_NNNNNN`, com NNNNNN sendo o offset em caracteres no `.txt` normalizado, casado por chave composta (`grupo + termo_encontrado + contexto_antes + contexto_depois`) com o `kwic.csv` original. Casamento confirmado 82/82.

2. **`pagina` fixa em "1"**: a coluna estava fixa em "1" para todas as linhas. Sem marcadores `<<PG_VOL=N>>` no corpo dos `.txt`, mapeei a posição absoluta de cada ocorrência ao parágrafo correspondente no texto normalizado e atribuí a página citável de tese: pp. 369-381 do *Soziale Welt* 47(4) para *Clarifications* (13 blocos = 13 páginas); pp. 16, 18, 20, 22, 24 do volume *Law & Hassard* para *Recalling* (5 blocos correspondentes às páginas pares do zip de OCR).

A planilha original `validacao_amostral_semantica_PREENCHIDA.csv` fica intocada como artefato auditável. A versão com bugs corrigidos é `validacao_amostral_semantica_PREENCHIDA_CORRIGIDA.csv`, lado a lado.

**Validação exaustiva do `textil` em *Clarifications***: o campo tem 39 ocorrências brutas no `kwic.csv` do artigo. A amostra A/B/C de 15 cobre 15 dessas 39 (38,5% de cobertura por ocorrência). Em diversidade de variantes a cobertura é maior: todas as variantes-chave (`fibrous`, `thread`, `thread-like`, `wiry`, `stringy`, `ropy`, `capillary`, `netting`, `lacing`, `weaving`, `twisting`, `fabric`, `fabrics`, `woven`, `threads`, `nets`) entraram na amostra; a variante `fiber` ficou fora. A taxa 0,967 é tratada como representativa do campo para fins da contagem refinada.

**Rendimento desigual da camada C (variantes raras)**: a camada C é informativa em campos com diversidade lexical interna (`topologia`, `textil`, e `actor_network` em escala menor) e perde discriminação em campos dominados por uma única variante. Caso de `network`, em que `networks` concentra a maior parte das ocorrências e a única variante rara (`networking`) tem uma única ocorrência. A camada C de `network`/Clarifications fica com taxa 0,600, próxima da camada B (0,800), perdendo o papel diagnóstico que tem nos outros campos. Para rodadas futuras, considerar critério de inclusão na camada C apenas quando o campo tem três ou mais variantes com pelo menos duas ocorrências cada.

**Subcategoria nova cunhada pela pesquisadora durante o preenchimento**: `definicao_operacional`, atribuída à passagem `AT makes use of some of the simplest properties of nets` (linha 9 da planilha), em que `nets` opera em registro transitório entre figural e técnico-matemático. Mantenho o rótulo como subcategoria sexta válida, em coerência com o princípio etnográfico do método.

**Aplicação retroativa aos livros**: gerei `outputs/etapa2/consolidado/metalinguistico_retroativo_livros.csv` com seis candidatos a uso `metalinguistico` nos campos `network` e `actor_network` dos três livros monográficos, identificados por gatilho automático (`the word`, `the notion`, `the term`, `the expression of`, `let us abandon`, `coffin`, `so-called`, `misunderstanding`). Distribuição: 4 candidatos `network` e 1 `actor_network` em *Science in Action*, 1 `actor_network` em *Pandora's Hope*, zero em *Laboratory Life*. A leitura manual dessas seis ocorrências fica como pendência para a Etapa 2-bis. Enquanto não houver classificação manual, a taxa de figuralidade para *Science in Action* na tabela `tab:textil-topologico-refinado` fica marcada como `pendente`.

### 13. Estado da Etapa 2 ao final da Etapa 2.6

Seis subetapas concluídas em sequência, com gates de revisão confirmados pela pesquisadora entre cada uma:

- **2.0** integração dos `.txt` normalizados ao corpus, escopo_etapa2 no `metadata.csv`, infraestrutura de scripts.
- **2.1** contagem bruta nas 5 obras com `02_kwic.py` e `03_frequencies.py`, tabela comparativa em `outputs/etapa2/consolidado/tabela_comparativa_5_obras.{csv,tex}`.
- **2.2** desambiguação automática do campo militar nos artigos (cobertura 4/4), com cinco categorias e gatilhos em `scripts/15_etapa2_desambiguar_militar.py`. Tabela militar refinada em `tabela_militar_refinada_5_obras.tex`.
- **2.3** não executada por desnecessidade: a cobertura automática 4/4 dispensou desambiguação manual de adição (a pesquisadora pode ainda ajustar `categoria_final` na planilha se discordar).
- **2.4** cocorrência com duas janelas (200 controle + proporcional 2%) para os artigos, com `--sufixo` em `05_cooccurrence.py`. Consolidado em `cocorrencia_comparacao.md`.
- **2.5** três tabelas finais consolidadas (comparativa geral, militar refinado, têxtil-topológico) e relatório `relatorio_etapa2.md` com leitura sintética dos contrastes.
- **2.6** planilhas A/B/C geradas, preenchidas pela pesquisadora e processadas. Outputs analíticos finais em `outputs/etapa2/consolidado/validacao_amostral_resultados.md`, `tabela_textil_topologico_refinada.tex`, `validacao_amostral_semantica_PREENCHIDA_CORRIGIDA.csv` (bugs do pipeline corrigidos: `id_kwic` único por offset, `pagina` recalculada por mapeamento de parágrafo), `metalinguistico_retroativo_livros.csv` (candidatos para Etapa 2-bis) e `log_execucao.md`.

**Pendências abertas** (Etapa 2-bis):

- Leitura manual dos seis candidatos `metalinguistico` retroativos nos livros (4 `network` em *Science in Action*, 1 `actor_network` em *Science in Action*, 1 `actor_network` em *Pandora's Hope*). Sem essa leitura, a taxa de figuralidade para *Science in Action* na tabela `tab:textil-topologico-refinado` fica como `pendente`.
- Validação A/B/C retroativa do protocolo aplicada aos três livros monográficos, para fechar a comparação cruzada de figuralidade entre artigos e livros sob a mesma instrumentação.
- PDF nativo do *Recalling*, caso acessível, para reanálise integral (cobertura atual: 80%).

---

## Etapa 2-bis — Reanálise do *Recalling ANT* a partir de TXT integral

Data da execução: 15 de maio de 2026, sequencial ao Gate 2.6 confirmado pela pesquisadora.

### 1. Motivação

A Etapa 2 original processou o *Recalling ANT* (Latour, 1999, *Sociological Review*, pp. 15-25) a partir de um zip de OCR página-a-página em que metade das páginas tinha OCR severamente truncado. O corpus normalizado da Etapa 2 cobria 1.241 palavras correspondendo a 5 das 11 páginas do volume (pp. 16, 18, 20, 22, 24). O relatório da Etapa 2 declarava cobertura de ~80% por subestimação do tamanho total do artigo (era estimado em ~1.500 palavras totais).

A pesquisadora forneceu nesta sessão um `.txt` nativo integral do artigo, com 4.825 palavras após normalização. A cobertura real do corpus antigo era 25,3%, não ~80%. A Etapa 2-bis refaz as Etapas 2.1, 2.2, 2.4 e 2.6 sobre o corpus integral, mantendo os outputs da Etapa 2 original intocados para auditoria.

### 2. Decisões metodológicas

**Origem do arquivo**: a pesquisadora obteve o `.txt` integral por canais de acesso institucional e revisou-o manualmente antes do depósito em `corpus/txt_fornecido/latour_1999_recalling_nativo.txt`. A cadeia é registrada como dado etnográfico análogo ao tratamento dado aos demais `.txt` normalizados externamente na Etapa 2.

**Bypass dos pipelines de extração e normalização**: como o `.txt` chega já em formato comparável ao output dos pipelines `01_extract_text.py` + `01b_normalize_text.py`, esses scripts não são executados sobre o material novo. Aplico apenas as operações de saneamento simétricas às registradas no Adendo 1 da Etapa 1 e na seção 4 da Etapa 2 (CRLF, soft hyphens, caracteres de controle, hifenização EOL). Detalhamento em `outputs/etapa2bis/recalling_extras/normalizacao_aplicada.md`.

**Paginação**: o `.txt` fornecido tem números de página espalhados no texto (artefato do scan original) correspondentes às pp. 16-25 do volume *Law & Hassard 1999*. Uso essa paginação editorial publicada para todas as citações na Etapa 2-bis, conforme o briefing § "O que não fazer". A página de cada ocorrência é registrada no campo `pagina` do `kwic.csv` da obra `latour_1999_recalling_bis` via heurística de proporção (`scripts/02_kwic.py` herda do Etapa 1).

**Novo slug e coluna `escopo_etapa2bis`**: para preservar os outputs da Etapa 2 original intocados, criei o slug `latour_1999_recalling_bis` no `metadata.csv` (com `escopo_etapa2bis=sim`) e adicionei a coluna `escopo_etapa2bis` ao schema. Os scripts `02_kwic.py`, `03_frequencies.py`, `04_visualizations.py` e `05_cooccurrence.py` aceitam `--escopo etapa2bis`.

**Janela de cocorrência proporcional**: 2% de 4.825 = 96,5 → 97 palavras. O briefing 2-bis antecipava ~30, baseado na premissa errada de 1.500 palavras totais. A janela 200 (controle) e a janela 97 (proporcional) coexistem em `outputs/etapa2bis/latour_1999_recalling_bis/csv/cocorrencia_j{200,prop}.csv`.

**Migração da validação amostral A/B/C**: 31 das 40 ocorrências do bis casam com ocorrências da planilha preenchida da Etapa 2.6 (por chave composta `campo + termo + trecho central`); essas classificações migram automaticamente. 9 ocorrências novas (oriundas das páginas antes excluídas) ficam em branco para preenchimento manual em sessão futura. Detalhamento em `outputs/etapa2bis/consolidado/validacao_amostral_migracao.md`.

### 3. Achados principais

A nova ocorrência **`alliance` em `vocabulary—association, translation, alliance, obligatory passage point`** é classificada automaticamente como `metalinguistico` (gatilho: `indicador_meta=1, tar=4`), confirmando a expectativa do briefing 2-bis e fechando a lacuna apontada como ressalva metodológica na Etapa 2.

A contagem refinada figural do `militar` no *Recalling* **permanece zero**, agora sustentada por duas ocorrências (uma `descritivo_historico` para `wars`, uma `metalinguistico` para `alliance`) em vez de uma só. O argumento da Etapa 2 sobre o recuo do vocabulário militar nos artigos é confirmado e reforçado.

A 2-bis revela um terceiro nível na divisão de trabalho metafórico: dentro do *Recalling*, há um regime fluido-circulatório (par `circulating_reference`–`topologia` com 9 cocorrências na j=97, ausente do corpus antigo) que se distingue do regime expositivo-figural do *Clarifications* e do regime descritivo-militar dos livros monográficos.

Detalhamento completo no `outputs/etapa2bis/consolidado/relatorio_etapa2bis.md`.

### 4. Pendências

- 9 linhas em branco na `validacao_amostral_semantica.csv` da 2-bis, aguardando preenchimento manual.
- Atualização da subseção do capítulo 2 da tese que referencia o *Recalling*: substituir colunas das tabelas pela versão `_bis`, reescrever a nota de rodapé sobre cobertura parcial (era ~80%, real era 25,3%, agora 100%), acrescentar nota argumentativa sobre a passagem `alliance` metalinguística.
- Pendências independentes da Etapa 2.6 (validação retroativa A/B/C nos três livros, leitura manual dos seis candidatos metalinguísticos retroativos) permanecem abertas.

---

## Etapa 3 — Análise lexicométrica de *An Inquiry into Modes of Existence* (Latour, 2013)

Data da execução: 15 de maio de 2026, posterior ao push da Etapa 2-bis.

### 1. Motivação e escopo

Estendo a análise para AIME (Latour 2013, Harvard University Press, tradução de Catherine Porter), o livro em que Latour declara estar completando a TAR. A motivação é etnográfica: a Etapa 2-bis documentou no *Recalling ANT* o gesto autocrítico que reduziu a refinada figural militar a zero; AIME é o livro que sai do "caixão" do *Recalling* e mobiliza um vocabulário figural novo. Estender até 2013 é gesto de justiça intelectual com Latour e gesto de integridade reflexiva da tese.

O escopo da Etapa 3 é parcial em relação à Etapa 2: aplico contagem bruta (análoga à 2.1), desambiguação automática do campo militar (análoga à 2.2) e cocorrência (análoga à 2.4). A validação amostral semântica A/B/C (análoga à 2.6) fica como pendência declarada. Detalhamento no `outputs/etapa3/consolidado/relatorio_etapa3.md`.

### 2. Decisões metodológicas

**Origem do arquivo**: a pesquisadora forneceu `.txt` extraído de PDF nativo via canais institucionais. Depositado em `corpus/txt_fornecido/latour_2013_aime_en.txt`. Normalizado em simetria com a Etapa 2-bis: 21.104 CRLF → LF, 0 soft hyphens, 519 caracteres de controle ASCII substituídos por espaço, 852 EOL hyphens reconstituídos, 402 replacement chars U+FFFD substituídos por espaço. Resultado final em `corpus/txt_norm/latour_2013_aime_en.txt`, com 194.454 palavras de corpo (`split`). Hashes em `outputs/etapa3/consolidado/txt_hashes.txt`.

**Dois catálogos em paralelo**:

- Catálogo antigo (19 campos das Etapas 1 e 2) aplicado para permitir leitura comparativa direta com as cinco obras anteriores.
- Catálogo novo (`campos_lexicais/catalogo_termos_aime.yaml`, 12 campos específicos de AIME) aplicado apenas em AIME. Decisão metodológica: os campos novos foram identificados a partir da leitura qualitativa do livro e da literatura sobre a guinada latouriana pós-2007; sua aplicação retroativa nas obras de 1986-1999 teria rendimento esperado muito baixo, em ordem de grandeza inferior ao ruído. Os doze campos novos são: `modos_existencia`, `preposicao`, `felicidade`, `diplomacia`, `gaia`, `valores`, `trajetoria_passe`, `instituicao`, `categorias_dominio`, `modernos`, `alteracao`, `experiencia`.

**Exclusões no catálogo novo**: retirei `value`/`values` isolados do campo `valores` (alta polissemia), `pass`/`passing`/`passes` isolados de `trajetoria_passe`, `mode`/`modes` isolados de `modos_existencia`, `modern` adjetivo isolado de `modernos`, `Earth` de `gaia`. As polissemias remanescentes (`experience`, `crossing`, `domain`) ficam como ruído documentado nas limitações da Etapa 3.

**Ajuste da janela proporcional de cocorrência**: AIME tem 194.454 palavras; 2% disso (3.880 palavras) é janela alta demais para significância analítica em cocorrência KWIC. Ajusto para 0,02% = 39 palavras, mantendo ordem de grandeza comparável à janela proporcional da Etapa 2 (157 palavras em *Clarifications*, 97 em *Recalling* bis). A janela 200 permanece como controle.

**Sem validação semântica A/B/C**: decisão registrada acima. Implica que a contagem bruta dos 31 campos em AIME carrega ruído de polissemia que a validação permitiria estimar. A tabela militar refinada (123 figurais de 129 brutas após desambiguação automática) tem leitura mais robusta porque a desambiguação automática cobre os principais não-figurais.

**Slug e escopo**: criei o slug `latour_2013_aime_en` no `metadata.csv`. Os scripts da Etapa 3 (`scripts/22_etapa3_aime_pipeline.py`) operam com caminho direto, sem usar `--escopo etapa3`; pelo volume isolado da extensão, não adicionei coluna `escopo_etapa3` ao schema. Decisão revisável se a Etapa 3 ganhar outras obras no futuro.

### 3. Achados centrais

A contagem refinada figural do `militar` em AIME (6,33/10k, 123 ocorrências) coloca o livro em patamar **intermediário** entre os artigos metateóricos (0,00) e os livros monográficos solo (12,19 em Pandora; 26,03 em Sci. Action). A inspeção amostral confirma uso predominantemente figural, **em registro deslocado** para o horizonte cosmopolítico-diplomático: as ocorrências articulam-se com `modernos` (144 cocorrências em j=200), `instituicao` (78), `topologia` (78), `diplomacia` (55) e `gaia` (45). A "diplomacia" como categoria operatória do livro convive em vizinhança com o vocabulário militar; não o elimina, o ressignifica.

A malha topológica que os artigos metateóricos de 1996/1999 inauguraram permanece em AIME: `topologia` 26,43/10k, `network` 13,11/10k, `textil` 10,34/10k, em densidades comparáveis às dos livros monográficos solo. As variantes top do `topologia` reorganizam-se em torno de `path` (90) e `trajectory` (61), articulando com o campo novo `trajetoria_passe` (433 ocorrências, par dominante `topologia`–`trajetoria_passe` com 584 cocorrências em j=200).

AIME redistribui o trabalho figurativo em três camadas (vocabulário antigo persistente, vocabulário novo específico, articulação entre as duas via cocorrência), conforme detalhado em § 7 do `relatorio_etapa3.md`.

### 4. Pendências

- Validação amostral semântica A/B/C dos 31 campos em AIME (Etapa 3.6 hipotética). Sem ela, as densidades brutas dos campos polissêmicos (`experiencia`, `categorias_dominio`, `crossing`, `domain`) carregam ruído não estimado.
- Validação retroativa das categorias `metalinguistico`, `descritivo_bibliografico` e `conceitual_debate` para os livros (pendência aberta desde a Etapa 2.6, inclui os seis candidatos retroativos de `outputs/etapa2/consolidado/metalinguistico_retroativo_livros.csv`).

## Etapa 1 — Camada R: classificação Reinert e AFC sobre as três obras (22/05/2026)

### 1. Motivação

Incorporo ao pipeline uma camada de lexicometria estilo IRaMuTeQ (classificação descendente hierárquica de Reinert e análise fatorial de correspondências) para visualizar a trajetória 1986-1999 no plano fatorial. A interpretação do capítulo 2 sobre o deslocamento do vocabulário entre as três obras ganha um output cartográfico que complementa as densidades por campo já calculadas em Python.

### 2. Decisões metodológicas

**Linguagem e ambiente**: implementação em R, via RStudio sobre o R instalado dentro do Anaconda (env `latour-r`). O IRaMuTeQ é uma GUI Python que chama R por baixo; trabalhar diretamente em R encurta a pilha e mantém o output versionado no repositório. Script em `scripts/R/10_reinert_afc.R`, instruções em `scripts/R/README.md`.

**Pacotes**: `rainette` (implementação moderna do Reinert no R, ativo no CRAN, autoria de Julien Barnier), `quanteda` para tokenização e DFM, `udpipe` para lematização, `FactoMineR` e `factoextra` para a AFC.

**Lematização**: feita em R via `udpipe` com modelo `english-ewt`, sobre os `corpus/txt_norm/*.txt` em escopo da Etapa 1. Os lematizados ficam cacheados em `corpus/txt_lemma_en/` para reaproveitamento. Decisão deliberada: o IRaMuTeQ lematiza por padrão, e trabalhar com lemas (e não formas) produz AFC mais legível, com `cereal` no lugar de `cereal/cereals`.

**Segmentação**: STs de cerca de 40 ocorrências via `rainette::split_segments`, replicando o default IRaMuTeQ para corpora dessa ordem. Estimativa de cerca de 9 mil STs distribuídos entre as três obras.

**Parâmetros Reinert**: k = 6 classes, `min_segment_size = 10`, stopwords inglesas do `quanteda` removidas, lemas com menos de 3 caracteres descartados, termos presentes em menos de 3 STs descartados (`min_docfreq = 3`) para estabilizar a partição.

**AFC**: dupla, uma sobre o cruzamento lema x classe Reinert (equivalente ao plano fatorial padrão do IRaMuTeQ) e outra sobre lema x obra (que conversa diretamente com o argumento da trajetória 1986-1999 no capítulo 2). Limite de 250 lemas mais frequentes para o gráfico legível; coordenadas completas exportadas em CSV.

**Seed**: 42, conforme convenção do projeto.

### 3. Pendências

- Rodar o script na máquina da Juliane e validar amostralmente os perfis de classe Reinert antes de incorporar gráficos à tese.
- Decidir se as figuras `afc_obras.png` e/ou `afc_classes_reinert.png` entram no capítulo 2 e em qual seção.
- Replicar a camada R para o corpus Haraway quando a Etapa 5 do refinamento atual avançar.

## Ramo paralelo experimental — Rede de coocorrência para Gephi (22/05/2026)

### 1. Status

Ramo paralelo, **experimental**, mantido fora do pipeline principal. Não alimenta diretamente o capítulo 2 nesta versão. Decisão tomada após a primeira execução bem sucedida da camada R: Juliane pediu material pronto para importar no Gephi caso queira explorar a visualização em rede mais à frente.

### 2. Decisões metodológicas

**Granularidade dos nós**: lema, não termo do catálogo figurativo. A escolha mantém o mesmo nível de análise da camada R (Reinert + AFC operam sobre lemas) e permite comparar diretamente a partição modular detectada pelo Gephi com a partição Reinert.

**Tipo de aresta**: coocorrência não dirigida dentro do mesmo ST de 40 lemas, com peso igual ao número de STs em que o par coocorre. STs são gerados pela mesma lógica do `scripts/R/10_reinert_afc.R`, então os dois métodos partem da mesma segmentação.

**Filtros padrão**: top 250 lemas por frequência total (igual ao limite usado nas AFCs do R) e peso mínimo de 3 coocorrências por aresta. Stopwords inglesas removidas, lemas com menos de 3 caracteres descartados. A rede resultante tem 250 nós e cerca de 27 mil arestas, manejável no Gephi sem prejuízo de leitura.

**Atributos dos nós**: além de `Frequency`, cada nó carrega `Obra_dominante` (obra em que o lema tem maior frequência absoluta) e `Classe_reinert` (classe à qual o lema mais se associa por chi², lida dos `perfis_classe_XX.csv`). Isso permite, no Gephi, colorir por obra ou por classe Reinert e comparar com a modularidade detectada in situ.

**Script e saídas**: `scripts/11_export_gephi.py`, saídas em `outputs/etapa1/gephi/{nodes.csv, edges.csv, README.md}`. README inclui instruções de importação e sugestões de layout/análise para Gephi 0.10+.

### 3. Justificativa de manter como ramo paralelo

A análise principal da Etapa 1 segue a tradição IRaMuTeQ (Reinert + AFC), que produz partição estatística com base estatística do chi². A análise em rede via Gephi opera sobre lógica diferente (modularidade, layouts força-dirigidos) e não é diretamente comparável. Trato a saída Gephi como complemento exploratório, não como evidência alternativa. Se for incorporada à tese, entra como ilustração visual da topologia do corpus, com a partição Reinert seguindo como base estatística da interpretação.

### 4. Pendências

- Rodar a importação no Gephi e produzir um PNG/SVG do layout. Decidir se entra no capítulo 2.
- Eventual comparação quantitativa entre comunidades de modularidade (Gephi) e classes Reinert (R), via tabela de contingência.
- Replicar para o corpus Haraway na Etapa 5 do refinamento atual, caso a rede seja incorporada à tese.

## Refinamento simétrico de war/wars em SIA (23/05/2026)

### 1. Status

Pendência resolvida. A versão simétrica da figura `densidade_militar_sia_pandora.png` foi gerada e fica em `outputs/etapa1/passo4/figuras/densidade_militar_sia_pandora_simetrica.png` (com espelho no `consolidado/figuras/`). A figura assimétrica original fica preservada para histórico.

### 2. Contexto

A figura `densidade_militar_sia_pandora.png`, gerada por `scripts/arquivo/11_passo4_graficos.py`, traçava a densidade do campo `militar` ao longo de \emph{Science in Action} (1987) e \emph{Pandora's Hope} (1999) por janela deslizante de 1.000 palavras. O tratamento de `war`/`wars` era assimétrico: em SIA usava todos os hits brutos (n=374); em Pandora removia os descritivos pelo cruzamento com `refinamento/war_pandora_classificacao.csv` (n=156 refinado). A assimetria existia porque SIA não tinha CSV equivalente de classificação manual.

A auditoria de figuras de 2026-05-23 (inventariada em `outputs/inventario_figuras.md`) tornou a assimetria explícita; decidi resolver gerando a classificação simétrica.

### 3. Classificação aplicada a SIA

Identifiquei as 18 ocorrências válidas de `war`/`wars` no campo `militar` em `outputs/etapa1/latour_1987_science_action_en/csv/kwic.csv` e classifiquei cada uma por leitura de janela, com a mesma rubrica aplicada em Pandora:

- **Descritivos** (11 ocorrências): a colocação `Second World Wars` (gatilho automático \enquote{World}); oito ocorrências no capítulo sobre Szilard, Pentagon e a bomba atômica (narrativa contínua da Segunda Guerra Mundial); `Franco-Prussian war` (gatilho automático \enquote{Franco-Prussian}); a referência bibliográfica final a Tolstoi, \emph{War and Peace}.
- **Figurativos** (7 ocorrências): tropos conceituais como `war machine`, `link between war and technoscience`, analogias como `war cries help karate fighters`, e exemplos filosóficos-categoriais sobre a noção de `situation of war` como exceção ao homicídio.

A classificação fica em `outputs/etapa1/refinamento/war_sia_classificacao.csv`, com schema idêntico ao do CSV de Pandora (colunas `pagina, termo, categoria_auto, gatilho_detectado, contexto_antes, trecho_central, contexto_depois, categoria_final, justificativa`). Cada linha carrega a justificativa, permitindo auditoria posterior.

Aplicação ao campo `militar`:

| Obra | Bruto | Descritivos | Refinado | Δ |
|---|---:|---:|---:|---:|
| Science in Action 1987 | 374 | 11 | 363 | -2,9\% |
| Pandora's Hope 1999 | 212 | 56 | 156 | -26,4\% |

O valor refinado de SIA cai 1 unidade em relação ao valor declarado em `MILITAR_REFINADO` no script `11_passo4_graficos.py` (364 vs 363 obtidos agora pela classificação por ocorrência). A diferença está dentro da margem de classificação manual e não impacta os outros gráficos do passo 4, que continuam usando os valores antigos hardcoded. Para evitar drift cross-figura, deixo o `MILITAR_REFINADO` antigo intocado; a nova classificação por ocorrência alimenta apenas a figura simétrica.

### 4. Script gerador

`scripts/arquivo/11b_passo4_densidade_simetrica.py`. O script:

1. Reabre o `kwic.csv` de SIA, filtra hits de `war`/`wars` no campo `militar`, aplica a classificação dicionarizada (`CLASSIFICACAO_SIA`) e escreve `war_sia_classificacao.csv`.
2. Reabre os hits do campo `militar` em SIA e PAN, filtra os descritivos pelo cruzamento com os dois CSVs de classificação (assinatura por contexto, sem `pagina`, porque o `kwic.csv` atual grava tudo com `pagina=1`).
3. Traça a figura no mesmo estilo (curva de linha em vermelho ferrugem `#B22222` com área preenchida, janela deslizante de 1.000 palavras, eixo X em milhares de palavras, painel vertical), com rótulo de painel exibindo o n refinado de cada obra e anotação no canto inferior da figura indicando que é a versão simétrica.

### 5. Decisão pendente

Qual versão usar no capítulo 2 da tese: a assimétrica (`densidade_militar_sia_pandora.png`, mantém o tratamento original mas exige nota de rodapé argumentativa explicando a divergência) ou a simétrica (`densidade_militar_sia_pandora_simetrica.png`, refinada em ambos os painéis). Recomendação técnica: simétrica, porque a desambiguação foi feita justamente para isolar o uso figural; manter assimetria reintroduz ruído descritivo-histórico em SIA. A decisão final cabe à Juliane.

### 6. Pendências derivadas

- Se a figura simétrica for adotada, considerar atualizar também `MILITAR_REFINADO` em `11_passo4_graficos.py` para o n=363 obtido aqui (afeta `comparacao_frequencias_tres_obras.png` e `frequencia_grupos_sia_refinada.png`, com mudança visualmente imperceptível).
- A versão assimétrica passa a estar oficialmente desatualizada; pode ser removida se a simétrica for adotada na tese.
