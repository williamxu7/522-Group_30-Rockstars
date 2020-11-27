# authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu
# date: 2020-11-27

"""Creates exploratory data visualizations and tables

Usage: eda_script.py --in_file1=<in_file1> --in_file2=<in_file2> --output_file=<output_file>

Options:
<in_file1>        File path (including filename) of the cleaned csv file 
<in_file2>        File path (including filename) of the cleaned train dataset file
<output_file>     Path of where to locally write the files
"""

import os
import pandas as pd
from docopt import docopt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data
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
    barchart.save(output_file + "barchart.svg")
    
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
    scatter.save(output_file + "scatter.svg")


    # Violin plots of binary features
    garage =(alt.Chart(train_df).transform_density(
        'ASSESSMENT',
        as_=['ASSESSMENT', 'density'],
        extent=[0, 1_600_000],
        groupby=['GARAGE']
    ).mark_area(orient='horizontal').encode(
        y=alt.Y('ASSESSMENT:Q'),
        color=alt.Color('GARAGE:N',legend=None),
        x=alt.X(
            'density:Q',
            stack='center',
            impute=None,
            title=None,
            axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
        ),
        column=alt.Column(
            'GARAGE:N',
            header=alt.Header(
                titleOrient='bottom',
                labelOrient='bottom',
                labelPadding=0,
            ),
        )
    ).properties(
        width=100
    ))
    
    fireplace = (alt.Chart(train_df).transform_density(
        'ASSESSMENT',
        as_=['ASSESSMENT', 'density'],
        extent=[0, 1_600_000],
        groupby=['FIREPLACE']
    ).mark_area(orient='horizontal').encode(
        y=alt.Y('ASSESSMENT:Q', title=''),
        color=alt.Color('FIREPLACE:N',legend=None),
        x=alt.X(
            'density:Q',
            stack='center',
            impute=None,
            title=None,
            axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
        ),
        column=alt.Column(
            'FIREPLACE:N',
            header=alt.Header(
                titleOrient='bottom',
                labelOrient='bottom',
                labelPadding=0,
            ),
        )
    ).properties(
        width=100
    ))
    
    
    basement = (alt.Chart(train_df).transform_density(
        'ASSESSMENT',
        as_=['ASSESSMENT', 'density'],
        extent=[0, 1_600_000],
        groupby=['BASEMENT']
    ).mark_area(orient='horizontal').encode(
        y=alt.Y('ASSESSMENT:Q', title=''),
        color=alt.Color('BASEMENT:N',legend=None),
        x=alt.X(
            'density:Q',
            stack='center',
            impute=None,
            title=None,
            axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
        ),
        column=alt.Column(
            'BASEMENT:N',
            header=alt.Header(
                titleOrient='bottom',
                labelOrient='bottom',
                labelPadding=0,
            ),
        )
    ).properties(
        width=100
    ))
    
    basementdevl = (alt.Chart(train_df).transform_density(
        'ASSESSMENT',
        as_=['ASSESSMENT', 'density'],
        extent=[0, 1_600_000],
        groupby=['BSMTDEVL']
    ).mark_area(orient='horizontal').encode(
        y=alt.Y('ASSESSMENT:Q', title=''),
        color=alt.Color('BSMTDEVL:N',legend=None),
        x=alt.X(
            'density:Q',
            stack='center',
            impute=None,
            title=None,
            axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
        ),
        column=alt.Column(
            'BSMTDEVL:N',
            header=alt.Header(
                titleOrient='bottom',
                labelOrient='bottom',
                labelPadding=0,
            ),
        )
    ).properties(
        width=100
    ))
    
    violinplot = alt.hconcat(garage, fireplace, basement, basementdevl).configure_facet(
        spacing=0
    ).configure_view(
        stroke=None
    )
    violinplot.save(output_file + "violinplot.svg")

if __name__ == "__main__":
    main(opt["--in_file1"], opt["--in_file2"], opt["--output_file"])
