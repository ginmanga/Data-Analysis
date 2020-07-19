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

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-March30ALL.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-March30ALL.csv.gz"))

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-APRIL16ALL.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-APRIL16ALL.csv.gz"))

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-APRIL16ALL.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-APRIL20ALL.csv.gz"))

FUNDIQ_lag = pd.read_csv(os.path.join(datadirectory, "FUNDIQ_lag-APRI24ALL.csv.gz"))
FUNDABS_lag = pd.read_csv(os.path.join(datadirectory, "FUNDABS_lag-APRIL24ALL.csv.gz"))


FUNDABS_lag = Functions.create_groups(FUNDABS_lag, 'fyear', "hostile_index_L1", 'HOST', grps=2)
FUNDABS_lag['dual_ext'] = np.where(FUNDABS_lag['fyear'] < 1978, np.nan, FUNDABS_lag['dual_ext'])

FUNDABS_descreg = FUNDABS_lag
FUNDIQ_descreg = FUNDIQ_lag
# FUNDABS_descreg = FUNDABS_lag[FUNDABS_lag.fyear > 2001]
FUNDABS_descreg['C/B'] = FUNDABS_descreg['LJUNK']
FUNDABS_descreg['BBB/A'] = FUNDABS_descreg['LIG']
FUNDABS_descreg['AA/AAA'] = FUNDABS_descreg['HIG']
FUNDABS_descreg['HHI-C8'] = FUNDABS_descreg['HH1']
FUNDABS_descreg['HHI-C5'] = FUNDABS_descreg['HH2']

FUNDIQ_descreg['HHI-IQ7'] = FUNDIQ_descreg['HH1_IQ']
FUNDIQ_descreg['HHI-IQ6'] = FUNDIQ_descreg['HH2_IQ']
FUNDABS_descreg['RATED'] = 1-FUNDABS_descreg['UR']

FUNDABS_descreg['NEGPROF'] = np.where(FUNDABS_descreg.PROF_cut_lag < 0, 1, 0)
FUNDIQ_descreg['NEGPROF'] = np.where(FUNDIQ_lag.PROF_cut_lag < 0, 1, 0)

FUNDABS_descreg['Deltadebt'] = FUNDABS_descreg['BLEV_cut'] - FUNDABS_descreg['BLEV_cut_lag']
FUNDIQ_descreg['Deltadebt'] = FUNDIQ_descreg['BLEV_cut'] - FUNDIQ_descreg['BLEV_cut_lag']
########INTER#############
FUNDABS_descreg['HC'] = (FUNDABS_descreg['hostile_index_L1'] - FUNDABS_descreg['hostile_index_L1'].mean())/ \
                        FUNDABS_descreg['hostile_index_L1'].std()
FUNDABS_descreg['HID'] = FUNDABS_descreg['HC']*FUNDABS_descreg['dual']
FUNDABS_descreg['HIDD'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['dual']
FUNDABS_descreg['HIDN'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['dual_ext']
FUNDIQ_descreg['HIDN'] = FUNDIQ_descreg['hostile_index_L1']*FUNDIQ_descreg['dual_ext']

FUNDABS_descreg['DebtHost'] = FUNDABS_descreg['Deltadebt']*FUNDABS_descreg['hostile_index_L1']
FUNDIQ_descreg['DebtHost'] = FUNDIQ_descreg['Deltadebt']*FUNDIQ_descreg['hostile_index_L1']
FUNDABS_descreg['DUALDEBT'] = FUNDABS_descreg['Deltadebt']*FUNDABS_descreg['dual_ext']
FUNDIQ_descreg['DUALDEBT'] = FUNDIQ_descreg['Deltadebt']*FUNDIQ_descreg['dual_ext']
FUNDABS_descreg['TRIPLE'] = FUNDABS_descreg['Deltadebt']*FUNDABS_descreg['dual_ext']*FUNDIQ_descreg['hostile_index_L1']
FUNDIQ_descreg['TRIPLE'] = FUNDIQ_descreg['Deltadebt']*FUNDIQ_descreg['dual_ext']*FUNDIQ_descreg['hostile_index_L1']


FUNDABS_desc_s = FUNDIQ_descreg[['hostile_index_L1', 'dual_ext', 'RD_cut', 'EINDEX', 'HIDN']]
FUNDABS_desc_s.corr()

FUNDABS_descreg['HIO'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['InstOwn_Perc']
FUNDABS_descreg['GI'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['GIGRP_2']
FUNDIQ_descreg['GI'] = FUNDIQ_descreg['hostile_index_L1']*FUNDIQ_descreg['GIGRP_2']
FUNDABS_descreg['HIO'] = FUNDABS_descreg['HC']*FUNDABS_descreg['InstOwn_Perc']
FUNDABS_descreg['GIC'] = FUNDABS_descreg['HC']*FUNDABS_descreg['GIGRP_2']

FUNDIQ_descreg['HIO'] = FUNDIQ_descreg['hostile_index_L1']*FUNDIQ_descreg['InstOwn_Perc']
FUNDABS_descreg['HIO'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['InstOwn_Perc']


FUNDIQ_descreg['HIO'] = FUNDIQ_descreg['hostile_index_L1']*FUNDIQ_descreg['INSTOWN_2']
FUNDABS_descreg['HIO'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['INSTOWN_2']

FUNDABS_descreg['HID'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['UR']
FUNDABS_descreg['HIT'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['TANG_cut_lag']
FUNDABS_descreg['HIS'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['size_lag']
FUNDABS_descreg['HIP'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['PROF_cut_lag']
FUNDABS_descreg['HID'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['DIVP_lag']
FUNDABS_descreg['HIV'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['income_std_4_cut_lag']
FUNDABS_descreg['HIR'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['RD_cut_lag']
FUNDABS_descreg['HIL'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['BLEV_cut_lag']

FUNDABS_descreg['HIRI'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['RD_cut_lag']*FUNDABS_descreg['INSTOWN_2']
FUNDABS_descreg['RDINST'] = FUNDABS_descreg['RD_cut_lag']*FUNDABS_descreg['INSTOWN_2']
inter_terms = ['HID','HIT', 'HIS', 'HIP', 'HID', 'HIV','HIR', 'HIL']

FUNDIQ_descreg['HID'] = FUNDIQ_descreg['hostile_index_L1']*FUNDIQ_descreg['board-independence_2']
FUNDABS_descreg['HID'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['board-independence_2']

FUNDIQ_descreg['HID'] = FUNDIQ_descreg['hostile_index_L1']*FUNDIQ_descreg['board-independence_2']
FUNDABS_descreg['HID'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['board-independence_2']
FUNDABS_descreg['HIDD'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['dual']

FUNDABS_descreg['SUP_G'] = np.where((FUNDABS_descreg['GIGRP_2'] == 1) | (FUNDABS_descreg['dual'] == 1), 1, 0)
FUNDABS_descreg['SUP_G'] = np.where(FUNDABS_descreg['GIGRP_2'].isna(), np.nan, FUNDABS_descreg['SUP_G'] )
FUNDABS_descreg['SUP_G'] = np.where(FUNDABS_descreg['dual'].isna(), np.nan, FUNDABS_descreg['SUP_G'] )
FUNDABS_descreg['Inter_sup'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['SUP_G']

FUNDABS_descreg['SUB_G'] = np.where((FUNDABS_descreg['GIGRP_2'] == 1) & (FUNDABS_descreg['dual'] == 0), 1, 0)
FUNDABS_descreg['SUB_G1'] = np.where((FUNDABS_descreg['GIGRP_2'] == 1) & (FUNDABS_descreg['dual'] == 1), 1, 0)
FUNDABS_descreg['SUB_G'] = np.where(FUNDABS_descreg['GIGRP_2'].isna(), np.nan, FUNDABS_descreg['SUB_G'] )
FUNDABS_descreg['SUB_G1'] = np.where(FUNDABS_descreg['GIGRP_2'].isna(), np.nan, FUNDABS_descreg['SUB_G1'] )
FUNDABS_descreg['SUB_G'] = np.where(FUNDABS_descreg['dual'].isna(), np.nan, FUNDABS_descreg['SUB_G'] )
FUNDABS_descreg['SUB_G1'] = np.where(FUNDABS_descreg['dual'].isna(), np.nan, FUNDABS_descreg['SUB_G1'] )
FUNDABS_descreg['Inter_sub'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['SUB_G']
FUNDABS_descreg['Inter_sub1'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['SUB_G1']


FUNDABS_descreg['GI'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['GIGRP_2']

FUNDABS_descreg['GD'] = FUNDABS_descreg['GIGRP_2']*FUNDABS_descreg['dual']
FUNDABS_descreg['Triple_inter'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['dual']*FUNDABS_descreg['GIGRP_2']

FUNDABS_descreg.to_csv(os.path.join(datadirectory, "FUNDABSR.csv"), index=False)
FUNDIQ_descreg.to_csv(os.path.join(datadirectory, "FUNDIQSR.csv"), index=False)




FUNDABS_descreg7802 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1977]
FUNDABS_descreg7802 = FUNDABS_descreg7802  [FUNDABS_descreg7802.fyear < 2003]

FUNDABS_descreg.to_csv(os.path.join(datadirectory, "FUNDABSR.csv"), index=False)
FUNDABS_descreg7802.to_csv(os.path.join(datadirectory, "FUNDABSR.csv"), index=False)

FUNDABS_descreg6979 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1968]
FUNDABS_descreg6979 = FUNDABS_descreg6979 [FUNDABS_descreg6979 .fyear < 1980]
FUNDABS_descreg8089 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1979]
FUNDABS_descreg8089 = FUNDABS_descreg8089 [FUNDABS_descreg8089 .fyear < 1990]
FUNDABS_descreg9099 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1989]
FUNDABS_descreg9099 = FUNDABS_descreg9099 [FUNDABS_descreg9099.fyear < 2000]
FUNDABS_descreg0009 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1999]
FUNDABS_descreg0009 = FUNDABS_descreg0009 [FUNDABS_descreg0009.fyear < 2010]
FUNDABS_descreg1018 = FUNDABS_descreg[FUNDABS_descreg.fyear > 2009]
FUNDABS_descreg1018 = FUNDABS_descreg1018 [FUNDABS_descreg1018.fyear < 2019]


FUNDABS_descreg7890 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1977]
FUNDABS_descreg7890 = FUNDABS_descreg7890 [FUNDABS_descreg7890.fyear < 1991]
FUNDABS_descreg9102 = FUNDABS_descreg[FUNDABS_descreg.fyear > 1990]
FUNDABS_descreg9102 = FUNDABS_descreg9102[FUNDABS_descreg9102.fyear < 2003]
year = pd.Categorical(FUNDABS_descreg7890.fyear)
FUNDABS_descreg7890 = FUNDABS_descreg7890.set_index(['FF48', 'fyear'])
FUNDABS_descreg7890['year'] = year
year = pd.Categorical(FUNDABS_descreg9102.fyear)
FUNDABS_descreg9102 = FUNDABS_descreg9102.set_index(['FF48', 'fyear'])
FUNDABS_descreg9102['year'] = year

year = pd.Categorical(FUNDABS_descreg6979.fyear)
FUNDABS_descreg6979 = FUNDABS_descreg6979.set_index(['FF48', 'fyear'])
FUNDABS_descreg6979['year'] = year
year = pd.Categorical(FUNDABS_descreg8089.fyear)
FUNDABS_descreg8089 = FUNDABS_descreg8089.set_index(['FF48', 'fyear'])
FUNDABS_descreg8089['year'] = year

year = pd.Categorical(FUNDABS_descreg9099.fyear)
FUNDABS_descreg9099 = FUNDABS_descreg9099.set_index(['FF48', 'fyear'])
FUNDABS_descreg9099['year'] = year
year = pd.Categorical(FUNDABS_descreg0009.fyear)
FUNDABS_descreg0009 = FUNDABS_descreg0009.set_index(['FF48', 'fyear'])
FUNDABS_descreg0009['year'] = year
year = pd.Categorical(FUNDABS_descreg1018.fyear)
FUNDABS_descreg1018 = FUNDABS_descreg1018.set_index(['FF48', 'fyear'])
FUNDABS_descreg1018['year'] = year



FUNDABS_descreg_short = FUNDABS_descreg[FUNDABS_descreg.fyear > 2001]
FUNDABS_descreg = FUNDABS_descreg.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDABS_descreg.fyear)
FUNDABS_descreg = FUNDABS_descreg.set_index(['FF48', 'fyear'])
FUNDABS_descreg['year'] = year



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

#Board-independence = 1 if board<0.5 in 2001
FUNDABS_descreg['Board2001'] = FUNDABS_descreg['hostile_index_L1']*FUNDABS_descreg['InstOwn_Perc']



# New

gover_vars = ['DE_INC', 'GINDEX', 'DUALCLASS', 'EINDEX', 'GIGRP_1', 'GIGRP_2',
              'INSTOWN_1', 'INSTOWN_2', 'InstOwn_Perc', 'ind_dir_per_ISS',
              'board-independence_1', 'board-independence_2']

take_vars = ['hostile_index', 'hostile_index_L1', 'hostile_index_L2',
            'hostile_index_L3', 'hostile_index_L4']







FUNDABS_descregs = FUNDABS_descreg[['hostile_index_L1', 'dual', 'HIDD', 'HID','HC']]

FUNDABS_descregs.corr()
exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag', 'hostile_index_L1', 'InstOwn_Perc', 'DUALCLASS', 'HIO', 'HID']
exog_3 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.',
          'HOST', 'ISNT', 'DUAL', 'INTER1', 'INTER2']



gover_vars = ['DE_INC', 'GINDEX', 'DUALCLASS', 'EINDEX', 'GIGRP_1', 'GIGRP_2',
              'INSTOWN_1', 'INSTOWN_2', 'InstOwn_Perc', 'ind_dir_per_ISS',
              'board-independence_1', 'board-independence_2']

exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'BLEV_cut_lag', 'hostile_index',
                   'dual_stock', 'HID2', 'INSTOWN_2']
exog_3 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'Book lev.',
          'HOST', 'DUAL', 'INTER', 'INSTOWN_2']
inter_terms = ['HID','HIT', 'HIS', 'HIP', 'HID', 'HIV','HIR']
FUNDABS_descreg['HIRI']
FUNDABS_descreg['RDINST']


exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'income_std_4_cut_lag',
                   'RD_cut_lag', 'UR', 'hostile_index_L1', 'dual', 'HIDD', 'InstOwn_Perc']
exog_3 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A', 'R\&D exp.', 'UR',
          'HOSTILE', 'DUAL', 'INTER', 'INST']


exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag',
                   'income_std_4_cut_lag', 'RD_cut_lag', 'hostile_index_L1', 'SUP_G',
                   'Inter_sup']


exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag',
                   'income_std_4_cut_lag', 'RD_cut_lag', 'hostile_index_L1', 'SUB_G', 'Inter_sub']

exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag',
                   'income_std_4_cut_lag', 'RD_cut_lag', 'hostile_index_L1', 'SUP_G', 'Inter_sup']


exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag',
                   'income_std_4_cut_lag', 'RD_cut_lag', 'BLEV_cut_lag', 'Deltadebt',
                   'hostile_index_L1', 'dual_ext', 'HIDN', 'DebtHost', 'DUALDEBT',
                   'TRIPLE', 'InstOwn_Perc']
exog_vars_cut_3 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag',
                   'income_std_4_cut_lag', 'RD_cut_lag', 'BLEV_cut_lag', 'Deltadebt',
                   'hostile_index_L1', 'dual_ext', 'DebtHost']
exog_vars_cut_4 = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag',
                   'income_std_4_cut_lag', 'RD_cut_lag', 'BLEV_cut_lag',
                   'hostile_index_L1', 'GIGRP_2', 'GI', 'InstOwn_Perc']

exog_3 = ['ln(Size)', 'M/B', 'Profitability', 'Div.payer', 'Tangibility', 'CFV\_A',
          'R\&D exp.', 'Book lev.', 'UR', 'INST']
b = ['OWN_A_1', 'OWN_A_2']
b = ['OWN_B_1', 'OWN_B_2']
b = ['OWN_C_1', 'OWN_C_2']

FUNDABS_descreg[['hostile_index_L1', 'dual', 'HIDD', 'HID','HC']]
#mean5cat = FUNDABS_descreg.groupby(['fyear'])[['dual_stock']].mean()

FUNDABS_descreg6979
FUNDABS_descreg8089
FUNDABS_descreg9099
FUNDABS_descreg0009
FUNDABS_descreg1018
datas = [FUNDABS_descreg6979, FUNDABS_descreg8089, FUNDABS_descreg9099,
         FUNDABS_descreg0009, FUNDABS_descreg1018]


endogs = [['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
          ['HHI-C5', 'HHI-C8']]

datas = [FUNDABS_descreg8089, FUNDABS_descreg9099,
         FUNDABS_descreg0009, FUNDABS_descreg1018]
endogs = [['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'],
          ['HHI-C5', 'HHI-C8']]


datas = [FUNDABS_descreg7802]
endogs = [['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8'], ['HHI-C5', 'HHI-C8']]
datas = [FUNDABS_descreg]
endogs = [['HHI-C5', 'HHI-C8']]
endog = ['HHI-C5', 'HHI-C8']



datas = [FUNDIQ_descreg, FUNDABS_descreg]
endogs = [['HHI-IQ7'], ['HHI-C5', 'HHI-C8']]
b3 = Functions.run_regressions_4(datas, endogs, exog_vars_cut_3, constant=1, options=0)
b4 = Functions.run_regressions_4(datas, endogs, exog_vars_cut_4, constant=1, options=0)

endog = ['HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8',
         'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8']
endog = ['HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8', 'HHI-C5', 'HHI-C8',
         'HHI-C5', 'HHI-C8']
Functions.write_file_latex_style(tables,
                                 "1.txt",
                                 Functions.prep_latex_table(
                                     Functions.print_reg(endog, exog_3,
                                                         Functions.prep_params(b3, constant=1))),
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

