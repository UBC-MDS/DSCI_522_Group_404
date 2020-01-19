# author: Group 404
# date: 2020-01-19
#
"This script downloads a dataset from the internet and saves it to a local path. This script takes two arguments: url and file path.

Usage: load_data.R <url1> <path1>
" -> doc

library(readr)
library(docopt)

opt <-  docopt(doc)

main <- function(url1, path1){
  
  # read in data
  data <- read_csv(url1)

  write.csv(data, file = path1) 
  
}

main(opt$url1, opt$path1)