FROM jupyter/scipy-notebook

# Install Python 3 packages
RUN conda install -c conda-forge --quiet --yes \
    'altair==4.1.*' \
    'altair_data_server' \
    'altair_saver' \
    'docopt' \
    'numpy' \
    'selenium' \
    'XGBoost'