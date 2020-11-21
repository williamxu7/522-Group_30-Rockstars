# Strathcona County Housing Price Predictor
* authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu

## Introduction
Property Assessment Prediction for Single-Family Dwellings in Strathcona County

The data set used in this project is 2020 Property Tax Assessment from the Open Data portal of Strathcona County, Alberta. It is based on a property valuation date as of July 1, 2017 and property condition date as of December 31, 2017. Each row in the data set represents a property in Strathcona County, and each column represents an attribute of that property (e.g., building size, year built, does it have a fireplace, etc.)

For this project we are trying to answer the question: can we build a prediction model of single-family dwelling property assessment values in Strathcona County based on property features? It is important because it can give those who are interested in buying or selling single family dwellings in that area a sense of the value of houses.

To answer the predictive question, we are planning to build a number of predictive regression model candidates and choose the model with the best accuracy. We plan to partition the data with train test split (90%:10%). Our exploratory data analysis will include creating a heatmap table to summarize the correlation of features and our target, as well as scatterplots for individual features and the target. 

Our data pipeline modelling will use a ColumnTransformer to apply different transformations to different feature data types. For example, some of our variables take on values of “Yes/No” and need to be converted to 0’s and 1’s. We also have a categorical feature that will need to be converted to a set of dummy variable features via One-Hot-Encoded Given that our target (property assessment value) is continuous, there are a couple of modelling approaches. This includes modelling via multi-variable linear regression and modeling via the Ridge method. In Ridge, we will do a hyperparameter optimization to find an alpha that works best for prediction accuracy and control the fundamental tradeoff in our model. Next, we will compare linear regression with Ridge, analyze results, and select a model with better validation accuracy. 

When we have the final model chosen, we will fit on the train data set, and evaluate performance with different loss-function metrics such as R2 and MAPE scores, mean squared error (MSE), root mean squared error (RMSE). The values will be saved in a dataframe and presented in our final report.

Our results will be made available in a R Markdown File. Components will include the predicted regression equation and a table of metrics related to the accuracy of our models.

We have conducted some preliminary exploratory data analysis, and it can be found here.


## Usage

## Dependencies

## License
The Strathcona County Housing Price Predictor materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References
