# Author: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu

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
