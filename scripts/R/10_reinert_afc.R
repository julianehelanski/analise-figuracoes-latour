# =============================================================================
# 10_reinert_afc.R
# Classificação Reinert (CHD) e Análise Fatorial de Correspondências (AFC)
# sobre as três obras de Latour em escopo da Etapa 1.
#
# Entrada:  corpus/txt_norm/{latour_woolgar_1986_lab_life_en,
#                            latour_1987_science_action_en,
#                            latour_1999_pandora_en}.txt
# Saída:    outputs/etapa1/reinert_afc/
#           corpus/txt_lemma_en/  (lemas gerados por udpipe, reaproveitáveis)
#
# Equivalente em R do fluxo IRaMuTeQ: lematização -> segmentação em STs ->
# Reinert (CHD) via rainette -> AFC via FactoMineR sobre o cruzamento
# lema x classe Reinert.
#
# Rodar em RStudio com o working directory na raiz do repositório
# (Session > Set Working Directory > To Project Directory).
# =============================================================================

set.seed(42)

# ---- pacotes ----------------------------------------------------------------

pacotes <- c("quanteda", "rainette", "udpipe", "FactoMineR",
             "factoextra", "ggplot2", "ggrepel", "dplyr", "readr", "tibble")

faltantes <- pacotes[!vapply(pacotes, requireNamespace, logical(1),
                             quietly = TRUE)]
if (length(faltantes) > 0) {
  stop("Pacotes ausentes: ", paste(faltantes, collapse = ", "),
       ". Instale com install.packages() antes de rodar.")
}

library(quanteda)
library(rainette)
library(udpipe)
library(FactoMineR)
library(factoextra)
library(ggplot2)
library(ggrepel)
library(dplyr)
library(readr)
library(tibble)

# ---- caminhos ---------------------------------------------------------------

raiz <- getwd()
dir_norm   <- file.path(raiz, "corpus", "txt_norm")
dir_lemma  <- file.path(raiz, "corpus", "txt_lemma_en")
dir_saida  <- file.path(raiz, "outputs", "etapa1", "reinert_afc")
dir.create(dir_lemma,  showWarnings = FALSE, recursive = TRUE)
dir.create(dir_saida,  showWarnings = FALSE, recursive = TRUE)

obras <- tibble::tribble(
  ~obra_id,           ~ano, ~arquivo,
  "lab_life_1986",    1986, "latour_woolgar_1986_lab_life_en.txt",
  "science_1987",     1987, "latour_1987_science_action_en.txt",
  "pandora_1999",     1999, "latour_1999_pandora_en.txt"
)
obras$caminho <- file.path(dir_norm, obras$arquivo)
stopifnot(all(file.exists(obras$caminho)))

# ---- 1. lematização via udpipe ---------------------------------------------
# Modelo english-ewt baixado automaticamente em ./udpipe_models/ na primeira
# execução. Lematizados ficam cacheados em corpus/txt_lemma_en/ para que
# execuções seguintes não repitam o trabalho pesado.

dir_modelos <- file.path(raiz, "udpipe_models")
dir.create(dir_modelos, showWarnings = FALSE)
modelo_path <- file.path(dir_modelos, "english-ewt-ud-2.5-191206.udpipe")
if (!file.exists(modelo_path)) {
  message("Baixando modelo udpipe english-ewt...")
  udpipe_download_model(language = "english-ewt", model_dir = dir_modelos)
  modelo_path <- list.files(dir_modelos, pattern = "english-ewt.*\\.udpipe$",
                            full.names = TRUE)[1]
}
modelo <- udpipe_load_model(modelo_path)

lematizar_obra <- function(caminho_in, caminho_out, modelo) {
  if (file.exists(caminho_out)) {
    message("  cache: ", basename(caminho_out))
    return(readr::read_file(caminho_out))
  }
  message("  lematizando: ", basename(caminho_in))
  texto <- readr::read_file(caminho_in)
  anot  <- udpipe_annotate(modelo, x = texto)
  df    <- as.data.frame(anot)
  # mantém apenas lemas alfabéticos; descarta pontuação, numerais, símbolos
  df <- df[!is.na(df$lemma) &
             grepl("^[A-Za-z]+$", df$lemma) &
             !(df$upos %in% c("PUNCT", "NUM", "SYM", "X")), ]
  df$lemma <- tolower(df$lemma)
  saida <- paste(df$lemma, collapse = " ")
  readr::write_file(saida, caminho_out)
  saida
}

textos_lemma <- character(nrow(obras))
for (i in seq_len(nrow(obras))) {
  out_i <- file.path(dir_lemma,
                     sub("\\.txt$", "_lemma.txt", obras$arquivo[i]))
  textos_lemma[i] <- lematizar_obra(obras$caminho[i], out_i, modelo)
}

# ---- 2. corpus quanteda + segmentação em STs (~40 ocorrências) -------------

corpus_l <- corpus(textos_lemma,
                   docnames = obras$obra_id,
                   docvars  = data.frame(obra = obras$obra_id,
                                         ano  = obras$ano))

# rainette::split_segments cria STs do tamanho-alvo, segmentando dentro de
# cada documento. 40 é o padrão IRaMuTeQ para corpora dessa ordem.
corpus_st <- rainette::split_segments(corpus_l, segment_size = 40)

cat("Total de STs gerados:", ndoc(corpus_st), "\n")
print(table(docvars(corpus_st, "obra")))

# ---- 3. matriz documento-termo (dfm) ---------------------------------------

stop_en <- quanteda::stopwords("en")

dtm <- corpus_st |>
  tokens(remove_punct = TRUE, remove_numbers = TRUE,
         remove_symbols = TRUE) |>
  tokens_remove(stop_en, min_nchar = 3L) |>
  dfm()

# Filtra termos raros (menos de 3 STs) para estabilizar a Reinert.
dtm <- dfm_trim(dtm, min_docfreq = 3)
# Remove STs que ficaram vazios após o trim.
dtm <- dfm_subset(dtm, ntoken(dtm) > 0)

cat("dfm:", ndoc(dtm), "STs x", nfeat(dtm), "lemas\n")

# ---- 4. classificação Reinert (CHD) ----------------------------------------
# k controla a profundidade máxima da partição; 5 a 6 classes é o
# patamar mais usado na literatura francófona. Mantemos k=6 com poda
# automática pelo critério qui-quadrado do próprio rainette.

res_reinert <- rainette(dtm, k = 6, min_segment_size = 10)

# Dendrograma simples via plot() do hclust (rainette herda de hclust).
# rainette_plot() tem rendering frágil em algumas combinações R/pacote;
# separamos dendrograma e perfis em dois PNGs robustos.
png(file.path(dir_saida, "reinert_dendrograma.png"),
    width = 1600, height = 900, res = 150)
plot(res_reinert,
     main = "Dendrograma Reinert (CHD), k = 6",
     xlab = "Classe", ylab = "Distância qui²", sub = "",
     hang = -1)
dev.off()

# Atribui a classe Reinert a cada ST.
docvars(dtm, "classe_reinert") <- cutree(res_reinert, k = 6)

# Exporta perfis de classe (lemas mais característicos por classe).
perfis <- rainette_stats(docvars(dtm, "classe_reinert"), dtm,
                         measure = "chi2", n_terms = 50,
                         show_negative = FALSE, max_p = 0.05)
for (i in seq_along(perfis)) {
  readr::write_csv(perfis[[i]],
                   file.path(dir_saida,
                             sprintf("perfis_classe_%02d.csv", i)))
}

# Barplot facetado dos lemas mais característicos por classe.
# Substitui o type = "bar" do rainette_plot, que falha em algumas versões.
perfis_top <- dplyr::bind_rows(
  lapply(seq_along(perfis), function(i) {
    df <- as.data.frame(perfis[[i]])
    df$classe <- sprintf("Classe %d", i)
    head(df, 15)
  })
)

g_perfis <- ggplot(perfis_top,
                   aes(x = chi2, y = reorder(feature, chi2))) +
  geom_col(fill = "steelblue") +
  facet_wrap(~ classe, scales = "free_y", ncol = 3) +
  labs(title = "Lemas mais característicos por classe Reinert (chi²)",
       x = "chi²", y = NULL) +
  theme_minimal(base_size = 10) +
  theme(strip.text = element_text(face = "bold"))

ggsave(file.path(dir_saida, "reinert_perfis_classes.png"),
       g_perfis, width = 14, height = 9, dpi = 150)

# ---- 5. AFC sobre a tabela lema x classe -----------------------------------
# Agrega o dfm pelas classes Reinert, fica uma tabela de contingência
# (lemas linhas, classes colunas) para a CA do FactoMineR. Equivale ao
# plano fatorial do IRaMuTeQ (eixos 1-2, com lemas posicionados).

dfm_por_classe <- dfm_group(dtm, groups = docvars(dtm, "classe_reinert"))
mat_lc <- t(as.matrix(dfm_por_classe))   # linhas = lemas, colunas = classes
colnames(mat_lc) <- paste0("classe_", seq_len(ncol(mat_lc)))

# Restringe às N lemas com maior soma para gráfico legível.
top_n <- 250
soma <- rowSums(mat_lc)
mat_lc_top <- mat_lc[order(-soma)[seq_len(min(top_n, nrow(mat_lc)))], ]

res_ca <- CA(mat_lc_top, graph = FALSE)

# Coordenadas dos lemas (linhas) e das classes (colunas).
df_lemas <- as.data.frame(res_ca$row$coord[, 1:2])
df_lemas$lemma <- rownames(df_lemas)
df_classes <- as.data.frame(res_ca$col$coord[, 1:2])
df_classes$classe <- rownames(df_classes)

# Associa cada lema à classe onde sua contribuição é maior, para colorir.
contrib_lema <- res_ca$row$contrib
df_lemas$classe_dom <- paste0("classe_",
                              apply(mat_lc_top, 1, which.max))

inercia <- res_ca$eig[1:2, "percentage of variance"]

g_afc <- ggplot(df_lemas,
                aes(x = `Dim 1`, y = `Dim 2`, label = lemma,
                    color = classe_dom)) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey60") +
  geom_vline(xintercept = 0, linetype = "dashed", color = "grey60") +
  geom_text_repel(size = 3, max.overlaps = 200,
                  segment.color = NA, show.legend = FALSE) +
  geom_label(data = df_classes,
             aes(x = `Dim 1`, y = `Dim 2`, label = classe),
             inherit.aes = FALSE,
             fill = "black", color = "white", fontface = "bold",
             size = 4) +
  labs(x = sprintf("fator 1 (%.2f %%)", inercia[1]),
       y = sprintf("fator 2 (%.2f %%)", inercia[2]),
       title = "AFC sobre classes Reinert, corpus Latour 1986-1999",
       color = "classe dominante") +
  theme_minimal(base_size = 12)

ggsave(file.path(dir_saida, "afc_classes_reinert.png"),
       g_afc, width = 12, height = 9, dpi = 150)

# ---- 6. AFC complementar lema x obra (trajetória 1986-1999) ----------------
# Esta é a AFC que conversa diretamente com o argumento do capítulo 2:
# como o vocabulário se desloca entre as três obras no plano fatorial.

dfm_por_obra <- dfm_group(dtm, groups = docvars(dtm, "obra"))
mat_lo <- t(as.matrix(dfm_por_obra))
mat_lo_top <- mat_lo[order(-rowSums(mat_lo))[seq_len(min(top_n, nrow(mat_lo)))], ]

res_ca_obra <- CA(mat_lo_top, graph = FALSE)
df_l2 <- as.data.frame(res_ca_obra$row$coord[, 1:2])
df_l2$lemma <- rownames(df_l2)
df_o2 <- as.data.frame(res_ca_obra$col$coord[, 1:2])
df_o2$obra <- rownames(df_o2)
inercia_o <- res_ca_obra$eig[1:2, "percentage of variance"]

g_afc_obra <- ggplot(df_l2,
                     aes(x = `Dim 1`, y = `Dim 2`, label = lemma)) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey60") +
  geom_vline(xintercept = 0, linetype = "dashed", color = "grey60") +
  geom_text_repel(size = 3, max.overlaps = 200,
                  segment.color = NA, color = "grey30") +
  geom_label(data = df_o2,
             aes(x = `Dim 1`, y = `Dim 2`, label = obra),
             inherit.aes = FALSE,
             fill = "firebrick", color = "white", fontface = "bold",
             size = 5) +
  labs(x = sprintf("fator 1 (%.2f %%)", inercia_o[1]),
       y = sprintf("fator 2 (%.2f %%)", inercia_o[2]),
       title = "AFC sobre obras, corpus Latour 1986-1999") +
  theme_minimal(base_size = 12)

ggsave(file.path(dir_saida, "afc_obras.png"),
       g_afc_obra, width = 12, height = 9, dpi = 150)

# ---- 7. exportações tabulares ----------------------------------------------

readr::write_csv(tibble::rownames_to_column(as.data.frame(res_ca$row$coord),
                                             "lemma"),
                 file.path(dir_saida, "afc_classes_coordenadas_lemas.csv"))
readr::write_csv(tibble::rownames_to_column(as.data.frame(res_ca$col$coord),
                                             "classe"),
                 file.path(dir_saida, "afc_classes_coordenadas_classes.csv"))
readr::write_csv(tibble::rownames_to_column(as.data.frame(res_ca_obra$row$coord),
                                             "lemma"),
                 file.path(dir_saida, "afc_obras_coordenadas_lemas.csv"))
readr::write_csv(tibble::rownames_to_column(as.data.frame(res_ca_obra$col$coord),
                                             "obra"),
                 file.path(dir_saida, "afc_obras_coordenadas_obras.csv"))

# Distribuição de classes por obra: tabela de contingência em R base
# (evita NSE do dplyr e pipe nativo, que falharam nesta combinação de
# versões instaladas).
distrib_tab <- table(obra           = docvars(dtm, "obra"),
                     classe_reinert = docvars(dtm, "classe_reinert"))
distrib_df  <- as.data.frame.matrix(distrib_tab)
names(distrib_df) <- paste0("classe_", names(distrib_df))
distrib_df  <- cbind(obra = rownames(distrib_df), distrib_df)
rownames(distrib_df) <- NULL
readr::write_csv(distrib_df,
                 file.path(dir_saida, "distribuicao_classes_por_obra.csv"))

cat("\nConcluído. Saídas em:", dir_saida, "\n")
install.packages("tidyr", repos = "https://cloud.r-project.org")

