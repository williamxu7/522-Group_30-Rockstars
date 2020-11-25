# authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu
# date: 2020-11-25

"""Downloads data csv data from the web to a local filepath as a csv.

Usage: data_cleaning.py --in_file=<in_file> --out_file=<out_file> 
 
Options:
<in_file>           Raw csv file path (downloaded from the website, must be in standard csv format)
<out_file>          Cleaned up data file path (in csv format)
"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

def main(in_file, out_file):
    
    data = pd.read_csv(in_file, skiprows = 1)
    data = data.query("ASSESSCLAS == 'Residential'")
    
    try:
        data.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index=False)



if __name__ == "__main__":
    main(opt["--in_file"], opt["--out_file"])
