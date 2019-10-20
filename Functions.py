import datetime, csv
#from sas7bdat import SAS7BDAT
import pandas as pd
import pandasql as ps
import numpy as np
import gzip, os, csv
import datetime
#want a function to get me a gvkey

def hhi_calculator(x, y, c, df):
    tt = [i + '_temp' for i in x]
    for i in x:
        df[i + '_temp'] = (df[i]/df[y])**2
    df[c] = df[tt].sum(axis=1)
    df[c] = (df[c]-(1/len(tt)))/(1-(1/len(tt)))
    return df.drop(tt, axis=1)

def pct_calculator(x, y, name, df):
    for i in x:
        df[i + name] = (df[i]/df[y])
    return df
