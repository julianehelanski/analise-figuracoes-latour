# Migração da validação amostral A/B/C: Etapa 2.6 → Etapa 2-bis

Data: 2026-05-15.

Total de linhas na nova planilha: **40**.
- Linhas migradas da Etapa 2.6 (mesma ocorrência, mesma classificação): **31**.
- Linhas novas (ficam em branco para preenchimento manual): **9**.

## Distribuição por campo e camada

| Campo | Camada | n na 2-bis | migradas | novas |
|---|---|---:|---:|---:|
| actor_network | exaustiva | 9 | 5 | 4 |
| network | A_top_densidade | 5 | 5 | 0 |
| network | B_aleatoria | 5 | 5 | 0 |
| network | C_variantes_raras | 5 | 5 | 0 |
| textil | exaustiva | 1 | 0 | 1 |
| topologia | A_top_densidade | 5 | 5 | 0 |
| topologia | B_aleatoria | 5 | 3 | 2 |
| topologia | C_variantes_raras | 5 | 3 | 2 |

## Procedimento de casamento

O casamento entre ocorrência da Etapa 2.6 e ocorrência da Etapa 2-bis foi feito pela chave composta (`campo` + `termo_encontrado` + `trecho_central`), normalizados a minúsculas. O casamento por offset absoluto seria mais preciso mas inaplicável aqui, porque o `.txt` normalizado mudou (passou de 1.241 para 4.825 palavras), o que altera todos os offsets em caracteres. A chave por trecho central é estável a essa renormalização.

## Pendência

As **9 linhas novas** ficam com colunas `uso_figural`, `subcategoria` e `comentario` em branco. Aguardam preenchimento manual da pesquisadora em sessão futura. Após o preenchimento, regerar `validacao_amostral_resultados.md` consolidando a Etapa 2-bis.