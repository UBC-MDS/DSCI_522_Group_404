# Docker file for Group_404
# Lori Fang, Feb, 2020

FROM rocker/tidyverse

# then install the R packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  && install2.r --error \
    --deps TRUE \
    readr \
    docopt \
    RCurl \
    testthat

# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# get python package dependencies
RUN apt-get install -y python3-tk

# install python packages
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install docopt 
RUN pip3 install requests 
RUN pip3 install scikit-learn 
RUN pip3 install altair 
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*
