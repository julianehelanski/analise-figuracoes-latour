# Amostra estratificada de validação: latour_woolgar_1986_lab_life_en

Seed = 42. Estratos = inicio_capitulo, corpo, notas_fim, paratexto, qualidade_baixa. N por estrato = 3.

Use este documento como guia de leitura ao percorrer o PDF. Codifique cada página no CSV `amostra_validacao.csv`:

- `estrato_correto`: o estrato atribuído pelo algoritmo é correto? (sim/nao/parcial)
- `classe_correta`: a classe específica predita é correta? (sim/nao/parcial)
- `erro_extracao`: caracteres corrompidos, palavras coladas, linhas misturadas?
- `decisao_metodologica`: qualquer observação a registrar.

Se a taxa de erro em um estrato passar de 20%, ajustar a heurística correspondente em `scripts/01_extract_text.py` e reprocessar.

## Estrato: `corpo`

### Página 2

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 2

**Início da página:**

> LABORATORY LIFE

**Meio:**

> LABORATORY LIFE

**Fim:**

> LABORATORY LIFE

### Página 5

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 93

**Início da página:**

> Published by Princeton University Press, 41 William Street, Princeton, New Jersey 08540 In the United Kingdom: Princeton University Press, Chichester, West Sussex Copyright © 1979 by Sage Publications, Inc. Copyright © 1986 by Princeton University Press All rights reserved LCC 85...

**Meio:**

> ceton University Press, 41 William Street, Princeton, New Jersey 08540 In the United Kingdom: Princeton University Press, Chichester, West Sussex Copyright © 1979 by Sage Publications, Inc. Copyright © 1986 by Princeton University Press All rights reserved LCC 85-43378 ISBN 0-692...

**Fim:**

> ress, 41 William Street, Princeton, New Jersey 08540 In the United Kingdom: Princeton University Press, Chichester, West Sussex Copyright © 1979 by Sage Publications, Inc. Copyright © 1986 by Princeton University Press All rights reserved LCC 85-43378 ISBN 0-692-09418-7 Princeton...

### Página 3

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 5

**Início da página:**

> This page intentionally left blank

**Meio:**

> This page intentionally left blank

**Fim:**

> This page intentionally left blank

## Estrato: `paratexto`

### Página 135

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 399

**Início da página:**

> 134 LABORATORY LIFE confirmed work by Guillemin. For example, one of Guillemin's papers contains the comment that "this paper [reference to a paper by Schally's group] confirmed our former hypothesis." Such differences are too striking to be interpreted simply as differences in c...

**Meio:**

> t be a simple polypeptide" (Burgus et al., 1966)-was borrowed as a quasi-fact in Schally's 1966 paper: "purified materials appear not to be a simple polypeptide since amino acids account for only 30% of its composition" (Schally et al., 1968). As we have already noted, a low conc...

**Fim:**

> atement was to seem extraordinary (see below). In 1966, Guillemin did not believe Schally's findings. It is also clear however, that Schally did not believe his own findings. Thus, Schally, wrote at the end of his 1966 paper: The results are consistent with a hypothesis that TRF ...

### Página 124

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 434

**Início da página:**

> The Construction of a Fact 123 as "gratuitous affirmation," "assays not specific enough anymore," "not really demonstrated," and "unreliable" are common. By contrast, Guillemin's group's first( 1962) paper was widely acclaimed(for example, it was said to be the "first uncontrover...

**Meio:**

> roper experiments but at that time it was very difficult to get hypothalami . . . he had to do it himself; no one realised that you need not 200 of them, but 20,000 of them . . . he then realised he simply could not compete . . . also you could not obtain radioactive iodine of hi...

**Fim:**

> ical research . . . There was a span of 5 or 7 years before we could work again, and not only conditioned reflexes (Anonymous, 1976b). This provides an example of the perceived influence of macrosociological factors on the field, rather than that of multiple fine social determina...

### Página 80

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 450

**Início da página:**

> An Anthropologist Visits the Laboratory 79 (or the lack of it). Basic relationships are thus embedded within appeals to "what is generally known" or to "what might reasonably be thought to be the case.'' The modalities in type 2 statements sometimes take the form of tentative sug...

**Meio:**

> in goldfish the hypothalamus has an inhibitory effect on the secretion of TSH. There is also this guy in Colorado. They claim that t h e y have got a precursor for H . . . . I just got the preprint of t h e i r paper ( I I I , 70). It may also signify that not everything seen, sa...

**Fim:**

> pond to changes in facticity seems plausible enough. At the level of empirical verification, however, this general scheme encounters certain d i f f i c u l t i e s . In any given instance, there seems to be no simple r e l a t i o n s h i p between the form of a statement and th...

## Estrato: `qualidade_baixa`

### Página 47

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 0

**Início da página:**

> 

**Meio:**

> 

**Fim:**

> 

### Página 226

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 1

**Início da página:**

> 225

**Meio:**

> 225

**Fim:**

> 225

### Página 296

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 0

**Início da página:**

> 

**Meio:**

> 

**Fim:**

> 
