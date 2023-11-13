####################################################################################################

sorter <- function(raw, dir = 'data') {

  # if (dir == NULL) dir = 'data'

  df <- read_tsv(paste0(dir, '/', raw, '.raw'), col_names = "authors")

  int <- 5
  up <- dim(df)[1]

  fr <- seq(0, up, by = int)

  tb <- df %>% pull(authors) %>% table


  for (f in fr) {
    tb[which(tb >= f & tb < (f + int))] %>% print
  }

  dc <- tibble(authors = names(tb), count = tb)

  dc %<>% arrange(desc(count))

  write.csv(as.data.frame(dc), paste0(dir, '/', raw, '.csv'), quote = F, row.names = F)

}

####################################################################################################

sorter('grabherr')
sorter('mauceli')
sorter('rivas-carrillo')

####################################################################################################
