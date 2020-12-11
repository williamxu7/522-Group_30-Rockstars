# Strathcona County Housing Price Predictor
* authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu

A data analysis project on Property Assessment Prediction for Single-Family Dwellings in Strathcona County for DSCI 522 (Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About

The data set used in our project are [2018 property assessments](https://data.strathcona.ca/Housing-Buildings/2018-Property-Tax-Assessment/6wvk-j7e9) , restricted strictly for single-family dwellings in Strathcona County, Alberta (“2018 Property Tax Assessment”). Each row in the data set represents a distinct property within Strathcona Counties borders, and each column represents a potential explanatory variable, along with our dependent variable (property assessment value). Our set of explanatory variables is composed of continuous, categorical, and binary data types, these being: Building Size, Building Description, Age of Property, Year Built, Presence of Basement, Presence of Furnished Basement, Presence of Garage, Presence of Fireplace, and Longitude and Latitude. Altogether our dataset is composed of 28,450 observations.
To get an accurate assessment of our predictive model, we build a training model using 90% of our observations, and reserve the remaining 10% as test data to assess goodness of fit.

## Report
The final report can be found [here](http://htmlpreview.github.io/?https://raw.githubusercontent.com/UBC-MDS/522-Group_30-Rockstars/main/doc/strathcona_housing_price_predict_report.html).

## Usage

There are two suggested ways to run this analysis:

#### 1. Using Docker
*note - the instructions in this section also depends on running this in a unix shell (e.g., terminal or Git Bash)*

To replicate the analysis, install [Docker](https://www.docker.com/get-started). Then clone this GitHub repository and run the following command at the command line/terminal from the root directory of this project:

To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) below. Finally, run the following commands in terminal from the root directory of this project:

```
docker run --rm -v /$(pwd):/home/data_analysis_eg group30 make -C /home/data_analysis_eg all
```

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:

```
docker run --rm -v /$(pwd):/home/data_analysis_eg group30 make -C /home/data_analysis_eg clean
```

#### 2. Without using Docker

To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) listed below, and run the following command at the command line/terminal from the root directory of this project:

```
make all
```

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:

```
make clean
```

## Dependencies
- Python 3.8.6 and Python packages:
   - altair==4.1.0
   - altair_data_server==0.4.1
   - altair_saver==0.5.0
   - docopt==0.6.2
   - matplotlib==3.3.3
   - numpy==1.19.4
   - pandas==0.24.2
   - scikit-learn==0.23.2
   - seaborn==0.11.0
   - selenium==3.141.0
   - vega-datasets==0.8.0
   - XGBoost==1.2.0
- R version 4.0.2 and R packages:
  - knitr==1.30
  - rmarkdown==2.5
  - reticulate==1.18
  - tidyverse==1.3.0

## License
The Strathcona County Housing Price Predictor materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References
“2018 Property Tax Assessment”. Strathcona County’s Open Data Portal. https://data.strathcona.ca/Housing-Buildings/2018-Property-Tax-Assessment/6wvk-j7e9
