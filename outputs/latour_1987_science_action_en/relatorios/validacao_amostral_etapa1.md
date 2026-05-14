# Amostra estratificada de validação: latour_1987_science_action_en

Seed = 42. Estratos = inicio_capitulo, corpo, notas_fim, paratexto, qualidade_baixa. N por estrato = 3.

Use este documento como guia de leitura ao percorrer o PDF. Codifique cada página no CSV `amostra_validacao.csv`:

- `estrato_correto`: o estrato atribuído pelo algoritmo é correto? (sim/nao/parcial)
- `classe_correta`: a classe específica predita é correta? (sim/nao/parcial)
- `erro_extracao`: caracteres corrompidos, palavras coladas, linhas misturadas?
- `decisao_metodologica`: qualquer observação a registrar.

Se a taxa de erro em um estrato passar de 20%, ajustar a heurística correspondente em `scripts/01_extract_text.py` e reprocessar.

## Estrato: `inicio_capitulo`

### Página 1

- classe_predita: `inicio_capitulo`, qualidade_predita: `boa`, n_palavras: 307

**Início da página:**

> Contents ...................................................................................................................................... 4 Acknowledgements .................................................................................................................... ...

**Meio:**

> .......... 148 CHAPTER 4. Insiders Out ..................................................................................................... 161 Part A. Interesting others in the laboratories ...................................................................... 162 Part B. Count...

**Fim:**

> ......................... 286 Chapter 5 ............................................................................................................................ 288 Chapter 6 ........................................................................................................

## Estrato: `corpo`

### Página 2

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 78

**Início da página:**

> SCIENCE IN ACTION How to follow scientists and engineers through society Bruno Latour Harvard University Press Cambridge, Massachusetts Copyright (c) 1987 by Bruno Latour All rights reserved Printed in the United States of America Eleventh printing, 2003 Library of Congress Catal...

**Meio:**

> paper)

**Fim:**

> SCIENCE IN ACTION How to follow scientists and engineers through society Bruno Latour Harvard University Press Cambridge, Massachusetts Copyright (c) 1987 by Bruno Latour All rights reserved Printed in the United States of America Eleventh printing, 2003 Library of Congress Catal...

### Página 3

- classe_predita: `corpo`, qualidade_predita: `boa`, n_palavras: 9

**Início da página:**

> To Michel Callon, this outcome of a seven-year discussion

**Meio:**

> To Michel Callon, this outcome of a seven-year discussion

**Fim:**

> To Michel Callon, this outcome of a seven-year discussion

## Estrato: `paratexto`

### Página 307

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 107

**Início da página:**

> logging 226, 255 logical, 204-205, consequence of a text 58, breach from logic 191 et seq., from form to content 196-202 logistics 234 et seq. Luria S. 196-197 Lyell C. 146 et seq., 157 Machiavelli 124-125, 128 machine 129 et seq., 253 et seq. Marey J. 92, 230 mathematics 237 et ...

**Meio:**

> , 204-205, consequence of a text 58, breach from logic 191 et seq., from form to content 196-202 logistics 234 et seq. Luria S. 196-197 Lyell C. 146 et seq., 157 Machiavelli 124-125, 128 machine 129 et seq., 253 et seq. Marey J. 92, 230 mathematics 237 et seq. Mead M. 84, 109-110...

**Fim:**

> a text 58, breach from logic 191 et seq., from form to content 196-202 logistics 234 et seq. Luria S. 196-197 Lyell C. 146 et seq., 157 Machiavelli 124-125, 128 machine 129 et seq., 253 et seq. Marey J. 92, 230 mathematics 237 et seq. Mead M. 84, 109-110 Mendeleev 235-236, 241-24...

### Página 221

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 584

**Início da página:**

> In the examples above, each conflict about what is associated to what traces what the world of the other people is made of. We do not have on the one hand 'knowledge' and on the other 'society'. We have many trials of strength through which are revealed which link is solid and wh...

**Meio:**

> is that 'flifli' has not got a chance of surviving if the girl is to live with English-speaking people. Bulmer, in the second story, is doing exactly the same thing as the little girl. He is learning both the Karam's language and society by testing the strength of the association...

**Fim:**

> made kobtiy stand apart from all the birds - especially because other New Guinea tribes were putting it in the category of birds like all Western taxonomists. But he slowly learned that so much was attached to this animal by the Karam that they could not change their taxonomy wit...

### Página 20

- classe_predita: `paratexto`, qualidade_predita: `boa`, n_palavras: 449

**Início da página:**

> 'Of course,' says the left side of Janus, 'everyone is convinced because Jim and Francis stumbled on the right structure. The DNA shape itself is enough to rally everyone.' 'No, says the right side, every time someone else is convinced it progressively becomes a more right struct...

**Meio:**

> appear strong once the structure is blackboxed. As long as it is not, Jim and Francis are still struggling to recruit them, modifying the DNA structure until everyone is satisfied. When they are through, they will follow the advice of Janus's right side. As long as they are still...

**Fim:**

> ys missing to close the black box once and for all. Until the last minute Eagle can fail if West is not careful enough to keep the Software people interested, to maintain the pressure on the debugging crew, to advertise the machine to the marketing department. (3) The first rule ...

## Estrato: `qualidade_baixa`

### Página 72

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 26

**Início da página:**

> 2. kolonne: A.C M-(A.C) M+(A.C) H(A.C) Frontline 3. kolonne: A.D M-(A.D) Frontline 4. kolonne E.D M-(E.D) M+(E.D) H(E.D) Frontline 5. kolonne: E.F M-(E.F) M+(E.F) H(E.F) E.F

**Meio:**

> . kolonne: A.C M-(A.C) M+(A.C) H(A.C) Frontline 3. kolonne: A.D M-(A.D) Frontline 4. kolonne E.D M-(E.D) M+(E.D) H(E.D) Frontline 5. kolonne: E.F M-(E.F) M+(E.F) H(E.F) E.F

**Fim:**

> 2. kolonne: A.C M-(A.C) M+(A.C) H(A.C) Frontline 3. kolonne: A.D M-(A.D) Frontline 4. kolonne E.D M-(E.D) M+(E.D) H(E.D) Frontline 5. kolonne: E.F M-(E.F) M+(E.F) H(E.F) E.F

### Página 314

- classe_predita: `qualidade_baixa`, qualidade_predita: `baixa`, n_palavras: 0

**Início da página:**

> 

**Meio:**

> 

**Fim:**

> 
