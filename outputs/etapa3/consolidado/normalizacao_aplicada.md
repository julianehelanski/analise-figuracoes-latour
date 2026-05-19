# Normalização aplicada ao `.txt` integral de AIME (Etapa 3, Passo 1)

Data: 2026-05-15.

Apliquei sobre `corpus/txt_fornecido/latour_2013_aime_en.txt` cinco operações simétricas às registradas para os demais `.txt` na Etapa 1 (Adendo 1), na Etapa 2 (saneamento de OCR) e na Etapa 2-bis (item 1 do Passo 1). O arquivo de saída fica em `corpus/txt_norm/latour_2013_aime_en.txt`.

## Operações aplicadas

| Operação | n | comentário |
|---|---:|---|
| CRLF → LF | 21.104 | o arquivo inteiro vinha com fim-de-linha Windows; convertido para Unix, transparente na leitura como texto |
| Soft hyphens U+00AD removidos | 0 | não há (extração de PDF nativo com texto vetorial, sem soft hyphens) |
| Caracteres de controle ASCII de baixa ordem substituídos por espaço | 519 | tratamento simétrico ao do *Recalling* (Etapa 2-bis) |
| EOL hyphenation `-\n[a-z]` reconstituída | 852 | análogo ao Adendo 1 (Lab Life: 500 reconstituções; Science in Action: 55; Pandora's Hope: 18) |
| Replacement chars U+FFFD substituídos por espaço | 402 | tratamento simétrico ao Adendo 1 (Pandora's Hope: 220 replacement chars) |
| Marcadores `((NN))` | 0 | não há (foi problema específico de *Science in Action*) |

## Contagem de palavras

- Antes da normalização (arquivo fornecido bruto): 195.706 palavras (`split`).
- Após CRLF/controle/EOL hyphens: 194.854.
- Após substituição de U+FFFD: 194.454.

A redução total (−1.252 tokens) decorre da reconstituição de palavras quebradas no fim de linha (−852) e da substituição de replacement chars que estavam isolados como tokens (−400 efetivos sobre 402 substituições; dois caracteres ficaram absorvidos por whitespace adjacente sem alterar a contagem).

## Inspeção dos replacement chars U+FFFD

Amostra de cinco contextos antes da substituição:

```
...f objective among the Moderns ◊ without respecting        kn...
...pes of passes. actor-network, ◊ which makes it possible to d...
...      are difficult to detect ◊ because of their they do not...
...ticular ties to institutions, ◊ and                         ...
...of reconstiamong the Moderns ◊              tuting the valu...
```

Onde `◊` representa o U+FFFD original. Os contextos sugerem que os FFFD ocupavam a posição de travessões longos (`—`) ou aspas tipográficas que o conversor de PDF não conseguiu decodificar. A substituição por espaço é benigna: os tokens vizinhos permanecem separáveis, e o casamento de termos do catálogo não é afetado.

## Não aplicado

Nenhuma operação foi adicionada além das registradas pelo Adendo 1 da Etapa 1 e pela seção 4 da Etapa 2 (saneamento de OCR adicional). Mantenho o `.txt` em `corpus/txt_fornecido/` como artefato auditável intocado.

## Comparação com expectativa do briefing

O briefing antecipava ~194.000 palavras. O número real, após normalização, é 194.454. Diferença de +454 (+0,2%), dentro da margem.
