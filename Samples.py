import datetime, csv
#from sas7bdat import SAS7BDAT
import pandas as pd
import pandasql as ps
import numpy as np
import gzip, os, csv
import datetime
import matplotlib.pyplot as plt
import Functions
import importlib

importlib.reload(Functions)
datadirectory = os.path.join(os.getcwd(), 'data')
dir_plots = os.path.join(os.getcwd(), 'plots')

FUNDABS = pd.read_csv(os.path.join(datadirectory, "BS1DF-ready-Dec20.csv.gz"))
FUNDABS['datadate'] = pd.to_datetime(FUNDABS['datadate'])
FUNDABS['UR'] = 1-FUNDABS['RATED']
print(len(FUNDABS))  # 376817 156014 144308
FUNDABS = FUNDABS.drop_duplicates()
print(len(FUNDABS))  # 376817 154263 142759

sample_stats_desc = ['AT_cut', 'MVBook_cut', 'DIVP', 'PROF_cut', 'CASH_cut',
                     'TANG_cut', 'CAPEX_cut', 'ADVERT_cut', 'RD_cut',
                     'MLEV_cut', 'BLEV_cut', 'AP_cut', 'income_std_12_at_cut',
                     'income_std_9_at_cut', 'sale_std_ff48_12_1', 'sale_std_ff48_9',
                     'sale_std_ff48_12_2', 'sale_std_ff48_4', 'FF48', 'sic_ch', 'AGE']

sample_stats_desc_un = ['AT', 'MVBook', 'PROF', 'CASH', 'TANG', 'CAPEX', 'ADVERT', 'RD', 'MLEV', 'BLEV', 'AP']

ratings = ['C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
ratings_1 = ['UR', 'C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
ratings_g = ['UR', 'LJUNK', 'HJUNK', 'LIG', 'HIG']



FUNDABS = FUNDABS.replace([np.inf, -np.inf], np.nan)

FUNDABS_desc = FUNDABS[FUNDABS[['NOTMISSING', 'SAMPLE', 'EXCHANGE', 'USCOMMON']].all(axis='columns')]
print(len(FUNDABS_desc))  # 153294 154263 142759

FUNDABS_desc[['AT_cut','AT']].describe()
FUNDABS_desc[['PROF_cut','PROF']].describe()
FUNDABS_desc[['HH1','HH2']].describe()


#CAPIQ


FUNDIQ = pd.read_csv(os.path.join(datadirectory, "IQ-ready-DEC20.csv.gz"))
FUNDIQ['datadate'] = pd.to_datetime(FUNDIQ['datadate'])

#FUNDIQ['BDIQ'] = FUNDIQ['DC_IQPCT'] + FUNDIQ['TL_IQPCT']
#FUNDIQ['BDCP'] = FUNDIQ['SHORT_CPCT'] + FUNDIQ['BD_CPCT']

FUNDIQ['UR'] = 1-FUNDIQ['RATED']
print(len(FUNDIQ)) #38816 33578
FUNDIQ = FUNDIQ.drop_duplicates()
print(len(FUNDIQ)) #36735 32193

FUNDIQ = FUNDIQ.replace([np.inf, -np.inf], np.nan)
print(len(FUNDIQ)) #36735 32193
FUNDIQ_desc = FUNDIQ[FUNDIQ[['NOTMISSING', 'SAMPLE', 'EXCHANGE', 'USCOMMON']].all(axis='columns')]
print(len(FUNDIQ_desc)) #36577 6735 32193

id = ['gvkey','datadate','fyear']
id.extend(sample_stats_desc)
id.extend(sample_stats_desc_un)
id.extend(ratings)
id.extend(ratings_g)
print(id)
FUNDIQ_desc = FUNDIQ_desc[id]