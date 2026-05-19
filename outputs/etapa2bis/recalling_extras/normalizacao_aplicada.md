# Normalização aplicada ao `.txt` integral do Recalling (Etapa 2-bis, Passo 1)

Data: 2026-05-15.

Apliquei sobre `corpus/txt_fornecido/latour_1999_recalling_nativo.txt` quatro operações de normalização simétricas às documentadas para os demais `.txt` na Etapa 1 (Adendo 1) e na Etapa 2 (saneamento de OCR adicional). O arquivo de saída fica em `corpus/txt_norm/latour_1999_recalling_bis.txt`, lado a lado com o `latour_1999_recalling_en.txt` da Etapa 2 original (que permanece intocado).

## Operações aplicadas

| Operação | n | comentário |
|---|---:|---|
| CRLF → LF | 0 (efetivos, vide nota) | a leitura via `read_text(encoding='utf-8')` já normaliza fim-de-linha; o diagnóstico anterior em `read_bytes()` indicava CRLFs presentes no arquivo bruto, transparentes na leitura como texto |
| Soft hyphens U+00AD removidos | 5 | tratamento simétrico ao Adendo 1 da Etapa 1 (Pandora's Hope: 2.367 soft hyphens) |
| Caracteres de controle ASCII de baixa ordem (`\x00-\x08`, `\x0b-\x1f`, `\x7f`) substituídos por espaço | 11 | tratamento simétrico ao `\x02` nos `.txt` dos demais artigos da Etapa 2 |
| EOL hyphenation `-\n[a-z]` reconstituída | 32 | tratamento simétrico ao Adendo 1 (Lab Life: 578 hifenizações EOL) |

## Contagem de palavras antes e depois

- Antes da normalização (arquivo fornecido bruto): 4.857 palavras (`split`).
- Após normalização: 4.825 palavras (`split`).

A redução de 32 tokens é consequência direta da reconstituição de hifenização EOL (cada padrão `palavra-\npalavra` que antes contava como dois tokens passa a contar como um). Não há perda de informação textual.

## Não aplicado

- Marcadores `((NN))`: 0 ocorrências (tratamento que foi necessário em *Science in Action*; não se aplica aqui).
- Replacement chars U+FFFD: 0 ocorrências.
- Cabeçalhos espaçados (`P A N D O R A`): não presentes neste artigo.

## Verificação adicional pedida pela pesquisadora

O briefing § Princípios pede que nenhuma normalização vá além das documentadas na Etapa 1. As quatro aplicadas acima estão integralmente cobertas pelos Adendos 1 e 2 da Etapa 1 e pela seção "Saneamento de OCR adicional no momento da leitura" da Etapa 2 (item 4 da seção Etapa 2 em `docs/decisoes_metodologicas.md`).

Nenhuma decisão metodológica nova precisa ser registrada na seção Etapa 2-bis de `docs/decisoes_metodologicas.md` para o Passo 1. Caso o relatório final da 2-bis identifique impacto interpretativo das normalizações, registro lá.
