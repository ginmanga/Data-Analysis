# Regs
from linearmodels.panel import PanelOLS
from linearmodels.panel import compare
from linearmodels.panel import PooledOLS
import statsmodels.api as sm
import pandas as pd
import numpy as np
import os
import Functions
import importlib

importlib.reload(Functions)


datadirectory = os.path.join(os.getcwd(), 'data')

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-DEC27.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-DEC27.csv.gz"))

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-Jan29.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-Jan29.csv.gz"))

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-Feb1.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-Feb1.csv.gz"))


# FUNDABS_descreg = FUNDABS_lag[FUNDABS_lag.fyear > 2001]
FUNDABS_descreg = FUNDABS_descreg.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDABS_descreg.fyear)
FUNDABS_descreg = FUNDABS_descreg.set_index(['FF48', 'fyear'])
FUNDABS_descreg['year'] = year

FUNDIQ_descreg = FUNDIQ_lag.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDIQ_descreg.fyear)
FUNDIQ_descreg = FUNDIQ_descreg.set_index(['FF48', 'fyear'])
FUNDIQ_descreg['year'] = year

FUNDABS_descreg['C/B'] = FUNDABS_descreg['LJUNK']
FUNDABS_descreg['BBB/A'] = FUNDABS_descreg['LIG']
FUNDABS_descreg['AA/AAA'] = FUNDABS_descreg['HIG']
FUNDABS_descreg['HHI-C8'] = FUNDABS_descreg['HH1']
FUNDABS_descreg['HHI-C5'] = FUNDABS_descreg['HH2']



#Size Quintiles

Size_1 = FUNDABS_descreg.groupby(['fyear'])[['at']].quantile(0.2)
Size_2 = FUNDABS_descreg.groupby(['fyear'])[['at']].quantile(0.4)
Size_3 = FUNDABS_descreg.groupby(['fyear'])[['at']].quantile(0.6)
Size_4 = FUNDABS_descreg.groupby(['fyear'])[['at']].quantile(0.8)
Size_5 = FUNDABS_descreg.groupby(['fyear'])[['at']].quantile(1)


Size_6 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(0.95)

FUNDABS_descreg['Size_1'] = 0
FUNDABS_descreg['Size_2'] = 0
FUNDABS_descreg['Size_3'] = 0
FUNDABS_descreg['Size_4'] = 0
FUNDABS_descreg['Size_5'] = 0

def size_sort2(x):
    if x['at'] <= Size_1.loc[x['fyear']][0]:
        x['Size_1'] = 1
    if Size_1.loc[x['fyear']][0] < x['at'] <= Size_2.loc[x['fyear']][0]:
        x['Size_2'] = 1
    if Size_2.loc[x['fyear']][0] < x['at'] <= Size_3.loc[x['fyear']][0]:
        x['Size_3'] = 1
    if Size_3.loc[x['fyear']][0] < x['at'] <= Size_4.loc[x['fyear']][0]:
        x['Size_4'] = 1
    if x['at'] > Size_4.loc[x['fyear']][0]:
        x['Size_5'] = 1
    return x

FUNDABS_descreg = FUNDABS_descreg.apply(lambda row: size_sort2(row), axis=1)

FUNDABS_descreg['Q1'] = FUNDABS_descreg['Size_1']
FUNDABS_descreg['Q2'] = FUNDABS_descreg['Size_2']
FUNDABS_descreg['Q3'] = FUNDABS_descreg['Size_3']
FUNDABS_descreg['Q4'] = FUNDABS_descreg['Size_4']
FUNDABS_descreg['Q5'] = FUNDABS_descreg['Size_5']




exog_vars_cut_1 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                 'RD_cut_lag', 'UR']

exog_vars_cut_2 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                 'RD_cut_lag', 'BLEV_cut_lag']

exog_vars_cut_2 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                 'RD_cut_lag', 'UR', 'BLEV_cut_lag']


exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                 'RD_cut_lag', 'UR']

exog_vars_cut_4 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                 'RD_cut_lag', 'UR', 'BLEV_cut_lag']


exog_vars_cut_5 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                 'RD_cut_lag', 'UR']

exog_vars_cut_5 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                 'RD_cut_lag', 'UR']

exog_vars_cut_6 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_10_FF48',
                 'RD_cut_lag', 'UR']

exog_vars_cut_7 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'cut_income_std_10_FF48',
                 'RD_cut_lag', 'UR']


b1 = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_1, exog_vars_cut_1)

b2 = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_2, exog_vars_cut_2)

b3 = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_3, exog_vars_cut_3)
b4 = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_4, exog_vars_cut_4)

endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']



exog_1 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_Q', 'R\&D exp.',
                 'Unrated']
exog_2 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_Q', 'R\&D exp.',
                 'Unrated',  'Book lev.']

exog_3 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_A', 'R\&D exp.',
                 'Unrated']
exog_4 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_A', 'R\&D exp.',
                 'Unrated', 'Book lev.']



a = Functions.prep_params(b)
Functions.write_file_latex_style(tables,
                                 "nrega1.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_1, Functions.prep_params(b1))),
                                 'w')

Functions.write_file_latex_style(tables,
                                 "nrega2.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_2, Functions.prep_params(b2))),
                                 'w')
Functions.write_file_latex_style(tables,
                                 "nrega3.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_3, Functions.prep_params(b3))),
                                 'w')
Functions.write_file_latex_style(tables,
                                 "nrega4.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_4, Functions.prep_params(b4))),
                                 'w')



b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg,
                              ['HH1_IQ', 'HH2_IQ', 'HH1_IQB', 'HH2_IQB', 'HH2', 'HH1'], ['HH2', 'HH1'],
                              exog_vars_cut_5, exog_vars_cut_5)


endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']
exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_A', 'R\&D exp.',
                 'Unrated']
Functions.write_file_latex_style(tables,
                                 "nrega6.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')


b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg,
                              ['HH1_IQ', 'HH2_IQ', 'HH1_IQB', 'HH2_IQB', 'HH2', 'HH1'], ['HH2', 'HH1'],
                              exog_vars_cut_6, exog_vars_cut_6, options=1)

endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']

exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_FF48', 'R\&D exp.',
                 'Unrated']
Functions.write_file_latex_style(tables,
                                 "nrega7.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')


b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg,
                              ['HH1_IQ', 'HH2_IQ', 'HH1_IQB', 'HH2_IQB', 'HH2', 'HH1'], ['HH2', 'HH1'],
                              exog_vars_cut_7, exog_vars_cut_7, options=1)

endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']

exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'CFV\_FF48CUT', 'R\&D exp.',
                 'Unrated']
Functions.write_file_latex_style(tables,
                                 "nrega8.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')



#### Add AP_cut


exog_vars_cut_8 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'AP_cut',
                   'income_std_10_FF48', 'RD_cut_lag', 'UR']

exog_vars_cut_9 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'AP_cut',
                   'cut_income_std_10_FF48', 'RD_cut_lag', 'UR']


b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_8, exog_vars_cut_8, options=1)
endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']

exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility',  'Accounts Payable', 'CFV\_FF48', 'R\&D exp.',
        'Unrated']
Functions.write_file_latex_style(tables,
                                 "nrega9.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')

exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'Accounts Payable', 'CFV\_FF48C', 'R\&D exp.',
        'Unrated']
b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_9, exog_vars_cut_9, options=1)
Functions.write_file_latex_style(tables,
                                 "nrega10.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')





exog_vars_cut_8 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'AP_cut',
                   'income_std_10_FF48', 'RD_cut_lag', 'UR', 'BLEV_cut_lag']

exog_vars_cut_9 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'AP_cut',
                   'cut_income_std_10_FF48', 'RD_cut_lag', 'UR', 'BLEV_cut_lag']


b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_8, exog_vars_cut_8, options=1)
endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']

exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility',  'Accounts Payable', 'CFV\_FF48', 'R\&D exp.',
        'Unrated', 'Book lev.']
Functions.write_file_latex_style(tables,
                                 "nrega11.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')

exog = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tagibility', 'Accounts Payable', 'CFV\_FF48C', 'R\&D exp.',
        'Unrated', 'Book lev.']
b = Functions.run_regressions(FUNDIQ_descreg, FUNDABS_descreg, ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1'], ['HH2', 'HH1'],
                    exog_vars_cut_9, exog_vars_cut_9, options=1)
Functions.write_file_latex_style(tables,
                                 "nrega12.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog, Functions.prep_params(b))),
                                 'w')


