#Colla et al sample:
a = pd.to_datetime('20020101')
#IQ_SAMPLE['datadate'] = pd.to_datetime(IQ_SAMPLE['datadate'])
b = pd.to_datetime('20091231')

COMP_SAMPLE_C['datadate'] = pd.to_datetime(COMP_SAMPLE_C['datadate'])
COMP_SAMPLE_C_COLLA = COMP_SAMPLE_C[COMP_SAMPLE_C.datadate >=  a]
COMP_SAMPLE_C_COLLA = COMP_SAMPLE_C_COLLA[COMP_SAMPLE_C.datadate <=b]
len(COMP_SAMPLE_C_COLLA) #15351

# MERGE IQ_SAMPLE and COMPUSTAT check what the fuck
###########
IQ_SAMPLE['datadate'] = pd.to_datetime(IQ_SAMPLE['datadate'])
COMP_SAMPLE['datadate'] = pd.to_datetime(COMP_SAMPLE['datadate'])

IQ_SAMPLE_THE = pd.merge(IQ_SAMPLE[['gvkey','datadate','HHI_IQ', 'CP_IQ', 'DC_IQ', 'TL_IQ', 'SBN_IQ',
                  'SUB_IQ', 'CL_IQ', 'OTHER_IQ']],
                    COMP_SAMPLE[['gvkey','datadate','HH3_C', 'SUB_C', 'SBN_C', 'BD_C', 'CL_C', 'SHORT_C']],
                    left_on=['gvkey','datadate'],
                    right_on=['gvkey','datadate'], how='left')

IQ_SAMPLE_THE['HHI_IQ'].corr(IQ_SAMPLE_THE['HH3_C'])
IQ_SAMPLE_THE['SBN_IQ'].corr(IQ_SAMPLE_THE['SBN_C'])
IQ_SAMPLE_THE['SUB_IQ'].corr(IQ_SAMPLE_THE['SUB_C'])

IQ_SAMPLE_IQCOLLA[['CP_IQPCT', 'DC_IQPCT','TL_IQPCT','SBN_IQPCT', 'SUB_IQPCT']].describe()
IQ_SAMPLE_IQCOLLA[['CL_IQPCT',]].describe()

IQ_SAMPLE_IQCOLLA['BD_IQPCT'] = IQ_SAMPLE_IQCOLLA['DC_IQPCT'] + IQ_SAMPLE_IQCOLLA['TL_IQPCT']
IQ_SAMPLE_IQCOLLA[['BD_IQPCT',]].describe()

#Colla et al sample:
a = pd.to_datetime('20020101')
#IQ_SAMPLE['datadate'] = pd.to_datetime(IQ_SAMPLE['datadate'])
b = pd.to_datetime('20091231')

#2002-2009
IQ_SAMPLE_IQCOLLA = IQ_SAMPLE[IQ_SAMPLE.datadate >=  a]
len(IQ_SAMPLE_IQCOLLA) #33673
IQ_SAMPLE_IQCOLLA = IQ_SAMPLE_IQCOLLA[IQ_SAMPLE_IQCOLLA.datadate <= b]
len(IQ_SAMPLE_IQCOLLA) #16751


COMP_SAMPLE_C['datadate'] = pd.to_datetime(COMP_SAMPLE_C['datadate'])
COMP_SAMPLE_C_COLLA = COMP_SAMPLE_C[COMP_SAMPLE_C.datadate >=  a]
COMP_SAMPLE_C_COLLA = COMP_SAMPLE_C_COLLA[COMP_SAMPLE_C.datadate <=b]
len(COMP_SAMPLE_C_COLLA) #18602

# MERGE IQ_SAMPLE and COMPUSTAT check what the fuck
###########
IQ_SAMPLE = IQ_SAMPLE.astype({'HHI_IQ': 'float'})

IQ_SAMPLE["HHI_IQ"] = IQ_SAMPLE["HHI_IQ"].convert_objects(convert_numeric=True)

IQ_SAMPLE['HHI_IQ'] = pd.to_numeric(IQ_SAMPLE['HHI_IQ'])

IQ_SAMPLE.describe('HHI_IQ')


IQ_SAMPLE_IQCOLLA["HHI_IQ"] = IQ_SAMPLE_IQCOLLA["HHI_IQ"].convert_objects(convert_numeric=True)

IQ_SAMPLE_IQCOLLA['HHI_IQ'] = pd.to_numeric(IQ_SAMPLE_IQCOLLA['HHI_IQ'])
#HHI
IQ_SAMPLE_IQCOLLA['HHI_IQ'].describe()
COMP_SAMPLE_C_COLLA['HH2_C'].describe()

#Debt TYpes by percentage
IQ_SAMPLE_IQCOLLA[['CP_IQPCT', 'DC_IQPCT','TL_IQPCT','SBN_IQPCT', 'SUB_IQPCT']].describe()
IQ_SAMPLE_IQCOLLA[['CL_IQPCT', 'OTHER_IQPCT','SHORT_CPCT']].describe()

COMP_SAMPLE_C_COLLA[['SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']].describe()


COMP_SAMPLE_C_COLLA['BD2_CPCT'] = COMP_SAMPLE_C_COLLA['BD_CPCT'] + COMP_SAMPLE_C_COLLA['SHORT_CPCT']
COMP_SAMPLE_C_COLLA['BD2_CPCT'].describe()
#firm characteristics

IQ_SAMPLE[['HHI_IQ', 'at']].describe()
IQ_SAMPLE_IQCOLLA[['HHI_IQ']].describe()

IQ_SAMPLE_IQCOLLA[['at','PROF','DIVP', 'MVBook']].describe()
IQ_SAMPLE_IQCOLLA[['DIVP', 'CASH','TANG', 'MLEV']].describe()

COMP_SAMPLE_C_COLLA = COMP_SAMPLE_C_COLLA.replace([np.inf, -np.inf], np.nan)
COMP_SAMPLE_C_COLLA[['at','PROF','DIVP', 'MVBook']].describe()
COMP_SAMPLE_C_COLLA[['DIVP', 'CASH','TANG', 'MLEV']].describe()


#IQ_SAMPLE_IQCOLLA['SHORT_IQ'] = IQ_SAMPLE_IQCOLLA['SHORT_IQ']
