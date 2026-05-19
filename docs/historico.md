# Histórico de documentos consumidos

Este arquivo condensa, em índice cronológico, os briefings operacionais e o plano de trabalho original que orientaram a execução das etapas concluídas. Os documentos fontes foram removidos do working tree e permanecem no histórico do git para consulta integral. As decisões metodológicas vivas (que ainda informam o estado atual do projeto) estão em `decisoes_metodologicas.md`.

A finalidade deste arquivo é etnográfica: registrar a cadeia de mediações entre o plano inicial, os briefings operacionais e o estado consolidado, em coerência com o tratamento que a tese dá às demais cadeias de mediação técnica.

---

## 13/05/2026 — `plano_de_trabalho.md`

Plano em oito etapas para análise textual de figurações em Latour e Haraway. As etapas previstas eram:

0. Preparação do ambiente e do corpus.
1. Lexicometria mínima sobre prova de conceito.
2. Validação amostral.
3. Extração com lematização e tagging morfossintático.
4. Frequências comparadas e visualizações.
5. Cocorrências e redes figurais.
6. Anotação manual amostral.
7. Leitura interpretativa assistida.
8. Consolidação para a tese.

A execução real divergiu da numeração: o que o repositório registra como Etapa 1 corresponde a um agregado das etapas 1, 3, 4 e 5 do plano, aplicado às três obras de Latour entre 1986 e 1999. As etapas 2 e 2-bis estenderam a instrumentação aos artigos teóricos; a Etapa 3 estendeu a AIME. As fases que mobilizam Haraway, Stengers e Ingold permanecem por executar.

---

## 14/05/2026 — `briefing_graficos_claude_code.md`

Especificação de três gráficos para a subseção do capítulo 2 sobre figuração militar em Latour: barras horizontais comparando densidade dos dezessete campos figurativos nas três obras (Figura 1), densidade do campo militar ao longo do texto (Figura 2), rede de cocorrência em *Science in Action* (Figura 3). Princípios estéticos (paleta sóbria, sem emojis, tipografia legível para impressão) e política de versionamento (PNG e SVG em `outputs/etapa1/<obra>/figuras/`). Implementado em `scripts/04_visualizations.py` e `scripts/05_cooccurrence.py`.

---

## 15/05/2026 — `briefing_claude_code.md` (Passo 4 do refinamento da Etapa 1)

Especificação do passo 4 do refinamento: KWIC ampliado em janela ±50 palavras sobre o campo militar nas três obras, com curadoria de 10 a 15 passagens citáveis. Implementado em `scripts/arquivo/10_passo4_kwic_ampliado.py` e `scripts/arquivo/11_passo4_graficos.py`. Os artefatos de reprodução extensa de Latour ficam fora do repositório público por questão de direito autoral (entrada correspondente em `.gitignore`); o script versionado reproduz-os localmente a partir dos PDFs em `CORPUS_PDF_PATH`.

O briefing também consolidou a dispensa da validação amostral semântica retroativa para os três livros da Etapa 1 (passo 2 do refinamento), por inviabilidade de tempo e por suficiência da validação A/B/C aplicada aos artigos teóricos da Etapa 2.

---

## 15/05/2026 — `briefing_etapa2_artigos_latour.md`

Especificação operacional da Etapa 2: análise lexicométrica comparativa dos cinco textos (três livros monográficos da Etapa 1 mais os dois artigos teóricos *On Actor-Network Theory: A Few Clarifications* de 1996 e *On Recalling ANT* de 1999). Sete subetapas (2.0 a 2.6) com gates de revisão entre cada, definindo catálogo (idêntico à Etapa 1), pipeline (`--escopo etapa2` nos scripts), origem dos `.txt` (normalizados fora do pipeline em sessão de chat anterior), restrição de cobertura do *Recalling* (~80% inicialmente declarados, ajustados para 25,3% na Etapa 2-bis), categorias novas de desambiguação do campo militar (`metalinguistico`, `descritivo_bibliografico`, `conceitual_debate`) e protocolo A/B/C da validação amostral semântica.

A Etapa 2 foi concluída em 15/05/2026. A Etapa 2-bis, executada na sequência sobre o `.txt` integral do *Recalling* fornecido por canais institucionais, refez 2.1, 2.2, 2.4 e migrou 2.6, fechando a lacuna metodológica.

---

## Documentos fontes removidos do working tree

- `plano_de_trabalho.md` (653 linhas).
- `briefing_graficos_claude_code.md` (289 linhas).
- `briefing_claude_code.md` (548 linhas).
- `briefing_etapa2_artigos_latour.md` (228 linhas).
- `decisoes_metodologicas.md` da raiz (71 linhas, conteúdo absorvido por `docs/decisoes_metodologicas.md`).

Para consulta integral, navegar no histórico do git anterior ao commit de condensação (`git log --all -- <caminho>` e `git show <hash>:<caminho>`).
