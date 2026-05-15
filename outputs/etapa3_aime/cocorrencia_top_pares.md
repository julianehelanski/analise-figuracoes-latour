# Cocorrencia em AIME: top pares por configuracao (Etapa 3, Passo 6)

Data: 2026-05-15.

Aplicada cocorrencia sobre os 31 campos (19 antigos + 12 novos) em duas configuracoes:

- **Janela 200 palavras** (controle, consistente com as demais obras).
- **Janela proporcional 0,02% das palavras totais = 39 palavras**. O briefing § Passo 6 ajustou a janela proporcional padrao de 2% (que daria ~3.880 palavras para AIME, valor alto demais para significancia analitica em cocorrencia KWIC) para 0,02%, mantendo ordem de grandeza comparavel a janela proporcional da Etapa 2 (157 palavras em Clarifications, 97 em Recalling-bis).

Total de ocorrencias validas (31 campos): **3557**.
Pares com cocorrencia positiva: **242** em pelo menos uma configuracao.

## Top 30 pares por forca de cocorrencia

| par (A, B) | j=200 | j=39 (prop.) |
|---|---:|---:|
| topologia, trajetoria_passe | 584 | 205 |
| network, topologia | 379 | 91 |
| network, trajetoria_passe | 301 | 54 |
| categorias_dominio, topologia | 285 | 53 |
| categorias_dominio, network | 264 | 70 |
| network, textil | 236 | 93 |
| categorias_dominio, trajetoria_passe | 276 | 33 |
| experiencia, modernos | 243 | 56 |
| instituicao, modernos | 212 | 48 |
| modernos, topologia | 201 | 37 |
| textil, topologia | 197 | 35 |
| categorias_dominio, modernos | 189 | 40 |
| experiencia, topologia | 188 | 36 |
| textil, trajetoria_passe | 183 | 37 |
| alteracao, trajetoria_passe | 160 | 36 |
| experiencia, trajetoria_passe | 168 | 28 |
| modos_existencia, trajetoria_passe | 143 | 41 |
| modernos, network | 158 | 25 |
| categorias_dominio, experiencia | 141 | 29 |
| militar, modernos | 144 | 25 |
| modernos, textil | 147 | 20 |
| categorias_dominio, textil | 133 | 30 |
| categorias_dominio, instituicao | 130 | 31 |
| modos_existencia, topologia | 133 | 26 |
| instituicao, topologia | 140 | 15 |
| diplomacia, modernos | 124 | 29 |
| felicidade, trajetoria_passe | 113 | 36 |
| modernos, trajetoria_passe | 136 | 10 |
| experiencia, textil | 104 | 30 |
| alteracao, topologia | 99 | 30 |

## Pares envolvendo `modos_existencia`

| par (A, B) | j=200 | j=39 |
|---|---:|---:|
| modos_existencia, trajetoria_passe | 143 | 41 |
| modos_existencia, topologia | 133 | 26 |
| modernos, modos_existencia | 97 | 22 |
| categorias_dominio, modos_existencia | 88 | 22 |
| experiencia, modos_existencia | 82 | 11 |
| instituicao, modos_existencia | 75 | 14 |
| modos_existencia, network | 68 | 15 |
| modos_existencia, textil | 61 | 11 |
| alteracao, modos_existencia | 48 | 16 |
| felicidade, modos_existencia | 42 | 14 |
| modos_existencia, preposicao | 35 | 8 |
| militar, modos_existencia | 29 | 7 |
| articulation, modos_existencia | 27 | 5 |
| diplomacia, modos_existencia | 26 | 6 |
| construction, modos_existencia | 18 | 2 |
| gaia, modos_existencia | 13 | 1 |
| immutable_mobile, modos_existencia | 11 | 2 |
| modos_existencia, translation | 10 | 3 |
| actor_network, modos_existencia | 9 | 1 |
| modos_existencia, valores | 7 | 1 |
| modos_existencia, proposition | 3 | 0 |
| black_box, modos_existencia | 1 | 0 |

## Pares envolvendo `diplomacia`

| par (A, B) | j=200 | j=39 |
|---|---:|---:|
| diplomacia, modernos | 124 | 29 |
| diplomacia, instituicao | 87 | 17 |
| diplomacia, militar | 55 | 9 |
| diplomacia, experiencia | 42 | 3 |
| diplomacia, gaia | 35 | 5 |
| categorias_dominio, diplomacia | 34 | 2 |
| diplomacia, modos_existencia | 26 | 6 |
| diplomacia, topologia | 18 | 4 |
| diplomacia, network | 17 | 2 |
| diplomacia, textil | 15 | 0 |
| diplomacia, trajetoria_passe | 14 | 1 |
| alteracao, diplomacia | 11 | 0 |
| diplomacia, preposicao | 11 | 1 |
| actor_network, diplomacia | 4 | 0 |
| construction, diplomacia | 4 | 1 |
| diplomacia, felicidade | 4 | 0 |
| articulation, diplomacia | 4 | 0 |
| diplomacia, immutable_mobile | 2 | 0 |
| diplomacia, valores | 1 | 0 |
| diplomacia, proposition | 1 | 0 |

## Pares envolvendo `network`

| par (A, B) | j=200 | j=39 |
|---|---:|---:|
| network, topologia | 379 | 91 |
| network, trajetoria_passe | 301 | 54 |
| categorias_dominio, network | 264 | 70 |
| network, textil | 236 | 93 |
| modernos, network | 158 | 25 |
| experiencia, network | 108 | 15 |
| instituicao, network | 107 | 17 |
| modos_existencia, network | 68 | 15 |
| militar, network | 45 | 6 |
| network, preposicao | 39 | 16 |
| network, valores | 33 | 11 |
| felicidade, network | 25 | 3 |
| alteracao, network | 19 | 4 |
| network, translation | 18 | 3 |
| diplomacia, network | 17 | 2 |
| construction, network | 17 | 8 |
| immutable_mobile, network | 15 | 2 |
| gaia, network | 13 | 1 |
| inscription, network | 10 | 3 |
| enrollment, network | 9 | 3 |
| articulation, network | 5 | 0 |
| network, proposition | 2 | 0 |
| black_box, network | 1 | 0 |

## Pares envolvendo `militar`

| par (A, B) | j=200 | j=39 |
|---|---:|---:|
| militar, modernos | 144 | 25 |
| instituicao, militar | 78 | 19 |
| militar, topologia | 78 | 13 |
| experiencia, militar | 73 | 6 |
| diplomacia, militar | 55 | 9 |
| gaia, militar | 45 | 7 |
| militar, network | 45 | 6 |
| militar, trajetoria_passe | 45 | 5 |
| categorias_dominio, militar | 36 | 3 |
| militar, textil | 35 | 6 |
| militar, modos_existencia | 29 | 7 |
| construction, militar | 18 | 1 |
| militar, translation | 18 | 5 |
| alteracao, militar | 16 | 2 |
| felicidade, militar | 10 | 0 |
| articulation, militar | 8 | 1 |
| militar, preposicao | 4 | 2 |
| inscription, militar | 4 | 1 |
| militar, proposition | 2 | 1 |
| militar, valores | 2 | 0 |
| enrollment, militar | 2 | 2 |
| actor_network, militar | 2 | 0 |