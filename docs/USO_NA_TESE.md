# Uso deste repositório na tese

Documento gerado em 09/10/2026 a partir da leitura dos arquivos `ex_cap*.tex` do repositório da tese (`julianehelanski/tecno-etnografia-centro-ia`, commit 3f0f671 (2026-10-08)). Repositório descrito: `julianehelanski/analise-figuracoes-latour`. A versão tabular está em `docs/uso_na_tese.csv`.

## Onde entra na tese

Capítulo 2, seção "Contando figurações: análise lexicométrica de Latour" (`sec:analise_lexicometrica`), com a subseção sobre *An Inquiry into Modes of Existence* (`subsec:figuracao_aime`). O capítulo 1 (seção de auditabilidade pública) remete a este repositório como o lugar dos scripts, dos catálogos de termos, das planilhas de validação e dos outputs de cada etapa. A tese cita o repositório em `ex_cap1.tex` com o endereço `analise_figuracoes`, nome anterior à renomeação para `analise-figuracoes-latour` (ver pendências no mapa de dados do repositório da tese).

## Como os dados foram usados

A análise rastreia, por catálogo de termos, o vocabulário figurativo de Latour em seis textos, em três etapas. A etapa 1 processa *Laboratory Life* (1986), *Science in Action* (1987) e *Pandora's Hope* (1999) com 17 rótulos; a etapa 2 estende o catálogo a 19 rótulos (adições `latour_textil_en_etapa2_adicoes.txt` e `latour_topologia_en_etapa2_adicoes.txt`) e processa *Clarifications* (1996) e *On Recalling ANT* (1999); a etapa 3 processa *AIME* (2013) com os 19 rótulos mais 12 rótulos novos (`catalogo_termos_aime.yaml`). As medidas reportadas são ocorrências por dez mil palavras (densidade) e contagem absoluta (frequência). O rótulo `militar` é reportado em duas versões, bruta e refinada pela desambiguação manual de `war`/`wars` (`scripts/_desambiguar_war.py`; camada manual em `outputs/etapa1/refinamento/war_<obra>_classificacao.csv`). As figuras da tese usam a versão refinada.

## Insumos e proveniência dos dados

Os textos analisados vêm de PDFs das edições citadas em `corpus/metadata.csv` (catálogo bibliográfico, fonte de verdade). Os PDFs ficam fora do repositório. A extração (`scripts/01_extract_text.py`) e a normalização (`scripts/01b_normalize_text.py`) produzem `corpus/txt/` e `corpus/txt_norm/`. Catálogos de termos: `campos_lexicais/catalogo_termos.yaml` e `campos_lexicais/catalogo_termos_aime.yaml`. Decisões metodológicas: `docs/decisoes_metodologicas.md`.

## Figuras e tabelas da tese que vêm deste repositório

| Capítulo | Seção da tese | Rótulo | Arquivo no repositório | Script | Estado da cópia na tese |
|---|---|---|---|---|---|
| capítulo 2 | Contando figurações: análise lexicométrica de seis obras de Bruno Lato | `fig:freq_densidade_lab_life` | `outputs/figuras/etapa1_lab_life_freq_e_densidade.png` | `scripts/arquivo/24_freq_densidade_por_obra.py (estilo em scripts/estilo_tese.py; militar refinado via scripts/_desambiguar_war.py)` | cópia na tese idêntica à do repositório |
| capítulo 2 | Contando figurações: análise lexicométrica de seis obras de Bruno Lato | `fig:freq_densidade_sia` | `outputs/figuras/etapa1_sia_freq_e_densidade.png` | `scripts/arquivo/24_freq_densidade_por_obra.py (estilo em scripts/estilo_tese.py; militar refinado via scripts/_desambiguar_war.py)` | cópia na tese idêntica à do repositório |
| capítulo 2 | Contando figurações: análise lexicométrica de seis obras de Bruno Lato | `fig:freq_densidade_pandora` | `outputs/figuras/etapa1_pandora_freq_e_densidade.png` | `scripts/arquivo/24_freq_densidade_por_obra.py (estilo em scripts/estilo_tese.py; militar refinado via scripts/_desambiguar_war.py)` | cópia na tese idêntica à do repositório |
| capítulo 2 | Contando figurações: análise lexicométrica de seis obras de Bruno Lato | `fig:comparacao_tres_obras` | `outputs/figuras/etapa1_passo4_comparacao_frequencias_tres_obras.png` | `scripts/arquivo/11_passo4_graficos.py (estilo em scripts/estilo_tese.py)` | cópia na tese idêntica à do repositório |
| capítulo 2 | O corpus estendido: o vocabulário metateórico de Clarifications e On R | `fig:freq_densidade_clarifications` | `outputs/figuras/etapa2_clarifications_freq_e_densidade.png` | `scripts/arquivo/24_freq_densidade_por_obra.py (estilo em scripts/estilo_tese.py; militar refinado via scripts/_desambiguar_war.py)` | cópia na tese idêntica à do repositório |
| capítulo 2 | O corpus estendido: o vocabulário metateórico de Clarifications e On R | `fig:freq_densidade_recalling` | `outputs/figuras/etapa2bis_recalling_integral_freq_e_densidade.png` | `scripts/arquivo/24_freq_densidade_por_obra.py (estilo em scripts/estilo_tese.py; militar refinado via scripts/_desambiguar_war.py)` | cópia na tese idêntica à do repositório |
| capítulo 2 | A figuração em An Inquiry into Modes of Existence | `fig:aime_freq_densidade` | `outputs/figuras/etapa3_aime_freq_e_densidade.png` | `scripts/arquivo/24_freq_densidade_por_obra.py (estilo em scripts/estilo_tese.py; militar refinado via scripts/_desambiguar_war.py)` | cópia na tese idêntica à do repositório |

Tabelas da tese derivadas deste repositório (compostas no texto do capítulo 2): catálogo lexical das etapas 1 e 2 (`campos_lexicais/catalogo_termos.yaml`, versão LaTeX em `outputs/latex/catalogo_lexical_campos.tex`), catálogo lexical da etapa 3 (`tab:aime_catalogo_novo`, a partir de `campos_lexicais/catalogo_termos_aime.yaml` e dos outputs de `outputs/etapa3/`) e quadros de mapeamento com *AIME* (`tab:aime_quadro1_grupo5`, `tab:mapeamento_quadro1_catalogo_novo`).

## Material do repositório sem uso direto na tese

Das 73 figuras em `outputs/figuras/`, 63 não aparecem em `ex_cap*.tex`. São saídas das etapas (redes de co-ocorrência, frequências por grupo, variantes em SVG, análise Reinert/AFC) que sustentam as medidas reportadas e permanecem como material de auditoria.

## Direitos autorais

Desde 09/10/2026 os textos integrais das obras de Latour (`corpus/txt/`, `corpus/txt_norm/`, `corpus/txt_lemma_en/`, `corpus/txt_fornecido/`) ficam fora do repositório público, em coerência com a nota do capítulo 1 da tese. O repositório versiona o SHA-256 de cada texto (`corpus/CHECKSUMS.sha256`) e o inventário de origem (`corpus/inventario_textos.csv`); as instruções de reconstrução e verificação estão em `corpus/README.md`. Os arquivos KWIC são versionados sem as colunas de contexto (`kwic*_publico.csv`, gerados por `scripts/12_kwic_publico.py`); os completos ficam na cópia local. Nos artigos curtos (*Clarifications*, *Recalling*), as planilhas de validação amostral e os relatórios `frequencias.md` ainda reproduzem 15% e 23% do texto (ver `docs/decisoes_metodologicas.md`, entradas de 09/10/2026).
