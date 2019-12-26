# Regs
from linearmodels.panel import PanelOLS
from linearmodels.panel import compare
from linearmodels.panel import PooledOLS
import statsmodels.api as sm

FUNDABS_descreg = FUNDABS_lag.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDABS_descreg.fyear)
FUNDABS_descreg = FUNDABS_descreg.set_index(['FF48', 'fyear'])
FUNDABS_descreg['year'] = year


FUNDIQ_descreg = FUNDIQ_lag.sort_values(by=['FF48', 'fyear'])
year = pd.Categorical(FUNDIQ_descreg.fyear)
FUNDIQ_descreg = FUNDIQ_descreg.set_index(['FF48', 'fyear'])
FUNDIQ_descreg['year'] = year
#FUNDIQ_descreg['size'] = np.log(FUNDIQ_descreg['AT_cut'])

FUNDIQ_descreg['HH1'] = np.where(FUNDIQ_descreg.HH2.isnull(), np.NaN, FUNDIQ_descreg['HH1'])
FUNDIQ_descreg['HH1_IQ'] = np.where(FUNDIQ_descreg.HH1.isnull(), np.NaN, FUNDIQ_descreg['HH1_IQ'])
FUNDIQ_descreg['HH2_IQ'] = np.where(FUNDIQ_descreg.HH1.isnull(), np.NaN, FUNDIQ_descreg['HH2_IQ'])

FUNDIQ_descregU = FUNDIQ_descreg[FUNDIQ_descreg.UR == 1]
FUNDIQ_descregR = FUNDIQ_descreg[FUNDIQ_descreg.UR == 0]

liste = ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1']
def make_exog(data, liste):
    for index, elem in liste:
        name = 'nonexog' + str(index + 1)
    name = data[elem]
    list
    return
non_exog1 = FUNDIQ_descreg['HH1_IQ']
non_exog2 = FUNDIQ_descreg['HH2_IQ']
non_exog3 = FUNDIQ_descreg['HH2']
non_exog4 = FUNDIQ_descreg['HH1']

non_exog1 = FUNDIQ_descregU['HH1_IQ']
non_exog2 = FUNDIQ_descregU['HH2_IQ']
non_exog3 = FUNDIQ_descregU['HH2']
non_exog4 = FUNDIQ_descregU['HH1']

non_exog1 = FUNDIQ_descregR['HH1_IQ']
non_exog2 = FUNDIQ_descregR['HH2_IQ']
non_exog3 = FUNDIQ_descregR['HH2']
non_exog4 = FUNDIQ_descregR['HH1']


exog_vars_cut = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'RD_cut_lag',
                 'income_std_12_cut_lag', 'UR_lag']

exog_vars_cut = ['size_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'RD_cut_lag',
                 'income_std_12_cut_lag']

exog_vars_cut = ['size_cut_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'RD_cut_lag',
                 'income_std_12_cut_lag', 'C_lag', 'B_lag', 'BB_lag', 'BBB_lag', 'A_lag', 'HIG_lag']

exog_vars_cut1 = ['size_cut_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'RD_cut_lag',
                 'income_std_4_cut_lag', 'UR_lag']

exog_vars_cut2 = ['size_cut_lag', 'MVBook_cut_lag', 'PROF_cut_lag', 'DIVP_lag', 'TANG_cut_lag', 'RD_cut_lag',
                 'sale_std_12_cut_lag', 'UR_lag']

exog_vars_cut = ['size','MVBook_cut', 'PROF_cut', 'DIVP', 'TANG_cut', 'RD_cut', 'income_std_9_cut', 'UR', 'BLEV']
exog_vars_cut = ['size','MVBook_cut', 'PROF_cut', 'DIVP', 'TANG_cut', 'RD_cut', 'sale_std_12_cut', 'UR']
exog_vars_cut = ['size', 'MVBook_cut', 'PROF_cut', 'DIVP', 'TANG_cut', 'RD_cut',  'income_std_12_cut',
                 'UR', 'BLEV', 'AP_cut']

exog_cut = sm.add_constant(FUNDIQ_descreg[exog_vars_cut])
exog_cut = sm.add_constant(FUNDIQ_descregU[exog_vars_cut])
exog_cut = sm.add_constant(FUNDIQ_descregR[exog_vars_cut])

exog_cut1 = sm.add_constant(FUNDIQ_descreg[exog_vars_cut1])




mod2 = PanelOLS(non_exog1, exog_cut, entity_effects=True, time_effects=True)
clust_entity5 = mod2.fit(cov_type='clustered', clusters=FUNDIQ_descreg.gvkey)
model1 = mod2.fit()

mod2 = PanelOLS(non_exog2, exog_cut, entity_effects=True, time_effects=True)
clust_entity6 = mod2.fit(cov_type='clustered', clusters=FUNDIQ_descreg.gvkey)
model2 = mod2.fit()

mod2 = PanelOLS(non_exog3, exog_cut, entity_effects=True, time_effects=True)
clust_entity7 = mod2.fit(cov_type='clustered', clusters=FUNDIQ_descreg.gvkey)
model3 = mod2.fit()

mod2 = PanelOLS(non_exog4, exog_cut, entity_effects=True, time_effects=True)
clust_entity8 = mod2.fit(cov_type='clustered', clusters=FUNDIQ_descreg.gvkey)
model4 = mod2.fit()

# print(compare({'1': model1, '2': model2, '3': model3, '4': model4}))
print(compare({'1': clust_entity1, '2': clust_entity2, '3': clust_entity3, '4': clust_entity4}))
print(compare({'1': clust_entity5, '2': clust_entity6, '3': clust_entity7, '4': clust_entity8}))


print(compare({'1': clust_entity1, '2': clust_entity2, '3': model1, '4': model2}))

clust_entity1.params
clust_entity1.pvalues

#COMPUSTAT
