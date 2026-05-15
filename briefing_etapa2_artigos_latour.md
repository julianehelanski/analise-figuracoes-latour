# Briefing — Etapa 2: análise exploratória das figurações nos artigos teóricos de Latour

**Para:** Claude Code, sessão `analise_figuracoes` da Juliane
**De:** Juliane Helanski (doutoranda, IFCH/Unicamp)
**Data:** maio de 2026
**Status:** briefing exploratório, a ser executado depois da conclusão dos passos 2 a 5 do refinamento da Etapa 1 já em andamento

---

## 1. Contexto e objetivo

A Etapa 1 do projeto produziu a análise lexicométrica de três livros monográficos de Latour (*Laboratory Life* 1986, *Science in Action* 1987, *Pandora's Hope* 1999) sobre 373.611 palavras, com catálogo de dezessete campos figurais, contagem refinada do campo `militar`, mapas de densidade e redes de cocorrência. Esses resultados sustentam, no capítulo 2 da minha tese, a subseção `subsec:figuracao_militar_evidencia`, em que mostro que a figuração militar-industrial é a marca lexical dominante da escrita latouriana nos livros monográficos, e que essa dominância se cristaliza em 1987 e se mantém em 1999.

A leitura qualitativa dos dois artigos teóricos centrais que Latour escreve nesse mesmo período, *On actor-network theory: a few clarifications* (1996, *Soziale Welt*) e *On recalling ANT* (1999, in Law & Hassard, *Actor Network Theory and After*, Blackwell, pp. 15-25), sugere uma divisão de trabalho metafórico entre dois gêneros textuais distintos da produção latouriana: nos livros monográficos, o vocabulário militar-industrial domina; nos artigos metateóricos para pares STS, o vocabulário recua sensivelmente e o léxico que ocupa o seu lugar é o **têxtil-topológico** (network, filament, fluid, weaving, thread, fibrous, knot, ropy, stringy, wiry).

O objetivo desta Etapa 2 é submeter essa hipótese qualitativa à mesma contagem sistemática que produzi para os livros, de modo que:

1. A subseção `subsec:figuracao_militar_evidencia` do capítulo 2 da tese ganhe um corpo de evidência adicional que preempta a objeção previsível da banca ("e os artigos? a teoria ator-rede se formula em artigos tanto quanto em livros").
2. O argumento sobre a especificidade da figuração militar-industrial ganhe contraste: ela é dominante no gênero textual em que Latour faz descrição de campo, e recua quando Latour reflete metateoricamente sobre o vocabulário que usa.
3. A passagem dos pp. 19-20 do *Recalling* (em que Latour reconhece que o vocabulário da TAR "contaminou" a operação descritiva da teoria) ganhe um lugar argumentativo mais preciso: é exatamente no texto em que Latour reconhece a contaminação que o vocabulário militar está em densidade muito baixa, e que outros léxicos ocupam o terreno.

O recorte fica circunscrito a **dois artigos**, ambos já presentes no projeto da Juliane (PDFs zipados, OCR página-a-página) e ambos do gênero textual metateórico. Não pretendo estender a análise a artigos descritivos de campo (Pasteur, vieiras, modos de existência), porque a hipótese a investigar opera precisamente sobre o contraste entre o registro descritivo-monográfico (que os livros já cobrem) e o registro metateórico-reflexivo (que os artigos cobrem). Investigar artigos descritivos diluiria o achado e estenderia o escopo para além do que a subseção do cap. 2 comporta.

---

## 2. Resultados preliminares (contagem exploratória feita à mão pelo Claude no chat)

Conferi por inspeção rápida com `grep -E` os dois PDFs do projeto. Os resultados confirmam, em ordem de grandeza, a hipótese qualitativa:

| Campo | *Recalling* 1999 (3.899 palavras) | *Clarifications* 1996 (7.854 palavras) | *Science in Action* 1987 (139.861 palavras, ref.) |
|---|---:|---:|---:|
| MILITAR (64 variantes) | 2 ocorr. → **5,13/10k** | 3 ocorr. → **3,82/10k** | 364 ocorr. → **26,03/10k** (refinada) |
| TÊXTIL (amostra de 50 variantes) | 0 ocorr. → **0,00/10k** | 15 ocorr. → **19,10/10k** | (a ser contado) |
| TOPOLOGIA (network, fluid, filament, surface) | 30 ocorr. → **76,94/10k** | 113 ocorr. → **143,88/10k** | (a ser contado) |

A magnitude do contraste sustenta o argumento: nos artigos, a densidade militar é cerca de **5 a 7 vezes menor** do que em *Science in Action*. A densidade topológica nos artigos é **muito alta** em comparação com a leitura cruzada de que faço dos livros.

Convém registrar duas observações qualitativas que a inspeção das ocorrências tornou visíveis:

1. No *Recalling*, das 2 ocorrências do campo militar, uma é interna à própria autocrítica que Latour faz do vocabulário da TAR. A linha 326 do OCR concatenado traz: "I vocabulary association, translation, **alliance**" — ou seja, "alliance" entra no texto como termo do vocabulário que Latour está submetendo à autocrítica, e não como gesto descritivo do que a ciência faz. A desambiguação metalinguística é necessária aqui, e pode ser o passo 1 do refinamento desta Etapa 2.

2. No *Clarifications*, a única ocorrência de "alliance" sem flexão é em **título de livro citado** ("Ilya Prigogine et Isabelle Stengers, La nouvelle alliance"), e a única ocorrência de "enemies" descreve a figura do "pré-relativista" como adversário teórico. Esses são usos descritivos de objetos historicamente nomeados, análogos aos casos de "Science Wars" e "World War II" que já foram desambiguados em *Pandora's Hope* no passo 1 do refinamento da Etapa 1.

A desambiguação amostral em duas camadas (automática + manual) que já apliquei em *Pandora's Hope* serve de modelo direto para esta Etapa 2.

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

Atualizar `metadata.csv` com as duas novas linhas.

### 3.3 Origem dos arquivos e extração

Os PDFs originais que tenho são **zips de OCRs página-a-página** (cada zip contém arquivos numerados `N.txt` e `N.jpeg`), e não PDFs únicos. Para integrar ao pipeline da Etapa 1, é preciso:

1. Extrair os zips em diretórios separados em `corpus/txt/` (não em `corpus/pdf/`, porque não há PDF unificado para versionar).
2. Concatenar os `.txt` em ordem numérica via `sort -V` (importante para que `10.txt` venha depois de `9.txt` e não de `1.txt`), produzindo `latour_1996_clarifications_en.txt` e `latour_1999_recalling_en.txt`.
3. Aplicar a mesma normalização que está em `scripts/01_extract_text.py` (que faz a normalização do texto extraído por `pdftotext`), com a salvaguarda de que o OCR dos zips pode ter quebras de linha indesejáveis dentro de palavras (hifenização de fim de linha) e caracteres de controle (`\r`, `\f`) que precisam ser limpos. Convém criar um script auxiliar, p.ex. `scripts/12_etapa2_extrair_ocr_zips.py`, que recebe um zip e produz o `.txt` normalizado, e documentar no cabeçalho do script o fluxo: descompactar → concatenar via sort -V → normalizar → salvar em `corpus/txt_norm/`.

A descrição etnográfica do gesto de partir de zips de OCR (em vez de PDFs unificados) precisa entrar em `docs/decisoes_metodologicas.md`, porque é tipo de mediação técnica que o capítulo 4 da tese examina em outro contexto e que importa registrar.

### 3.4 Pipeline

Reaproveitar a estrutura de scripts existente, com os mesmos parâmetros que rodaram para a Etapa 1:

- `scripts/02_kwic.py`: janela KWIC de 5 palavras de cada lado, paths em `outputs/<obra_id>/csv/kwic.csv`
- `scripts/03_frequencies.py`: contagem absoluta + densidade por 10k palavras, paths em `outputs/<obra_id>/csv/frequencias.csv`
- `scripts/05_cooccurrence.py`: janelas de 200 palavras para cocorrência, paths em `outputs/<obra_id>/csv/cocorrencia.csv`

Os parâmetros não devem ser alterados, pelo mesmo motivo do catálogo lexical: o contraste entre artigos e livros depende de instrumentação idêntica.

**Atenção a um ponto sensível:** as janelas de cocorrência de 200 palavras foram pensadas para textos longos. Em *Recalling*, com apenas 3.899 palavras, a janela de 200 palavras corresponde a cerca de 5% do texto total, e a matriz de cocorrência pode se inflar artificialmente em comparação com os livros. Documentar isso em `docs/decisoes_metodologicas.md`, e apresentar para os artigos **uma versão alternativa em janela proporcional ao tamanho do texto** (p. ex. 1% das palavras totais arredondado, o que dá 39 palavras para *Recalling* e 79 para *Clarifications*). A apresentação final dos resultados de cocorrência dos artigos pode usar a janela proporcional, com a janela de 200 palavras como controle. A decisão final é minha (Juliane), depois de ver as duas matrizes.

### 3.5 Refinamento do campo militar

A desambiguação automática + manual aplicada à Etapa 1 (gatilhos lexicais para *Science Wars*, *World War*, *Cold War*, *Franco-Prussian War*, *Ministry of War*, *phony war*, *War and Peace* etc.) deve ser estendida para os artigos com **dois gatilhos adicionais específicos**:

1. **Uso metalinguístico**: ocorrências em que Latour cita seu próprio vocabulário ("our vocabulary: association, translation, alliance, obligatory passage point") devem ser desambiguadas como **metalinguísticas**, não figurativas. No *Recalling*, a ocorrência de "alliance" da linha 326 do OCR concatenado é exemplo. Classificá-la como descritivo-histórica desfiguraria o argumento; o registro adequado é uma nova categoria, `metalinguístico`, que pode ser apresentada à parte na tabela final.

2. **Títulos de obras citadas**: ocorrências em referências bibliográficas e em citações de títulos (no *Clarifications*, "La nouvelle alliance" de Prigogine & Stengers) devem ser classificadas como **descritivo-bibliográficas**, igualmente desfiguradas do uso figurativo.

A planilha de classificação manual deve seguir o mesmo formato de `refinamento/war_pandora_classificacao.csv` (já no projeto), com colunas para `obra_id`, `linha_kwic`, `termo`, `classificacao` (figurativa / descritivo-histórica / metalinguística / descritivo-bibliográfica), `gatilho` (se automática) e `nota` (se manual).

### 3.6 Validação amostral semântica

A Etapa 1 já tem em curso (em paralelo) o passo 2 da validação amostral semântica em 3 camadas (A/B/C) para os trechos figurativos dos livros. Esta Etapa 2 deve aplicar **a mesma validação amostral** aos trechos figurativos dos artigos, com a mesma estratificação A/B/C e o mesmo procedimento de preenchimento das planilhas geradas. A amostra dos artigos será necessariamente menor em volume absoluto, porque o número total de ocorrências é menor, mas o método é idêntico.

---

## 4. Outputs esperados

### 4.1 Outputs por obra (rotina já existente)

- `outputs/latour_1996_clarifications_en/csv/{kwic,frequencias,cocorrencia}.csv`
- `outputs/latour_1999_recalling_en/csv/{kwic,frequencias,cocorrencia}.csv`
- `outputs/latour_1996_clarifications_en/figuras/` (densidade militar ao longo do texto, ranking de campos)
- `outputs/latour_1999_recalling_en/figuras/` (idem)

### 4.2 Outputs comparativos (Etapa 2 propriamente dita)

Um diretório novo, `outputs/etapa2_artigos/`, com:

1. **`tabela_comparativa_5_obras.csv`** e **`tabela_comparativa_5_obras.tex`**: linha por obra (3 livros + 2 artigos), coluna por campo lexical (dos dezessete campos do catálogo). Apresentar contagem absoluta e densidade por 10k palavras. Esta tabela é a que provavelmente entrará na subseção do cap. 2 da tese.

2. **`tabela_campo_militar_refinado_5_obras.csv`** e **`tabela_campo_militar_refinado_5_obras.tex`**: foco no campo `militar`, com colunas para bruta, descritivo-histórica, metalinguística, descritivo-bibliográfica, figurativa refinada. Esta tabela é a que sustenta a leitura do contraste entre gêneros textuais.

3. **`tabela_textil_topologico_5_obras.csv`** e **`tabela_textil_topologico_5_obras.tex`**: foco nos campos têxteis e topológicos, para tornar visível o léxico que ocupa o terreno deixado pelo vocabulário militar nos artigos.

4. **`relatorio_etapa2.md`**: relatório curto (2-3 páginas) que sintetiza os achados da Etapa 2, com:
   - Tabela comparativa principal das densidades militares por 10k palavras nas 5 obras
   - KWIC com 5 exemplos representativos da figuração têxtil em *Clarifications* (pp. 76-91, segundo a inspeção qualitativa: "fibrous, thread-like, wiry, stringy, ropy, capillary")
   - KWIC com os 2 exemplos do campo militar em *Recalling* e os 3 em *Clarifications*, com sua classificação de desambiguação ao lado
   - Leitura sintética: a divisão de trabalho metafórico por gênero textual como achado empírico
   - Pendência: passos seguintes (validação amostral semântica nos artigos)

### 4.3 Mensagem clara que NÃO entra como output do Claude Code

A leitura analítica final (a redação da subseção do cap. 2 que incorpora esses achados) **é minha, e não do Claude Code**. O briefing pede a contagem, as tabelas e o relatório operacional; a interpretação argumentativa, a costura com a literatura secundária e a inserção na arquitetura da tese ficam por minha conta. Esse limite é parte da divisão do trabalho que descrevo em `docs/decisoes_metodologicas.md` para o apêndice da tese.

---

## 5. Plano de execução em etapas com gates

Cada etapa fecha em um artefato verificável, e cada gate é um momento em que eu (Juliane) reviso o output antes da próxima começar.

**Etapa 2.0 — preparação do corpus**
- Extrair os zips de OCR (`P77RECALLINGANTGBpdf.PDF`, `Latour_ANT_Clarifications.PDF`), concatenar via `sort -V`, normalizar.
- Atualizar `metadata.csv`.
- Atualizar `corpus/README.md` documentando que os dois novos textos vieram de zips de OCR e não de PDFs únicos.
- **Gate 2.0**: eu confirmo a integridade dos `.txt` normalizados (verifico contagem de palavras, sample qualitativo de cada `.txt`).

**Etapa 2.1 — contagem bruta**
- Rodar `scripts/03_frequencies.py` sobre os dois novos textos, gerar tabela comparativa preliminar das 5 obras.
- **Gate 2.1**: eu confirmo que as densidades fazem sentido (cf. ordem de grandeza preliminar registrada na seção 2 deste briefing). Resultados muito divergentes do esperado devem ser investigados (problema de OCR? variante não capturada?).

**Etapa 2.2 — KWIC e desambiguação automática**
- Rodar `scripts/02_kwic.py` com janela 5+5.
- Aplicar desambiguação automática nas ocorrências do campo militar (gatilhos da Etapa 1 + dois novos gatilhos: metalinguístico, descritivo-bibliográfico).
- **Gate 2.2**: eu reviso a planilha de classificação automática e marco as discordâncias.

**Etapa 2.3 — desambiguação manual**
- Eu (Juliane) completo a classificação manual das ocorrências não capturadas pela camada automática.
- **Gate 2.3**: planilha manual concluída, com nota etnográfica sobre as discordâncias com a automática.

**Etapa 2.4 — cocorrência**
- Rodar `scripts/05_cooccurrence.py` com janela 200 (controle) e janela proporcional (1% do texto, arredondada).
- Gerar matriz de cocorrência das duas versões.
- **Gate 2.4**: eu confirmo qual janela apresentar na tese (ou as duas, lado a lado, com nota metodológica).

**Etapa 2.5 — outputs comparativos**
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
- Redação da subseção do cap. 2 da tese. Como registrei em 4.3, isso é meu.

---

## 7. Pendências antes de começar

1. Confirmar que o passo 2 da validação amostral semântica da Etapa 1 (já em andamento, planilhas geradas, aguardando preenchimento) **não precisa estar concluído** para começar a Etapa 2. As duas linhas de trabalho podem rodar em paralelo, desde que a validação semântica dos artigos siga o mesmo protocolo.

2. Decidir, no Gate 2.0, se os zips de OCR precisam de inspeção qualitativa adicional. Em particular, conferir se há problemas de OCR em páginas específicas (caracteres trocados, palavras quebradas por hifenização de fim de linha) que precisem de correção manual antes de entrar no pipeline. Posso fazer isso eu mesma ou pedir ao Claude Code para gerar amostra para minha revisão.

3. Confirmar a entrada bibtex que vou usar no .bib da tese para o *Recalling*. A entrada atual no .bib do cap. 2 é:

```
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

A entrada `latour1996clarifications` precisa ser auditada (não fui eu quem a criou; confirmar se está consistente com o padrão biblatex/ABNT do resto do .bib).

---

**Fim do briefing.**
Quando iniciar uma sessão na pasta `analise_figuracoes`, leia este briefing junto com o `CLAUDE.md` e o `plano_de_trabalho.md`, e aguarde minha confirmação antes de iniciar a Etapa 2.0.
