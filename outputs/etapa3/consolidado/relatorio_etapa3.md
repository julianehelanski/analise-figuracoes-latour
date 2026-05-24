# Relatório da Etapa 3: análise lexicométrica de *An Inquiry into Modes of Existence* (Latour, 2013)

Data: 2026-05-15.

## Sumário executivo

*An Inquiry into Modes of Existence* (AIME, 2013) é o livro em que Latour declara estar completando a teoria ator-rede, e em que a TAR vira apenas um dos quinze modos de existência sob a notação `[net]`, com limitação explícita: o `[net]` não qualifica valores. A análise lexicométrica da Etapa 3 documenta o desfecho figural dessa guinada teórica em registro contável. AIME mantém a malha topológica que os artigos metateóricos de 1996 e 1999 inauguraram (`network` 13,11/10k, `topologia` 26,43/10k, `textil` 10,34/10k), reduz o vocabulário militar refinado figural para patamar intermediário (6,33/10k, entre os zero dos artigos e os 12-26 dos livros monográficos solo), e introduz uma camada figural nova densa (12 campos somando 2.214 ocorrências, com destaque para `trajectory_pass` 22,27, `moderns` 20,42, `domain_category` 14,45 por 10k) que se articula com o vocabulário têxtil-topológico anterior. O desfecho da trajetória 1986-2013 é, portanto, **continuidade do vocabulário têxtil-topológico, reentrada moderada do vocabulário militar (em registro deslocado para o horizonte cosmopolítico-diplomático), e introdução de camada figural própria de AIME (modos, preposições, felicidade, alteração, diplomacia, Gaia)**.

## 1. Objeto e justificativa da extensão

AIME foi publicado em 2013 pela Harvard University Press na tradução de Catherine Porter, sob título completo *An Inquiry into Modes of Existence: An Anthropology of the Moderns*. O livro original em francês (*Enquête sur les modes d'existence*) saiu pela La Découverte em 2012. A escolha pelo texto em inglês mantém simetria com a Etapa 1 (originais ou versões anglo-saxônicas de cada obra de Latour). O corpus tem 194.454 palavras de corpo após normalização (hashes e detalhamento em `outputs/etapa3_aime/txt_hashes.txt` e `normalizacao_aplicada.md`).

A motivação para estender a análise até 2013 é etnográfica e ressoa com o gesto reflexivo da tese. A Etapa 2-bis havia documentado, no *Recalling ANT*, a frase autocrítica `"the very expression of network invites this reaction"` e o gesto de pregar quatro pregos no caixão da TAR. AIME é o livro que sai do caixão. Duas passagens-âncora ancoram a justificativa:

- Capítulo 12 (linha 14.809 do corpus normalizado): `"the actor-network theory, which the present inquiry seeks to complete"`. Latour declara que AIME completa a TAR, não a abandona.
- Capítulo 1 (linha 95): `"networks [net] have a limitation: they do not qualify values"`. A TAR vira um dos quinze modos (notado `[net]`), com limitação que motiva a expansão.

Para minha tese, estender a análise a AIME é gesto de justiça intelectual com Latour (não congelá-lo em 1987) e gesto de integridade reflexiva (mostrar que parti da TAR, refleti sobre ela, e o capítulo 2 mostra esse percurso).

## 2. Catálogos aplicados

Apliquei em paralelo dois catálogos sobre AIME:

- **Catálogo antigo** (`campos_lexicais/catalogo_termos.yaml` + adições `latour_textil_en_etapa2_adicoes.txt` e `_topologia_en_etapa2_adicoes.txt`): 19 campos figurativos das Etapas 1 e 2. Aplicação aqui permite leitura comparativa direta com as cinco obras anteriores.
- **Catálogo novo** (`campos_lexicais/catalogo_termos_aime.yaml`): 12 campos específicos de AIME, identificados a partir da leitura qualitativa do livro e da literatura sobre a guinada latouriana pós-2007.

A decisão de aplicar o catálogo novo apenas em AIME é metodológica e está registrada em `docs/decisoes_metodologicas.md` § Etapa 3. Justificativa: os 12 campos novos derivam de vocabulário introduzido por Latour em AIME (`modes of existence`, `preposition`, `felicity condition`, `category mistake`, `Moderns`, `being-as-other`, etc.); sua aplicação retroativa nas obras de 1986-1999 teria rendimento esperado muito baixo, em ordem de grandeza inferior ao ruído. Decisões pontuais do catálogo novo:

- `value`/`values` isolados retirados do campo `values` por polissemia (uso econômico, axiológico geral). Mantive apenas combinações com `qualify` e `system`.
- `pass`/`passes`/`passing` isolados retirados do campo `trajectory_pass` por polissemia. Mantive `course of action`, `trajectory`, `hiatus`, `discontinuity`, `continuity`, `leap`.
- `mode`/`modes` isolados retirados do campo `modes_of_existence`. Mantive apenas `mode/modes of existence` como expressão completa.
- `modern` adjetivo isolado retirado do campo `moderns`. Mantive `Moderns` (substantivo próprio do livro), `modernity`, `modernizing`, `modernism`, `modernization`.
- `Earth` retirado do campo `gaia` por polissemia (solo, planeta, terra fértil).

A Etapa 3 não inclui validação amostral semântica. Os campos de alta polissemia (`experience` com `experience`/`empirical`; `domain_category` com `crossing`; e os campos cuja decisão acima já restringe os termos) carregam ruído que a contagem bruta reflete. A leitura interpretativa precisa considerar esse ruído. A pendência da validação semântica fica declarada em § 8.

## 3. Catálogo antigo nas seis obras

A tabela `tab:figuracoes_latour_6_obras` (em `outputs/etapa3_aime/tabela_comparativa_6_obras.tex`) estende a tabela das cinco obras com AIME como sexta coluna. Os números em densidade por 10.000 palavras, com contagem absoluta entre parênteses, para os campos com presença em AIME:

| Campo | Lab Life | Sci. Action | Pandora | Clarifications | Recalling bis | **AIME** |
|---|---:|---:|---:|---:|---:|---:|
| Palavras | 105.749 | 139.861 | 128.001 | 7.848 | 4.825 | **194.454** |
| `topologia` | 13,81 | 34,68 | 27,58 | 150,36 | 99,48 | **26,43 (514)** |
| `network` | 4,26 | 9,08 | 2,73 | 118,50 | 58,03 | **13,11 (255)** |
| `textil` | 1,23 | 7,94 | 8,20 | 49,69 | 2,07 | **10,34 (201)** |
| `militar` (bruta) | 3,69 | 26,74 | 16,56 | 3,82 | 4,15 | **6,63 (129)** |
| `construction` | 19,29 | 3,79 | 4,84 | 2,55 | 4,15 | 3,81 (74) |
| `articulation` | -- | 0,29 | 4,14 | -- | 2,07 | 2,88 (56) |
| `translation` | 0,28 | 5,58 | 5,47 | 5,10 | 4,15 | 2,06 (40) |
| `inscription` | 11,82 | 4,43 | 1,09 | -- | 2,07 | 1,03 (20) |
| `immutable_mobile` | -- | 0,29 | 0,23 | -- | -- | 1,03 (20) |
| `actor_network` | -- | 1,22 | 2,42 | 24,21 | 18,65 | 0,87 (17) |

Campos zerados em AIME (presença nula): `centre_of_calculation`, `trial_of_strength`, `factish`, `circulating_reference`, `spokesperson`. Continuidade ou recuo notável:

**Continuidade do vocabulário têxtil-topológico**: `topologia` em 26,43/10k (entre Sci. Action 1987 e Pandora 1999), `network` em 13,11/10k (maior que nos três livros monográficos), `textil` em 10,34/10k (na faixa de Sci. Action e Pandora). A malha topológica que os artigos metateóricos de 1996/1999 inauguraram permanece no léxico de AIME, em densidade comparável à dos livros monográficos (não à dos artigos, que eram extremamente densos por brevidade). A diferença em relação aos livros é qualitativa: as variantes top do `topologia` em AIME são `path` (90), `trajectory` (61), `outside` (55), `trajectories` (34), `paths` (33), enquanto em Sci. Action e Pandora dominavam `inside`/`outside`/`scale`/`flow`. O vocabulário topológico em AIME se reorganiza em torno de `trajectory`/`path`, que articula com o campo novo `trajectory_pass`.

**Reentrada moderada do vocabulário militar bruto**: 6,63/10k em AIME, entre o patamar dos artigos metateóricos (0 figural; bruta de 3 a 8) e dos livros monográficos solo (16-26 figural). As 129 ocorrências têm variantes top `war` (22), `mobilizing` (20), `defend` (12), `enemies` (9), `wars` (7). A reentrada não é restauração: o vocabulário militar volta em AIME em densidade reduzida e em registro deslocado (vide § 5).

**Recuo do `actor_network`**: 17 ocorrências (0,87/10k) em AIME, menor que em Pandora (2,42) e Sci. Action (1,22). O termo permanece, mas em densidade que sinaliza o deslocamento do conceito para uma posição entre quinze modos. Em paralelo, `network` (255 ocorrências) mantém densidade alta, sinal de que o vocabulário de rede permanece operacional mesmo após o `[net]` ter virado um modo entre outros.

**Substituição/sucessão de conceitos**: `circulating_reference` (presente em Pandora) e `factish` (presente em Pandora) zeram em AIME. O vocabulário epistemológico característico do livro de 1999 é abandonado.

Figuras: a comparação visual da densidade dos 19 campos nas seis obras pode ser construída em sessão posterior a partir de `outputs/etapa3_aime/tabela_comparativa_6_obras.tex` e dos CSVs.

## 4. Catálogo novo: os 12 campos próprios de AIME

A tabela `tab:aime_catalogo_novo` (em `outputs/etapa3_aime/tabela_aime_catalogo_novo.tex`) consolida os 12 campos novos:

| Campo | n | freq./10k | variantes top |
|---|---:|---:|---|
| `trajectory_pass` | 433 | 22,27 | `continuity` (92), `hiatus` (65), `trajectory` (61), `discontinuities` (50), `leap` (40) |
| `moderns` | 397 | 20,42 | `Moderns` (315), `modernization` (30), `modernism` (27), `modernity` (13), `modernizing` (12) |
| `domain_category` | 281 | 14,45 | `crossing` (99), `domain` (64), `category mistake` (43), `domains` (28), `category mistakes` (25) |
| `experience` | 276 | 14,19 | `experience` (233), `experiences` (21), `empirical` (16), `experienced` (5), `experiential` (1) |
| `institution` | 227 | 11,67 | `institution` (107), `institutions` (85), `instituted` (16), `institute` (13), `instituting` (5) |
| `modes_of_existence` | 167 | 8,59 | `mode of existence` (80), `modes of existence` (69), e variantes de quebra de linha |
| `alteration` | 112 | 5,76 | `alteration` (53), `being-as-other` (28), `alterations` (17), `altered` (7), `altering` (2) |
| `felicity` | 92 | 4,73 | `felicity` (64), `infelicity` (28) |
| `diplomacy` | 84 | 4,32 | `diplomacy` (20), `diplomatic` (17), `negotiations` (11), `negotiate` (8), `negotiation` (8) |
| `preposition` | 71 | 3,65 | `prepositions` (41), `preposition` (27), `prepositional` (3) |
| `gaia` | 52 | 2,67 | `gaia` (17), `ecology` (11), `climate` (8), `climatologist` (6), `ecological` (4) |
| `values` | 22 | 1,13 | `qualify` (15), `value system` (4), `qualify values` (3) |

Total dos 12 campos: 2.214 ocorrências.

**Exemplos KWIC dos cinco campos mais densos:**

1. `trajectory_pass`: `"the [net] type plus a particular relation between continuities and discontinuities (41). Thanks to a third type of pass..."` (Cap. 1, sumário). Vocabulário próprio do livro para descrever os modos como tipos de movimento descontínuo.

2. `moderns`: `"An Inquiry into Modes of Existence. An Anthropology of the Moderns. Bruno Latour, translated by Catherine Porter, Harvard..."` (página de rosto). O substantivo `Moderns` (capitalizado) é a designação central do livro para o que ele investiga.

3. `domain_category`: `"fieldwork among the Moderns (28) without respecting domain boundaries, thanks to the notion of actor-network..."` (Cap. 1). O vocabulário da crítica à confusão entre modos opera em torno de `domain`, `crossing` e `category mistake`.

4. `experience`: `"it becomes a hypothesis too contrary to experience (116) and the magic of rationalism vanishes (117)"`. Vocabulário pragmatista que ancora a investigação. Alta polissemia esperada (vide § 8).

5. `institution`: `"Trusting Institutions Again?"` (Introdução). O `instituir` que AIME propõe como gesto político-cosmopolítico.

A leitura quantitativa indica que o vocabulário **novo** de AIME é tão denso quanto o vocabulário **antigo** (catálogo antigo soma 1.343 ocorrências, catálogo novo soma 2.214). A operação teórica do livro não é deslocamento total nem continuidade simples: é justaposição. AIME continua mobilizando o vocabulário da TAR e dos livros monográficos (em densidades intermediárias) e acrescenta uma camada figural própria, dominada por `trajectory_pass` e `moderns`.

## 5. Desambiguação militar em AIME

A desambiguação automática (aplicada via `scripts/15_etapa2_desambiguar_militar.py`) sobre as 129 ocorrências brutas do campo `militar` em AIME produziu a seguinte distribuição:

| Categoria | n | % |
|---|---:|---:|
| `figurativo` | 123 | 95,3 |
| `metalinguistico` | 4 | 3,1 |
| `descritivo_historico` | 2 | 1,6 |
| `descritivo_bibliografico` | 0 | 0,0 |
| `conceitual_debate` | 0 | 0,0 |

A contagem refinada figural: **n=123, densidade 6,33/10k**. A tabela `tab:militar-refinado-6-obras` (em `outputs/etapa3_aime/tabela_militar_refinada_6_obras.tex`) consolida o campo militar refinado nas seis obras:

| Obra | Palavras | Bruta n | Bruta /10k | Refinada n | Refinada /10k |
|---|---:|---:|---:|---:|---:|
| *Laboratory Life* 1986 | 105.749 | 39 | 3,69 | 37 | 3,50 |
| *Science in Action* 1987 | 139.861 | 374 | 26,74 | 364 | **26,03** |
| *Pandora's Hope* 1999 | 128.001 | 212 | 16,56 | 156 | **12,19** |
| *Clarifications* 1996 | 7.848 | 3 | 3,82 | 0 | 0,00 |
| *Recalling ANT* 1999 (bis) | 4.825 | 2 | 4,15 | 0 | 0,00 |
| **AIME 2013** | 194.454 | 129 | 6,63 | **123** | **6,33** |

Inspeção amostral de 12 das 123 ocorrências classificadas como `figurativo` (com `seed=42`): confirmei que o uso militar em AIME é predominantemente figural, mas **em registro deslocado** em relação ao dos livros monográficos solo. Onde *Science in Action* mobilizava `ally`/`mobilise`/`enroll`/`battle` para descrever a prática científica em si, AIME mobiliza o mesmo vocabulário em torno de modos cosmopolíticos: o título do Cap. 14 é `"Mobilizing the Beings of Passionate Interest"` (modo `[ATT]`, atração econômica), e ocorrências como `"battles have ceased for want of combatants"` ou `"for new wars a new peace"` operam em registro evocativo-cosmopolítico, no horizonte do `Gaia` e da `diplomacy`. A figuralidade militar permanece, mas dirigida a outro objeto.

Os 4 casos `metalinguistico` (Latour cita o próprio vocabulário militar para tematizá-lo) e os 2 `descritivo_historico` (alusões a guerras nomeadas) são marginais. A categoria `descritivo_bibliografico` e `conceitual_debate` ficam zeradas, sinal de que AIME, mesmo com aparato bibliográfico extenso, não concentra ocorrências militares em rodapé ou em polêmicas teóricas explícitas.

## 6. Cocorrência em AIME

Cocorrência computada sobre os 31 campos (19 antigos + 12 novos), com 3.557 ocorrências válidas. Duas configurações:

- Janela 200 palavras (controle, consistente com as obras monográficas).
- Janela proporcional **0,02%** das palavras totais = **39 palavras**. Ajuste documentado em `docs/decisoes_metodologicas.md` § Etapa 3: a janela proporcional padrão de 2% daria ~3.880 palavras para AIME, alta demais para significância analítica em cocorrência KWIC.

### Top 10 pares por força de cocorrência (j=200)

| Par | n (j=200) | n (j=39) |
|---|---:|---:|
| `topologia`–`trajectory_pass` | 584 | 205 |
| `network`–`topologia` | 379 | 91 |
| `network`–`trajectory_pass` | 301 | 54 |
| `domain_category`–`topologia` | 285 | 53 |
| `domain_category`–`trajectory_pass` | 276 | 33 |
| `domain_category`–`network` | 264 | 70 |
| `experience`–`moderns` | 243 | 56 |
| `network`–`textil` | 236 | 93 |
| `institution`–`moderns` | 212 | 48 |
| `moderns`–`topologia` | 201 | 37 |

O par dominante em AIME é `topologia`–`trajectory_pass`, articulação inédita: o vocabulário topológico do catálogo antigo se conecta com o vocabulário de movimento descontínuo do catálogo novo (`continuity`, `hiatus`, `discontinuities`, `leap`). Esse é o achado central da cocorrência: a malha figural de AIME se estrutura em torno do par topologia+trajetória/passe, com `network` e `domain_category` como satélites.

### Pares envolvendo `modes_of_existence`

| Par | j=200 | j=39 |
|---|---:|---:|
| `modes_of_existence`–`trajectory_pass` | 143 | 41 |
| `modes_of_existence`–`topologia` | 133 | 26 |
| `modes_of_existence`–`moderns` | 97 | 22 |
| `modes_of_existence`–`domain_category` | 88 | 22 |
| `modes_of_existence`–`experience` | 82 | 11 |
| `modes_of_existence`–`institution` | 75 | 14 |
| `modes_of_existence`–`network` | 68 | 15 |
| `modes_of_existence`–`textil` | 61 | 11 |
| `modes_of_existence`–`alteration` | 48 | 16 |
| `modes_of_existence`–`felicity` | 42 | 14 |
| `modes_of_existence`–`preposition` | 35 | 8 |
| `modes_of_existence`–`values` | 7 | 1 |

O conceito central do livro (`modes_of_existence`) se articula sobretudo com `trajectory_pass`, `topologia`, `moderns` e `domain_category`. A baixa cocorrência com `preposition` (35) e com `values` (7) é registro a documentar: embora as preposições orientem cada modo e os modos existam para qualificar valores (cf. Cap. 1), no nível da cocorrência KWIC os três campos aparecem em distribuição mais dispersa do que se esperaria pela leitura conceitual. Esse achado é registro documentado; a interpretação fica para a tese.

### Pares envolvendo `diplomacy`

| Par | j=200 | j=39 |
|---|---:|---:|
| `diplomacy`–`moderns` | 124 | 29 |
| `diplomacy`–`institution` | 87 | 17 |
| `diplomacy`–`militar` | 55 | 9 |
| `diplomacy`–`experience` | 42 | 3 |
| `diplomacy`–`gaia` | 35 | 5 |
| `diplomacy`–`domain_category` | 34 | 2 |
| `diplomacy`–`modes_of_existence` | 26 | 6 |
| `diplomacy`–`topologia` | 18 | 4 |
| `diplomacy`–`network` | 17 | 2 |

A diplomacia se articula com `moderns`, `institution` e, em terceiro lugar, com `militar` (55 cocorrências na janela 200). A proximidade entre o vocabulário diplomático e o vocabulário militar em AIME é dado documentado, e ressoa com a leitura amostral das ocorrências `figurativo` do campo militar: a "diplomacia" como categoria operatória de AIME convive em vizinhança com o vocabulário militar, não o elimina; o ressignifica como passagem para o registro cosmopolítico.

### Pares envolvendo `network`

| Par | j=200 | j=39 |
|---|---:|---:|
| `network`–`topologia` | 379 | 91 |
| `network`–`trajectory_pass` | 301 | 54 |
| `domain_category`–`network` | 264 | 70 |
| `network`–`textil` | 236 | 93 |
| `moderns`–`network` | 158 | 25 |
| `experience`–`network` | 108 | 15 |
| `institution`–`network` | 107 | 17 |
| `modes_of_existence`–`network` | 68 | 15 |
| `militar`–`network` | 45 | 6 |

`network` mantém em AIME a centralidade que tinha nos artigos metateóricos: lidera com `topologia` (379), articula-se com `trajectory_pass` (301) e com `domain_category` (264). A malha topológica não se desfaz com a virada para os modos; o `[net]` permanece nó da rede figural mesmo quando se torna um modo entre quinze.

### Pares envolvendo `militar`

| Par | j=200 | j=39 |
|---|---:|---:|
| `militar`–`moderns` | 144 | 25 |
| `militar`–`institution` | 78 | 19 |
| `militar`–`topologia` | 78 | 13 |
| `militar`–`experience` | 73 | 6 |
| `militar`–`diplomacy` | 55 | 9 |
| `militar`–`gaia` | 45 | 7 |
| `militar`–`network` | 45 | 6 |
| `militar`–`trajectory_pass` | 45 | 5 |
| `militar`–`domain_category` | 36 | 3 |
| `militar`–`textil` | 35 | 6 |

A topologia da cocorrência do `militar` confirma o registro deslocado: em AIME, o vocabulário militar não está periférico (ele articula em 144 cocorrências com `moderns`, o termo mais frequente do catálogo novo), mas tampouco está no centro como nos livros monográficos solo. Articula-se sistematicamente com `moderns`, `institution`, `topologia`, `experience`, `diplomacy` e `gaia`. A constelação `militar`–`diplomacy`–`gaia`–`moderns` é a articulação cosmopolítica do livro.

## 7. Síntese: AIME na trajetória 1986-2013

Três parágrafos costurando a posição de AIME na trajetória.

### 7.1. AIME mantém o vocabulário têxtil-topológico dos artigos metateóricos e o estende

A densidade do campo `topologia` em AIME (26,43/10k) coloca o livro no patamar dos livros monográficos solo (34,68 em Sci. Action; 27,58 em Pandora), e abaixo das densidades extraordinárias dos artigos (150,36 em *Clarifications*; 99,48 no *Recalling* bis), que são valores inflados pela brevidade dos artigos. O campo `network` em AIME (13,11/10k) é o mais alto dos quatro livros do corpus (4,26 em Lab Life, 9,08 em Sci. Action, 2,73 em Pandora) e fica em ordem de grandeza intermediária entre os livros e os artigos. O campo `textil` em AIME (10,34/10k) também fica em densidade comparável à dos livros monográficos solo (7,94 e 8,20). A leitura quantitativa indica continuidade do vocabulário têxtil-topológico, com reorganização interna: as variantes top do `topologia` em AIME são `path` e `trajectory`, em articulação com o campo novo `trajectory_pass`, que constitui o eixo de movimento próprio do livro.

### 7.2. O vocabulário militar-industrial reentra em AIME em registro deslocado

A contagem refinada figural do `militar` em AIME (6,33/10k, 123 ocorrências em 95,3% das 129 brutas) está em patamar intermediário entre os artigos metateóricos (0,00) e os livros monográficos solo (12,19 em Pandora, 26,03 em Sci. Action). A reentrada é moderada, e a inspeção amostral confirma que ela está em **registro deslocado**: as ocorrências militares em AIME articulam-se com `moderns` (144 cocorrências em j=200), `institution` (78), `diplomacy` (55) e `gaia` (45), formando uma constelação cosmopolítico-diplomática distinta da constelação descritivo-agonística que dominava os livros de 1987 e 1999. O título do Capítulo 14, `"Mobilizing the Beings of Passionate Interest"`, é exemplar: `mobilizing`, termo central do campo militar nos livros monográficos (28 ocorrências em Sci. Action no campo `enrollment`), aparece em AIME para descrever o que o modo `[ATT]` faz com `Beings of Passionate Interest`. O vocabulário militar volta, mas o objeto militarmente descrito muda.

### 7.3. AIME redistribui o trabalho figurativo em três camadas

A análise mostra que AIME redistribui o trabalho figurativo entre três camadas. A primeira camada é a do vocabulário **antigo** persistente (catálogo de 19 campos, 1.343 ocorrências em AIME): `topologia`, `network`, `textil`, `militar`, `construction`, `articulation`, `translation`, `inscription`, `immutable_mobile`, `actor_network` em densidades intermediárias. A segunda camada é o vocabulário **novo** específico do livro (catálogo de 12 campos, 2.214 ocorrências em AIME): `trajectory_pass`, `moderns`, `domain_category`, `experience`, `institution`, `modes_of_existence`, `alteration`, `felicity`, `diplomacy`, `preposition`, `gaia`, `values`. A terceira camada é a articulação entre as duas, evidenciada pela cocorrência: o par dominante `topologia`–`trajectory_pass` (584 em j=200) costura o léxico antigo ao novo, e os pares `domain_category`–`topologia` (285), `domain_category`–`network` (264) e `network`–`trajectory_pass` (301) sustentam a malha figural integrada do livro. Em relação à divisão de trabalho metafórico por gênero textual estabelecida pela Etapa 2 (livros monográficos solo = militar; artigos metateóricos = têxtil-topológico), AIME ocupa posição **intermediária e integradora**: é livro monográfico (formalmente), mas em registro metateórico (Latour reescreve seu próprio vocabulário), e a contagem mostra que o livro mantém o vocabulário militar em densidade reduzida e deslocada, sustenta o vocabulário têxtil-topológico dos artigos, e acrescenta um terceiro patamar de vocabulário próprio (modos, preposições, felicidade, alteração, diplomacia, Gaia) que nenhuma das obras anteriores tinha.

## 8. Limitações declaradas

1. **A Etapa 3 não inclui validação amostral semântica A/B/C**. As taxas de figuralidade dos 31 campos em AIME não foram aferidas em registro semântico. Pendência registrada para uma Etapa 3.6 hipotética.

2. **Polissemia dos termos do catálogo novo** carrega ruído que a validação semântica permitiria estimar. Termos especialmente polissêmicos: `experience` (233 ocorrências, parte certamente em uso comum), `crossing` (99 ocorrências, com `street crossing` e `crossover` em meio aos `category crossings` técnicos), `domain` (64 ocorrências, com possíveis usos genéricos). A contagem bruta dada aqui reflete esse ruído; a leitura interpretativa precisa considerá-lo. A inspeção qualitativa amostral das primeiras ocorrências de cada campo (vide § 4) sugere que o uso técnico do AIME domina, mas não a percentagens próximas dos 96-97% que a validação A/B/C produziu para `textil` e `topologia` em *Clarifications* (Etapa 2.6).

3. **A descoberta tardia da Etapa 2-bis** (cobertura real de 25,3% do *Recalling* na Etapa 2 original, e não os ~80% declarados) tem efeito direto na tabela comparativa 6 obras: as colunas *Recalling* nas tabelas da Etapa 3 são da versão bis (corpus integral). Os outputs da Etapa 2 original em `outputs/latour_1999_recalling_en/` permanecem intocados, mas a tabela da Etapa 3 usa o *Recalling* bis para preservar a integridade da comparação.

4. **AIME tem 194.454 palavras**, ~40% maior que cada um dos três livros monográficos anteriores. As densidades por 10.000 palavras são comparáveis sem ajuste adicional. A janela proporcional da cocorrência precisou ser ajustada (0,02% em vez de 2%), conforme briefing § Passo 6, para manter ordem de grandeza analítica.

5. **A pista do par `circulating_reference`–`topologia`** identificada na Etapa 2-bis (9 cocorrências na j=97 do *Recalling* bis) não se mantém em AIME: o campo `circulating_reference` zera em AIME (0 ocorrências, contra 18 em Pandora e 2 no *Recalling* bis). O vocabulário fluido-circulatório dos textos pós-1996 não é central em AIME, que mobiliza um vocabulário de fluxo distinto (`trajectory_pass` e a articulação topologia+modernos). Registro o achado documentadamente, sem desenvolver interpretação que excederia o que a contagem mostra; a leitura interpretativa fica para a tese.

## 9. Outputs gerados

- `corpus/txt_fornecido/latour_2013_aime_en.txt` (entrada).
- `corpus/txt_norm/latour_2013_aime_en.txt` (normalizado).
- `campos_lexicais/catalogo_termos_aime.yaml` (catálogo novo, 12 campos).
- `outputs/etapa3_aime/`:
  - `txt_hashes.txt`
  - `normalizacao_aplicada.md`
  - `verificacao_passagens.md`
  - `militar_classificacao_automatica.csv`
  - `cocorrencia_top_pares.md`
  - `tabela_comparativa_6_obras.tex`
  - `tabela_aime_catalogo_novo.tex`
  - `tabela_militar_refinada_6_obras.tex`
  - `relatorio_etapa3.md` (este arquivo)
- `outputs/latour_2013_aime_en/`:
  - `csv/kwic_catalogo_antigo.csv` (1.343 ocorrências dos 19 campos antigos).
  - `csv/kwic_catalogo_aime.csv` (2.214 ocorrências dos 12 campos novos).
  - `csv/frequencias_catalogo_antigo.csv`
  - `csv/frequencias_catalogo_aime.csv`
  - `csv/cocorrencia_j200.csv`, `cocorrencia_jprop.csv`
  - `figuras/rede_cocorrencia_j200.{png,svg}`, `rede_cocorrencia_jprop.{png,svg}`
  - `relatorios/frequencias.md`, `cocorrencia_j200.md`, `cocorrencia_jprop.md`
- `scripts/22_etapa3_aime_pipeline.py` (pipeline da Etapa 3).
