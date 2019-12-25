import datetime, csv
# from sas7bdat import SAS7BDAT
import pandas as pd
import numpy as np
import gzip, os, csv
import datetime
import matplotlib.pyplot as plt
import Functions
import importlib
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

#FUNDABSBBB = FUNDABS[FUNDABS.BBB==1]
##FUNDABSBBBMF = FUNDABSBBB[['gvkey','datadate', 'DD1',
#'SUBNOTCONV_C','SUBCONV_C','CONV_C','DD_C','DN_C','CL_C','SBN_C','SBN_CPCT', 'TOTALDEBT_C_2', 'TOTALDEBT_C']]
#FUNDABSBBBMF_S = FUNDABSBBBMF[FUNDABSBBBMF.SBN_CPCT>1]
#FUNDABS = Functions.hhi_calculator(['SUB_C','SBN_C','BD_C', 'CL_C', 'SHORT_C', 'OTHER_C'], 'TOTALDEBT_C', 'HH2C', FUNDABS)
#FUNDABS = Functions.hhi_calculator(['SUBNOTCONV_C','SUBCONV_C','CONV_C', 'DD_C', 'DN_C', 'BD_C', 'CL_C','SHORT_C', 'OTHER_C'],
                                     #'TOTALDEBT_C', 'HH1C', FUNDABS)

a = ['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']
aa = ['SUBNOTCONV_CPCT','SUBCONV_CPCT','CONV_CPCT', 'DD_CPCT', 'DN_CPCT', 'BD_CPCT', 'CL_CPCT','SHORT_CPCT']
b = ['UR','LJUNK','HJUNK','LIG','HIG']
bb = ['C','B','BB','BBB','A','AA', 'AAA']
bbb = ['UR', 'C', 'B', 'BB', 'BBB', 'A', 'HIG']
bbbb = ['B','BB','BBB','A']
b5 = ['UR', 'B', 'BB', 'BBB', 'A', 'HIG']

Functions.plot_maker(['HH1', 'HH2'], FUNDABS_desc, b=[], save=[0, dir_plots, "HHICA"], year=1969, method='mean')
Functions.plot_maker(['HH1'], FUNDABS_desc, ratings_g,  save=[0, dir_plots, "title"], year=1986, method='mean')
Functions.plot_maker(['HH2'], FUNDABS_desc, ratings_g,  save=[1, dir_plots, "5CATRATING"], year=1986, method='mean', label=1)

Functions.plot_maker(['HH1'], FUNDABS_desc, b5,  save=[0, dir_plots, "title"], year=1986, method='mean')
Functions.plot_maker(['HH1'], FUNDABS_desc, bbb,  save=[0, dir_plots, "title"], year=1986, method='mean')
Functions.plot_maker(['HH2'], FUNDABS_desc, b5,  save=[0, dir_plots, "title"], year=1986, method='mean')
Functions.plot_maker(['HH2'], FUNDABS_desc, b,  save=[0, dir_plots, "title"], year=1986, method='mean')

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