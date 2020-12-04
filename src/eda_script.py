# authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu
# date: 2020-11-27

"""Creates exploratory data visualizations and tables to eventually be used in final report

Usage: eda_script.py --in_file1=<in_file1> --in_file2=<in_file2> --output_file=<output_file>

Options:
--in_file1=<in_file1>           File path and filename of the input cleaned csv file 
--in_file2=<in_file2>           File path and filename of the input cleaned train csv file
--output_file=<output_file>     Path of where to locally write .PNG EDA figures
"""

import os
import pandas as pd
from docopt import docopt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from altair_saver import save
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(in_file1, in_file2, output_file):
    
    df = pd.read_csv(in_file1)
    train_df = pd.read_csv(in_file2)
    
    # Property assessment value distribution
    barchart = alt.Chart(df).mark_bar().encode(
    alt.X('ASSESSMENT', bin=alt.Bin(maxbins=60), scale=alt.Scale(domain=(0,2000000)), title='Assessment Value($)'),
    alt.Y('count()'),
    tooltip='count()')
    barchart.save(output_file + "barchart.png")
    
    # Train data information
    train_info = train_df.info()

    # Correlation map
    corrmat = df.corr(method='pearson')
    f, ax = plt.subplots(figsize=(8, 8))
    cormap = sns.heatmap(corrmat, vmax=1., square=True)
    correlation_map = cormap.get_figure()
    # plt.title("Correlation map", fontsize=16)
    correlation_map.savefig(output_file + 'corrmat.png')
    
    # Relationship between building sizes and assessed values
    df_bsav = train_df.groupby('BLDG_FEET').mean('ASSESSMENT')
    df_bsav = df_bsav.reset_index()

    alt.data_transformers.disable_max_rows()
    population = alt.Chart(train_df, title = "Relationship between building sizes and assessed values").mark_circle(color='grey').encode(
        alt.X('BLDG_FEET', title = "Building Size(fts)"),
        alt.Y('ASSESSMENT', title = "Assessment Value($)"))

    conditional = alt.Chart(df_bsav).mark_circle(opacity=0.3, color='blue').encode(
        alt.X('BLDG_FEET', title = "Building Size(fts)"),
        alt.Y('ASSESSMENT', title = "Assessment Value($)"))

    scatter = (population + conditional).configure_title(fontSize=17)
    scatter.save(output_file + "scatter.png")

    boxplot = (alt.Chart(train_df).mark_boxplot().encode(
        x=alt.X(alt.repeat(), type='nominal'),
        y='ASSESSMENT'
    ).properties(height=200, width=100
    ).repeat(['GARAGE', 'FIREPLACE', 'BASEMENT', 'BSMTDEVL']
    ))

    boxplot.save(output_file + "boxplot.png")

    
if __name__ == "__main__":
    main(opt["--in_file1"], opt["--in_file2"], opt["--output_file"])
