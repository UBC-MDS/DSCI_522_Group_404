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
RUN pip3 install jupyter_contrib_nbextensions
RUN pip3 install altair 
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*


# enable nbextension PythonMarkdown (not working...)
#RUN jupyter nbextension enable PythonMarkdown/main

# install lightGBM (code from: https://github.com/microsoft/LightGBM/blob/master/docker/dockerfile-python)

ARG CONDA_DIR=/opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        cmake \
        build-essential \
        gcc \
        g++ \
        git \
        wget && \
    # python environment
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    /bin/bash Miniconda3-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    export PATH="$CONDA_DIR/bin:$PATH" && \
    conda config --set always_yes yes --set changeps1 no && \
    # lightgbm
    conda install -q -y numpy scipy "scikit-learn<=0.21.3" pandas && \
    git clone --recursive --branch stable --depth 1 https://github.com/Microsoft/LightGBM && \
    cd LightGBM/python-package && python setup.py install && \
    # clean
    apt-get autoremove -y && apt-get clean && \
    conda clean -a -y && \
    rm -rf /usr/local/src/*
