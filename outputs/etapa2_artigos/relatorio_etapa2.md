# Relatório preliminar da Etapa 2.1: contagem bruta dos artigos teóricos de Latour

Data da execução: 15 de maio de 2026.

Este relatório consolida a contagem lexicométrica nos dezenove campos figurativos (dezessete do catálogo da Etapa 1 e duas adições da Etapa 2: `textil` e `topologia`) para as cinco obras de Latour em análise: três livros monográficos e dois artigos metateóricos. A pergunta empírica que orienta a tabela é a divisão de trabalho metafórico por gênero textual proposta no briefing da Etapa 2.

## Densidade do campo militar (ocorrências por 10.000 palavras)

| Obra | Palavras | n militar | freq./10k |
|---|---:|---:|---:|
| Lab Life 1986 | 105.749 | 39 | 3.69 |
| Sci. in Action 1987 | 139.861 | 374 | 26.74 |
| Pandora 1999 | 128.001 | 212 | 16.56 |
| Clarifications 1996 | 7.848 | 3 | 3.82 |
| Recalling 1999 | 1.241 | 1 | 8.06 |

A leitura quantitativa sustenta o contraste central do briefing: nos livros monográficos em que Latour é autor solo, a densidade do campo militar oscila entre 16,56 e 26,74 ocorrências por 10.000 palavras, ao passo que nos dois artigos metateóricos a densidade fica entre 3,82 e 8,06. Em *Laboratory Life* 1986, escrita em coautoria com Steve Woolgar, a densidade militar (3,69) está em patamar próximo ao dos artigos, fato que merece registro etnográfico: a inflexão militar-industrial parece consolidar-se com Latour solo a partir de 1987.

A contagem bruta do *Recalling* (n=1) e do *Clarifications* (n=3) cai para próximo de zero após a desambiguação prevista para a Etapa 2.2:

- *Recalling* 1999: a única ocorrência é `wars` em `"the recent Science Wars"` (referência ao debate público dos anos 1990 entre cientistas e estudiosos das ciências, categoria `descritivo-historica`).
- *Clarifications* 1996: `allies` em `"network of allies and extend his power"` é uso que Latour cita para criticar (categoria `metalinguistico`); `enemies` em `"pre-relativist enemies"` é uso conceitual-debate; `alliance` em `"La nouvelle alliance"` (Prigogine e Stengers) é título de livro citado (categoria `descritivo-bibliografico`).

Nenhuma das ocorrências militares dos dois artigos é uso figural do vocabulário militar-industrial como tropo para a prática científica, contrário ao que predomina em *Science in Action* (de onde provêm `allies`(92), `mobilisation`(28), `mobilised`(24), `alliances`(22) entre as variantes top).

## Densidade dos campos têxtil e topologia

| Obra | Palavras | n têxtil | freq./10k | n topologia | freq./10k |
|---|---:|---:|---:|---:|---:|
| Lab Life 1986 | 105.749 | 13 | 1.23 | 146 | 13.81 |
| Sci. in Action 1987 | 139.861 | 111 | 7.94 | 485 | 34.68 |
| Pandora 1999 | 128.001 | 105 | 8.20 | 353 | 27.58 |
| Clarifications 1996 | 7.848 | 39 | 49.69 | 118 | 150.36 |
| Recalling 1999 | 1.241 | 0 | 0.00 | 13 | 104.75 |

O campo `topologia` é o vocabulário que ocupa o terreno deixado pelo vocabulário militar nos artigos: a densidade no *Clarifications* (150,36/10k) e no *Recalling* (104,75/10k) supera a do mesmo campo nos livros monográficos (entre 13,81 e 34,68/10k). O campo `textil` segue padrão análogo no *Clarifications* (49,69/10k), enquanto no *Recalling* a densidade é nula, o que sugere uma especialização interna entre os dois artigos: *Clarifications* mobiliza vocabulário têxtil-topológico de modo denso, *Recalling* concentra-se na topologia.

Variantes top do `textil` em *Clarifications*: `net`(10), `nets`(3), `tied`(3), `tie`(2). A passagem que ancora qualitativamente esse achado está na página 76 do PDF interno, com a sequência `"fibrous, thread-like, wiry, stringy, ropy, capillary character"` (confirmada por sanity check em `scripts/13_audit_articles_etapa2.py`). A inspeção das variantes do campo na Etapa 2.2 (KWIC) é necessária para depurar polissemias prováveis como `tie` (laço/empate), `net` (rede/líquido), `string` (corda/sequência de caracteres).

## Ressalvas metodológicas

1. O *Recalling* opera sobre 1.241 palavras de corpo (convenção `split`), cerca de 80% do artigo original. As páginas 15 e 25 do volume estão excluídas por falha sistemática de OCR. Detalhamento em `docs/decisoes_metodologicas.md`, seção Etapa 2 § 3.

2. O briefing § 2 previa a presença, no *Recalling*, da citação metalinguística `"vocabulary association, translation, alliance, obligatory passage point"`. A inspeção do `.txt` confirma que essa passagem não está no corpus disponível, o que sugere que ela se encontra em uma das páginas excluídas (15 ou 25 do volume). A contagem efetiva do campo militar no *Recalling* (n=1, com `wars` em `Science Wars`) é portanto distinta da prevista (n=1, com `alliance` metalinguístico). O argumento comparativo de divisão de trabalho metafórico não é afetado: a única ocorrência permanece não-figural.

3. As contagens dos campos `textil` e `topologia` carregam polissemia esperada. A validação amostral semântica da Etapa 2.6, com mesma estratificação A/B/C aplicada à Etapa 1, vai estabelecer a taxa de uso figural por campo.

## Outputs gerados

- `outputs/etapa2_artigos/tabela_comparativa_5_obras_n.csv` (contagem absoluta).
- `outputs/etapa2_artigos/tabela_comparativa_5_obras_freq.csv` (densidade por 10k).
- `outputs/etapa2_artigos/tabela_comparativa_5_obras.tex` (LaTeX, pronto para inclusão).
- `outputs/<obra>/csv/frequencias.csv` (atualizados nas 5 obras com `textil` e `topologia`).

## Próximos passos (Gate 2.1 pendente)

A pesquisadora confirma que as densidades acima fazem sentido em ordem de grandeza, antes de prosseguir para:

- Etapa 2.2: KWIC com desambiguação automática do campo militar nos artigos, incluindo os gatilhos novos `metalinguistico` e `descritivo-bibliografico`.
- Etapa 2.3: desambiguação manual.
- Etapa 2.4: cocorrência com janela 200 (controle) e janela proporcional (27 / 159 palavras).
- Etapa 2.5: outputs comparativos consolidados (3 tabelas).
- Etapa 2.6: validação amostral semântica A/B/C.