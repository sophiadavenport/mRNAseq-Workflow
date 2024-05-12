library("DESeq2")

counts <- read.csv('results/verse_concat_filtered.csv', row.names = 'gene')

coldata <- data.frame(samples = colnames(counts), time = c(rep('AD', 2), rep('P0', 2), rep('P4', 2), rep('P7', 2)), row.names = 'samples')
coldata$time <- as.factor(coldata$time)
coldata$time <- relevel(coldata$time, ref='P0')

run_deseq <- function(count_dataframe, coldata, item1, item2) {
  dds <- DESeqDataSetFromMatrix(countData = count_dataframe, colData = coldata, design= ~time)
  
  deseq_dds <- DESeq(dds)

  res <- results(deseq_dds, contrast=c("time", item1, item2))
  
  return(res)
}

results <- run_deseq(counts, coldata, "AD", "P0")
#rows as column, give metadata cols that match, then merge

write.csv('results/deseq2_results.csv')