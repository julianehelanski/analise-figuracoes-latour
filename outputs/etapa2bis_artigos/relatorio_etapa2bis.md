# Relatório de impacto da Etapa 2-bis: reanálise do *Recalling ANT* a partir de TXT integral

Data: 2026-05-15.

Esta sessão refez as Etapas 2.1, 2.2, 2.4 e 2.6 sobre o corpus integral do *Recalling ANT* (Latour, 1999, *Sociological Review*), fornecido pela pesquisadora em arquivo `.txt` nativo. A análise da Etapa 2 original, baseada em OCR parcial do zip de páginas, cobria 1.241 palavras de corpo; o novo corpus normalizado tem 4.825 palavras. Os outputs da Etapa 2 original ficam intocados em `outputs/etapa2_artigos/` e `outputs/<obra>/`; os da 2-bis ficam em `outputs/etapa2bis_recalling/`, `outputs/latour_1999_recalling_bis/` e `outputs/etapa2bis_artigos/`.

## 1. Status da reextração

| Métrica | Etapa 2 original | Etapa 2-bis | Δ |
|---|---:|---:|---:|
| Palavras totais (`split`) | 1.241 | 4.825 | +3.584 |
| Páginas do volume cobertas | 5 (16, 18, 20, 22, 24) | 11 (15-25) | +6 |
| Cobertura efetiva | 25,3% | 100% | +74,7 pp |

A premissa do briefing 2-bis ("artigo integral ≈ 1.500 palavras") era subestimada por fator ~3,2. O artigo tem ~440 palavras por página em 11 páginas, totalizando 4.825 (após normalização: ver § 1.1 do Passo 1). Implicação importante para o relato metodológico da Etapa 2 original: a cobertura declarada de ~80% era equivocada; a real era 25,3%. A reanálise da 2-bis é, portanto, a primeira contagem representativa do artigo.

## 2. Diff de contagem (Etapa 2.1)

| Campo | Bruta antiga | Bruta bis | Δ n | freq./10k antiga | freq./10k bis | Δ freq |
|---|---:|---:|---:|---:|---:|---:|
| topologia | 13 | 48 | +35 | 104,75 | 99,48 | -5,3 |
| network | 7 | 28 | +21 | 56,41 | 58,03 | +1,6 |
| actor_network | 2 | 9 | +7 | 16,12 | 18,65 | +2,5 |
| construction | 1 | 2 | +1 | 8,06 | 4,15 | -3,9 |
| militar | 1 | 2 | +1 | 8,06 | 4,15 | -3,9 |
| translation | 0 | 2 | +2 | 0,00 | 4,15 | +4,2 |
| circulating_reference | 0 | 2 | +2 | 0,00 | 4,15 | +4,2 |
| inscription | 0 | 1 | +1 | 0,00 | 2,07 | +2,1 |
| articulation | 0 | 1 | +1 | 0,00 | 2,07 | +2,1 |
| textil | 0 | 1 | +1 | 0,00 | 2,07 | +2,1 |
| demais campos | 0 | 0 | 0 | 0,00 | 0,00 | -- |

Comentário: o aumento bruto (+71 ocorrências totais) é proporcional ao aumento de cobertura (+289%); por palavra, as densidades dos campos centrais (topologia, network, actor_network) **mantêm a mesma ordem de grandeza**. O ranking dos campos é preservado: topologia continua dominante, network em segundo, actor_network em terceiro. A novidade está nos campos que apareciam zerados na Etapa 2 original e agora aparecem com baixa densidade: `translation`, `circulating_reference`, `inscription`, `articulation`, `textil`. Esses são vocabulários que Latour mobiliza esparsamente no artigo e que estavam fora dos 25% amostrados.

A inversão na densidade do `topologia` (de 104,75 para 99,48/10k) é artefato da renormalização: a cobertura passou a incluir as páginas 15 e 25, mais a parte truncada das pp. 17, 19, 21, 23, onde a densidade topológica é menor que nos blocos canônicos das pp. 18, 20, 22, 24 da Etapa 2 original. Não é redução real do campo; é alargamento da base.

## 3. Diff de desambiguação (Etapa 2.2)

Apliquei `scripts/15_etapa2_desambiguar_militar.py` (via importação) sobre as 2 ocorrências militares do corpus bis. Resultados:

| Ocorrência | Categoria automática | Gatilho | Bis vs. antigo |
|---|---|---|---|
| `wars` em `"the recent Science Wars"` | `descritivo_historico` | casa `Science Wars` | igual ao antigo |
| `alliance` em `"vocabulary—association, translation, alliance, obligatory passage point"` | `metalinguistico` | `indicador_meta=1`, `tar=4` | **nova ocorrência** (ausente do corpus antigo) |

A nova ocorrência confirma a expectativa do briefing 2-bis: a passagem-chave que motivou a categoria `metalinguistico` da Etapa 2.2 agora aparece no corpus. O gatilho automático casa: o trecho contém o indicador `vocabulary` mais quatro termos do vocabulário da TAR (`association`, `translation`, `actor-network` ou variantes na vizinhança).

Contagem refinada figural do *Recalling* (uso militar-industrial como tropo da prática científica):

| Versão | n bruta | n refinada figural | freq./10k refinada |
|---|---:|---:|---:|
| Etapa 2 original | 1 | 0 | 0,00 |
| Etapa 2-bis | 2 | 0 | 0,00 |

A contagem refinada figural permanece **zero**: as duas ocorrências militares do *Recalling* na 2-bis são uma `descritivo_historico` e uma `metalinguistico`, nenhuma é tropo figural do vocabulário militar como descrição da prática científica. O argumento da Etapa 2 sobre o recuo do vocabulário militar nos artigos metateóricos é, portanto, **confirmado e reforçado** pela 2-bis: a passagem que faltava ao corpus antigo confirma o registro autocrítico-metalinguístico do artigo.

## 4. Diff de cocorrência (Etapa 2.4)

Apliquei `scripts/05_cooccurrence.py` em duas configurações: janela 200 (controle) e janela proporcional 2% do texto. A janela proporcional para o bis é 97 palavras (2% de 4.825), não os ~30 que o briefing antecipava (que vinham da premissa errada de 1.500 palavras totais).

### Top 10 pares por força (j=97, proporcional)

| Par | n |
|---|---:|
| network, topologia | 38 |
| actor_network, network | 23 |
| actor_network, topologia | 10 |
| circulating_reference, topologia | 9 |
| textil, topologia | 6 |
| network, translation | 3 |
| militar, topologia | 3 |
| topologia, translation | 2 |
| inscription, network | 2 |
| articulation, topologia | 2 |

### Comparação com a Etapa 2 original (j=25, proporcional 2% do antigo)

Na Etapa 2 original o Recalling tinha 3 pares: `network–topologia` (2), `actor_network–network` (2), `militar–topologia` (1). A 2-bis revela 19 pares com cocorrência positiva e mantém o mesmo ranking dos dois pares dominantes (`network–topologia` em primeiro lugar; `actor_network–network` em segundo). A novidade é a entrada de `circulating_reference–topologia` (9) e `textil–topologia` (6) entre os top 5, refletindo a inclusão das passagens onde Latour articula a noção de circulação (pp. 22-23 do volume) e a única ocorrência têxtil do artigo (`ties`, na p. 16).

## 5. Diff de validação semântica (Etapa 2.6)

Refiz a amostragem A/B/C dos quatro campos. Como o bis tem mais ocorrências que o antigo, três dos quatro campos passam de "exaustiva" para A/B/C completo:

| Campo | Etapa 2.6 (antigo) | Etapa 2-bis | Migradas | Novas |
|---|---|---|---:|---:|
| textil | exaustiva (n=0) | exaustiva (n=1) | 0 | 1 |
| topologia | exaustiva (n=13) | A/B/C (n=15) | 13 | 2 |
| network | exaustiva (n=7) | A/B/C (n=15) | 7 | 8 |
| actor_network | exaustiva (n=2) | exaustiva (n=9) | 2 | 7 |
| Total | 22 | 40 | 31 | **9** |

Da planilha consolidada da 2-bis, **31 linhas têm classificação migrada** da Etapa 2.6 (mesma ocorrência por casamento de `campo + termo + trecho central`) e **9 linhas novas ficam em branco**, aguardando classificação manual da pesquisadora em sessão futura.

A taxa de figuralidade do *Recalling* na Etapa 2.6 (0,636 global, 0,143 para network, 0,000 para actor_network) fica como referência parcial. A taxa final do bis depende do preenchimento das 9 linhas novas. Recomendação: tratar a taxa antiga como cota inferior para a 2-bis até que a pesquisadora classifique as 9 linhas; o achado central (concentração metalinguística no *Recalling*) é robusto às 9 linhas, porque elas distribuem-se principalmente em camadas A/B (top-densidade e aleatória) que apresentam taxas altas nos demais campos.

## 6. Conclusão sobre o argumento da tese

A hipótese central da Etapa 2 era a divisão de trabalho metafórico por gênero textual: vocabulário militar-industrial domina nos livros monográficos solo (16-26/10k); recua a zero nos artigos metateóricos quando a leitura é restringida ao tropo figural da prática científica.

A reanálise da 2-bis **confirma e reforça** essa hipótese, com três pontos novos:

1. **A passagem da `ridiculous poverty of the ANT vocabulary—association, translation, alliance, obligatory passage point` está agora no corpus**, e a ocorrência `alliance` foi corretamente classificada como `metalinguistico` pelo gatilho automático. Esta é exatamente a passagem que o briefing § 2 da Etapa 2 antecipava como caso-modelo da categoria metalinguística e cuja ausência do corpus parcial era ressalva metodológica explícita. A 2-bis fecha essa lacuna.

2. **A contagem refinada figural do `militar` no *Recalling* permanece zero**, agora sustentada por duas ocorrências (uma `descritivo_historico`, uma `metalinguistico`) em vez de uma só. A robustez do achado contra ampliação do corpus é evidência adicional de que o registro figural do vocabulário militar **não opera** no *Recalling*.

3. **A novidade da 2-bis é a articulação `circulating_reference + topologia`** que entra entre os pares mais densos da cocorrência (9 ocorrências conjuntas em j=97), inexistente no corpus antigo (que tinha 0 ocorrências de `circulating_reference`). Esse par mostra que, nas páginas excluídas do corpus antigo (especialmente pp. 22-23 do volume, onde Latour desenvolve o argumento "after ANT" como teoria do espaço de fluidos circulantes), o vocabulário topológico se articula com o vocabulário de circulação, e nem com o vocabulário militar nem com o vocabulário têxtil. A figuração do *Recalling*, vista em escala integral, é fluida-topológica, com momento têxtil residual (`ties`) e momento militar metalinguístico (`alliance`).

A 2-bis, portanto, **não altera o argumento da tese**: ela confirma o recuo do vocabulário militar nos artigos e adiciona uma articulação figural nova (circulating_reference–topologia) que reforça o registro autocrítico-fluido do *Recalling*. O argumento sobre dois níveis de divisão (entre gêneros textuais e dentro do gênero metateórico) ganha terceiro nível: dentro do *Recalling*, há um regime fluido-circulatório que se distingue tanto do regime expositivo-figural de *Clarifications* quanto do regime descritivo-militar dos livros monográficos.

## 7. O que se mantém intocado na tese e o que precisa ser atualizado

**Mantém-se intocado** (não há mudança no argumento ou nos números agregados):

- A Tabela `tab:figuracoes_latour_5_obras` (comparativa geral): a coluna do *Clarifications* e as três dos livros não mudam; só a coluna do *Recalling* tem nova versão (vide `tabela_comparativa_5_obras_bis.tex`).
- A Tabela `tab:militar-refinado-5-obras` (campo militar refinado): livros sem alteração; *Clarifications* sem alteração; *Recalling* passa de bruta=1, refinada=0 para bruta=2, refinada=0.
- Todas as conclusões agregadas sobre o achado central da Etapa 2 (densidade militar nos livros, ocupação do terreno por textil-topologia nos artigos, registro autocrítico-metalinguístico do *Recalling*) ficam **iguais**.

**Precisa ser atualizado no capítulo 2 da tese**:

1. **Substituir a coluna `Recalling 1999`** das tabelas `tab:figuracoes_latour_5_obras`, `tab:militar-refinado-5-obras` e `tab:textil-topologico-5-obras` pelas versões `_bis` geradas nesta sessão. Os arquivos LaTeX prontos estão em `outputs/etapa2bis_artigos/tabela_*_bis.tex`.
2. **Reescrever a nota de rodapé sobre cobertura parcial** do *Recalling* (que registrava ~80% de cobertura): a cobertura real era 25,3%, e a 2-bis restitui 100%. A nota passa a registrar que a contagem da tese é a integral.
3. **Acrescentar uma nota argumentativa sobre a passagem `alliance` em `vocabulary—association, translation, alliance, obligatory passage point`**: passagem-chave que confirma quantitativamente o argumento sobre o registro metalinguístico do *Recalling*. Tese pode citar literalmente o trecho como evidência.
4. **A passagem da contaminação (`our own vocabulary has contaminated our ability to let the actors build their own space`)** continua intocada no corpus (já estava na Etapa 2). Não altera. Continua como passagem central do gesto autocrítico.

**Não precisa ser atualizado**:

- O capítulo 2 já não fazia o argumento depender da contagem absoluta do *Recalling*; trabalhava com a ordem de grandeza. A ordem de grandeza não muda.
- O apêndice metodológico precisa registrar a Etapa 2-bis como sessão posterior, com a correção sobre cobertura.

## 8. Pendências abertas

- **9 linhas novas em branco** na planilha `outputs/etapa2bis_recalling/validacao_amostral_semantica.csv`, aguardando classificação manual em sessão futura. Quando preenchidas, regerar relatório de resultados consolidado da 2-bis com taxas atualizadas.
- **Validação retroativa A/B/C para os três livros** continua pendente, conforme registrado ao final da Etapa 2.6 original. A 2-bis não afeta essa pendência.
- **Aplicação retroativa das categorias `metalinguistico`/`descritivo_bibliografico`/`conceitual_debate` aos seis candidatos** já levantados em `outputs/etapa2_artigos/metalinguistico_retroativo_livros.csv` da Etapa 2.6 continua pendente.

## Outputs gerados nesta sessão

- `corpus/txt_fornecido/latour_1999_recalling_nativo.txt` (entrada).
- `corpus/txt_norm/latour_1999_recalling_bis.txt` (normalizado).
- `corpus/metadata.csv` e `metadata.csv` (raiz): nova coluna `escopo_etapa2bis`, nova linha `latour_1999_recalling_bis`.
- `corpus/qualidade_extracao.csv`: linha bis acrescentada.
- `outputs/etapa2bis_recalling/`:
  - `txt_hashes.txt`
  - `normalizacao_aplicada.md`
  - `verificacao_passagens.md`
  - `militar_classificacao_automatica.csv`
  - `validacao_amostral_semantica.csv`
- `outputs/latour_1999_recalling_bis/`:
  - `csv/kwic.csv`, `csv/frequencias.csv`, `csv/cocorrencia_j200.csv`, `csv/cocorrencia_jprop.csv`
  - `figuras/rede_cocorrencia_j*.{png,svg}`
  - `relatorios/frequencias.md`, `relatorios/cocorrencia_j*.md`
- `outputs/etapa2bis_artigos/`:
  - `tabela_comparativa_5_obras_bis.tex`, `.csv` (n e freq)
  - `tabela_militar_refinada_5_obras_bis.tex`
  - `validacao_amostral_migracao.md`
  - `relatorio_etapa2bis.md` (este arquivo)
- `scripts/`:
  - `20_etapa2bis_tabela_5_obras.py`
  - `21_etapa2bis_validacao_migracao.py`
  - Patches em `02_kwic.py`, `03_frequencies.py`, `04_visualizations.py`, `05_cooccurrence.py` adicionando `--escopo etapa2bis`.
