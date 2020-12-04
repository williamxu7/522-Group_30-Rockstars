# authors: Cal Schafer, Daniel Ortiz, Jordan Lau, William Xu
# date: 2020-11-20

"""Downloads data csv data from the web to a local filepath.

Usage: download_data.py --url=<url> --out_file=<out_file> 
 
Options:
--url=<url>                    URL from where to download the data (must be in csv format)
--out_file=<out_file>          Path and filename where to locally write the file
"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

def main(url, out_file):
    data = pd.read_csv(url, header=None, low_memory = False)
    try:
        data.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index=False)



if __name__ == "__main__":
    main(opt["--url"], opt["--out_file"])
