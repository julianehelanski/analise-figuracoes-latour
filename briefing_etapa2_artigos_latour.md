# Briefing — Etapa 2: análise exploratória das figurações nos artigos teóricos de Latour

**Para:** Claude Code, sessão `analise_figuracoes` da Juliane
**De:** Juliane Helanski (doutoranda, IFCH/Unicamp)
**Data:** maio de 2026
**Versão:** v2 (atualiza v1 com .txt já normalizados e ajustes de OCR)
**Status:** briefing exploratório, a ser executado depois da conclusão dos passos 2 a 5 do refinamento da Etapa 1 já em andamento

---

## 1. Contexto e objetivo

A Etapa 1 do projeto produziu a análise lexicométrica de três livros monográficos de Latour (*Laboratory Life* 1986, *Science in Action* 1987, *Pandora's Hope* 1999) sobre 373.611 palavras, com catálogo de dezessete campos figurais, contagem refinada do campo `militar`, mapas de densidade e redes de cocorrência. Esses resultados sustentam, no capítulo 2 da minha tese, a subseção `subsec:figuracao_militar_evidencia`, em que mostro que a figuração militar-industrial é a marca lexical dominante da escrita latouriana nos livros monográficos, e que essa dominância se cristaliza em 1987 e se mantém em 1999.

A leitura qualitativa dos dois artigos teóricos centrais que Latour escreve nesse mesmo período, *On actor-network theory: a few clarifications* (1996, *Soziale Welt*) e *On recalling ANT* (1999, in Law & Hassard, *Actor Network Theory and After*, Blackwell, pp. 15-25), sugere uma divisão de trabalho metafórico entre dois gêneros textuais distintos da produção latouriana: nos livros monográficos, o vocabulário militar-industrial domina; nos artigos metateóricos para pares STS, o vocabulário recua sensivelmente e o léxico que ocupa o seu lugar é o **têxtil-topológico** (network, filament, fluid, weaving, thread, fibrous, knot, ropy, stringy, wiry).

O objetivo desta Etapa 2 é submeter essa hipótese qualitativa à mesma contagem sistemática que produzi para os livros, de modo que:

1. A subseção `subsec:figuracao_militar_evidencia` do capítulo 2 da tese ganhe um corpo de evidência adicional que preempta a objeção previsível da banca ("e os artigos? a teoria ator-rede se formula em artigos tanto quanto em livros").
2. O argumento sobre a especificidade da figuração militar-industrial ganhe contraste: ela é dominante no gênero textual em que Latour faz descrição de campo, e recua quando Latour reflete metateoricamente sobre o vocabulário que usa.
3. A passagem dos pp. 19-20 do *Recalling* (em que Latour reconhece que o vocabulário da TAR "contaminou" a operação descritiva da teoria) ganhe um lugar argumentativo mais preciso: é exatamente no texto em que Latour reconhece a contaminação que o vocabulário militar está em densidade muito baixa, e que outros léxicos ocupam o terreno.

O recorte fica circunscrito a **dois artigos**, ambos do gênero textual metateórico. Não pretendo estender a análise a artigos descritivos de campo (Pasteur, vieiras, modos de existência), porque a hipótese a investigar opera precisamente sobre o contraste entre o registro descritivo-monográfico (que os livros já cobrem) e o registro metateórico-reflexivo (que os artigos cobrem). Investigar artigos descritivos diluiria o achado e estenderia o escopo para além do que a subseção do cap. 2 comporta.

---

## 2. Resultados preliminares (contagem exploratória sobre os .txt normalizados)

Já normalizei os dois textos a partir dos OCRs originais (vide seção 3.3 sobre os ajustes específicos de OCR). Apliquei uma contagem manual exploratória com regex de borda de palavra sobre os arquivos normalizados, restringindo a contagem ao corpo do texto (excluindo o cabeçalho de metadados). Os resultados confirmam a hipótese:

| Campo | *Recalling* 1999 (1.344 palavras de corpo) | *Clarifications* 1996 (7.934 palavras de corpo) | *Science in Action* 1987 (139.861 palavras, ref. Etapa 1) |
|---|---:|---:|---:|
| MILITAR (64 variantes do catálogo) | 1 ocorrência → **7,44/10k** | 3 ocorr. → **3,78/10k** | 364 ocorr. (refinadas) → **26,03/10k** |
| TÊXTIL (amostra de 50 variantes) | 0 → **0,00/10k** | 15 → **18,91/10k** | (a contar na Etapa 2) |
| TOPOLOGIA (network, fluid, filament, surface, node) | 10 → **74,40/10k** | 113 → **142,43/10k** | (a contar na Etapa 2) |

A magnitude do contraste sustenta o argumento: nos artigos, a densidade militar é cerca de **3 a 7 vezes menor** do que em *Science in Action*. A densidade topológica nos artigos é várias vezes maior do que se esperaria pela leitura cruzada dos livros (a contagem dos campos nos livros ainda precisa ser feita simetricamente para os campos têxtil e topologia, que não estavam destacados na Etapa 1).

Observações qualitativas que a inspeção das ocorrências tornou visíveis:

1. No *Recalling*, a única ocorrência do campo militar é "alliance" em "vocabulary association, translation, alliance, obligatory passage point" — usada **metalinguisticamente** por Latour para citar o próprio vocabulário da TAR que ele submete à autocrítica. Esse uso é categoricamente distinto do gesto descritivo dos livros e exige uma categoria nova de desambiguação (vide 3.5).

2. No *Clarifications*, das 3 ocorrências do campo militar:
   - "network of allies" descreve uso ingênuo do termo TAR como rede de aliados políticos (Latour critica essa leitura).
   - "enemies" descreve a figura do "pré-relativista" como adversário teórico (uso conceitual-debate).
   - "La nouvelle alliance" aparece como **título de livro citado** (Prigogine & Stengers 1979). Uso descritivo-bibliográfico.

Nenhuma dessas ocorrências é uso figurativo do vocabulário militar como tropo para a prática científica, ao contrário do que predomina em *Science in Action*. A desambiguação por gatilhos vai depurar isso.

---

## 3. Decisões metodológicas para esta Etapa 2

### 3.1 Catálogo lexical

Reutilizar **exatamente** o mesmo catálogo de dezessete campos figurais usado na Etapa 1, sem nenhuma alteração. O contraste entre artigos e livros só é defensável se os instrumentos de medição forem idênticos. Os arquivos estão em `campos_lexicais/latour_*_en.txt` no repositório atual. Se for necessário acrescentar variantes, fazer em arquivos separados (`campos_lexicais/latour_*_en_etapa2_adicoes.txt`) e documentar a decisão em `docs/decisoes_metodologicas.md` antes de aplicá-las.

### 3.2 Corpus

Adicionar dois textos ao corpus:

| Slug | Obra | Autor | Ano | Idioma | Edição-fonte |
|---|---|---|---|---|---|
| `latour_1996_clarifications_en` | On actor-network theory: a few clarifications | Bruno Latour | 1996 | inglês | *Soziale Welt*, v. 47, n. 4, pp. 369-381 |
| `latour_1999_recalling_en` | On recalling ANT | Bruno Latour | 1999 | inglês | in Law & Hassard (orgs.), *Actor Network Theory and After*, Oxford: Blackwell, pp. 15-25 |

Atualizar `metadata.csv` com as duas novas linhas. Acrescentar no `corpus/README.md` a nota sobre origem dos arquivos (vide 3.3) e sobre a restrição de cobertura do Recalling (vide nota crítica abaixo).

### 3.3 Origem dos arquivos: .txt JÁ NORMALIZADOS (mudança desde a v1 do briefing)

Os dois `.txt` normalizados estão prontos e devem ser depositados pela Juliane na pasta Drive sincronizada com o restante do corpus, junto aos `.txt` dos três livros. A normalização foi feita fora do pipeline, em sessão prévia com o Claude no chat, pelas razões etnograficamente registradas em `docs/decisoes_metodologicas.md` (gesto análogo ao que o capítulo 4 da tese descreve para outras cadeias de mediação técnica).

Os arquivos têm cabeçalho de metadados em comentário (linhas iniciadas por `#`) com slug, autor, ano, edição-fonte, idioma, paginação original, e uma nota_estrutura sobre o OCR. O pipeline deve pular essas linhas antes de fazer a contagem (regex `^#` é suficiente).

**Nota crítica sobre o Recalling, a ser explicitada em `docs/decisoes_metodologicas.md`:**

O OCR do *Recalling* veio em zip de 11 páginas, das quais apenas as páginas com numeração par no zip (2, 4, 6, 8, 10) tinham OCR limpo, cobrindo as páginas 16, 18, 20, 22, 24 do volume original. As páginas com numeração ímpar do zip (1, 3, 5, 7, 9, 11) tinham OCR severamente truncado nas primeiras letras de cada linha (artefato do scan ou da binarização), com palavras cortadas como "llix" (= Felix), "ncrediblepretensions" (= Incredible pretensions), "Ivenot" (= I have not). Em alguns casos, o conteúdo das páginas ímpares duplicava parcialmente o das pares vizinhas, em uma sobreposição que distorceria a contagem por dobrar artificialmente ocorrências dos termos.

A decisão tomada foi **excluir as páginas ímpares do zip do corpus** e manter apenas as páginas pares, que cobrem **pp. 16-24 do volume** (texto principal limpo). As páginas 15 (abertura + abstract) e 25 (final + bibliografia) do volume não estão integralmente representadas no corpus, mas a passagem-chave dos pp. 19-20 sobre a contaminação do vocabulário está **integralmente incluída** (página 6 do zip = página 20 do volume).

Consequências:

- A contagem do *Recalling* cobre **aproximadamente 80% do artigo**, com 1.344 palavras de corpo. Essa é a base sobre a qual todas as densidades por 10k palavras são calculadas.
- A limitação é registrada explicitamente no cabeçalho do `.txt` e em `docs/decisoes_metodologicas.md`. Ela enfraquece um pouco a quantificação absoluta mas **não enfraquece o argumento comparativo**: a densidade do campo militar nas pp. 16-24 do volume é representativa do tom geral do artigo (a passagem-chave da contaminação está incluída, e as páginas 15 e 25 não contêm conteúdo argumentativo distinto que mudaria o padrão).
- **Pendência futura**: se for possível obter um PDF nativo do *Recalling* (em vez do zip de OCR), reanálise pode incluir o artigo integral e oferecer contagem mais robusta. Essa é uma pendência aberta para uma eventual Etapa 2-bis.

O *Clarifications* não tem essa restrição: as 14 páginas estão íntegras e foram todas incluídas.

### 3.4 Pipeline

Reaproveitar a estrutura de scripts existente, com os mesmos parâmetros que rodaram para a Etapa 1:

- `scripts/02_kwic.py`: janela KWIC de 5 palavras de cada lado, paths em `outputs/<obra_id>/csv/kwic.csv`
- `scripts/03_frequencies.py`: contagem absoluta + densidade por 10k palavras, paths em `outputs/<obra_id>/csv/frequencias.csv`
- `scripts/05_cooccurrence.py`: janelas de 200 palavras para cocorrência, paths em `outputs/<obra_id>/csv/cocorrencia.csv`

Os parâmetros não devem ser alterados.

**Atenção à janela de cocorrência:** as janelas de 200 palavras foram pensadas para textos longos. Em *Recalling* (1.344 palavras de corpo), a janela de 200 palavras corresponde a cerca de 15% do texto total, e em *Clarifications* (7.934 palavras), a 2,5%. Documentar isso em `docs/decisoes_metodologicas.md`, e apresentar para os artigos **uma versão alternativa em janela proporcional** (p. ex. 2% das palavras totais arredondado, dando ~27 palavras para *Recalling* e ~159 para *Clarifications*). A apresentação final pode usar a janela proporcional, com a janela de 200 palavras como controle. A decisão final é minha (Juliane), depois de ver as duas matrizes.

### 3.5 Refinamento do campo militar: duas categorias novas de desambiguação

A desambiguação automática + manual aplicada na Etapa 1 (gatilhos lexicais para *Science Wars*, *World War*, *Cold War*, *Franco-Prussian War*, *Ministry of War*, *phony war*, *War and Peace* etc.) precisa ser estendida com **duas categorias novas** específicas para os artigos metateóricos:

1. **`metalinguistico`**: ocorrências em que Latour cita seu próprio vocabulário (como em "vocabulary association, translation, alliance, obligatory passage point"). Essas ocorrências precisam ser desambiguadas como metalinguísticas, não figurativas. A única ocorrência do campo militar no *Recalling* (segundo a contagem preliminar) entra nessa categoria. Gatilho automático possível: ocorrência dentro de aspas, ou em vizinhança imediata (cinco palavras) com termos do vocabulário próprio da TAR (`association`, `translation`, `passage point`, `actor-network`, `enrollment`).

2. **`descritivo-bibliografico`**: ocorrências em referências bibliográficas e em títulos de obras citadas (como "La nouvelle alliance" de Prigogine & Stengers). Gatilho automático: ocorrência em itálico, ou em vizinhança imediata com nomes de autores e/ou anos entre parênteses, ou em formatação de bibliografia ao final do artigo.

A planilha de classificação manual deve seguir o mesmo formato de `refinamento/war_pandora_classificacao.csv` (já no projeto), com colunas para `obra_id`, `linha_kwic`, `termo`, `classificacao` (figurativa | descritivo-historica | metalinguistico | descritivo-bibliografico), `gatilho` (se automática) e `nota` (se manual).

### 3.6 Validação amostral semântica

A Etapa 1 já tem em curso (em paralelo) o passo 2 da validação amostral semântica em 3 camadas (A/B/C) para os trechos figurativos dos livros. Esta Etapa 2 deve aplicar **a mesma validação amostral** aos trechos figurativos dos artigos, com a mesma estratificação A/B/C e o mesmo procedimento de preenchimento das planilhas geradas. A amostra dos artigos será necessariamente menor em volume absoluto, porque o número total de ocorrências é menor, mas o método é idêntico.

---

## 4. Outputs esperados

### 4.1 Outputs por obra (rotina já existente)

- `outputs/latour_1996_clarifications_en/csv/{kwic,frequencias,cocorrencia}.csv`
- `outputs/latour_1999_recalling_en/csv/{kwic,frequencias,cocorrencia}.csv`
- `outputs/latour_1996_clarifications_en/figuras/` (densidade militar ao longo do texto, ranking de campos)
- `outputs/latour_1999_recalling_en/figuras/` (idem; mas atenção ao texto curto, o que limita a expressividade dos gráficos de densidade)

### 4.2 Outputs comparativos (Etapa 2 propriamente dita)

Um diretório novo, `outputs/etapa2_artigos/`, com:

1. **`tabela_comparativa_5_obras.csv`** e **`tabela_comparativa_5_obras.tex`**: linha por obra (3 livros + 2 artigos), coluna por campo lexical (dos dezessete campos do catálogo). Apresentar contagem absoluta e densidade por 10k palavras. Esta tabela é a que provavelmente entrará na subseção do cap. 2 da tese.

2. **`tabela_campo_militar_refinado_5_obras.csv`** e **`tabela_campo_militar_refinado_5_obras.tex`**: foco no campo `militar`, com colunas para bruta, descritivo-histórica, metalinguística, descritivo-bibliográfica, figurativa refinada. Esta tabela é a que sustenta a leitura do contraste entre gêneros textuais.

3. **`tabela_textil_topologico_5_obras.csv`** e **`tabela_textil_topologico_5_obras.tex`**: foco nos campos têxteis e topológicos, para tornar visível o léxico que ocupa o terreno deixado pelo vocabulário militar nos artigos. **Atenção**: isso vai exigir a contagem dos campos têxtil e topologia também para os três livros (que não estavam consolidados na Etapa 1). Se já estão nos `frequencias.csv` dos livros, basta cruzar; se não, é necessário rodar `scripts/03_frequencies.py` retroativamente sobre os três livros com o catálogo expandido.

4. **`relatorio_etapa2.md`**: relatório curto (2-3 páginas) que sintetiza os achados da Etapa 2, com:
   - Tabela comparativa principal das densidades militares por 10k palavras nas 5 obras.
   - KWIC com 5 exemplos representativos da figuração têxtil-topológica em *Clarifications* (esperados nas pp. 76-91 segundo a inspeção qualitativa: "fibrous, thread-like, wiry, stringy, ropy, capillary").
   - KWIC com a única ocorrência militar em *Recalling* e as 3 em *Clarifications*, com classificação de desambiguação ao lado.
   - Leitura sintética: a divisão de trabalho metafórico por gênero textual como achado empírico.
   - Pendência: passos seguintes (validação amostral semântica nos artigos, e PDF nativo do Recalling para análise completa).

### 4.3 Limite explícito do que o Claude Code faz

A leitura analítica final (a redação da subseção do cap. 2 que incorpora esses achados) **é minha, e não do Claude Code**. O briefing pede a contagem, as tabelas e o relatório operacional; a interpretação argumentativa, a costura com a literatura secundária e a inserção na arquitetura da tese ficam por minha conta. Esse limite é parte da divisão do trabalho que entra em `docs/decisoes_metodologicas.md` e que vai compor o apêndice metodológico da tese.

---

## 5. Plano de execução em etapas com gates

Cada etapa fecha em um artefato verificável, e cada gate é um momento em que eu (Juliane) reviso o output antes da próxima começar.

**Etapa 2.0 — integração dos .txt normalizados ao corpus** (simplificada em relação à v1)
- Os dois `.txt` (`latour_1996_clarifications_en.txt` e `latour_1999_recalling_en.txt`) já vão estar na pasta Drive sincronizada, junto aos `.txt` dos livros, depositados por mim antes da sessão.
- Atualizar `metadata.csv` com as duas novas linhas (slug, autor, ano, título, publicação, idioma, paginação).
- Atualizar `corpus/README.md` documentando os dois novos textos e a restrição de cobertura do Recalling.
- Registrar em `docs/decisoes_metodologicas.md` as decisões de OCR (vide 3.3) e os ajustes ao pipeline (vide 3.4 sobre janela de cocorrência, 3.5 sobre novas categorias de desambiguação).
- **Gate 2.0**: eu confirmo a integridade dos `.txt` (verifico cabeçalho de metadados, contagem de palavras, sanity check sobre presença da passagem-chave em cada um).

**Etapa 2.1 — contagem bruta**
- Rodar `scripts/03_frequencies.py` sobre os dois novos textos (com filtro para pular cabeçalho `#`), gerar tabela comparativa preliminar das 5 obras.
- **Gate 2.1**: eu confirmo que as densidades fazem sentido (cf. ordem de grandeza preliminar registrada na seção 2 deste briefing). Resultados muito divergentes do esperado devem ser investigados (problema de OCR adicional? variante não capturada?).

**Etapa 2.2 — KWIC e desambiguação automática**
- Rodar `scripts/02_kwic.py` com janela 5+5.
- Aplicar desambiguação automática nas ocorrências do campo militar (gatilhos da Etapa 1 + dois gatilhos novos: metalinguístico, descritivo-bibliográfico).
- **Gate 2.2**: eu reviso a planilha de classificação automática e marco as discordâncias.

**Etapa 2.3 — desambiguação manual**
- Eu (Juliane) completo a classificação manual das ocorrências não capturadas pela camada automática.
- **Gate 2.3**: planilha manual concluída, com nota etnográfica sobre as discordâncias com a automática.

**Etapa 2.4 — cocorrência**
- Rodar `scripts/05_cooccurrence.py` com janela 200 (controle) e janela proporcional (2% do texto, arredondada).
- Gerar matriz de cocorrência das duas versões.
- **Gate 2.4**: eu confirmo qual janela apresentar na tese (ou as duas, lado a lado, com nota metodológica).

**Etapa 2.5 — outputs comparativos**
- Verificar se as contagens dos campos têxtil e topologia já estão nos `frequencias.csv` dos três livros da Etapa 1; se não, rodar retroativamente.
- Gerar tabelas LaTeX e CSV dos três cortes: comparativa geral, campo militar refinado, têxtil-topológico.
- Gerar `relatorio_etapa2.md`.
- **Gate 2.5**: relatório aprovado, tabelas LaTeX prontas para inserção na tese.

**Etapa 2.6 — validação amostral semântica** (em paralelo com o passo 2 já em andamento da Etapa 1)
- Gerar planilhas de validação amostral A/B/C para os trechos figurativos dos artigos.
- **Gate 2.6**: planilhas geradas, aguardando preenchimento.

---

## 6. O que NÃO está no escopo desta Etapa 2

- Análise de outros artigos de Latour (Pragmatogonies 1994, On Technical Mediation 1994, Where Are the Missing Masses 1992, Dingpolitik 2005, etc.). A justificativa do recorte está na seção 1.
- Análise dos artigos de Donna Haraway. A análise de Haraway é objeto da Etapa 3 do projeto, que precede e excede o escopo desta etapa.
- Reformulação dos parâmetros do pipeline (janelas, catálogos, scripts). O argumento depende de instrumentação idêntica à Etapa 1.
- Reanálise do *Recalling* com PDF nativo (vide 3.3, pendência aberta para Etapa 2-bis).
- Redação da subseção do cap. 2 da tese. Como registrei em 4.3, isso é meu.

---

## 7. Pendências antes de começar

1. Os dois `.txt` normalizados precisam estar na pasta Drive sincronizada antes da sessão. Eu (Juliane) coloco-os lá.

2. Confirmar que o passo 2 da validação amostral semântica da Etapa 1 (já em andamento, planilhas geradas, aguardando preenchimento) **não precisa estar concluído** para começar a Etapa 2. As duas linhas de trabalho podem rodar em paralelo, desde que a validação semântica dos artigos siga o mesmo protocolo.

3. Confirmar a entrada bibtex que vou usar no `.bib` da tese para o *Recalling*. A entrada atual no `.bib` do cap. 2 é:

```bibtex
@incollection{Latour1999Recalling,
  author    = {Latour, Bruno},
  title     = {On Recalling {ANT}},
  booktitle = {Actor Network Theory and After},
  editor    = {Law, John and Hassard, John},
  publisher = {Blackwell},
  address   = {Oxford},
  year      = {1999},
  pages     = {15--25}
}
```

A entrada `latour1996clarifications` precisa ser auditada (não fui eu quem a criou; confirmar se está consistente com o padrão biblatex/ABNT do resto do `.bib`).

4. Auditar se o `scripts/01_extract_text.py` (ou outro script de leitura inicial) pula linhas iniciadas por `#` quando ingere os `.txt` do corpus. Se não pular, precisa pular: o cabeçalho de metadados não deve entrar na contagem.

---

**Fim do briefing v2.**
Quando iniciar uma sessão na pasta `analise_figuracoes`, leia este briefing junto com o `CLAUDE.md` e o `plano_de_trabalho.md`, e aguarde minha confirmação antes de iniciar a Etapa 2.0.
