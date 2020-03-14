import datetime, csv
import pandas as pd
import numpy as np
import gzip, os, csv
import datetime
import matplotlib.pyplot as plt
import Functions
import importlib

dir_plots = " "
########################################
FUNDABS = 0
FUNDABS_desc = 0
ratings = ['C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
ratings_1 = ['UR', 'C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
ratings_g = ['UR', 'LJUNK', 'HJUNK','LIG', 'HIG']
########################################


FUNDABS[['HH1', 'HH2']].mean()
FUNDABS[['HH1', 'HH2']].describe()

FUNDABS[['HH1','HH2']].groupby(FUNDABS['fyear']).count()
FUNDABS[['HH1','HH2']].groupby(FUNDABS['fyear']).mean()
FUNDABS[['HH1','HH2']].groupby(FUNDABS['fyear']).median()
#Sample statistics

a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
aa = ['SUBNOTCONV_CPCT', 'SUBCONV_CPCT', 'CONV_CPCT', 'DD_CPCT', 'DN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
b = ['UR','LJUNK', 'HJUNK', 'LIG', 'HIG']
bb = ['C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
bbb = ['UR', 'C', 'B', 'BB', 'BBB', 'A', 'HIG']
bbbb = ['B', 'BB', 'BBB', 'A', 'HIG']
b5 = ['UR', 'LJUNK', 'BB', 'LIG', 'HIG']

FUNDABS_desc['C/B'] = FUNDABS_desc['LJUNK']
FUNDABS_desc['BBB/A'] = FUNDABS_desc['LIG']
FUNDABS_desc['AA/AAA'] = FUNDABS_desc['HIG']
FUNDABS_desc['HHI-C8'] = FUNDABS_desc['HH1']
FUNDABS_desc['HHI-C5'] = FUNDABS_desc['HH2']

FUNDABS_desc['SBN'] = FUNDABS_desc['SBN_CPCT']
FUNDABS_desc['SUB'] = FUNDABS_desc['SUB_CPCT']
FUNDABS_desc['DLTO'] = FUNDABS_desc['BD_CPCT']
FUNDABS_desc['CL'] = FUNDABS_desc['CL_CPCT']
FUNDABS_desc['SHORT'] = FUNDABS_desc['SHORT_CPCT']

FUNDABS_desc['DD'] = FUNDABS_desc['DD_CPCT']
FUNDABS_desc['DN'] = FUNDABS_desc['DN_CPCT']
FUNDABS_desc['SUBNOTCONV'] = FUNDABS_desc['SUBNOTCONV_CPCT']
FUNDABS_desc['SUBCONV'] = FUNDABS_desc['SUBCONV_CPCT']
FUNDABS_desc['CONV'] = FUNDABS_desc['CONV_CPCT']


FUNDABS_desc['NDIVP'] = 1-FUNDABS_desc['DIVP']

b5 = ['UR', 'C/B', 'BB', 'BBB/A', 'AA/AAA']
b5 = ['UR', 'RATED', 'C/B', 'BB', 'BBB/A', 'AA/AAA']
FUNDABS_desc['Dividend'] = 1-FUNDABS_desc['DIVP']
FUNDABS_desc['UR'] = 1-FUNDABS_desc['RATED']



# Get series of low high everything


#Create quintiles
FUNDABS_desc = Functions.create_groups(FUNDABS_desc, "AT_cut", 'Q',  grps=5)
FUNDABS_desc = Functions.create_groups(FUNDABS_desc, "AP_cut", 'AP',  grps=5)
FUNDABS_desc = Functions.create_groups(FUNDABS_desc, "income_std_10_FF48", 'Sig',  grps=5)

FS = FUNDABS_desc[FUNDABS_desc.gvkey <= 1240]
FUNDABS_desc = Functions.create_groups(FUNDABS_desc, 'fyear', "AT", 'S', grps=3, quintiles=[0.25, 0.5, 1],
                                       sub_grp='EXCHCD', sub_grp_val=1)

#Size
b = ['Small', 'Medium', 'Large']
#Ownership
b = ['OWN_A_1', 'OWN_A_2']
b = ['OWN_B_1', 'OWN_B_2']
b = ['OWN_C_1', 'OWN_C_2']
#Governance
b = ['GIGRP_1', 'GIGRP_2']
b = ['NOTDUAL', 'DUALCLASS']
#Other firm characteristics
b = ['DIVP', 'NDIVP']
b = ['MB_1', 'MB_2']
b = ['PROF_1', 'PROF_2']
b = ['CASH_1', 'CASH_2']
b = ['TANG_1', 'TANG_2']
b = ['CAPEX_1', 'CAPEX_2']
b = ['RD_1', 'RD_2']
b = ['CFV_1', 'CFV_2']
b = ['AP_1', 'AP_2']
b = ['INV_1', 'INV_2']
b = ['AR_1', 'AR_2']
b = ['WCAP_1', 'WCAP_2']
b = ['BLEV_1', 'BLEV_2']
#Size New
b = ['MB_1', 'MB_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
b = ['PROF_1', 'PROF_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
b = ['CASH_1', 'CASH_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
b = ['TANG_1', 'TANG_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

b = ['RD_1', 'RD_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

b = ['CFV_1', 'CFV_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

b = ['AP_1', 'AP_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

b = ['INV_1', 'INV_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

b = ['AR_1', 'AR_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
b = ['WCAP_1', 'WCAP_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
b = ['BLEV_1', 'BLEV_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
b = ['UR', 'RATED']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)


b = ['RD_1', 'RD_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

b = ['CFV_1', 'CFV_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

b = ['AP_1', 'AP_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)
b = ['INV_1', 'INV_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

b = ['AR_1', 'AR_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)
b = ['WCAP_1', 'WCAP_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)
b = ['BLEV_1', 'BLEV_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)
b = ['UR', 'RATED']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1986, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)

b = ['Small', 'Medium', 'Large']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[1, dir_plots, "S5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[1, dir_plots, "S8"], year=1969, method='mean', label=0)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc[FUNDABS_desc.fyear<2000], b, save=[0, dir_plots, "DIVP5"], year=1980, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc[FUNDABS_desc.fyear<2000], b, save=[0, dir_plots, "DIVP8"], year=1980, method='median', label=0)

Functions.plot_maker(['HHI-IQ7'], FUNDIQ_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-IQ6'], FUNDIQ_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

Functions.plot_maker(['HHI-IQ7'], FUNDIQ_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-IQ6'], FUNDIQ_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

FUNDABS_desc[b].groupby(FUNDABS_desc['fyear']).sum()
S = FUNDABS_desc[FUNDABS_desc.S_3==1]
b = ['UR', 'C/B', 'BB', 'BBB', 'A', 'AA/AAA']
b = ['C/B', 'BB', 'BBB', 'A', 'AA/AAA']
b = ['Small', 'Medium', 'Large']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP5"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP8"], year=1986, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)

S[b5].groupby(S['fyear']).sum()

a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']

Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.S_1 == 1], b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.S_2 == 1], b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.S_3 == 1], b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)

a = ['DD_CPCT', 'DN_CPCT', 'SUBNOTCONV_CPCT', 'SUBCONV_CPCT', 'CONV_CPCT']
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.S_1 == 1], b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.S_2 == 1], b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.S_3 == 1], b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
# Ownership
b = ['OWN_A_1', 'OWN_A_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

b = ['OWN_B_1', 'OWN_B_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

b = ['OWN_C_1', 'OWN_C_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)
b = ['OWN_C_1', 'OWN_C_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)
#Governance
b = ['GIGRP_1', 'GIGRP_2']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

Functions.plot_maker(['HHI-IQ7'], FUNDIQ_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-IQ6'], FUNDIQ_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

FUNDABS_desc['NOTDUAL'] = 1 - FUNDABS_desc['DUALCLASS']
FUNDABS_desc['DUALCLASS'].sum()
FUNDABS_desc['NOTDUAL'].sum()
FUNDABS_desc.groupby(['fyear'])[['DUALCLASS']].sum()
b = ['NOTDUAL', 'DUALCLASS']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP5"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP8"], year=1969, method='median', label=0)

# Dividend payer
b = ['DIVP', 'NDIVP']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[1, dir_plots, "DIVP5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[1, dir_plots, "DIVP8"], year=1969, method='mean', label=0)

# Size Quinile payer
FUNDABS_desc['Q1'] = FUNDABS_desc['Q_1']
FUNDABS_desc['Q2'] = FUNDABS_desc['Q_2']
FUNDABS_desc['Q3'] = FUNDABS_desc['Q_3']
FUNDABS_desc['Q4'] = FUNDABS_desc['Q_4']
FUNDABS_desc['Q5'] = FUNDABS_desc['Q_5']
b = ["Q1", "Q2", "Q3", "Q4", "Q5"]
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[1, dir_plots, "SIZE5"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[1, dir_plots, "SIZE8"], year=1969, method='mean', label=0)

DIVP = FUNDABS_desc[FUNDABS_desc.DIVP == 1]
NDIVP = FUNDABS_desc[FUNDABS_desc.DIVP == 0]
DIVP.groupby(['fyear'])[['HHI-C8']].mean()
a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
Functions.plot_maker(a, DIVP, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)
Functions.plot_maker(a, NDIVP, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b=[], save=[0, dir_plots, "HHI5"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b=[], save=[1, dir_plots, "HHI5"], year=1969, method='median', label=0)


Functions.plot_maker(['HHI-C5', 'HHI-C8'], FUNDABS_desc, b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, ratings_g,  save=[0, dir_plots, "5CATRATING19862"], year=1986, method='mean')

b5 = ['UR', 'LJUNK', 'BB', 'BBB', 'A', 'HIG']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b5,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b5,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='mean', label=1)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, bbb,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, bbb,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='median', label=1)

Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b5,  save=[1, dir_plots, "8CATRATING1986"], year=1986, method='mean', label=0)

####  Debt Types
a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
Functions.plot_maker(a, FUNDABS_desc, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)
o = FUNDABS_desc[FUNDABS_desc.Size_1 == 1]
Functions.plot_maker(a, o, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)

o = FUNDABS_desc[FUNDABS_desc.Size_2 == 1]
Functions.plot_maker(a, o, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)

o = FUNDABS_desc[FUNDABS_desc.Size_3 == 1]
Functions.plot_maker(a, o, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)

o = FUNDABS_desc[FUNDABS_desc.Size_4 == 1]
Functions.plot_maker(a, o, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)

o = FUNDABS_desc[FUNDABS_desc.Size_5 == 1]
Functions.plot_maker(a, o, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean', label=1)

FUNDABS_86 = FUNDABS_desc[(FUNDABS_desc['fyear'] == 1986)]
FUNDABS_18 = FUNDABS_desc[(FUNDABS_desc['fyear'] == 2018)]

list_data_sets = [FUNDABS_86, FUNDABS_18]
variables = ['HHI-C5']


### DEBT TYPES
FUNDABSUR = FUNDABS_desc[FUNDABS_desc.UR == 1]
FUNDABSLIG = FUNDABS_desc[FUNDABS_desc.LIG == 1]
FUNDABSHIG = FUNDABS_desc[FUNDABS_desc.HIG == 1]
FUNDABSBB= FUNDABS_desc[FUNDABS_desc.BB == 1]
FUNDABSBBB = FUNDABS_desc[FUNDABS_desc.BBB == 1]
FUNDABSA = FUNDABS_desc[FUNDABS_desc.A == 1]
FUNDABSLJUNK= FUNDABS_desc[FUNDABS_desc.LJUNK == 1]

# SIZE
FUNDABQ1 = FUNDABS_desc[FUNDABS_desc.Q1 == 1]
FUNDABQ2 = FUNDABS_desc[FUNDABS_desc.Q2== 1]
FUNDABQ3 = FUNDABS_desc[FUNDABS_desc.Q3 == 1]
FUNDABQ4 = FUNDABS_desc[FUNDABS_desc.Q4 == 1]
FUNDABQ5 = FUNDABS_desc[FUNDABS_desc.Q5 == 1]

FUNDABS_desc_rated = FUNDABS_desc[FUNDABS_desc.RATED == 1]
FUNDABS_desc
FUNDABS_desc.groupby(['fyear'])['RATED'].count()
FUNDABS_desc.groupby(['fyear'])['C'].sum()
FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].mean()

a = ['SBN_CPCT', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']


# Dividend Payer
DIVP = FUNDABS_desc[FUNDABS_desc.DIVP == 1]
NDIVP = FUNDABS_desc[FUNDABS_desc.DIVP == 0]
DIVP.groupby(['fyear'])[['HHI-C5']].mean() # min 1981 0.525859
NDIVP.groupby(['fyear'])[['HHI-C5']].mean() #  min 1978 0.556525

a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.DIVP == 0], b=[], year=1969, save=[1, dir_plots, "5TNDIV"],
                     method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.DIVP == 1], b=[], year=1969, save=[1, dir_plots, "5TDIV"],
                     method='mean')
a = ['DD', 'DN', 'SUBNOTCONV', 'SUBCONV', 'CONV']
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.DIVP == 0], b=[], year=1969, save=[1, dir_plots, "5ETNDIV"],
                     method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.DIVP == 1], b=[], year=1969, save=[1, dir_plots, "5ETDIV"],
                     method='mean')

# Rating
a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']

a = ['SUB', 'DLTO', 'CL', 'SHORT']
FUNDABSSHORT = FUNDABS_desc[FUNDABS_desc.fyear<=1995]
Functions.plot_maker(a, FUNDABSSHORT[FUNDABSSHORT.UR == 1], b=[], year=1986, save=[0, dir_plots, "5CATUR"], method='mean', label=1)
Functions.plot_maker(a, FUNDABSSHORT[FUNDABSSHORT.LJUNK == 1], b=[], year=1986, save=[0, dir_plots, "5CATULJUNK"], method='mean')
Functions.plot_maker(a, FUNDABSSHORT[FUNDABSSHORT.BB == 1], b=[], year=1986, save=[0, dir_plots, "5CATULBB"], method='mean')
Functions.plot_maker(a, FUNDABSSHORT[FUNDABSSHORT.BBB == 1], b=[], year=1986, save=[0, dir_plots, "5CATULBB"], method='mean')
Functions.plot_maker(a, FUNDABSSHORT[FUNDABSSHORT.A == 1], b=[], year=1986, save=[0, dir_plots, "5CATULIG"], method='mean')
Functions.plot_maker(a, FUNDABSSHORT[FUNDABSSHORT.HIG == 1], b=[], year=1986, save=[0, dir_plots, "5CATUHIG"], method='mean')


FUNDABSUR.groupby(['fyear'])[a].mean()
FUNDABSLJUNK.groupby(['fyear'])[a].mean()
FUNDABSBB.groupby(['fyear'])[a].mean()
FUNDABSLIG.groupby(['fyear'])[a].mean()
FUNDABSHIG.groupby(['fyear'])[a].mean()


#### MAke Table like table 2 of paper,
# 1969 0 2918 yearls, columns: average HHI-C5 HHI-C8 HHI-IQ7 HHI-IQ8 leverage obs


#Write a functions, takes datasets, calculates trends multiplies them by 100 prints them in a table

























































# Size different

b = ['Small', 'Medium', 'Large']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "S5S"], year=2002, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "S8S"], year=2002, method='mean', label=0)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[1, dir_plots, "S55S"], year=2002, method='median', label=0)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[1, dir_plots, "S88S"], year=2002, method='median', label=0)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc[FUNDABS_desc.fyear<2000], b, save=[0, dir_plots, "DIVP5"], year=1980, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc[FUNDABS_desc.fyear<2000], b, save=[0, dir_plots, "DIVP8"], year=1980, method='median', label=0)



Functions.plot_maker(['HHI-IQ7'], FUNDIQ_desc, b, save=[1, dir_plots, "SIQ77"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-IQ6'], FUNDIQ_desc, b, save=[1, dir_plots, "SIQ66"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-IQ7'], FUNDIQ_desc, b, save=[1, dir_plots, "SIQ7"], year=1969, method='median', label=0)
Functions.plot_maker(['HHI-IQ6'], FUNDIQ_desc, b, save=[1, dir_plots, "SIQ6"], year=1969, method='median', label=0)

FUNDABS_desc[b].groupby(FUNDABS_desc['fyear']).sum()
S = FUNDABS_desc[FUNDABS_desc.S_3==1]
b = ['UR', 'C/B', 'BB', 'BBB', 'A', 'AA/AAA']
b = ['C/B', 'BB', 'BBB', 'A', 'AA/AAA']
b = ['Small', 'Medium', 'Large']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP5"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP8"], year=1986, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP5"], year=1986, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc[FUNDABS_desc.fyear<1995], b, save=[0, dir_plots, "DIVP8"], year=1986, method='median', label=0)


FUNDIQ_desc_s_1 = FUNDIQ_desc[FUNDIQ_desc.Small==1]
FUNDABS_desc_s_1 = FUNDABS_desc[FUNDABS_desc.Small==1]
FUNDIQ_desc_s_2 = FUNDIQ_desc[FUNDIQ_desc.Small==2]
FUNDABS_desc_s_2 = FUNDABS_desc[FUNDABS_desc.Small==2]
FUNDIQ_desc_s_3 = FUNDIQ_desc[FUNDIQ_desc.Small==3]
FUNDABS_desc_s_3 = FUNDABS_desc[FUNDABS_desc.Small==3]

meanCP_1 = FUNDABS_desc_s_1.groupby(['fyear'])[['HHI-C5', 'HHI-C8']].mean()
medianCP_1 = FUNDABS_desc_s_1.groupby(['fyear'])[['HHI-C5', 'HHI-C8']].median()


meanCP = meanCP.rename(columns={'HHI-C5': 'Average HHI-C5', 'HHI-C8': 'Average HHI-C8',
                                'BLEV_cut': 'Average Leverage Compustat'})
medianCP = medianCP.rename(columns={'HHI-C5': 'Median HHI-C5', 'HHI-C8': 'Median HHI-C8',
                                'BLEV_cut': 'Median Leverage Compustat'})
sumobscompCP = sumobscompCP.rename(columns={'HHI-C5': 'Obs. Compustat'})


meanIQ = FUNDIQ_desc_s.groupby(['fyear'])[['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']].mean()
medianIQ  = FUNDIQ_desc_s.groupby(['fyear'])[['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']].median()
sumobsIQ  = FUNDIQ_desc_s.groupby(['fyear'])[['HHI-IQ7']].count()

meanIQ = meanIQ.rename(columns={'HHI-IQ7': 'Average HHI-IQ7', 'HHI-IQ6': 'Average HHI-IQ6',
                                'BLEV_cut': 'Average Leverage Capital IQ'})
medianIQ = medianIQ.rename(columns={'HHI-IQ7': 'Median HHI-IQ7', 'HHI-IQ6': 'Median HHI-IQ6',
                                'BLEV_cut': 'Median Leverage Capital IQ'})
sumobsIQ = sumobsIQ.rename(columns={'HHI-IQ7': 'Obs. Capital IQ'})
capi = pd.concat([meanIQ, medianIQ, sumobsIQ], axis=1)

