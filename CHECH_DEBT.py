

var_debt = ['gvkey', 'datadate', 'dd','ds','dn','dd1','dcvt']
list_replace =['gvkey', 'datadate', 'dltt','cmp','dcvsub','ds','dd','dn','dlto','dlc','dclo','dcvt','dltp','dd1']
FUNDABSCHECK = pd.merge(FUNDABS,
                FUNDADEBT[list_replace],
                left_on=['gvkey','datadate'],
                right_on = ['gvkey','datadate'], how='left')


FUNDABSCHECK['CHECK_DEBT'] = FUNDABSCHECK['dd'] + FUNDABSCHECK['dn'] + FUNDABSCHECK['dcvt'] + \
                          FUNDABSCHECK['dlto'] + FUNDABSCHECK['ds'] + FUNDABSCHECK['dclo']

FUNDABSCHECK['CCC'] = FUNDABSCHECK['dltt'] - FUNDABSCHECK['CHECK_DEBT']
FUNDABSCHECK['PCCC'] = (FUNDABSCHECK['dltt'] - FUNDABSCHECK['CHECK_DEBT'])/FUNDABSCHECK['dltt']


FUNDABSCHECK['NCHECK'] = np.where((FUNDABSCHECK['dltt'] == 0) & (FUNDABSCHECK['dd1'] > 0), 1, 0)
FUNDABSCHECK['NP_A'] = np.where((FUNDABSCHECK['CCC'] >= -0.001001) & (FUNDABSCHECK['CCC'] <= 0.001001), 1, 0)
FUNDABSCHECK['NP_OVER'] = np.where((FUNDABSCHECK['CCC'] > 0.001001), 1, 0)
#FUNDABSCHECK['NP_UNDER'] = np.where((FUNDABSCHECK['CCC'] < -0.001001), 1, 0)

FUNDABSCHECK['rcc'] = np.where((FUNDABSCHECK['NP_OVER'] == 1), FUNDABSCHECK['CCC'] - FUNDABSCHECK['dd1'],
                               FUNDABSCHECK['CCC'] + FUNDABSCHECK['dd1'])

FUNDABSCHECK['C_A'] = np.where((FUNDABSCHECK['rcc'] >= -0.00101)
                                       & (FUNDABSCHECK['rcc'] <= 0.00101), 1, 0)

FUNDABSCHECK['last_1'] = FUNDABSCHECK['CCC']/ FUNDABSCHECK['dltt']
FUNDABSCHECK['keep'] = np.where((FUNDABSCHECK['last_1'] >= -0.1)
                                       & (FUNDABSCHECK['last_1'] <= 0.1), 1, 0)


FUNDABSCHECK['TOKEEP'] = np.where((FUNDABSCHECK['NP_A'] == 1) | (FUNDABSCHECK['C_A'] == 1)|(FUNDABSCHECK['keep'] == 1)
                                  , 1, 0)
FUNDABSCHECK['TOKEEPF'] = np.where((FUNDABSCHECK['TOKEEP'] == 1)
                                       & (FUNDABSCHECK['NCHECK'] == 0), 1, 0)

FUNDABSCHECKss = FUNDABSCHECK[FUNDABSCHECK['NKEEP'] == 1]

#merge with fundabs and finalize sample, and get summary stats

FUNDABS = pd.merge(FUNDABS,
                FUNDABSCHECK[['gvkey','datadate','TOKEEPF']],
                left_on=['gvkey','datadate'],
                right_on = ['gvkey','datadate'], how='left')
len(FUNDABS) # 145412
FUNDABS = FUNDABS.drop_duplicates()
len(FUNDABS) # 145356
FUNDABS = FUNDABS[FUNDABS.TOKEEPF == 1]
len(FUNDABS) # 143918



#############################
#############################
#############################
FUNDABSCHECK['NCHECK'].sum()
FUNDABSCHECKSSS = FUNDABSCHECK[FUNDABSCHECK.NCHECK == 1]
del FUNDABSCHECKSSS
len(FUNDABSCHECK)

df.replace([np.inf, -np.inf], np.nan).dropna(subset=["col1", "col2"], how="all")

len(FUNDABSCHECK)
FUNDABSCHECK = FUNDABSCHECK.drop_duplicates()
len(FUNDABSCHECK)

FUNDABSCHECK['D1'] = FUNDABSCHECK['dd1']
FUNDABSCHECK['CHECK_DEBT'] = FUNDABSCHECK['dd'] + FUNDABSCHECK['dn'] + FUNDABSCHECK['dcvt'] + \
                          FUNDABSCHECK['dlto'] + FUNDABSCHECK['ds'] + FUNDABSCHECK['dclo']

FUNDABSCHECK['CCC'] = FUNDABSCHECK['dltt'] - FUNDABSCHECK['CHECK_DEBT']
FUNDABSCHECK['PCCC'] = (FUNDABSCHECK['dltt'] - FUNDABSCHECK['CHECK_DEBT'])/FUNDABSCHECK['dltt']


FUNDABSCHECK['NP'] = np.where(FUNDABSCHECK['CCC'] == 0, 1, 0) #Exactly
FUNDABSCHECK['NP_A'] = np.where((FUNDABSCHECK['CCC'] >= -0.001001) & (FUNDABSCHECK['CCC'] <= 0.001001), 1, 0)
FUNDABSCHECK['NP_AA'] = np.where((FUNDABSCHECK['PCCC'] >= -0.001001) & (FUNDABSCHECK['PCCC'] <= 0.001001), 1, 0)

FUNDABSCHECK['NP_OVER'] = np.where((FUNDABSCHECK['CCC'] > 0.001001), 1, 0)
FUNDABSCHECK['NP_UNDER'] = np.where((FUNDABSCHECK['CCC'] < -0.001001), 1, 0)

FUNDABSCHECK_SMALL = FUNDABSCHECK[FUNDABSCHECK.NP_A == 1]
FUNDABSCHECK_SMALL_1 = FUNDABSCHECK[FUNDABSCHECK.NP_OVER == 1]
FUNDABSCHECK_SMALL_2 = FUNDABSCHECK[FUNDABSCHECK.NP_UNDER == 1]

FUNDABSCHECK_SMALL_1['rcc'] = FUNDABSCHECK_SMALL_1['CCC'] - FUNDABSCHECK_SMALL_1['dd1']
FUNDABSCHECK_SMALL_2['rcc'] = FUNDABSCHECK_SMALL_2['CCC'] + FUNDABSCHECK_SMALL_2['dd1']

FUNDABSCHECK_SMALL_1['C_A'] = np.where((FUNDABSCHECK_SMALL_1['rcc'] >= -0.00101)
                                       & (FUNDABSCHECK_SMALL_1['rcc'] <= 0.00101), 1, 0)
FUNDABSCHECK_SMALL_2['C_A'] = np.where((FUNDABSCHECK_SMALL_2['rcc'] >= -0.00101)
                                       & (FUNDABSCHECK_SMALL_2['rcc'] <= 0.00101), 1, 0)

FUNDABSCHECK_SMALL_11 = FUNDABSCHECK_SMALL_1[FUNDABSCHECK_SMALL_1.C_A==0]
FUNDABSCHECK_SMALL_21 = FUNDABSCHECK_SMALL_2[FUNDABSCHECK_SMALL_2.C_A==0]

FUNDABSCHECK_SMALL_11['last_1'] = FUNDABSCHECK_SMALL_11['CCC']/ FUNDABSCHECK_SMALL_11['dltt']
FUNDABSCHECK_SMALL_21['last_1'] = FUNDABSCHECK_SMALL_21['CCC']/ FUNDABSCHECK_SMALL_21['dltt']

FUNDABSCHECK_SMALL_11['last_2'] = FUNDABSCHECK_SMALL_11['rcc']/ FUNDABSCHECK_SMALL_11['dltt']
FUNDABSCHECK_SMALL_21['last_2'] = FUNDABSCHECK_SMALL_21['rcc']/ FUNDABSCHECK_SMALL_21['dltt']

FUNDABSCHECK_SMALL_11['last_1'] = FUNDABSCHECK_SMALL_11['last_1']#*100
FUNDABSCHECK_SMALL_21['last_1'] =  FUNDABSCHECK_SMALL_21['last_1']#*100
FUNDABSCHECK_SMALL_11['last_2'] = FUNDABSCHECK_SMALL_11['last_2']#*100
FUNDABSCHECK_SMALL_21['last_2'] =  FUNDABSCHECK_SMALL_21['last_2']#*100


FUNDABSCHECK_SMALL_11['keep'] = np.where((FUNDABSCHECK_SMALL_11['last_1'] >= -0.1)
                                       & (FUNDABSCHECK_SMALL_11['last_1'] <= 0.1), 1, 0)
FUNDABSCHECK_SMALL_21['keep'] = np.where((FUNDABSCHECK_SMALL_21['last_1'] >= -0.1)
                                       & (FUNDABSCHECK_SMALL_21['last_1'] <= 0.1), 1, 0)


FUNDABSCHECK_SMALL_21['last_1'] =  FUNDABSCHECK_SMALL_21['CCC']/ FUNDABSCHECK_SMALL_21['dltt']

a1 = FUNDABSCHECK['NP'].describe()
FUNDABSCHECK['NP_A'].describe()
FUNDABSCHECK['NP_OVER'].describe()
FUNDABSCHECK['NP_UNDER'].describe()

FUNDABSCHECK_SMALL['NP_A'].describe()
FUNDABSCHECK_SMALL_1['C_A'].describe()
FUNDABSCHECK_SMALL_2['C_A'].describe()

FUNDABSCHECK_SMALL['NP_A'].count()
FUNDABSCHECK_SMALL_11['last_1'].count()
FUNDABSCHECK_SMALL_21['last_1'].count()

FUNDABSCHECK_SMALL_11['last_1'].describe()
FUNDABSCHECK_SMALL_21['last_1'].describe()

FUNDABSCHECK_SMALL_11['last_2'].describe()
FUNDABSCHECK_SMALL_21['last_2'].describe()

FUNDABSCHECK_SMALL_11['keep'].describe()
FUNDABSCHECK_SMALL_21['keep'].describe()


FUNDABSCHECK_SMALL_21[FUNDABSCHECK_SMALL_21.last_1 == 'NaN']

a1 = FUNDABSCHECK['NP'].describe()
a2 = FUNDABSCHECK_SMALL_1['C_A'].describe()
a3 = FUNDABSCHECK_SMALL_2['C_A'].describe()

combo = [a1,a2,a3]
result = pd.concat(combo, axis=1)
FUNDABSCHECK_SMALL['COMP']
# define final sample