# Análise de figurações em Latour

Este repositório reúne os dados, os *scripts* e os resultados da análise lexicométrica que fiz do vocabulário figurativo de Bruno Latour para o capítulo 2 da minha tese de doutorado, *Tecnografias de um centro de inteligência artificial: seguindo cientistas e engenheiros universidade afora* (Programa de Pós-Graduação em Ciências Sociais, IFCH, Unicamp, 2026). O capítulo argumenta a tensão entre o vocabulário militar-industrial latouriano (alistar, aliados, provas de força, máquina de guerra) e a figuração têxtil-feminista de Donna Haraway; esta análise dá a esse argumento uma base empírica contável e citável para o lado de Latour.

## O que fiz

Rastreei, por catálogos de termos, de 17 a 31 campos figurativos (inscrição, móvel imutável, caixa-preta, tradução, prova de força, alistamento, rede, militar, entre outros) em seis textos de Latour publicados entre 1986 e 2013, lidos nos originais em inglês:

| Etapa | Textos | Catálogo |
|---|---|---|
| 1 | *Laboratory Life* (1986), *Science in Action* (1987), *Pandora's Hope* (1999) | `campos_lexicais/catalogo_termos.yaml` (17 campos) |
| 2 | *On Actor-Network Theory: A Few Clarifications* (1996), *On Recalling ANT* (1999) | o mesmo, com as adições têxtil e topologia (19 campos) |
| 3 | *An Inquiry into Modes of Existence* (2013) | os 19 campos mais 12 novos (`catalogo_termos_aime.yaml`) |

Para cada texto extraí e normalizei o texto dos PDFs, levantei as ocorrências em KWIC (janela de ±10 palavras), calculei frequência absoluta e densidade (ocorrências por dez mil palavras), redes de co-ocorrência e, sobre as três obras da etapa 1, uma classificação de Reinert com análise fatorial de correspondências em R. Validei por amostragem as heurísticas de extração e a pertinência semântica dos termos de cada campo.

O campo militar recebeu um tratamento à parte: classifiquei manualmente cada ocorrência de `war`/`wars` como descritivo-histórica (a guerra como acontecimento) ou figurativa (a guerra como modelo da prática científica). A classificação manual fica em CSV auditável (`outputs/etapa1/refinamento/war_<obra>_classificacao.csv`, coluna `categoria_final`) e o *pipeline* a aplica sem recomputá-la. As contagens do campo militar são reportadas em duas versões, bruta e refinada; as figuras da tese usam a refinada (37 ocorrências em *Laboratory Life*, 363 em *Science in Action*, 156 em *Pandora's Hope*).

Todas as decisões de método estão datadas em [`docs/decisoes_metodologicas.md`](docs/decisoes_metodologicas.md).

## O que entra na tese

No capítulo 2, seção "Contando figurações: análise lexicométrica de Latour", e na subseção sobre *An Inquiry into Modes of Existence*:

- sete figuras de frequência e densidade por campo, uma para cada texto e uma comparação entre as três obras da etapa 1 (`outputs/figuras/`);
- as tabelas do catálogo lexical das etapas 1 a 3 e os quadros de mapeamento com *AIME* (versões LaTeX em `outputs/latex/`).

A correspondência figura a figura, com o *script* e os dados de origem de cada uma, está em [`docs/USO_NA_TESE.md`](docs/USO_NA_TESE.md) (versão tabular em [`docs/uso_na_tese.csv`](docs/uso_na_tese.csv)). As demais saídas (redes de co-ocorrência, Reinert/AFC, relatórios por etapa, planilhas de validação) ficam como material de auditoria.

## Dados e direitos autorais

Os PDFs e os textos integrais das obras não estão no repositório, por direitos autorais. No lugar deles guardo:

- `corpus/metadata.csv`: as edições exatas analisadas;
- `corpus/CHECKSUMS.sha256` e `corpus/inventario_textos.csv`: o SHA-256 e a origem de cada texto, para que quem adquirir as mesmas edições verifique se chegou aos textos que analisei;
- os KWIC sem as colunas de contexto (`kwic*_publico.csv`).

Detalhes de reconstrução e verificação em [`corpus/README.md`](corpus/README.md).

## Como reproduzir

```bash
git clone https://github.com/julianehelanski/analise-figuracoes-latour.git
cd analise-figuracoes-latour
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm

cp .env.example .env      # informar em CORPUS_PDF_PATH a pasta local com os PDFs
bash scripts/run_etapa1.sh
```

Os PDFs devem seguir os nomes da coluna `arquivo_pdf` de `corpus/metadata.csv`. As etapas 2 e 3 foram rodadas pelos *scripts* de `scripts/arquivo/` (numerados de 13 a 24), e a camada R está em `scripts/R/10_reinert_afc.R` (instruções em [`scripts/R/README.md`](scripts/R/README.md)). As amostragens usam `seed=42`.

## Estrutura

```
corpus/            catálogo, checksums e inventário dos textos (textos integrais fora do git)
campos_lexicais/   catálogos de termos (YAML) e adições auditáveis da etapa 2
scripts/           pipeline (01 a 12), módulo de desambiguação de war, camada R, scripts por etapa
outputs/           resultados por etapa e por obra, figuras, consolidado e versões LaTeX
docs/              decisões metodológicas e uso na tese
```

## Uso de inteligência artificial generativa

Fiz a análise deste repositório com o Claude Code, a partir das especificações metodológicas que defini e registrei em `docs/decisoes_metodologicas.md` e em `CLAUDE.md` (o arquivo de memória do projeto, lido pela ferramenta a cada sessão). O Claude Code é a interface de linha de comando da Anthropic que dá ao modelo de linguagem acesso aos arquivos do projeto, para ler, escrever e executar *scripts*. Com ele escrevi e executei os *scripts* de extração e normalização dos textos, KWIC, frequências, co-ocorrência, visualização e camada R, e a camada automática da desambiguação de `war`/`wars`. São minhas a definição do corpus e dos catálogos de termos, a classificação manual das ocorrências, a validação amostral e a interpretação dos resultados no capítulo 2.

**Modelos registrados no histórico de versões:** Claude Opus 4.8, Claude Opus 5.5 e Claude Sonnet 5.5 (maio a outubro de 2026). Os *commits* mais antigos, de maio de 2026, não registram a versão do modelo.

Os *commits* com autor `Claude`, ou com a linha `Co-Authored-By: Claude …`, foram feitos em sessões do Claude Code; a marcação é gerada pela ferramenta e registra em que pontos do histórico o modelo participou do trabalho. A autoria e a responsabilidade pelo conteúdo são minhas e, conforme a Deliberação CONSU-A-005/2026 da Unicamp, as ferramentas de IA generativa não figuram como coautoras. A declaração formal de uso de IA generativa da tese está no [Anexo 1](https://github.com/julianehelanski/tecno-etnografia-centro-ia/blob/main/ex_ane1.tex).

## Citação

> CARDOSO, Juliane Cristina Helanski. *Análise de figurações em Latour*: dados e *scripts*. Campinas: Unicamp, 2026. Disponível em: https://github.com/julianehelanski/analise-figuracoes-latour.

> CARDOSO, Juliane Cristina Helanski. *Tecnografias de um centro de inteligência artificial*: seguindo cientistas e engenheiros universidade afora. Orientadora: Maria Suely Kofes. 2026. Tese (Doutorado em Ciências Sociais) – Instituto de Filosofia e Ciências Humanas, Universidade Estadual de Campinas, Campinas, 2026.

ORCID da autora: https://orcid.org/0000-0001-8649-8986.

Metadados de citação em [`CITATION.cff`](CITATION.cff).

## Licença

Código sob licença [MIT](LICENSE); dados que produzi (catálogos de termos, CSV, relatórios, tabelas e figuras) sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br), conforme [`LICENSE-DADOS.md`](LICENSE-DADOS.md). As obras de Latour permanecem sob os direitos de seus autores e editores e não são distribuídas aqui.

## Contato

Juliane Cristina Helanski Cardoso, doutora em Ciências Sociais pela Unicamp (2026).
