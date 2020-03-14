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

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-March09.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-March04.csv.gz"))


FUNDABS_descreg = FUNDABS_lag
# FUNDABS_descreg = FUNDABS_lag[FUNDABS_lag.fyear > 2001]
FUNDABS_descreg['C/B'] = FUNDABS_descreg['LJUNK']
FUNDABS_descreg['BBB/A'] = FUNDABS_descreg['LIG']
FUNDABS_descreg['AA/AAA'] = FUNDABS_descreg['HIG']
FUNDABS_descreg['HHI-C8'] = FUNDABS_descreg['HH1']
FUNDABS_descreg['HHI-C5'] = FUNDABS_descreg['HH2']

FUNDABS_descreg['RATED'] = 1-FUNDABS_descreg['UR']

FUNDABS_descreg['NEGPROF'] = np.where(FUNDABS_descreg.PROF_cut_lag < 0, 1, 0)
FUNDIQ_lag['NEGPROF'] = np.where(FUNDIQ_lag.PROF_cut_lag < 0, 1, 0)

FUNDABS_descreg_short = FUNDABS_descreg[FUNDABS_descreg.fyear > 2001]
FUNDABS_descreg = FUNDABS_descreg.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDABS_descreg.fyear)
FUNDABS_descreg = FUNDABS_descreg.set_index(['FF48', 'fyear'])
FUNDABS_descreg['year'] = year



FUNDIQ_descreg = FUNDIQ_lag.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDIQ_descreg.fyear)
FUNDIQ_descreg = FUNDIQ_descreg.set_index(['FF48', 'fyear'])
FUNDIQ_descreg['year'] = year
FUNDIQ_descreg['RATED'] = 1-FUNDIQ_descreg['UR']
FUNDIQ_descreg['HHI-IQ7'] = FUNDIQ_descreg['HH1_IQ']
FUNDIQ_descreg['HHI-IQ6'] = FUNDIQ_descreg['HH2_IQ']



FUNDABS_descreg_short = FUNDABS_descreg_short.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDABS_descreg_short.fyear)
FUNDABS_descreg_short = FUNDABS_descreg_short.set_index(['FF48', 'fyear'])
FUNDABS_descreg_short['year'] = year



### DO A REGRESSION AS FOLLOWS:
### FULL SAMPLE COMPUSTAT (HHI-C5, HHI-C8) Full Sample Capital IQ (HHI-7) and equivalent compustat sample, typical regression

exog_vars_cut_1 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                   'RD_cut_lag', 'Unrated', 'BLEV_cut_lag']

exog_vars_cut_2 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag']

exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag', 'RATED']

exog_vars_cut_4 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag', 'AP_cut_lag', 'AREC_TOT_cut_lag', 'INV_TOT_cut_lag']

exog_vars_cut_5 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag', 'RATED', 'AP_cut_lag', 'AREC_TOT_cut_lag', 'INV_TOT_cut_lag']

dats = [FUNDIQ_descreg, FUNDABS_descreg_short, FUNDABS_descreg]
endog = [['HHI-IQ7'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8']]


b1 = Functions.run_regressions_a(FUNDIQ_descreg, FUNDABS_descreg_short, FUNDABS_descreg,
                               ['HHI-IQ7'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
                               exog_vars_cut_1, exog_vars_cut_1, exog_vars_cut_1)
b2 = Functions.run_regressions_a(FUNDIQ_descreg, FUNDABS_descreg_short, FUNDABS_descreg,
                               ['HHI-IQ7'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
                               exog_vars_cut_2, exog_vars_cut_2, exog_vars_cut_2)

b3 = Functions.run_regressions_a(FUNDIQ_descreg, FUNDABS_descreg_short, FUNDABS_descreg,
                               ['HHI-IQ7'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
                               exog_vars_cut_3, exog_vars_cut_3, exog_vars_cut_3)

b4 = Functions.run_regressions_a(FUNDIQ_descreg, FUNDABS_descreg_short, FUNDABS_descreg,
                               ['HHI-IQ7'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
                               exog_vars_cut_4, exog_vars_cut_4, exog_vars_cut_4)


b5 = Functions.run_regressions_a(FUNDIQ_descreg, FUNDABS_descreg_short, FUNDABS_descreg,
                               ['HHI-IQ7'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
                               exog_vars_cut_5, exog_vars_cut_5, exog_vars_cut_5)

endog = ['HHI-IQ7', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']

exog_1 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_Q', 'R\&D exp.', 'Book lev.']
exog_2 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.']

exog_3 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.', 'Rated']

exog_4 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.',
          'Accounts Payable', 'Accounts Receivable', 'Inventories']

exog_5 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.',
          'Rated', 'Accounts Payable', 'Accounts Receivable', 'Inventories']


Functions.write_file_latex_style(tables,
                                 "1.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_1, Functions.prep_params(b1))),
                                 'w')

Functions.write_file_latex_style(tables,
                                 "2.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_2, Functions.prep_params(b2))),
                                 'w')

Functions.write_file_latex_style(tables,
                                 "3.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_3, Functions.prep_params(b3))),
                                 'w')

Functions.write_file_latex_style(tables,
                                 "4.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_4, Functions.prep_params(b4))),
                                 'w')

Functions.write_file_latex_style(tables,
                                 "5.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_5, Functions.prep_params(b5))),
                                 'w')



# Do following regressions: Four different measures IQ Compustat, Capital IQ sample, Capital IQ with Compustat

FUNDIQ_descreg['HHI-C8'] = FUNDIQ_descreg['HH1']
FUNDIQ_descreg['HHI-C5'] = FUNDIQ_descreg['HH2']
FUNDIQ_descregCP = FUNDIQ_descreg.dropna(subset=['HHI-C5'])

exog_vars_cut_1 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                   'RD_cut_lag', 'UR', 'BLEV_cut_lag']

exog_vars_cut_2 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'UR', 'BLEV_cut_lag']

exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'UR', 'BLEV_cut_lag' , 'AP_cut_lag']

endog = [['HHI-IQ7', 'HHI-IQ6'], ['HHI-C5', 'HHI-C8'], ['HHI-IQ7', 'HHI-IQ6'], ['HHI-C5', 'HHI-C8']]



datas = [FUNDIQ_descregCP, FUNDIQ_descreg, FUNDIQ_descreg, FUNDABS_descreg_short]
b1 = Functions.run_regressions_4(datas, endog, exog_vars_cut_1)

endog = ['HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8','HHI-IQ7', 'HHI-IQ6', 'HHI-C5', 'HHI-C8']

exog_1 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_Q', 'R\&D exp.', 'Unrated', 'Book lev.']
exog_2 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Unrated', 'Book lev.']

Functions.write_file_latex_style(tables,
                                 "11.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_1, Functions.prep_params(b1))),
                                 'w')






# Do interaction between credit ratings and all of the variables
FUNDABS_descreg['C/B'] = FUNDABS_descreg['LJUNK']
FUNDABS_descreg['BBB/A'] = FUNDABS_descreg['LIG']
FUNDABS_descreg['AA/AAA'] = FUNDABS_descreg['HIG']
FUNDABS_descreg['UR'] = FUNDABS_descreg['UR']

FUNDABS_UR = FUNDABS_descreg[FUNDABS_descreg.UR == 1]
FUNDABS_LJUNK = FUNDABS_descreg[FUNDABS_descreg.LJUNK == 1]
FUNDABS_BB = FUNDABS_descreg[FUNDABS_descreg.BB == 1]
FUNDABS_BBB = FUNDABS_descreg[FUNDABS_descreg.BBB == 1]
FUNDABS_A = FUNDABS_descreg[FUNDABS_descreg.A == 1]
FUNDABS_LIG = FUNDABS_descreg[FUNDABS_descreg.LIG == 1]
FUNDABS_HIG = FUNDABS_descreg[FUNDABS_descreg.HIG == 1]

FUNDABS_URS = FUNDABS_descreg_short[FUNDABS_descreg_short.UR == 1]
FUNDABS_LJUNKS = FUNDABS_descreg_short[FUNDABS_descreg_short.LJUNK == 1]
FUNDABS_BBS = FUNDABS_descreg_short[FUNDABS_descreg_short.BB == 1]
FUNDABS_BBBS = FUNDABS_descreg_short[FUNDABS_descreg_short.BBB == 1]
FUNDABS_AS = FUNDABS_descreg_short[FUNDABS_descreg_short.A == 1]
FUNDABS_LIGS = FUNDABS_descreg_short[FUNDABS_descreg_short.LIG == 1]
FUNDABS_HIGS = FUNDABS_descreg_short[FUNDABS_descreg_short.HIG == 1]

FUNDIQ_UR = FUNDIQ_descreg[FUNDIQ_descreg.UR == 1]
FUNDIQ_LJUNK = FUNDIQ_descreg[FUNDIQ_descreg.LJUNK == 1]
FUNDIQ_BB = FUNDIQ_descreg[FUNDIQ_descreg.BB == 1]
FUNDIQ_BBB = FUNDIQ_descreg[FUNDIQ_descreg.BBB == 1]
FUNDIQ_A = FUNDIQ_descreg[FUNDIQ_descreg.A == 1]
FUNDIQ_LIG = FUNDIQ_descreg[FUNDIQ_descreg.LIG == 1]
FUNDIQ_HIG = FUNDIQ_descreg[FUNDIQ_descreg.HIG == 1]

endog = [['HHI-IQ7'], ['HHI-IQ7'], ['HHI-IQ7'], ['HHI-IQ7'], ['HHI-IQ7'], ['HHI-IQ7']]
endog = [['HHI-C5'], ['HHI-C5'], ['HHI-C5'], ['HHI-C5'], ['HHI-C5'], ['HHI-C5']]
endog = [['HHI-C8'], ['HHI-C8'], ['HHI-C8'], ['HHI-C8'], ['HHI-C8'], ['HHI-C8']]
exog_vars_cut_4 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_12_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag', 'AP_cut_lag', 'AREC_TOT_cut_lag', 'INV_TOT_cut_lag']




datas = [FUNDIQ_UR, FUNDIQ_LJUNK, FUNDIQ_BB, FUNDIQ_BBB, FUNDIQ_A, FUNDIQ_HIG]
datas = [FUNDABS_UR, FUNDABS_LJUNK, FUNDABS_BB, FUNDABS_BBB, FUNDABS_A, FUNDABS_HIG]
datas = [FUNDABS_URS, FUNDABS_LJUNKS, FUNDABS_BBS, FUNDABS_BBBS, FUNDABS_AS, FUNDABS_HIGS]

b5 = Functions.run_regressions_4(datas, endog, exog_vars_cut_4)

endog = ['HHI-IQ7', 'HHI-IQ7', 'HHI-IQ7', 'HHI-IQ7', 'HHI-IQ7', 'HHI-IQ7']
endog = ['HHI-C5', 'HHI-C5', 'HHI-C5', 'HHI-C5', 'HHI-C5', 'HHI-C5']
endog = ['HHI-C8', 'HHI-C8', 'HHI-C8', 'HHI-C8', 'HHI-C8', 'HHI-C8']

exog_4 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.',
          'Accounts Payable', 'Accounts Receivable', 'Inventories']

Functions.write_file_latex_style(tables,
                                 "10.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_4, Functions.prep_params(b5))),
                                 'w')



b4 = Functions.run_regressions(FUNDIQ_UR, FUNDABS_UR,
                               ['HHI-IQ7'], ['HHI-C5', 'HHI-C8'],
                               exog_vars_cut_4, exog_vars_cut_4)

Functions.write_file_latex_style(tables,
                                 "4a.txt",
                                 Functions.prep_latex_table(Functions.print_reg(endog, exog_4, Functions.prep_params(b4))),
                                 'w')











#Trend regressions

