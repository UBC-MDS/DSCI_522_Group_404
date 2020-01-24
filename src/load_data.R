# Author: Group 404
# Date: 2020-01-19
#
"This script downloads a dataset from the internet and saves it to a local path. 
 This script takes two arguments: url and file path.

Usage: load_data.R <url1> <path1> 
" -> doc

library(readr)
library(docopt)
library(RCurl)
library(testthat)


opt <-  docopt(doc)

main <- function(url1, path1){
  download_data(url1, path1)
} 

#' download a dataset to a provided path
#'
#' @param url1 a string containing a valid url address
#' @param path1 a string containing a valid path
#' @return None
#' @examples
#' download_data('https://dl.dropboxusercontent.com/s/5o9gmtpq2q8cshp/flights.csv?dl=0', 'data/filename.csv')
download_data <-function(url1,path1){
  if(!is.character(url1)){
    stop("Url must be a string")
  } else if(!url.exists(url1)){
    stop("Url provided is not valid.")
  } else {
    # read in data
    data <- read_csv(url1)
    
    
    if(!is.character(path1)){
      stop("Path must be a string")
    } else {
      # write data file to path provided
      write.csv(data, file = path1) 
    }
  }
}



test_download_data <- function(){
  url_targ <-  "https://dl.dropboxusercontent.com/s/5o9gmtpq2q8cshp/flights.csv?dl=0"
  path_targ <- "/data/flights.csv"
  
  test_that("Invalid urls should throw an error", {
    expect_error(download_data(404, path_targ))
    expect_error(download_data("w.google.com",path_targ))
  })

  test_that("Invalid file paths should throw an error", {
    expect_error(download_data(url_targ, 404))

  })  
  
}
  
test_download_data()
  
main(opt$url1, opt$path1)
