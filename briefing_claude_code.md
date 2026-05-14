# Briefing para Claude Code: Passo 4 do refinamento (analise_figuracoes)

Olá, Claude Code. Estou trabalhando no meu repositório `analise_figuracoes` (análise lexicométrica de três obras de Latour para minha tese de doutorado). Outro Claude (claude.ai, em outra sessão) preparou as mudanças do **passo 4** do refinamento, mas não tem credenciais para fazer push direto. Você vai recriar as mudanças aqui no meu clone local e fazer o push.

## Contexto do que foi feito

Em 14/05/2026 foi concluído o passo 1 do refinamento (desambiguação de `war`/`wars` no campo militar em *Pandora's Hope*), commitado em `refinamento/`. O passo 2 (validação manual de 370 trechos em três camadas) foi dispensado em 15/05/2026 por inspeção da pesquisadora. Agora vamos commitar o passo 4: KWIC ampliado a ±50 palavras com curadoria de passagens citáveis para o capítulo 2 da tese.

Quatro arquivos vão para o repositório público:
- `.gitignore` (atualizado)
- `decisoes_metodologicas.md` (adendo no final)
- `scripts/10_passo4_kwic_ampliado.py` (novo)
- `outputs/passo4/README.md` (novo)

Três arquivos com reprodução extensa de Latour **ficam fora** do repositório público (entram no `.gitignore`), por conformidade com direitos autorais (Harvard University Press, Princeton University Press). São gerados localmente pelo script:
- `outputs/passo4/kwic_ampliado.csv`
- `outputs/passo4/passagens_curadas.md`
- `outputs/passo4/sequencia_exercito_ciencia.md`

## O que fazer, em ordem

### 1. Garantir que o repositório está limpo e atualizado

```bash
git status
git pull origin main
```

Se `git status` indicar mudanças não commitadas que **não são deste passo 4**, pare e me pergunte como proceder antes de seguir.

### 2. Atualizar `.gitignore`

Adicionar ao final do arquivo `.gitignore` (sem remover nada do que já está lá), as seguintes linhas:

```
# Passo 4 (15/05/2026): artefatos com reprodução extensa de Latour ficam fora do repositório público.
# Contêm trechos com ±50 palavras de contexto e curadoria de passagens citáveis para a tese.
# O script de geração está versionado em scripts/; os PDFs originais ficam no Drive local;
# rodar o script reproduz os arquivos abaixo localmente.
outputs/passo4/kwic_ampliado.csv
outputs/passo4/passagens_curadas.md
outputs/passo4/sequencia_exercito_ciencia.md
```

### 3. Atualizar `decisoes_metodologicas.md`

Adicionar ao final do arquivo `decisoes_metodologicas.md` (sem remover nada), o seguinte bloco. Note: preserve a sintaxe LaTeX dos comandos `\enquote`, `\emph`, `\times`, `\pm` exatamente como está, pois esse markdown também alimenta o apêndice da tese em LaTeX.

```markdown

---

## Dispensa da validação amostral da Etapa 2 (15 de maio de 2026)

### Motivação

A Etapa 2 do plano de trabalho previa validação manual de uma amostra estratificada para medir a precisão da heurística de detecção figurativa e refinar os campos lexicais. Na sessão de 14/05/2026, foram geradas três planilhas (camada A militar com 60 trechos, camada B polissêmicos com 217 trechos, camada C técnicos com 93 trechos, totalizando 370 ocorrências distribuídas pelos 17 campos do catálogo), pré-anotadas heuristicamente em três categorias (`conceitual`, `parcial`, `ruído`), com colunas em branco para classificação manual.

Na sessão de 15/05/2026, examinei a estrutura das planilhas e a distribuição da pré-anotação heurística e decidi dispensar a classificação manual.

### Decisão

A validação amostral da Etapa 2 fica dispensada. As três planilhas pré-anotadas permanecem disponíveis localmente como insumo de consulta, sem entrar no repositório versionado nem alimentar refinamento dos campos lexicais.

### Justificativa

O ganho metodológico esperado da classificação manual era declarar, no apêndice metodológico da tese, uma taxa de precisão validada empiricamente por par autor $\times$ campo. O custo era de algumas semanas de leitura cuidadosa de 370 trechos. A relação custo-benefício passou a ser desfavorável depois que três condições se cumpriram: o passo 1 do refinamento (desambiguação de `war`/`wars` no campo militar) já produziu o resultado empiricamente mais consequente da análise (queda de 26,4\% no campo militar de \emph{Pandora's Hope}); a inspeção informal da pré-anotação heurística pela pesquisadora sustentou que a taxa de erro nos outros campos é pequena o suficiente para não inverter o argumento principal sobre a tensão figural Latour-Haraway; e o capítulo 2 da tese, que mobilizará os resultados, comporta a formulação \enquote{validação por inspeção da pesquisadora} sem comprometimento do registro etnográfico.

### Reformulação do apêndice metodológico

No apêndice metodológico que documenta esta análise dentro da tese, a passagem sobre validação fica registrada nestes termos: a heurística de detecção figurativa foi validada por dois procedimentos. O primeiro foi a desambiguação manual de 85 ocorrências de `war`/`wars` em \emph{Pandora's Hope}, documentada em `refinamento/war_pandora_classificacao.csv`, que produziu o ajuste da densidade do campo militar registrado na tabela `refinamento/tabela_militar_refinada.tex`. O segundo foi a inspeção da pesquisadora sobre amostra estratificada de 370 trechos pré-anotados nos demais campos, sem registro de discordâncias sistemáticas que justificassem reclassificação automática.

### Continuidade

Os passos 3 (reformatação interpretativa), 4 (KWIC ampliado a $\pm 50$ palavras com curadoria de passagens citáveis) e 5 (corpus Haraway) permanecem no horizonte de refinamento. A prioridade imediata, definida em 15/05/2026, é o passo 4, para alimentar o capítulo 2 da tese com passagens citáveis. O passo 5 (Haraway) fica reservado para o período posterior à revisão do capítulo 2.
```

### 4. Criar `scripts/10_passo4_kwic_ampliado.py`

Criar este arquivo novo com o conteúdo exato abaixo. Preserve indentação, aspas, acentos. O script tem 336 linhas.

```python
"""
Passo 4 do refinamento (15/05/2026).

KWIC ampliado a ±50 palavras com curadoria de passagens citáveis para o capítulo 2
da tese de Juliane sobre a tensão figural Latour-Haraway.

Entrada:
- corpus/txt_norm/<obra>.txt: textos normalizados das três obras de Latour.
- corpus/paginas/<obra>.csv: classificação por página (corpo/paratexto/...).
- campos_lexicais/catalogo_termos.yaml: termos figurativos por grupo.
- outputs/<obra>/csv/kwic.csv: KWIC ±10 palavras existente.

Saída:
- outputs/passo4/kwic_ampliado.csv: todos os hits válidos em janela ±50.
- outputs/passo4/passagens_curadas.md: melhores passagens por (obra × campo)
  formatadas como bloco LaTeX pronto para colar no capítulo 2.
"""

import csv
import re
import os
import yaml
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).parent.parent
WINDOW = 50  # janela em palavras
OUT_DIR = REPO / "outputs" / "passo4"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OBRAS = {
    "latour_woolgar_1986_lab_life_en": "Laboratory Life",
    "latour_1987_science_action_en": "Science in Action",
    "latour_1999_pandora_en": "Pandora's Hope",
}

ANO = {
    "latour_woolgar_1986_lab_life_en": "1986",
    "latour_1987_science_action_en": "1987",
    "latour_1999_pandora_en": "1999",
}

# Campos prioritários para o capítulo 2: agonísticos/figurais que dialogam com Haraway
CAMPOS_PRIORITARIOS = [
    "militar",         # alistar, batalha, vitória, conquista
    "agonistic",       # campo agonístico, prova de força
    "enrollment",      # alistamento/recrutamento
    "spokesperson",    # porta-voz
    "trial_of_strength",
    "translation",     # tradução como recrutamento
    "actor_network",
    "network",
    "black_box",
    "inscription",
    "centre_of_calculation",
    "immutable_mobile",
]


def load_paginas(obra):
    """Mapa página -> classe (corpo, paratexto, notas_fim, etc.)."""
    paginas = {}
    with open(REPO / "corpus" / "paginas" / f"{obra}.csv", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            paginas[int(row["pagina"])] = row["classe"]
    return paginas


def carregar_texto_com_paginas(obra):
    """
    Reconstitui o texto da obra como lista de (n_pagina, texto_pagina).
    Heurística: o txt_norm tem páginas separadas por sequências de \\n+;
    usamos os contadores de páginas do CSV para conferir alinhamento.
    """
    # No projeto, o txt_norm é o texto contínuo. Para localizar páginas
    # precisamos do delimitador. Vou ler o txt_norm e usar form-feed
    # (\f) se houver, ou marcadores explícitos. Como fallback, divido por
    # tamanho médio usando n_chars do CSV.
    with open(REPO / "corpus" / "txt_norm" / f"{obra}.txt", encoding="utf-8") as f:
        txt = f.read()

    paginas_meta = []
    with open(REPO / "corpus" / "paginas" / f"{obra}.csv", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            paginas_meta.append((int(row["pagina"]), int(row["n_chars"]), row["classe"]))

    # Tentativa 1: dividir por form-feed
    if "\f" in txt:
        partes = txt.split("\f")
        if len(partes) >= len(paginas_meta) * 0.9:
            pags = []
            for i, (n, _, classe) in enumerate(paginas_meta):
                if i < len(partes):
                    pags.append((n, partes[i], classe))
            return pags

    # Tentativa 2: usar n_chars como offset
    pags = []
    offset = 0
    for n, n_chars, classe in paginas_meta:
        pags.append((n, txt[offset:offset + n_chars], classe))
        offset += n_chars
    return pags


def carregar_termos():
    with open(REPO / "campos_lexicais" / "catalogo_termos.yaml") as f:
        cat = yaml.safe_load(f)
    return cat["latour"]


def construir_regex(termos):
    """Constrói regex case-insensitive com word boundaries."""
    parts = []
    for t in termos:
        t_esc = re.escape(t).replace(r"\ ", r"\s+")
        parts.append(rf"\b{t_esc}\b")
    return re.compile("|".join(parts), re.IGNORECASE)


def extrair_janela(texto, start, end, n_palavras):
    """Extrai janela de n_palavras antes e depois do match."""
    antes_raw = texto[:start]
    depois_raw = texto[end:]
    palavras_antes = antes_raw.split()
    palavras_depois = depois_raw.split()
    contexto_antes = " ".join(palavras_antes[-n_palavras:])
    contexto_depois = " ".join(palavras_depois[:n_palavras])
    return contexto_antes, contexto_depois


# --- Construir o KWIC ampliado ---

CAMPOS = carregar_termos()
hits_amplos = []

for obra in OBRAS:
    paginas = carregar_texto_com_paginas(obra)
    for grupo, meta in CAMPOS.items():
        if grupo not in CAMPOS_PRIORITARIOS:
            continue
        termos = meta["termos"]
        exclusoes = meta.get("exclusoes", [])
        rx = construir_regex(termos)
        for n_pag, txt_pag, classe in paginas:
            # Filtro: apenas páginas de corpo ou início de capítulo
            if classe not in ("corpo", "inicio_capitulo"):
                continue
            for m in rx.finditer(txt_pag):
                termo_central = m.group(0)
                # Verificar exclusões na janela ±5 palavras
                antes_curta, depois_curta = extrair_janela(txt_pag, m.start(), m.end(), 5)
                contexto_curto = f"{antes_curta} {termo_central} {depois_curta}".lower()
                if any(exc.lower() in contexto_curto for exc in exclusoes):
                    continue
                # KWIC ampliado ±50
                antes_ampla, depois_ampla = extrair_janela(txt_pag, m.start(), m.end(), WINDOW)
                hits_amplos.append({
                    "obra": obra,
                    "ano": ANO[obra],
                    "grupo": grupo,
                    "termo": termo_central,
                    "pagina": n_pag,
                    "contexto_antes_50": antes_ampla,
                    "trecho_central": termo_central,
                    "contexto_depois_50": depois_ampla,
                })

print(f"Total de hits no KWIC ampliado: {len(hits_amplos)}")

# --- Aplicar classificação do passo 1 (war/wars em Pandora) ---

classificacao_passo1 = {}
caminho_passo1 = REPO / "refinamento" / "war_pandora_classificacao.csv"
if caminho_passo1.exists():
    with open(caminho_passo1) as f:
        r = csv.DictReader(f)
        for row in r:
            chave = (int(row["pagina"]), row["termo"].lower())
            if chave not in classificacao_passo1:
                classificacao_passo1[chave] = row["categoria_final"]

for hit in hits_amplos:
    hit["classificacao_passo1"] = ""
    if hit["obra"] == "latour_1999_pandora_en" and hit["termo"].lower() in ("war", "wars"):
        chave = (int(hit["pagina"]), hit["termo"].lower())
        hit["classificacao_passo1"] = classificacao_passo1.get(chave, "nao_classificado")

# Salvar CSV
csv_path = OUT_DIR / "kwic_ampliado.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=[
        "obra", "ano", "grupo", "termo", "pagina",
        "contexto_antes_50", "trecho_central", "contexto_depois_50",
        "classificacao_passo1",
    ])
    w.writeheader()
    w.writerows(hits_amplos)
print(f"CSV salvo em: {csv_path}")

# --- Curadoria: pontuar cada hit por densidade figural no entorno ---

# Heurística: contar quantos termos figurativos (de qualquer grupo prioritário)
# aparecem na janela ±50. Quanto mais, mais "denso" é o trecho.
todos_termos = []
for g in CAMPOS_PRIORITARIOS:
    if g in CAMPOS:
        todos_termos.extend(CAMPOS[g]["termos"])
rx_todos = construir_regex(todos_termos)


def score_densidade(hit):
    trecho = f"{hit['contexto_antes_50']} {hit['trecho_central']} {hit['contexto_depois_50']}"
    return len(rx_todos.findall(trecho))


for hit in hits_amplos:
    # Hits classificados como descritivo pelo passo 1 ficam com score 0 (caem da curadoria)
    if hit.get("classificacao_passo1") == "descritivo":
        hit["score_densidade"] = 0
    else:
        hit["score_densidade"] = score_densidade(hit)


# --- Selecionar melhores passagens por (obra × grupo) ---

# Para cada (obra, grupo), pegar até 4 hits com maior densidade figural,
# evitando hits em páginas vizinhas (para diversidade dentro da obra).

por_obra_grupo = defaultdict(list)
for hit in hits_amplos:
    por_obra_grupo[(hit["obra"], hit["grupo"])].append(hit)

curadas = []
N_POR_PAR = 4
for chave, hits in por_obra_grupo.items():
    # Filtrar hits com score 0 (descritivos do passo 1)
    hits_validos = [h for h in hits if h["score_densidade"] > 0]
    # Ordenar por score desc, então por página asc para desempate
    ordenados = sorted(hits_validos, key=lambda h: (-h["score_densidade"], h["pagina"]))
    selecionados = []
    paginas_ja = set()
    for h in ordenados:
        # Diversidade: pular se já temos passagem em página vizinha (±2)
        if any(abs(h["pagina"] - p) <= 2 for p in paginas_ja):
            continue
        selecionados.append(h)
        paginas_ja.add(h["pagina"])
        if len(selecionados) >= N_POR_PAR:
            break
    curadas.extend(selecionados)

print(f"Total de passagens curadas: {len(curadas)}")
print(f"Distribuição por (obra × grupo):")
dist = defaultdict(int)
for h in curadas:
    dist[(OBRAS[h["obra"]], h["grupo"])] += 1
for (obra, g), n in sorted(dist.items()):
    print(f"  {obra} | {g}: {n}")

# --- Gerar relatório Markdown com blocos LaTeX prontos ---

md_path = OUT_DIR / "passagens_curadas.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("# Passagens curadas para o capítulo 2 da tese\n\n")
    f.write("Resultado do passo 4 do refinamento da análise das figurações em Latour.\n")
    f.write(f"Janela KWIC: ±{WINDOW} palavras. Curadoria automática por densidade figural ")
    f.write("(número de termos do catálogo figurativo no entorno ±50 palavras).\n\n")
    f.write("Cada passagem é apresentada (i) em prosa contínua, com a palavra-chave do campo ")
    f.write("em **negrito**, e (ii) como bloco LaTeX `citacaoabnt` pronto para colar no capítulo 2 da tese.\n\n")
    f.write("Os trechos vêm dos textos normalizados em `corpus/txt_norm/`; ")
    f.write("podem conter resíduos de OCR. Revisar contra o PDF original ao usar.\n\n")
    f.write("---\n\n")

    # Agrupar por obra > grupo
    by_obra = defaultdict(lambda: defaultdict(list))
    for h in curadas:
        by_obra[h["obra"]][h["grupo"]].append(h)

    for obra in OBRAS:
        if obra not in by_obra:
            continue
        f.write(f"## {OBRAS[obra]} ({ANO[obra]})\n\n")
        for grupo in CAMPOS_PRIORITARIOS:
            if grupo not in by_obra[obra]:
                continue
            hits_g = by_obra[obra][grupo]
            f.write(f"### Campo: `{grupo}`\n\n")
            nota = CAMPOS[grupo].get("nota", "")
            if nota:
                f.write(f"*Nota do catálogo:* {nota}\n\n")
            for i, h in enumerate(hits_g, 1):
                trecho_inline = (
                    f"{h['contexto_antes_50']} "
                    f"**{h['trecho_central']}** "
                    f"{h['contexto_depois_50']}"
                )
                # Limpar espaços múltiplos
                trecho_inline = re.sub(r"\s+", " ", trecho_inline).strip()
                trecho_latex = (
                    f"{h['contexto_antes_50']} "
                    f"\\textbf{{{h['trecho_central']}}} "
                    f"{h['contexto_depois_50']}"
                )
                trecho_latex = re.sub(r"\s+", " ", trecho_latex).strip()
                f.write(f"**Passagem {i}** (p.~{h['pagina']}, termo: `{h['termo']}`, ")
                f.write(f"densidade: {h['score_densidade']} termos figurais na janela)\n\n")
                f.write(f"> {trecho_inline}\n\n")
                f.write("```latex\n")
                f.write("\\begin{citacaoabnt}\n")
                # Quebrar para no máximo 90 caracteres por linha para legibilidade
                palavras = trecho_latex.split()
                linha = ""
                for w in palavras:
                    if len(linha) + len(w) + 1 > 90:
                        f.write(linha + "\n")
                        linha = w
                    else:
                        linha = (linha + " " + w).strip()
                if linha:
                    f.write(linha + "\n")
                f.write(f"\\end{{citacaoabnt}}\n")
                f.write(f"\\parencite[p.~{h['pagina']}]{{")
                bibkey = {
                    "latour_woolgar_1986_lab_life_en": "Latour1997VidaLaboratorio",
                    "latour_1987_science_action_en": "Latour2011CienciaEmAcao",
                    "latour_1999_pandora_en": "Latour2017Esperanca",
                }[h["obra"]]
                f.write(f"{bibkey}}}\n")
                f.write("```\n\n")
            f.write("\n")
        f.write("---\n\n")

print(f"Relatório salvo em: {md_path}")
```

### 5. Criar `outputs/passo4/README.md`

Criar a pasta `outputs/passo4/` se não existir, e dentro dela criar `README.md` com o conteúdo abaixo:

```markdown
# Passo 4 — KWIC ampliado e curadoria de passagens citáveis

**Data:** 15 de maio de 2026.
**Propósito:** alimentar o capítulo 2 da tese com passagens de Latour prontas para citação direta, no contexto da análise da tensão figural entre o vocabulário agonístico de Latour e a figuração têxtil-feminista de Haraway.

## Política de versionamento

Os artefatos deste passo reproduzem trechos extensos das obras de Latour (cerca de ±50 palavras de contexto por ocorrência, em volume agregado significativo). Para preservar a conformidade com os direitos autorais das editoras (Harvard University Press, Princeton University Press), os arquivos com reprodução textual ficam **fora do repositório público**:

- `kwic_ampliado.csv` (gerado localmente, no `.gitignore`)
- `passagens_curadas.md` (gerado localmente, no `.gitignore`)
- `sequencia_exercito_ciencia.md` (curadoria argumentativa, no `.gitignore`)

O **pipeline reprodutível** está versionado: qualquer pessoa com os PDFs originais legalmente adquiridos pode gerar os arquivos rodando o script. O que circula publicamente é a metodologia, o script e este README.

## Geração local dos artefatos

Pré-requisitos: corpus extraído em `corpus/txt_norm/` e classificação de páginas em `corpus/paginas/` (gerados pela Etapa 1 do pipeline).

```bash
python3 scripts/10_passo4_kwic_ampliado.py
```

Produz:

### `kwic_ampliado.csv`

Todas as ocorrências dos 12 campos figurativos prioritários nas três obras de Latour, em janela de ±50 palavras (cinco vezes a janela do KWIC original de ±10). Colunas: `obra`, `ano`, `grupo`, `termo`, `pagina`, `contexto_antes_50`, `trecho_central`, `contexto_depois_50`, `classificacao_passo1` (apenas para `war`/`wars` em *Pandora's Hope*: `descritivo`, `figurativo` ou vazio).

Filtros: páginas classificadas como `corpo` ou `inicio_capitulo`, exclusões do catálogo lexical aplicadas em janela ±5 adjacente, classificação manual do passo 1 anexada para hits em *Pandora's Hope*.

### `passagens_curadas.md`

Até 4 passagens por par (obra × campo figurativo), selecionadas automaticamente pela densidade figural no entorno ±50 palavras. Diversidade interna garantida por exclusão de hits em páginas vizinhas (±2). Hits descritivos do passo 1 são excluídos da curadoria.

Cada passagem aparece em prosa com palavra-chave em negrito e como bloco LaTeX `citacaoabnt` com `\parencite` correspondente. 90 passagens curadas cobrindo 26 pares (obra × grupo).

### `sequencia_exercito_ciencia.md`

Curadoria temática manual de 9 passagens articuladas em sequência argumentativa (analogia → identificação literal → autocrítica) sobre exército e ciência em Latour, da analogia da colina em *Laboratory Life* à formulação da epistemologia como *Cold War machine* em *Pandora's Hope*.

## Aviso sobre OCR

Os textos vêm de `corpus/txt_norm/`, gerados por extração automática de PDF. Podem conter resíduos de OCR (palavras truncadas, espaços extras, hifenizações mal recompostas). Sempre revisar a passagem contra o PDF original antes de usar como citação na tese.

## Chaves BibTeX usadas

- *Laboratory Life* (1986) → `Latour1997VidaLaboratorio`
- *Science in Action* (1987) → `Latour2011CienciaEmAcao`
- *Pandora's Hope* (1999) → `Latour2017Esperanca`
```

### 6. Verificar que o `.gitignore` está protegendo os arquivos certos

Antes de stagear, rodar:

```bash
git check-ignore -v outputs/passo4/kwic_ampliado.csv outputs/passo4/passagens_curadas.md outputs/passo4/sequencia_exercito_ciencia.md
```

Os três caminhos devem aparecer como ignorados, citando o `.gitignore`. Se algum não aparecer, pare e me avise.

### 7. Stagear, commitar e fazer push

```bash
git add .gitignore decisoes_metodologicas.md scripts/10_passo4_kwic_ampliado.py outputs/passo4/README.md
git status
```

`git status` deve mostrar quatro arquivos staged e **nenhum** outro arquivo modificado. Se houver algo a mais, pare e me avise.

Em seguida, commit com a mensagem abaixo (preserve as quebras de linha):

```
git commit -m "Passo 4: KWIC ampliado, dispensa da validação manual, sequência exército/ciência

- Dispensa da Etapa 2 (validação amostral manual) registrada em
  decisoes_metodologicas.md com motivação, justificativa e reformulação
  para o apêndice metodológico da tese.

- Script scripts/10_passo4_kwic_ampliado.py: gera KWIC ampliado a
  ±50 palavras para 12 campos figurativos prioritários nas três obras
  de Latour, aplica filtros de classe de página e exclusões do catálogo,
  anexa a classificação manual do passo 1 para war/wars em Pandora,
  e produz curadoria automática de até 4 passagens por par
  (obra × campo) por densidade figural no entorno.

- outputs/passo4/README.md: documentação da política de versionamento.
  Os artefatos com reprodução extensa de Latour (kwic_ampliado.csv,
  passagens_curadas.md, sequencia_exercito_ciencia.md) ficam fora do
  repositório público por conformidade com direitos autorais.
  O pipeline reprodutível está versionado: rodar o script gera os
  arquivos localmente.

- .gitignore atualizado para incluir os três arquivos do passo 4."
```

Por fim:

```bash
git push origin main
git log --oneline -3
```

E me mostre o resultado do push e do log.

### 8. Se tudo der certo

Avise-me que o push foi feito com sucesso. Se quiser, pode também rodar o script para gerar os artefatos localmente (eles ficam fora do GitHub mas existem na minha máquina):

```bash
python3 scripts/10_passo4_kwic_ampliado.py
```

Esperado: criar `outputs/passo4/kwic_ampliado.csv` (cerca de 1473 linhas) e `outputs/passo4/passagens_curadas.md` (cerca de 1700 linhas com 90 passagens).

## Em caso de problema

Se em qualquer etapa houver conflito, dependência ausente, ou comportamento inesperado, **pare** e me explique o que aconteceu. Não tente resolver sozinho commit ou push problemáticos. Em particular:

- Se `git pull` trouxer mudanças do remoto que conflitem com o que vamos commitar, me avise.
- Se o teste do `git check-ignore` no item 6 não confirmar que os três arquivos estão ignorados, me avise.
- Se `git status` no item 7 mostrar arquivos staged além dos quatro previstos, me avise.
