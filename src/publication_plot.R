
df <- read_tsv('mauceli.raw', col_names = "authors")

int <- 5
up <- 40

fr <- seq(0, up, by = int)

tb <- df %>% pull(authors) %>% table


for (f in fr) {
  tb[which(tb >= f & tb < (f + int))] %>% print
}

dc <- tibble(authors = names(tb), count = tb)

dc %<>% arrange(desc(count))

write.csv(as.data.frame(dc), 'mauceli.csv', quote = F, row.names = F)

