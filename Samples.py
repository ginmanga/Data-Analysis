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

FUNDABS = pd.read_csv(os.path.join(datadirectory, "BS1DF-ready-Dec24.csv.gz"))
FUNDABS['datadate'] = pd.to_datetime(FUNDABS['datadate'])
FUNDABS['UR'] = 1-FUNDABS['RATED']
FUNDABS['size'] = np.log(FUNDABS['AT'])
print(len(FUNDABS))  # 376348 376817 156014 144308
FUNDABS = FUNDABS.drop_duplicates()
FUNDABS = FUNDABS.drop_duplicates(subset=['gvkey', 'fyear'])
print(len(FUNDABS))  # 376348 376817 154263 142759
FUNDABS = FUNDABS.replace([np.inf, -np.inf], np.nan)





sample_stats_desc = ['AT_cut', 'size', 'MVBook_cut', 'DIVP', 'PROF_cut', 'CASH_cut', 'TANG_cut', 'CAPEX_cut', 'ADVERT_cut',
                     'RD_cut', 'MLEV_cut', 'BLEV_cut', 'AP_cut', 'income_std_12_cut', 'income_std_9_cut',
                     'sale_std_12_cut', 'sale_std_9_cut',  'sale_std_ff48_12_1', 'sale_std_ff48_9',
                     'sale_std_ff48_12_2', 'sale_std_ff48_4', 'FF48', 'sic_ch', 'AGE', 'HH1', 'HH2', 'HH1_IQ', 'HH2_IQ',
                     'SHORT_CPCT', 'SUBNOTCONV_CPCT', 'SUBCONV_CPCT', 'DD_CPCT', 'DN_CPCT', 'SBN_CPCT', 'SUB_CPCT',
                     'BD_CPCT', 'CL_CPCT']

sample_stats_desc_C = ['AT_cut', 'size', 'MVBook_cut', 'DIVP', 'PROF_cut', 'CASH_cut', 'TANG_cut', 'CAPEX_cut',
                       'ADVERT_cut', 'RD_cut', 'MLEV_cut', 'BLEV_cut', 'AP_cut',  'HH1', 'HH2',  'income_std_12_cut',
                       'income_std_9_cut', 'income_std_4_cut', 'sale_std_12_cut', 'sale_std_9_cut',
                       'sale_std_ff48_12_1', 'sale_std_ff48_12_2', 'sale_std_ff48_9', 'sale_std_ff48_4', 'FF48',
                       'sic_ch', 'AGE', 'SHORT_CPCT', 'SUBNOTCONV_CPCT', 'SUBCONV_CPCT', 'DD_CPCT', 'DN_CPCT',
                       'SBN_CPCT', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT']

sample_stats_desc = ['AT_cut', 'size', 'MVBook_cut', 'DIVP', 'PROF_cut', 'CASH_cut', 'TANG_cut', 'CAPEX_cut',
                     'ADVERT_cut', 'RD_cut', 'MLEV_cut', 'BLEV_cut', 'AP_cut', 'income_std_12_cut', 'income_std_9_cut',
                     'income_std_4_cut', 'sale_std_12_cut', 'sale_std_9_cut', 'sale_std_ff48_12_1',
                     'sale_std_ff48_12_2', 'sale_std_ff48_9', 'sale_std_ff48_4', 'FF48', 'sic_ch', 'AGE', 'HH1', 'HH2',
                     'HH1_IQ', 'HH2_IQ', 'SHORT_CPCT', 'SUBNOTCONV_CPCT', 'SUBCONV_CPCT', 'DD_CPCT', 'DN_CPCT',
                     'SBN_CPCT', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT']

sample_stats_desc_un = ['AT', 'MVBook', 'PROF', 'CASH', 'TANG', 'CAPEX', 'ADVERT', 'RD', 'MLEV', 'BLEV', 'AP']
sample_stats_desc_iq = ['CP_IQPCT', 'DC_IQPCT', 'TL_IQPCT', 'SBN_IQPCT', 'SUB_IQPCT', 'CL_IQPCT', 'OTHER_IQPCT',
                        'BDIQ', 'BDCP']

ratings = ['D', 'C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
ratings_1 = ['UR', 'C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
ratings_g = ['UR', 'LJUNK', 'HJUNK', 'LIG', 'HIG']

FUNDABS = FUNDABS.replace([np.inf, -np.inf], np.nan)

FUNDABS['SAMPLE'] = np.where((FUNDABS.HH2 <= 1.1) & (FUNDABS.TOTALDEBT_C >= 0) & (FUNDABS.HH2 >= 0), 1, 0)
FUNDABS['SAMPLE_TIME'] = np.where(FUNDABS['fyear'] >= 1969, 1, 0)



FUNDABS_desc = FUNDABS[FUNDABS[['NOTMISSING', 'SAMPLE', 'EXCHANGE', 'USCOMMON']].all(axis='columns')]
print(len(FUNDABS_desc))  # 153294 154263 142759


#CAPIQ


FUNDIQ = pd.read_csv(os.path.join(datadirectory, "IQ-ready-DEC24.csv.gz"))
FUNDIQ['datadate'] = pd.to_datetime(FUNDIQ['datadate'])

FUNDIQ = FUNDIQ.sort_values(by=['gvkey', 'datadate'])
FUNDIQ = FUNDIQ.reset_index(drop=True)

FUNDIQ['SAMPLE'] = np.where((FUNDIQ.HH1_IQ <= 1.1) & (FUNDIQ.TOTALDEBT_C >= 0) & (FUNDIQ.HH1_IQ >= 0)
                               & (FUNDIQ.CHECK_IQ <= 0.1), 1, 0)

FUNDIQ['SAMPLE_TIME'] = np.where(FUNDIQ['fyear'] >= 2002, 1, 0)

list_sum = ['CP_IQ','DC_IQ','TL_IQ','SBN_IQ', 'SUB_IQ', 'CL_IQ', 'OTHER_IQ']
FUNDIQ = Functions.pct_calculator(list_sum, 'TOTALDEBT_C', 'PCT', FUNDIQ)

FUNDIQ['BDIQ'] = FUNDIQ['DC_IQPCT'] + FUNDIQ['TL_IQPCT']
FUNDIQ['BDCP'] = FUNDIQ['SHORT_CPCT'] + FUNDIQ['BD_CPCT']
FUNDIQ['UR'] = 1 - FUNDIQ['RATED']
FUNDIQ['size'] = np.log(FUNDIQ['AT'])


print(len(FUNDIQ))  # 66521 38816 33578
FUNDIQ = FUNDIQ.drop_duplicates()
print(len(FUNDIQ))  #66521 36735 32193
FUNDIQ = FUNDIQ.drop_duplicates(subset=['gvkey', 'fyear'])
print(len(FUNDIQ))  #66501 66521 36735 32193
FUNDIQ = FUNDIQ.replace([np.inf, -np.inf], np.nan)




FUNDIQ['HH1'] = np.where(FUNDIQ.HH1_IQ.isnull(), np.NaN, FUNDIQ['HH1'])
FUNDIQ['HH2'] = np.where(FUNDIQ.HH1_IQ.isnull(), np.NaN, FUNDIQ['HH2'])
FUNDIQ['HH1_IQ'] = np.where(FUNDIQ.fyear < 2002, np.NaN, FUNDIQ['HH1_IQ'])
FUNDIQ['HH2_IQ'] = np.where(FUNDIQ.fyear < 2002, np.NaN, FUNDIQ['HH2_IQ'])
FUNDIQ['HH1'] = np.where(FUNDIQ.fyear < 2002, np.NaN, FUNDIQ['HH1'])
FUNDIQ['HH2'] = np.where(FUNDIQ.fyear < 2002, np.NaN, FUNDIQ['HH2'])

print(len(FUNDIQ)) # 66521 36735 32193
FUNDIQ_desc = FUNDIQ[FUNDIQ[['NOTMISSING', 'SAMPLE', 'EXCHANGE', 'USCOMMON', 'SAMPLE_TIME']].all(axis='columns')]
FUNDIQ_desc2 = FUNDIQ[FUNDIQ[['NOTMISSING', 'SAMPLE_TIME', 'EXCHANGE', 'USCOMMON']].all(axis='columns')]
FUNDIQ_desc = FUNDIQ_desc.reset_index(drop=True)
FUNDIQ_desc2 = FUNDIQ_desc2.reset_index(drop=True)
print(len(FUNDIQ_desc))  # 36204 36577 6735 32193

id = ['gvkey', 'datadate', 'fyear', 'NOTMISSING', 'SAMPLE', 'SAMPLE_TIME', 'EXCHANGE', 'USCOMMON', 'TOTALDEBT_C']
id.extend(sample_stats_desc)
id.extend(sample_stats_desc_un)
id.extend(sample_stats_desc_iq)
id.extend(ratings)
id.extend(ratings_g)
print(id)
FUNDIQ_short = FUNDIQ[id]
FUNDIQ_desc = FUNDIQ_desc[id]
FUNDIQ_desc2 = FUNDIQ_desc2[id]


FUNDIQ_desc[['AT_cut', 'AT']].describe()
FUNDIQ_desc[['AT_cut', 'AT']].quantile(0.99)
FUNDIQ_desc[['PROF_cut', 'PROF']].describe()
FUNDIQ_desc[['MVBook_cut', 'MVBook']].describe()
FUNDIQ_desc[['HH1', 'HH2', 'HH1_IQ', 'HH2_IQ']].describe()




##### Lag exogenous variables and print the dan thing
FUNDIQ_lag = FUNDIQ[id]
FUNDIQ_lag = FUNDIQ_lag[FUNDIQ_lag.fyear >= 2001]
FUNDIQ_lag = Functions.winsor(FUNDIQ_lag, column=['size'], cond_list=['NOTMISSING', 'SAMPLE_TIME', 'EXCHANGE', 'USCOMMON'],
                              cond_num=[1, 1, 1, 1], quantiles=[0.99, 0.01], year=2001)

print(FUNDIQ_lag['size'].describe())
print(FUNDIQ_lag['size_cut'].describe())

list_to_lag = ['gvkey', 'AT_cut', 'size_cut', 'size', 'MVBook_cut', 'DIVP', 'PROF_cut', 'CASH_cut', 'TANG_cut',
               'CAPEX_cut', 'ADVERT_cut', 'RD_cut', 'MLEV_cut', 'BLEV_cut', 'AP_cut', 'income_std_12_cut',
               'income_std_9_cut', 'income_std_4_cut', 'sale_std_12_cut', 'sale_std_9_cut', 'sale_std_ff48_12_1',
               'sale_std_ff48_12_2', 'sale_std_ff48_9', 'sale_std_ff48_4', 'D', 'C', 'B', 'BB', 'BBB', 'A', 'AA',
               'AAA', 'UR', 'LJUNK', 'HJUNK', 'LIG', 'HIG']

for i in list_to_lag:
    name = i + '_lag'
    FUNDIQ_lag[name] = FUNDIQ_lag.groupby('gvkey')[i].shift(1)

FUNDIQ_lag = FUNDIQ_lag.dropna(subset=['HH1_IQ', 'size_cut_lag'])
FUNDIQ_lag = FUNDIQ_lag[FUNDIQ_lag[['NOTMISSING', 'SAMPLE', 'EXCHANGE', 'USCOMMON', 'SAMPLE_TIME']].all(axis='columns')]




##### Lag exogenous variables and print the dan thing

id = ['gvkey', 'datadate', 'fyear', 'NOTMISSING', 'SAMPLE', 'SAMPLE_TIME', 'EXCHANGE', 'USCOMMON', 'TOTALDEBT_C']
id.extend(sample_stats_desc_C)
id.extend(sample_stats_desc_un)
id.extend(ratings)
id.extend(ratings_g)
print(id)

FUNDABS_lag = FUNDABS[id]
FUNDABS_lag = FUNDABS_lag[FUNDABS_lag.fyear >= 1968]
FUNDABS_lag = Functions.winsor(FUNDABS_lag, column=['size'],
                               cond_list=['NOTMISSING', 'SAMPLE_TIME', 'EXCHANGE', 'USCOMMON'],
                               cond_num=[1, 1, 1, 1], quantiles=[0.99, 0.01], year=2001)

print(FUNDABS_lag['size'].describe())
print(FUNDABS_lag['size_cut'].describe())

list_to_lag = ['gvkey', 'AT_cut', 'size_cut', 'size', 'MVBook_cut', 'DIVP', 'PROF_cut', 'CASH_cut', 'TANG_cut',
               'CAPEX_cut', 'ADVERT_cut', 'RD_cut', 'MLEV_cut', 'BLEV_cut', 'AP_cut', 'income_std_12_cut',
               'income_std_9_cut', 'income_std_4_cut', 'sale_std_12_cut', 'sale_std_9_cut', 'sale_std_ff48_12_1',
               'sale_std_ff48_12_2', 'sale_std_ff48_9', 'sale_std_ff48_4', 'D', 'C', 'B', 'BB', 'BBB', 'A', 'AA',
               'AAA', 'UR', 'LJUNK', 'HJUNK', 'LIG', 'HIG']

for i in list_to_lag:
    name = i + '_lag'
    FUNDABS_lag[name] = FUNDABS_lag.groupby('gvkey')[i].shift(1)

FUNDABS_lag = FUNDABS_lag.dropna(subset=['HH2', 'size_cut_lag'])
FUNDABS_lag = FUNDABS_lag[FUNDABS_lag[['NOTMISSING', 'SAMPLE', 'EXCHANGE', 'USCOMMON', 'SAMPLE_TIME']].all(axis='columns')]

#Time periods







# save to csv file and run in R
FUNDIQ_R = FUNDIQ[id]
print(len(FUNDIQ_R))
FUNDIQ_R = FUNDIQ_R.drop_duplicates(subset=['gvkey', 'fyear'])
print(len(FUNDIQ_R))
FUNDIQ_R.to_csv(os.path.join(datadirectory, "FUNDIQR.csv"), index=False)


FUNDIQ_RC = FUNDIQ_R[FUNDIQ_R.fyear < 2002]