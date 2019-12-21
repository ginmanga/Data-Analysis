# Regs
from linearmodels.panel import PanelOLS
from linearmodels.panel import PooledOLS
import statsmodels.api as sm
year = pd.Categorical(FUNDIQ.fyear)

FUNDIQ = FUNDIQ.sort_values(by=['FF48', 'fyear'])

FUNDIQP = FUNDIQ.set_index(['FF48', 'fyear'])
FUNDIQP['year'] = year
FUNDIQP[['MVBook']].describe()
FUNDIQP[['MVBook']].percentile()

FUNDIQP['MVBook'].quantile(0.01)
FUNDIQP['PROF'].quantile(0.99)

FUNDIQP['size'] = np.log(FUNDIQP['AT'])

exog_vars = ['AT','MVBook', 'PROF', 'DIVP', 'TANG', 'UR', 'MLEV','income_std_12_at','sale_std_ff48_12_2', 'AGE']
non_exog = FUNDIQP['HH1_IQ']
exog_vars = ['AT','PROF', 'DIVP', 'TANG', 'UR', 'MLEV','sale_std_ff48_12_2']
exog_vars = ['AT','MVBook', 'PROF', 'DIVP', 'TANG'] # 'AGE']
exog_vars = ['size']
#exog_vars = ['AT']
exog = sm.add_constant(FUNDIQP[exog_vars])
exog = FUNDIQP[exog_vars]

#mod = PooledOLS(non_exog, exog)#,entity_effects=True)
mod = PanelOLS(non_exog, exog,entity_effects=True)
pooled_res = mod.fit()
print(pooled_res)