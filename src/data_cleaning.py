# authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu
# date: 2020-11-26

"""Converts downloaded csv data into a cleaned data set.

Usage: data_cleaning.py --in_file=<in_file> --out_file1=<out_file1> 
                        --out_file2=<out_file2> --out_file3=<out_file3>
 
Options:
<in_file>        file path of the raw csv file 
<out_file1>      file path of the cleaned csv file
<out_file2>      file path of the train portion of the csv file
<out_file3>      file path of the test portion of the csv file

"""

import os
import pandas as pd
from docopt import docopt
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(in_file, out_file1, out_file2, out_file3):

    
    data = pd.read_csv(in_file, skiprows = 1)
    data = data.query("ASSESSCLAS == 'Residential'")
    data = data.drop(columns = ['the_geom', 'TAX_YEAR','ROLL_NUM', 'ADDRESS', 'BLDG_METRE'])
    data['AGE'] =  2018 - data['YEAR_BUILT']
    
    train_df, test_df = train_test_split(data, train_size = 0.9, random_state = 123)


    try:
        data.to_csv(out_file1, index=False)
    except:
        os.makedirs(os.path.dirname(out_file1))
        data.to_csv(out_file1, index=False)
        
        
    try:
        train_df.to_csv(out_file2, index=False)
    except:
        os.makedirs(os.path.dirname(out_file2))
        train_df.to_csv(out_file2, index=False)
        
    try:
        test_df.to_csv(out_file3, index=False)
    except:
        os.makedirs(os.path.dirname(out_file3))
        test_df.to_csv(out_file3, index=False)


if __name__ == "__main__":
    main(opt["--in_file"], opt["--out_file1"], opt["--out_file2"], opt["--out_file3"])
