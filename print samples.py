list_funda_c = ['gvkey', 'datadate', 'TOTALDEBT_C', 'SUB_C', 'SBN_C', 'BD_C', 'CL_C', 'SHORT_C', 'OTHER_C',
              'SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT', 'OTHER_CPCT', # 'CURLIAPCT_C',
              'HH1_C', 'HH2_C', 'HH3_C', 'dltt', 'dlc', 'dn','dd','dm','ds','dlto', 'dltp','dcvsub','dcvt']

list_variables_bs = ['gvkey', 'datadate', 'at', 'sale', 'MVEquity','MVBook', 'PROF', 'DIVP','CASH',
                     'TANG', 'CAPEX', 'ADVERT', 'RD', 'MLEV', 'BLEV']
FUNDADEBT['SHORT_CPCT'] = FUNDADEBT['SHORT_C']/FUNDADEBT['TOTALDEBT_C']


COMP_SAMPLE = pd.merge(COMPUCRSPIQCR[['gvkey', 'datadate', 'fyear', 'exchg','sic', 'splticrm', 'AGE','fic']],
                    FUNDADEBT[list_funda_c],
                    left_on=['gvkey','datadate'],
                    right_on = ['gvkey','datadate'], how='left')

COMP_SAMPLE = pd.merge(COMP_SAMPLE,
                    BS1DF[list_variables_bs],
                    left_on=['gvkey','datadate'],
                    right_on=['gvkey','datadate'], how='left')


len(COMP_SAMPLE) # 219255
COMP_SAMPLE_C = COMP_SAMPLE[COMP_SAMPLE.TOTALDEBT_C > 0]
len(COMP_SAMPLE_C) #190401
COMP_SAMPLE_C = COMP_SAMPLE_C[COMP_SAMPLE_C.HH1_C >= 0]
len(COMP_SAMPLE_C) #180635
COMP_SAMPLE_C= COMP_SAMPLE_C[COMP_SAMPLE_C.HH1_C <= 1]
len(COMP_SAMPLE_C) #179723

COMP_SAMPLE_C = COMP_SAMPLE_C[COMP_SAMPLE_C.fyear < 2019]
len(COMP_SAMPLE_C) #179602

COMP_SAMPLE_C = COMP_SAMPLE_C[(COMP_SAMPLE_C.exchg == 11.00)|
                              (COMP_SAMPLE_C.exchg == 12.00) |
                              (COMP_SAMPLE_C.exchg == 14.00)]
len(COMP_SAMPLE_C) #124526


#COMP_SAMPLE_C = COMP_SAMPLE_C[COMP_SAMPLE_C.D != 1]
#len(COMP_SAMPLE_C) #124355


COMP_SAMPLE_C = COMP_SAMPLE_C[COMP_SAMPLE_C.fic == 'USA']
len(COMP_SAMPLE_C)  #111955


COMP_SAMPLE_C['rated'] = [1 if x in ratings else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['INVGRADE'] = [1 if x in ig else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['JUNK'] = [1 if x in junk else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['HJUNK'] = [1 if x in hjunk else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['LJUNK'] = [1 if x in lj else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['HIG'] = [1 if x in hig else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['LIG'] = [1 if x in lig else 0 for x in COMP_SAMPLE_C['splticrm']]
COMP_SAMPLE_C['D'] = [1 if x in D else 0 for x in COMP_SAMPLE_C['splticrm']]


series2 = COMP_SAMPLE_C[['fyear', 'at', 'gvkey', 'SBN_CPCT', 'dn', 'INVGRADE', 'rated', 'SUB_CPCT', 'BD_CPCT', 'CL_CPCT',
                                        'SHORT_CPCT', 'OTHER_CPCT', 'splticrm','dd','ds','dlto','dm', 'dltp','dcvsub','dcvt']]
series2 = series2.astype({'fyear': 'int64'})

series_2n = series2.groupby(['fyear'])[['at', 'SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT',
                                        'SHORT_CPCT', 'OTHER_CPCT']].mean().reset_index()

datadirectory
series2.to_csv(os.path.join(datadirectory, "series2.csv"))
