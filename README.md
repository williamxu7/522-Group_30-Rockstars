# Strathcona County Housing Price Predictor
* authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu

A data analysis project on Property Assessment Prediction for Single-Family Dwellings in Strathcona County for DSCI 522 (Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## Introduction

The data set used in this project is 2018 Property Tax Assessment from the Open Data portal of Strathcona County, Alberta. It is based on a property valuation date as of July 1, 2017 and property condition date as of December 31, 2017. Each row in the data set represents a property in Strathcona County, and each column represents an attribute of that property (e.g., building size, year built, does it have a fireplace, etc.)

For this project we are trying to answer the question: can we build a prediction model of single-family dwelling property assessment values in Strathcona County based on property features? It is important because it can give those who are interested in buying or selling single family dwellings in that area a sense of the value of houses.

To answer the predictive question, we are planning to build a number of predictive regression model candidates and choose the model with the best accuracy. We plan to partition the data with train test split (90%:10%). Our exploratory data analysis will include creating a heatmap table to summarize the correlation of features and our target, as well as scatterplots for individual features and the target. 

Our data pipeline modelling will use a ColumnTransformer to apply different transformations to different feature data types. For example, some of our variables take on values of “Yes/No” and need to be converted to 0’s and 1’s. We also have a categorical feature that will need to be converted to a set of dummy variable features via One-Hot-Encoder. Given that our target (property assessment value) is continuous, there are a couple of modelling approaches. This includes modelling via multi-variable linear regression and modeling via the Ridge method. In Ridge, we will do a hyperparameter optimization to find an alpha that works best for prediction accuracy and control the fundamental tradeoff in our model. Next, we will compare linear regression with Ridge, analyze results, and select a model with better validation accuracy. 

When we have the final model chosen, we will fit on the train data set, and evaluate performance with different loss-function metrics such as R2 and MAPE scores, mean squared error (MSE), root mean squared error (RMSE). The values will be saved in a dataframe and presented in our final report.

Our results will be made available in a R Markdown File. Components will include the predicted regression equation and a table of metrics related to the accuracy of our models.

We have conducted some preliminary exploratory data analysis, and it can be found [here](src/housing_pred_eda.ipynb).


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
   - vega-datasets==0.8.0
- R version 4.0.2 and R packages:
  - knitr==1.29

## License
The Strathcona County Housing Price Predictor materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References
“2018 Property Tax Assessment”. Strathcona County’s Open Data Portal. <https://data.strathcona.ca/Housing-Buildings/2018-Property-Tax-Assessment/6wvk-j7e9>
