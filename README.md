# Análise de Figurações em Latour e Haraway

Análise textual sistemática das figurações e metáforas mobilizadas por Bruno Latour e Donna Haraway, com extensões para Isabelle Stengers e Tim Ingold, conduzida com auxílio de Claude Code como mediador técnico. Esta pesquisa integra a tese de doutorado em Ciências Sociais sobre o C4AI-USP e o sistema Spira, em andamento na Unicamp.

---

## Por que este projeto

O capítulo 2 da minha tese argumenta que existe uma tensão figural entre dois vocabulários teóricos amplamente mobilizados nos estudos sociais da ciência e tecnologia: o vocabulário militar-industrial latouriano (alistar, aliados, provas de força, máquina de guerra) e a figuração têxtil-feminista de Donna Haraway (string figures, tramas, costuras, sympoiesis). Essa tensão organiza um eixo reflexivo da tese, e este projeto produz a evidência empírica que sustenta o argumento.

Em vez de inferir a tensão por leitura interpretativa apenas, a análise textual sistematiza a presença e a distribuição dos termos figurais ao longo das obras de cada autor. O resultado é dado citável para a tese: tabelas de frequência, redes de cocorrência, mapas de densidade lexical, e passagens densas codificadas qualitativamente.

A análise é, ela mesma, parte do argumento da tese. Que ela seja possível hoje, com Claude Code como mediador, demonstra concretamente o que descrevo no capítulo 2 sobre mediação técnica e agência distribuída na IA generativa contemporânea. O apêndice metodológico que sairá deste projeto descreve essa cadeia de mediações em registro etnográfico.

---

## Estrutura do repositório

```
analise_figuracoes/
├── README.md                       este arquivo
├── CLAUDE.md                       memória do projeto para Claude Code
├── metadata.csv                    catálogo bibliográfico (espelho de corpus/metadata.csv)
├── pyproject.toml                  dependências Python
├── requirements.txt                dependências fixadas
├── .env                            (local) caminho da pasta Drive com os PDFs
├── .gitignore
│
├── corpus/
│   ├── README.md                   documenta as obras esperadas
│   ├── metadata.csv                fonte de verdade do catálogo
│   ├── txt/                        texto cru extraído dos PDFs
│   ├── txt_norm/                   texto normalizado (lido pelo pipeline)
│   └── paginas/                    classificação por página (front/back matter, corpo, ...)
│
├── campos_lexicais/
│   ├── catalogo_termos.yaml        17 campos de Latour (Etapas 1 e 2)
│   ├── catalogo_termos_aime.yaml   12 campos novos de AIME (Etapa 3)
│   └── latour_*_etapa2_adicoes.txt suplementos auditáveis da Etapa 2
│
├── scripts/
│   ├── 01_extract_text.py … 08_validate_sample.py   pipeline reutilizável
│   ├── _paths.py                                    mapeamento obra → etapa
│   ├── run_etapa1.sh                                orquestrador da Etapa 1
│   └── arquivo/                                     scripts one-shot já consumidos
│
├── outputs/
│   ├── etapa1/<obra>/{csv,relatorios,figuras}    por obra
│   ├── etapa1/{passo4,refinamento}/              consolidados da Etapa 1
│   ├── etapa1/trajetoria_latour_1986_1999.{md,csv}
│   ├── etapa2/<obra>/...
│   ├── etapa2/consolidado/                       tabelas e relatórios da Etapa 2
│   ├── etapa2bis/<obra>/...
│   ├── etapa2bis/{consolidado,recalling_extras}/
│   ├── etapa3/<obra>/...
│   ├── etapa3/consolidado/
│   ├── consolidado/                              consolidado final cross-etapas
│   └── latex/                                    versões LaTeX para a tese
│
└── docs/
    ├── decisoes_metodologicas.md   decisões vivas, datadas e revisáveis
    └── historico.md                índice cronológico de briefings consumidos
```

**Observação importante**: a pasta dos PDFs **não existe localmente nem é versionada**. Os PDFs são lidos diretamente da pasta Google Drive sincronizada (ver "Como usar" abaixo).

---

## Como usar

### Primeira vez no repositório

#### 1. Clone o repositório

```bash
git clone https://github.com/julianehelanski/analise_figuracoes.git
cd analise_figuracoes
```

#### 2. Configure o ambiente Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm
python -m spacy download pt_core_news_sm
```

#### 3. Sincronize a pasta Drive com os PDFs

Os PDFs dos livros do corpus estão armazenados em uma pasta privada do Google Drive (não commitada por questões de copyright). Para que o pipeline acesse os PDFs localmente, é preciso sincronizar a pasta Drive com a máquina.

**Passos**:

1. Instale o **Google Drive for Desktop**:
   - Mac/Windows: <https://www.google.com/drive/download/>
   - Linux: alternativas via `rclone` (consulte documentação do `rclone` se for o caso).

2. Faça login com a conta que possui acesso à pasta do corpus.

3. Configure a sincronização para a pasta que contém os PDFs:
   - No Drive for Desktop, vá em **Preferências → Pastas do Drive**.
   - Marque a pasta `analise_figuracoes_corpus` (ou nome equivalente) para "Espelhar arquivos" (Mirror files), de modo que os PDFs fiquem disponíveis offline.

4. Após sincronização, identifique o caminho local da pasta. Geralmente é algo como:
   - macOS: `/Users/<seu_usuario>/Library/CloudStorage/GoogleDrive-<email>/My Drive/analise_figuracoes_corpus/`
   - Windows: `G:\My Drive\analise_figuracoes_corpus\` (a letra varia)
   - Linux com rclone: o caminho onde você montou o Drive.

#### 4. Configure o arquivo `.env`

Copie o template e ajuste o caminho:

```bash
cp .env.example .env
```

Edite `.env` e preencha:

```
# Caminho local da pasta Drive sincronizada com os PDFs do corpus
CORPUS_PDF_PATH=/Users/juliane/Library/CloudStorage/GoogleDrive-seu_email/My Drive/analise_figuracoes_corpus
```

O arquivo `.env` **não** é versionado (está no `.gitignore`), porque cada máquina sua tem caminho local diferente, e porque manter caminhos de material privado fora do git é boa prática.

#### 5. Inicie o Claude Code no diretório raiz

```bash
claude
```

#### 6. Diga ao Claude Code

> "Leia `CLAUDE.md` e `docs/decisoes_metodologicas.md` para entender o estado atual e as decisões fixadas. Aguarde minha confirmação antes de avançar para qualquer etapa."

### Sessões subsequentes

A cada sessão, Claude Code lê automaticamente `CLAUDE.md`, que mantém memória do projeto: corpus atual, etapa em andamento, decisões já tomadas, pendências.

### Trabalho em múltiplas máquinas

Se quiser trabalhar em mais de uma máquina:

1. Em cada máquina, clone o repositório e configure o ambiente Python.
2. Em cada máquina, sincronize a pasta Drive e configure o `.env` local apontando para o caminho local específico da máquina.
3. O repositório do GitHub mantém a versão única do código, scripts, campos lexicais e outputs. Cada máquina tem seu próprio `.env`.

---

## Princípios metodológicos

1. **Cada etapa é fechada**: produz artefato próprio que pode ser usado isoladamente, mesmo que a etapa seguinte não venha a ser executada.

2. **Validação humana é estrutural**: a cada etapa há um gate em que eu (Juliane) reviso o output antes da próxima começar. Discordâncias entre minha leitura e a pré-anotação do Claude Code são registradas como dado metodológico.

3. **Reprodutibilidade**: seeds aleatórias fixas, scripts versionados, decisões documentadas em `docs/decisoes_metodologicas.md`. Outra pesquisadora deveria poder reexecutar o pipeline.

4. **Tradução como mediação explícita**: os campos lexicais são produzidos por idioma (inglês, francês, português) e não cruzados sem mediação. Diferenças entre versões em línguas diferentes são parte do dado.

5. **O método é parte do argumento**: a cadeia mim → Claude Code → minha revisão é descrita no apêndice metodológico em registro etnográfico, em coerência com a tese sobre mediação técnica em IA generativa.

6. **PDFs ficam fora do git**: o repositório versiona código, campos lexicais e outputs estruturados. PDFs ficam no Drive privado e são lidos via sincronização local. Outras pesquisadoras que queiram replicar adquirem as obras por canais próprios.

---

## Estado atual

Ver `CLAUDE.md` para a etapa em andamento, decisões já tomadas e pendências.

## Licença

Código sob licença MIT. Os dados produzidos (CSVs, relatórios, figuras) estão sob CC BY 4.0. Os PDFs do corpus permanecem sob copyright dos respectivos autores e editores; não são distribuídos por este repositório nem por qualquer canal público.

## Contato

Juliane Helanski, doutoranda no Programa de Pós-Graduação em Ciências Sociais da Unicamp.
