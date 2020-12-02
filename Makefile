# Makefile
# Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu, Dec 2020

# This driver script runs our script 1 to script 5 for the project.

# example usage:
# make data/2018_Property_Tax_Assessment_clean.csv data/2018_Property_Tax_Assessment_clean_train.csv data/2018_Property_Tax_Assessment_clean_test.csv results/ 

all : doc/count_report.md

# download data
data/2018_Property_Tax_Assessment.csv : src/download_data.py
	python src/download_data.py --url=https://data.strathcona.ca/api/views/c9fr-ivqf/rows.csv?accessType=DOWNLOAD --out_file=data/2018_Property_Tax_Assessment.csv
	
# preprocess data
data/2018_Property_Tax_Assessment_clean.csv data/2018_Property_Tax_Assessment_clean_train.csv data/2018_Property_Tax_Assessment_clean_test.csv : data/2018_Property_Tax_Assessment.csv src/data_cleaning.py
	python src/data_cleaning.py --in_file=data/2018_Property_Tax_Assessment.csv --out_file1=data/2018_Property_Tax_Assessment_clean.csv --out_file2=data/2018_Property_Tax_Assessment_clean_train.csv --out_file3=data/2018_Property_Tax_Assessment_clean_test.csv
	
# create exploratory data analysis figure and write to file 
results/ : data/2018_Property_Tax_Assessment_clean_train.csv data/2018_Property_Tax_Assessment_clean.csv src/eda_script.py
	python src/eda_script.py --in_file1=data/2018_Property_Tax_Assessment_clean.csv --in_file2=data/2018_Property_Tax_Assessment_clean_train.csv --output_file=results/	

clean :
	rm -rf data/2018_Property_Tax_Assessment.csv 
	rm -rf data/2018_Property_Tax_Assessment_clean.csv data/2018_Property_Tax_Assessment_clean_train.csv data/2018_Property_Tax_Assessment_clean_test.csv
	rm -rf results/ 