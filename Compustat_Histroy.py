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

FUNDABS_desc['NDIVP'] = 1-FUNDABS_desc['DIVP']

b5 = ['UR', 'C/B', 'BB', 'BBB/A', 'AA/AAA']
b5 = ['UR', 'RATED', 'C/B', 'BB', 'BBB/A', 'AA/AAA']
FUNDABS_desc['Dividend'] = 1-FUNDABS_desc['DIVP']
FUNDABS_desc['UR'] = 1-FUNDABS_desc['RATED']
b = ['DIVP', 'NDIVP']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "DIVP"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "HHICA"], year=1969, method='mean')

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b=[], save=[0, dir_plots, "HHI5"], year=1969, method='mean', label=0)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b=[], save=[1, dir_plots, "HHI5"], year=1969, method='median', label=0)


Functions.plot_maker(['HHI-C5', 'HHI-C8'], FUNDABS_desc, b=[], save=[0, dir_plots, "HHICA"],
                     year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, ratings_g,  save=[0, dir_plots, "5CATRATING19862"], year=1986, method='mean')

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b5,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b5,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='median', label=1)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, bbb,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, bbb,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='median', label=1)

Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b5,  save=[0, dir_plots, "5CATRATING1986"], year=1986, method='mean')

####  Debt Types
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

result_temps = ['temp' + str(i) for i in list(range(1, len(b5) + 1))]
for index, elem in enumerate(b5):
    """Loop through grouping variables"""
    #print(i)
    len(list_data_sets)
    temps = ['temp' + str(i) for i in list(range(1, len(list_data_sets)+1))]
    print(temps)
    for index2, elem2 in enumerate(list_data_sets):
        """Loop through different time periods"""
        #make it so we can choose the function
        temps[index2] = elem2[elem2[elem] == 1][variables].mean()
        #temps[index2] = elem2[elem2[elem] == 1][variables].count()
        #.to_frame().reset_index()
    result_temps[index] = pd.concat(temps, axis=1)
new2 = pd.concat(result_temps, axis=0)
print(new2)


### DEBT TYPES

FUNDABSLIG = FUNDABS_desc[FUNDABS_desc.LIG == 1]
FUNDABSHIG = FUNDABS_desc[FUNDABS_desc.HIG == 1]
FUNDABSBB= FUNDABS_desc[FUNDABS_desc.BB == 1]
FUNDABSBBB = FUNDABS_desc[FUNDABS_desc.BBB == 1]
FUNDABSA = FUNDABS_desc[FUNDABS_desc.A == 1]
FUNDABSLJUNK= FUNDABS_desc[FUNDABS_desc.LJUNK == 1]

FUNDABS_desc_rated = FUNDABS_desc[FUNDABS_desc.RATED == 1]
FUNDABS_desc
FUNDABS_desc.groupby(['fyear'])['RATED'].count()
FUNDABS_desc.groupby(['fyear'])['C'].sum()
FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].mean()

a = ['SBN_CPCT', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
Functions.plot_maker(a, FUNDABSHIG, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABSLIG, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABSBB, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABSBBB, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABSA, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABSLJUNK, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABSLJUNK, b=[], save=[0, dir_plots, "HHICA"], year=1986, method='mean', label=1)
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.UR == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year=1986)
#Divide firms into size quintiles by year

Size_1 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(0.2)
Size_2 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(0.4)
Size_3 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(0.6)
Size_4 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(0.8)
Size_5 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(1)


Size_6 = FUNDABS_desc.groupby(['fyear'])[['at']].quantile(0.95)

FBIG = FUNDABS_desc.apply(lambda row: row['at'] > Size_6.loc[row['fyear']][0], axis=1)
Functions.plot_maker(a, FBIGG, b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
FBIGG = FUNDABS_desc[FBIG]
FUNDABS_desc['Size_1'] = 0
FUNDABS_desc['Size_2'] = 0
FUNDABS_desc['Size_3'] = 0
FUNDABS_desc['Size_4'] = 0
FUNDABS_desc['Size_5'] = 0

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
FSMALL = FUNDABS_desc[FUNDABS_desc.gvkey == 3401]

FSMALL = FSMALL.apply(size_sort2, axis=1)

FUNDABS_desc = FUNDABS_desc.apply(lambda row: size_sort2(row), axis=1)
b = ['Size_1', 'Size_2', 'Size_3', 'Size_4', 'Size_5']
b = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']

FUNDABS_desc['Q1'] = FUNDABS_desc['Size_1']
FUNDABS_desc['Q2'] = FUNDABS_desc['Size_2']
FUNDABS_desc['Q3'] = FUNDABS_desc['Size_3']
FUNDABS_desc['Q4'] = FUNDABS_desc['Size_4']
FUNDABS_desc['Q5'] = FUNDABS_desc['Size_5']
b = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']



Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[1, dir_plots, "SIZEM"], year=1969, method='median', label=1)

Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE2"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[1, dir_plots, "SIZE2M"], year=1969, method='median', label=1)
a = ['SBN_CPCT', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q5 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q4 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q3 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q2 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q1 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')

a = ['DD_CPCT', 'DN_CPCT', 'SUBNOTCONV_CPCT', 'SUBCONV_CPCT']
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q5 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q4 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q3 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q2 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Q1 == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')

Sig_1 = FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].quantile(0.2)
Sig_2 = FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].quantile(0.4)
Sig_3 = FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].quantile(0.6)
Sig_4 = FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].quantile(0.8)
Sig_5 = FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].quantile(1)

Sig_1a = FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].quantile(0.2)
Sig_2a = FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].quantile(0.4)
Sig_3a = FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].quantile(0.6)
Sig_4a = FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].quantile(0.8)
Sig_5a = FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].quantile(1)

FUNDABS_desc['Sig_1'] = 0
FUNDABS_desc['Sig_2'] = 0
FUNDABS_desc['Sig_3'] = 0
FUNDABS_desc['Sig_4'] = 0
FUNDABS_desc['Sig_5'] = 0

FUNDABS_desc['Sig_1a'] = 0
FUNDABS_desc['Sig_2a'] = 0
FUNDABS_desc['Sig_3a'] = 0
FUNDABS_desc['Sig_4a'] = 0
FUNDABS_desc['Sig_5a'] = 0

def sig_sort2(x, a, var):
    if x[var] <= a[0].loc[x['fyear']][0]:
        x['Sig_1a'] = 1
    if a[0].loc[x['fyear']][0] < x[var] <= a[1].loc[x['fyear']][0]:
        x['Sig_2a'] = 1
    if a[1].loc[x['fyear']][0] < x[var] <= a[2].loc[x['fyear']][0]:
        x['Sig_3a'] = 1
    if a[2].loc[x['fyear']][0] < x[var] <= a[3].loc[x['fyear']][0]:
        x['Sig_4a'] = 1
    if x[var] > a[3].loc[x['fyear']][0]:
        x['Sig_5a'] = 1
    return x
FSMALL = FUNDABS_desc[FUNDABS_desc.gvkey == 3401]
a = [Sig_1a, Sig_2a, Sig_3a, Sig_4a]
FSMALL = FSMALL.apply(lambda row: sig_sort2(row, a, 'income_std_10_FF48'), axis=1)

FUNDABS_desc = FUNDABS_desc.apply(lambda row: sig_sort2(row, a, 'income_std_10_FF48'), axis=1)

a = ['SBN_CPCT', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT', 'HHI-C5']
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_5a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_4a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_3a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_2a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_1a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='mean')

Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_5a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='median')
Functions.plot_maker(a, FUNDABS_desc[FUNDABS_desc.Sig_1a == 1], b=[], year=1969, save=[0, dir_plots, "title"], method='median')

b = ['Sig_1', 'Sig_2', 'Sig_3', 'Sig_4', 'Sig_5']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='mean', label=1)

b = ['Sig_1a', 'Sig_2a', 'Sig_3a', 'Sig_4a', 'Sig_5a']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='mean', label=1)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='median', label=1)

Functions.plot_maker(['HH1'], FUNDABS_desc, b5,  save=[0, dir_plots, "title"], year=1986, method='mean')

Functions.plot_maker(['HH1'], FUNDABS_desc, bbb,  save=[0, dir_plots, "title"], year=1986, method='mean')
Functions.plot_maker(['HH2'], FUNDABS_desc, b5,  save=[0, dir_plots, "title"], year=1986, method='mean')
Functions.plot_maker(['HH2'], FUNDABS_desc, b,  save=[0, dir_plots, "title"], year=1986, method='mean')


## AP



AP_1 = FUNDABS_desc.groupby(['fyear'])[['AP_cut']].quantile(0.2)
AP_2 = FUNDABS_desc.groupby(['fyear'])[['AP_cut']].quantile(0.4)
AP_3 = FUNDABS_desc.groupby(['fyear'])[['AP_cut']].quantile(0.6)
AP_4 = FUNDABS_desc.groupby(['fyear'])[['AP_cut']].quantile(0.8)
AP_5 = FUNDABS_desc.groupby(['fyear'])[['AP_cut']].quantile(1)

FUNDABS_desc['AP_1'] = 0
FUNDABS_desc['AP_2'] = 0
FUNDABS_desc['AP_3'] = 0
FUNDABS_desc['AP_4'] = 0
FUNDABS_desc['AP_5'] = 0

def ap_sort2(x, a, var, initial, grps=5):
    if x[var] <= a[0].loc[x['fyear']][0]:
        x[initial + '_1'] = 1
    if a[0].loc[x['fyear']][0] < x[var] <= a[1].loc[x['fyear']][0]:
        x[initial + '_2'] = 1
    if a[1].loc[x['fyear']][0] < x[var] <= a[2].loc[x['fyear']][0]:
        x[initial + '_3'] = 1
    if a[2].loc[x['fyear']][0] < x[var] <= a[3].loc[x['fyear']][0]:
        x[initial + '_4'] = 1
    if x[var] > a[3].loc[x['fyear']][0]:
        x[initial + '_5'] = 1
    return x
FSMALL = FUNDABS_desc[FUNDABS_desc.gvkey == 3401]
a = [AP_1, AP_2, AP_3, AP_4, AP_5]

FUNDABS_desc = FUNDABS_desc.apply(lambda row: ap_sort2(row, a, 'AP_cut', 'AP'), axis=1)


b = ['AP_1', 'AP_2', 'AP_3', 'AP_4', 'AP_5']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "SIZE"], year=1969, method='mean', label=1)


CH_1 = FUNDABS_desc.groupby(['fyear'])[['CASH_cut']].quantile(0.2)
CH_2 = FUNDABS_desc.groupby(['fyear'])[['CASH_cut']].quantile(0.4)
CH_3 = FUNDABS_desc.groupby(['fyear'])[['CASH_cut']].quantile(0.6)
CH_4 = FUNDABS_desc.groupby(['fyear'])[['CASH_cut']].quantile(0.8)
CH_5 = FUNDABS_desc.groupby(['fyear'])[['CASH_cut']].quantile(1)

FUNDABS_desc['CH_1'] = 0
FUNDABS_desc['CH_2'] = 0
FUNDABS_desc['CH_3'] = 0
FUNDABS_desc['CH_4'] = 0
FUNDABS_desc['CH_5'] = 0

a = [CH_1, CH_2, CH_3, CH_4, CH_5]

FUNDABS_desc = FUNDABS_desc.apply(lambda row: ap_sort2(row, a, 'CASH_cut', 'CH'), axis=1)


b = ['CH_1', 'CH_2', 'CH_3', 'CH_4', 'CH_5']
Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='mean', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='mean', label=1)

Functions.plot_maker(['HHI-C5'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='median', label=1)
Functions.plot_maker(['HHI-C8'], FUNDABS_desc, b, save=[0, dir_plots, "Sig"], year=1969, method='mean', label=1)
### CREDDIOT RATNG


FUNDABSC = FUNDABS[FUNDABS.C == 1]
FUNDABSB = FUNDABS[FUNDABS.B == 1]
FUNDABSBB = FUNDABS[FUNDABS.BB == 1]
FUNDABSBBB = FUNDABS[FUNDABS.BBB == 1]

ratings = ['D', 'C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']
FUNDABSS = FUNDABS_desc[FUNDABS_desc.fyear>=1986]
FUNDABSS[['UR', 'D', 'C', 'B', 'BB', 'BBB', 'A', 'AA', 'AAA']].groupby(FUNDABSS['fyear']).sum()

FUNDABSC['HH2'].groupby(FUNDABSC['fyear']).sum()
FUNDABSB['HH2'].groupby(FUNDABSB['fyear']).mean()
FUNDABSBB['HH2'].groupby(FUNDABSBB['fyear']).mean()
FUNDABSBBB['HH2'].groupby(FUNDABSBBB['fyear']).mean()

Functions.plot_maker(a, FUNDABS[FUNDABS.UR == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year=1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.B == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year=1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.BB == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year=1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.BBB == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year=1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.HIG == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year = 1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.LIG == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year = 1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.HJUNK == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year = 1986)
Functions.plot_maker(a, FUNDABS[FUNDABS.LJUNK == 1], b=[],  save=[0, dir_plots, "title"], method='mean', year = 1986)



Functions.plot_maker(a, FUNDABS[FUNDABS.UR == 1], b=[], save=[0, dir_plots, "title"], method='mean', year = 1986)
Functions.plot_maker(aa, FUNDABS[FUNDABS.UR == 1], b=[], save=[0, dir_plots, "title"], method='mean', year = 1986)

#Calculate statistics and write them down
#statistics for tghe whole sample, and per decade 1969-1979, 1980-1989, 1990-1999, 2000-2009,2010-2018
FUNDABS_1 = FUNDABS[FUNDABS.fyear < 1980]
FUNDABS_2 = FUNDABS[(FUNDABS['fyear'] >= 1980) & (FUNDABS['fyear'] < 1990)]
FUNDABS_3 = FUNDABS[(FUNDABS['fyear'] >= 1990 ) & (FUNDABS['fyear'] < 1999)]
FUNDABS_4 = FUNDABS[(FUNDABS['fyear'] >= 2000 ) & (FUNDABS['fyear'] < 2009)]
FUNDABS_5 = FUNDABS[(FUNDABS['fyear'] >= 2010 ) & (FUNDABS['fyear'] < 2018)]
#Second Grouping 1986-1990, 1991-2000, 2001-2010, 2011-2018
FUNDABS_6 = FUNDABS[(FUNDABS['fyear'] >= 1986 ) & (FUNDABS['fyear'] < 1990)]
FUNDABS_6 = FUNDABS[(FUNDABS['fyear'] >= 1986 ) & (FUNDABS['fyear'] < 1990)]


combo = [i,ii,iii,iv,v]
result = pd.concat(combo, axis=1)

FUNDABS[['HH1','HH2']].groupby(FUNDABS['fyear']).count()
FUNDABS[['HH1','HH2']].groupby(FUNDABS['fyear']).mean()



#By groups
FUNDABS_6[FUNDABS_6.UR == 1][['HH2_C', 'HH4_C']].describe()
FUNDABS_3[FUNDABS_3.UR == 1][['HH2_C', 'HH4_C']].describe()
FUNDABS_4[FUNDABS_4.UR == 1][['HH2_C', 'HH4_C']].describe()
FUNDABS_5[FUNDABS_5.UR == 1][['HH2_C', 'HH4_C']].describe()
#Describe the process of creating the HH2_C index?

ox = FUNDABS_6[FUNDABS_6.UR == 1][['HH2_C', 'HH4_C']].mean()
FUNDABS_6[FUNDABS_6.UR == 1][['HH2_C', 'HH4_C']].mean()
FUNDABS_6[FUNDABS_6.UR == 1][['HH2_C', 'HH4_C']].mean()
FUNDABS_6[FUNDABS_6.UR == 1][['HH2_C', 'HH4_C']].mean()

#Set new sample and recalculate debt types and HHI indexes

list_data_sets = [FUNDABS_6, FUNDABS_3, FUNDABS_4, FUNDABS_5]
variables = ['HH2_C', 'HH4_C']
b = ['UR','LJUNK','HJUNK','LIG','HIG']
result_temps = ['temp' + str(i) for i in list(range(1, len(b) + 1))]
for index, elem in enumerate(b):
    """Loop through grouping variables"""
    #print(i)
    len(list_data_sets)
    temps = ['temp' + str(i) for i in list(range(1,len(list_data_sets)+1))]
    print(temps)
    for index2, elem2 in enumerate(list_data_sets):
        """Loop through different time periods"""
        #print("hello")
        #print(elem2[elem2[i] == 1][variables].mean())
        #make it so we can choose the function
        #temps[index2] = elem2[elem2[elem] == 1][variables].mean()
        temps[index2] = elem2[elem2[elem] == 1][variables].count()
        #.to_frame().reset_index()
    result_temps[index] = pd.concat(temps, axis=1)
new2 = pd.concat(result_temps, axis=0)
print(new2)