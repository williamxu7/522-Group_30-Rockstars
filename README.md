# Strathcona County Housing Price Predictor
* authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu

A data analysis project on Property Assessment Prediction for Single-Family Dwellings in Strathcona County for DSCI 522 (Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About

The data set used in our project are [2018 property assessments](https://data.strathcona.ca/Housing-Buildings/2018-Property-Tax-Assessment/6wvk-j7e9) , restricted strictly for single-family dwellings in Strathcona County, Alberta (“2018 Property Tax Assessment”). Each row in the data set represents a distinct property within Strathcona Counties borders, and each column represents a potential explanatory variable, along with our dependent variable (property assessment value). Our set of explanatory variables is composed of continuous, categorical, and binary data types, these being: Building Size, Building Description, Age of Property, Year Built, Presence of Basement, Presence of Furnished Basement, Presence of Garage, Presence of Fireplace, and Longitude and Latitude. Altogether our dataset is composed of 28,450 observations.
To get an accurate assessment of our predictive model, we build a training model using 90% of our observations, and reserve the remaining 10% as test data to assess goodness of fit.

## Report
The final report can be found [here](http://htmlpreview.github.io/?https://raw.githubusercontent.com/UBC-MDS/522-Group_30-Rockstars/main/doc/strathcona_housing_price_predict_report.html).

## Usage
To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) below. Finally, run the following commands in terminal from the root directory of this project:

```
# download data
python src/download_data.py --url=https://data.strathcona.ca/api/views/c9fr-ivqf/rows.csv?accessType=DOWNLOAD --out_file=data/2018_Property_Tax_Assessment.csv

# preprocess data
python src/data_cleaning.py --in_file=data/2018_Property_Tax_Assessment.csv --out_file1=data/2018_Property_Tax_Assessment_clean.csv --out_file2=data/2018_Property_Tax_Assessment_clean_train.csv --out_file3=data/2018_Property_Tax_Assessment_clean_test.csv

# create exploratory data analysis figure and write to file 
python src/eda_script.py --in_file1=data/2018_Property_Tax_Assessment_clean.csv --in_file2=data/2018_Property_Tax_Assessment_clean_train.csv --output_file=results/

# tune and test model
python src/housing_assessment_prediction.py --in_file1=data/2018_Property_Tax_Assessment_clean_train.csv --in_file2=data/2018_Property_Tax_Assessment_clean_test.csv --out_file1=results/validation_table.csv --out_file2=results/test_score.csv --out_file3=results/coefficients_table.csv

# render final model
Rscript -e "rmarkdown::render('doc/strathcona_housing_price_predict_report.Rmd')"
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
  - tidyverse==1.3.0

## License
The Strathcona County Housing Price Predictor materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References
“2018 Property Tax Assessment”. Strathcona County’s Open Data Portal. https://data.strathcona.ca/Housing-Buildings/2018-Property-Tax-Assessment/6wvk-j7e9
