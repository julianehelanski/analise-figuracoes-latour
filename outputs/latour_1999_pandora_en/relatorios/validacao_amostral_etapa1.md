# Amostra estratificada de validação: latour_1999_pandora_en

Seed = 42. Estratos = inicio_capitulo, corpo, notas_fim, paratexto, qualidade_baixa. N por estrato = 3.

Use este documento como guia de leitura ao percorrer o PDF. Codifique cada página no CSV `amostra_validacao.csv`:

- `estrato_correto`: o estrato atribuído pelo algoritmo é correto? (sim/nao/parcial)
- `classe_correta`: a classe específica predita é correta? (sim/nao/parcial)
- `erro_extracao`: caracteres corrompidos, palavras coladas, linhas misturadas?
- `decisao_metodologica`: qualquer observação a registrar.

Se a taxa de erro em um estrato passar de 20%, ajustar a heurística correspondente em `scripts/01_extract_text.py` e reprocessar.

## Estrato: `corpo`

### Página 2

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 23

**Início da página:**

> ' PANDORA S HOPE ESSAYS ON THE REALITY OF SCIENCE STUDIES Bruno Latour HARVARD UNIV ERSITY PRESS Cambridge, Massachusetts London, England 1 999

**Meio:**

> ESSAYS ON THE REALITY OF SCIENCE STUDIES Bruno Latour HARVARD UNIV ERSITY PRESS Cambridge, Massachusetts London, England 1 999

**Fim:**

> ' PANDORA S HOPE ESSAYS ON THE REALITY OF SCIENCE STUDIES Bruno Latour HARVARD UNIV ERSITY PRESS Cambridge, Massachusetts London, England 1 999

### Página 4

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 13

**Início da página:**

> To Shirley Strum, Donna Haraway, Steve Glickman, and their baboons, cyborgs, and hyenas

**Meio:**

> To Shirley Strum, Donna Haraway, Steve Glickman, and their baboons, cyborgs, and hyenas

**Fim:**

> To Shirley Strum, Donna Haraway, Steve Glickman, and their baboons, cyborgs, and hyenas

### Página 3

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 68

**Início da página:**

> Copyright © 1999 by the President and Fellows of Harvard College All rights reserved Printed in the United States of America LIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Latour, Bruno. Pandora's hope: essays on the reality of science studies I Bruno Latour p. cm. Includes b...

**Meio:**

> All rights reserved Printed in the United States of America LIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Latour, Bruno. Pandora's hope: essays on the reality of science studies I Bruno Latour p. cm. Includes bibliographical references and index. ISBN 0-674-65335-1 (alk:. pa...

**Fim:**

> ed in the United States of America LIBRARY OF CONGRESS CATALOGING-IN-PUBLICATION DATA Latour, Bruno. Pandora's hope: essays on the reality of science studies I Bruno Latour p. cm. Includes bibliographical references and index. ISBN 0-674-65335-1 (alk:. paper). - ISBN 0-674-65336-...

## Estrato: `paratexto`

### Página 126

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 438

**Início da página:**

> FROM FAB R I C ATI O N TO REALITY 11 5 weapons in a polarized battle against truth and reality. All too often the implication is that if something is fabricated it is false ; likewise, if it is constructed it must also be deconstructible. These are the main reasons why the more w...

**Meio:**

> own to us, if we really wish to understand sci ence in action. This reconfiguration is what I hope to accomplish in this chapter by visiting yet another empirical site, this time Louis Pas teur's laboratory. Let us follow in some detail the "Memoire sur la fer mentation appelee l...

**Fim:**

> umans? Thus to the ontological drama is added an epistemological one. We will be able to see, using Pasteur's own words, how a scientist solves for himself and for us two of the ba sic problems of science studies. First let us turn to the uplifting story of Cinderella-the-yeast. ...

### Página 265

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 469

**Início da página:**

> PA N D O R A ' S HOPE 2 54 impossible requirements-the whole thing ending, as we know, in the afterworld of shadows. Quite a feat ! And one that, in my view, should be met with grinding of teeth rather than cheers of admiration. Gorgias, the first to enter the scene, is easily pa...

**Meio:**

> ed an enormously long conditioning to see this question as crucially important. Even if morality were taken as nothing more than a sort of basic ethological aptitude of primates in groups, it would still be pretty close to such an assessment. The only thing Socrates adds to turn ...

**Fim:**

> g we do is the opposite of what you imply we should be doing" (481c) . It is great luck for Socrates that Plato hands him foils like this one, because, without the Sophists' indignation, what Socrates says and what the common people say would be undistinguishable. As is usual wit...

### Página 316

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 414

**Início da página:**

> GLOSSARY 305 CONCRESCENCE: A term employed by Whitehead to designate an event* without using the Kantian idiom of the phenomenon*. Concrescence is not an act of knowledge applying human categories to indifferent stuff out there but a modification of all the components or circumst...

**Meio:**

> f the hu man position in the world but a recentering of the object around the human ability to know. The expression "counter-Copernican revolution" thus com bines two metaphors, one from astronomy and one from political upheaval, to refer to the movement away from all sorts of an...

**Fim:**

> use the word "differentiation" instead. Differentiation does not require the generation of one normative distinction between science and nonscience, but allows for many differences, making possible a much finer normative judgment that does not rely on the weaknesses of the modern...

## Estrato: `qualidade_baixa`

### Página 1

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 0

**Início da página:**

> 

**Meio:**

> 

**Fim:**

> 

### Página 336

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 0

**Início da página:**

> 

**Meio:**

> 

**Fim:**

> 

### Página 5

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 0

**Início da página:**

> 

**Meio:**

> 

**Fim:**

> 
