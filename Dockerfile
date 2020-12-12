# Dockerfile for Strathcona County Housing Price Predictor
# Author: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu
# Dec 2020

FROM jupyter/scipy-notebook

# Install Python 3 packages
RUN conda install -c conda-forge --quiet --yes \
    'altair==4.1.*' \
    'altair_data_server==0.4.*' \
    'altair_saver==0.5.*' \
    'docopt==0.6.*' \
    'numpy==1.19.*' \
    'selenium==3.141.*' \
    'XGBoost==1.2.*'

USER root    
    
# R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    unixodbc \
    unixodbc-dev \
    r-cran-rodbc \
    gfortran \
    gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Fix for devtools https://github.com/conda-forge/r-devtools-feedstock/issues/4
RUN ln -s /bin/tar /bin/gtar

USER $NB_UID

# Install R packages
RUN conda install -c conda-forge --quiet --yes \
    'r-base=4.0.3' \
    'r-tidyverse=1.3*' \
    'r-rmarkdown=2.5*' \
    'r-knitr=1.29.*' \
    'r-reticulate' \
    && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}"
