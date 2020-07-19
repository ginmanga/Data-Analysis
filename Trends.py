

meanCP = FUNDABS_desc.groupby(['fyear'])[['HHI-C5', 'HHI-C8', 'BLEV_cut']].mean()
medianCP = FUNDABS_desc.groupby(['fyear'])[['HHI-C5', 'HHI-C8', 'BLEV_cut']].median()
sumobscompCP = FUNDABS_desc.groupby(['fyear'])[['HHI-C5']].count()

meanCP = meanCP.rename(columns={'HHI-C5': 'Average HHI-C5', 'HHI-C8': 'Average HHI-C8',
                                'BLEV_cut': 'Average Leverage Compustat'})
medianCP = medianCP.rename(columns={'HHI-C5': 'Median HHI-C5', 'HHI-C8': 'Median HHI-C8',
                                'BLEV_cut': 'Median Leverage Compustat'})
sumobscompCP = sumobscompCP.rename(columns={'HHI-C5': 'Obs. Compustat'})

comp = pd.concat([meanCP, medianCP, sumobscompCP], axis=1)

# FUNDIQ_desc = FUNDIQ_desc.reindex()
FUNDIQ_desc_s = FUNDIQ_desc[['fyear', 'HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']]
meanIQ = FUNDIQ_desc_s.groupby(['fyear'])[['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']].mean()
medianIQ  = FUNDIQ_desc_s.groupby(['fyear'])[['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']].median()
sumobsIQ  = FUNDIQ_desc_s.groupby(['fyear'])[['HHI-IQ7']].count()

meanIQ = meanIQ.rename(columns={'HHI-IQ7': 'Average HHI-IQ7', 'HHI-IQ6': 'Average HHI-IQ6',
                                'BLEV_cut': 'Average Leverage Capital IQ'})
medianIQ = medianIQ.rename(columns={'HHI-IQ7': 'Median HHI-IQ7', 'HHI-IQ6': 'Median HHI-IQ6',
                                'BLEV_cut': 'Median Leverage Capital IQ'})
sumobsIQ = sumobsIQ.rename(columns={'HHI-IQ7': 'Obs. Capital IQ'})
capi = pd.concat([meanIQ, medianIQ, sumobsIQ], axis=1)
compIQ = pd.merge(comp, capi, left_index=True, right_index=True, how='left')

compIQ.to_csv(os.path.join(tables_notregs, "table1.csv"), index=True)
compIQ['trend'] = range(1, 1 + len(compIQ))

#Trend regresions


trend = ['Average HHI-C5', 'Average HHI-C8', 'Average HHI-IQ7', 'Average HHI-IQ6',
         'Median HHI-C5', 'Median HHI-C8', 'Median HHI-IQ7', 'Median HHI-IQ6']
periods = [[1969, 2018], [1969, 1979], [1980, 1990], [1990, 2000], [2000, 2010], [2002, 2010], [2010, 2018],
           [1979, 2010], [2002, 2018]]
#compIQ.loc[1972.0:1979.0]

holder_par, holder_std = Functions.trend_parameters(compIQ, trend, periods)
holder_list = Functions.list_maker_deluxe(holder_par, holder_std)
for i in holder_list:
    Functions.really_short_latex(i)

FUNDIQ_desc_s = FUNDIQ_desc[['fyear', 'HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']]
### Now do the same, but for size
FUNDABS_desc_s1 = FUNDABS_desc[FUNDABS_desc.S_3 == 1]
FUNDIQ_desc_s1 = FUNDIQ_desc[FUNDIQ_desc.S_3 == 1]

# FUNDIQ_desc = FUNDIQ_desc.reindex()

meanIQ = FUNDIQ_desc_s1.groupby(['fyear'])[['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']].mean()
medianIQ  = FUNDIQ_desc_s1.groupby(['fyear'])[['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut']].median()
sumobsIQ  = FUNDIQ_desc_s1.groupby(['fyear'])[['HHI-IQ7']].count()

meanIQ = meanIQ.rename(columns={'HHI-IQ7': 'Average HHI-IQ7', 'HHI-IQ6': 'Average HHI-IQ6',
                                'BLEV_cut': 'Average Leverage Capital IQ'})
medianIQ = medianIQ.rename(columns={'HHI-IQ7': 'Median HHI-IQ7', 'HHI-IQ6': 'Median HHI-IQ6',
                                'BLEV_cut': 'Median Leverage Capital IQ'})
sumobsIQ = sumobsIQ.rename(columns={'HHI-IQ7': 'Obs. Capital IQ'})



compIQ['trend'] = range(1, 1 + len(compIQ))

trend = ['Average HHI-C5', 'Average HHI-C8', 'Average HHI-IQ7', 'Average HHI-IQ6',
         'Median HHI-C5', 'Median HHI-C8', 'Median HHI-IQ7', 'Median HHI-IQ6']
periods = [[1969, 2018], [1969, 1979], [1980, 1990], [1990, 2000], [2000, 2010], [2002, 2010], [2010, 2018], [2002, 2018]]
#compIQ.loc[1972.0:1979.0]

holder_par, holder_std = Functions.trend_parameters(compIQ, trend, periods)
holder_list = Functions.list_maker_deluxe(holder_par, holder_std)
for i in holder_list:
    Functions.really_short_latex(i)

#Time priods for averages

FUNDABS_desc_s1 = FUNDABS_desc[FUNDABS_desc.S_3 == 1]
FUNDIQ_desc_s1 = FUNDIQ_desc[FUNDIQ_desc.S_3 == 1]
# Function, takes data and a condition: returns a data frame with average, median of the desired vatriables
del temp
temp_c_s = Functions.tempish(FUNDABS_desc, ['HHI-C5', 'HHI-C8', 'BLEV_cut'], ['Average', 'Median'],
               ['','', 'Leverage Compustat'], [0,0,1], ['mean', 'median'], 'S_1', count=1, sample_name='Compustat')

temp_q_s = Functions.tempish(FUNDIQ_desc, ['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut'], ['Average', 'Median'],
               ['','', 'Leverage Capital IQ'], [0,0,1], ['mean', 'median'], 'S_1', count=1, sample_name='Capital IQ')

temp_c_m = Functions.tempish(FUNDABS_desc, ['HHI-C5', 'HHI-C8', 'BLEV_cut'], ['Average', 'Median'],
               ['','', 'Leverage Compustat'], [0,0,1], ['mean', 'median'], 'S_2', count=1, sample_name='Compustat')

temp_q_m = Functions.tempish(FUNDIQ_desc, ['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut'], ['Average', 'Median'],
               ['','', 'Leverage Capital IQ'], [0,0,1], ['mean', 'median'], 'S_2', count=1, sample_name='Capital IQ')

temp_c_l = Functions.tempish(FUNDABS_desc, ['HHI-C5', 'HHI-C8', 'BLEV_cut'], ['Average', 'Median'],
               ['','', 'Leverage Compustat'], [0,0,1], ['mean', 'median'], 'S_3', count=1, sample_name='Compustat')

temp_q_l = Functions.tempish(FUNDIQ_desc, ['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut'], ['Average', 'Median'],
               ['','', 'Leverage Capital IQ'], [0,0,1], ['mean', 'median'], 'S_3', count=1, sample_name='Capital IQ')

compIQ = pd.merge(comp, capi, left_index=True, right_index=True, how='left')
capi = pd.concat([meanIQ, medianIQ, sumobsIQ], axis=1)

tps = [[1969,1974], [1975,1979], 1980-1984, 1985-1989, 1990-1994, 1995-1999, 2000-2004, 2005-2009, 2010-2014, 2015-2018]
tps = [[1969,1974], [1975,1979], [1980,1984], [1985,1989], [1990,1994], [1995,1999], [2000,2001], [2002,2004],
       [2005,2009], [2010,2014], [2015,2018]]


FUNDABS_desc
FUNDIQ_desc

def build_period_var(data, a):
    holder_names=[]
    holder_lists=[]
    print(a)
    for index, elem in enumerate(a):
        print(elem)
        name = str(elem[0]) + '-' + str(elem[1])
        data[name] = 0
        data[name] =  data.apply(lambda x: 1 if (elem[0] <= x['fyear']) and (x['fyear'] <= elem[1]) else 0, axis=1)

def build_period_var(data, a):
    holder_names=[]
    holder_lists=[]
    print(a)
    data['4YEARP'] = 0
    for index, elem in enumerate(a):
        print(elem)
        name = str(elem[0]) + '-' + str(elem[1])
        data['4YEARP'] =  data.apply(lambda x: name if (elem[0] <= x['fyear']) and (x['fyear'] <= elem[1]) else x['4YEARP'], axis=1)


periods = [[1969, 2018], [1969, 1979], [1980, 1990], [1990, 2000], [2000, 2010], [2002, 2010], [2010, 2018], [2002, 2018]]
build_period_var(FUNDABS_desc, tps)
build_period_var(FUNDIQ_desc, tps)

for i in debt_comp_1:
    Functions.really_short_latex(i)
debt_comp_1.apply(lambda x: Functions.really_short_latex(x), axis=1)
### Debt type tables
a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']

#debt_comp_1.to_csv(os.path.join(tables_notregs, "debt.csv"), index=True)

debt_comp_1 = Functions.tempish(FUNDABS_desc, var_1=a, var_2=['Average', 'Median'], options=[0,0,0,0,0],
                                methods=['mean', 'median'], time_var='4YEARP')

a = ['DD', 'DN', 'SUBNOTCONV', 'SUBCONV', 'CONV']
debt_comp_2 = Functions.tempish(FUNDABS_desc, var_1=a, var_2=['Average', 'Median'], options=[0,0,0,0,0],
                                methods=['mean', 'median'], time_var='4YEARP')

a = ['SBN', 'SUB', 'DC', 'TL','CL', 'CP', 'OTHER']

debt_iq = Functions.tempish(FUNDIQ_desc, var_1=a, var_2=['Average', 'Median'], options=[0, 0, 0, 0, 0, 0, 0],
                                methods=['mean', 'median'], time_var='4YEARP')
debt_iq.to_csv(os.path.join(tables_notregs, "debtIQ.csv"), index=True)

### TRENDS FOR DEBT TYPES
a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']

debt_comp_1 = Functions.tempish(FUNDABS_desc, var_1=a, var_2=['Average', 'Median'], options=[0,0,0,0,0],
                                methods=['mean', 'median'], time_var='fyear')

a = ['SBN', 'SUB', 'DC', 'TL','CL', 'CP', 'OTHER']
debt_iq = Functions.tempish(FUNDIQ_desc, var_1=a, var_2=['Average', 'Median'], options=[0, 0, 0, 0, 0, 0, 0],
                                methods=['mean', 'median'], time_var='fyear')

trend = ['Average HHI-C5', 'Average HHI-C8', 'Average HHI-IQ7', 'Average HHI-IQ6',
         'Median HHI-C5', 'Median HHI-C8', 'Median HHI-IQ7', 'Median HHI-IQ6']

trend = ['Average SBN', 'Average SUB', 'Average DLTO', 'Average CL', 'Average SHORT']

periods = [[1969, 2018], [1979, 2018], [1969, 1979], [1980, 1990], [1990, 2000], [2000, 2010], [2002, 2010], [2010, 2018], [2002, 2018]]
#compIQ.loc[1972.0:1979.0]
debt_comp_1['trend'] = range(1, 1 + len(debt_comp_1))
holder_par, holder_std = Functions.trend_parameters(debt_comp_1, trend, periods)
debt_iq['trend'] = range(1, 1 + len(debt_iq))
trend = ['Average SBN', 'Average SUB', 'Average DC',  'Average TL', 'Average CL', 'Average CP', 'Average OTHER']
periods = [[2002, 2010], [2010, 2018],  [2002, 2018]]
holder_par, holder_std = Functions.trend_parameters(debt_iq, trend, periods)
holder_list = Functions.list_maker_deluxe(holder_par, holder_std)
for i in holder_list:
    Functions.really_short_latex(i)

build_period_var(FUNDABS_desc_s1, tps)

C = FUNDABS_desc_s1.groupby(['4ps'])[['HHI-C5', 'HHI-C8', 'BLEV_cut']].mean()
a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']
a = ['HHI-C5', 'HHI-C8']
a = ['BLEV_cut']
small_comp = Functions.tempish(FUNDABS_desc, a, ['Average', 'Median'],
               ['Small', 'Small', 'Leverage Compustat'], [0,0,0,0,0], ['mean', 'median'], 'S_1', time_var='4YEARP',
                               count=1, sample_name='Compustat')
med_comp = Functions.tempish(FUNDABS_desc, a, ['Average', 'Median'],
               ['Medium','Medium', 'Leverage Compustat'],  [0,0,0,0,0], ['mean', 'median'], 'S_2', time_var='4YEARP',
                             count=1, sample_name='Compustat')
lar_comp = Functions.tempish(FUNDABS_desc, a, ['Average', 'Median'],
               ['Large','Large', 'Leverage Compustat'],  [0,0,0,0,0], ['mean', 'median'], 'S_3', time_var='4YEARP',
                             count=1, sample_name='Compustat')

a = ['SBN', 'SUB', 'DC', 'TL','CL', 'CP', 'OTHER']
small_iq = Functions.tempish(FUNDIQ_desc, var_1=a, var_2= ['Average', 'Median'],
                             var_3=['Small', 'Small', 'Leverage Capital IQ'],  methods=['mean', 'median'],
                             grp='S_1', time_var='4YEARP', count=1, sample_name='Capital IQ')

med_iq = Functions.tempish(FUNDIQ_desc, var_1=a, var_2= ['Average', 'Median'],
                             var_3=['Small', 'Small', 'Leverage Capital IQ'],  methods=['mean', 'median'],
                             grp='S_2', time_var='4YEARP', count=1, sample_name='Capital IQ')
lar_iq =  Functions.tempish(FUNDIQ_desc, var_1=a, var_2= ['Average', 'Median'],
                             var_3=['Small', 'Small', 'Leverage Capital IQ'],  methods=['mean', 'median'],
                             grp='S_3', time_var='4YEARP', count=1, sample_name='Capital IQ')

small_comp.to_csv(os.path.join(tables_notregs, "smalldebtC.csv"), index=True)
small_iq.to_csv(os.path.join(tables_notregs, "smalldebtIQ.csv"), index=True)


med_comp.to_csv(os.path.join(tables_notregs, "meddebtC.csv"), index=True)
med_iq.to_csv(os.path.join(tables_notregs, "meddebtIQ.csv"), index=True)

lar_comp.to_csv(os.path.join(tables_notregs, "lardebtC.csv"), index=True)
lar_iq.to_csv(os.path.join(tables_notregs, "lardebtIQ.csv"), index=True)
for i in holder_list:
    Functions.really_short_latex(i)
Functions.really_short_latex(lar_comp)
a = ['Average HHI-C5', 'Median HHI-C5']
b =  ['Average HHI-IQ7', 'Median HHI-IQ7']
compIQ_small = pd.merge(small_comp[a], small_iq[b], left_index=True, right_index=True, how='left')
compIQ_small = pd.merge(med_comp[a], med_iq[b], left_index=True, right_index=True, how='left')
compIQ_small = pd.merge(lar_comp[a], lar_iq[b], left_index=True, right_index=True, how='left')

a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']
b = ['SBN', 'SUB', 'DC', 'TL','CL', 'CP', 'OTHER']
compIQ_small = pd.merge(small_comp[a], small_iq[b], left_index=True, right_index=True, how='left')
compIQ_small = pd.merge(med_comp[a], med_iq[b], left_index=True, right_index=True, how='left')
compIQ_small = pd.merge(lar_comp[a], lar_iq[b], left_index=True, right_index=True, how='left')

tempt_trans = compIQ_small.T
tempt_trans.to_csv(os.path.join(tables_notregs, "tempt_trans.csv"), index=True)
small_comp.to_csv(os.path.join(tables_notregs, "smallcomp.csv"), index=True)
small_iq.to_csv(os.path.join(tables_notregs, "smalliq.csv"), index=True)


compIQ_small = pd.merge(small_comp, small_iq, left_index=True, right_index=True, how='left')

HHI5_Mean = pd.merge(small_comp['Small Average HHI-C5'], med_comp['Medium Average HHI-C5'],
                     left_index=True, right_index=True, how='left')
HHI5_Mean = pd.merge(HHI5_Mean[['Small Average HHI-C5', 'Medium Average HHI-C5']],
                     lar_comp['Large Average HHI-C5'], left_index=True, right_index=True, how='left')

HHI5_Median= pd.merge(small_comp['Small Median HHI-C5'], med_comp['Medium Median HHI-C5'],
                     left_index=True, right_index=True, how='left')
HHI5_Median = pd.merge(HHI5_Median[['Small Median HHI-C5', 'Medium Median HHI-C5']],
                     lar_comp['Large Median HHI-C5'], left_index=True, right_index=True, how='left')
HHI5_Median_transposed = HHI5_Median.T # or df1.transpose()


HHI8_Median= pd.merge(small_comp['Small Median HHI-C8'], med_comp['Medium Median HHI-C8'],
                     left_index=True, right_index=True, how='left')
HHI8_Median = pd.merge(HHI8_Median[['Small Median HHI-C8', 'Medium Median HHI-C8']],
                     lar_comp['Large Median HHI-C8'], left_index=True, right_index=True, how='left')
HHI8_Median_transposed = HHI8_Median.T # or df1.transpose()



HHI7_Median= pd.merge(small_iq['Small Median HHI-IQ7'], med_iq['Medium Median HHI-IQ7'],
                     left_index=True, right_index=True, how='left')
HHI7_Median = pd.merge(HHI7_Median[['Small Median HHI-IQ7', 'Medium Median HHI-IQ7']],
                     lar_iq['Large Median HHI-IQ7'], left_index=True, right_index=True, how='left')
HHI7_Median_transposed = HHI7_Median.T # or df1.transpose()

HHI6_Median= pd.merge(small_iq['Small Median HHI-IQ6'], med_iq['Medium Median HHI-IQ6'],
                     left_index=True, right_index=True, how='left')
HHI6_Median = pd.merge(HHI6_Median[['Small Median HHI-IQ6', 'Medium Median HHI-IQ6']],
                     lar_iq['Large Median HHI-IQ6'], left_index=True, right_index=True, how='left')
HHI6_Median_transposed = HHI6_Median.T # or df1.transpose()

tempt = pd.merge(HHI5_Median, HHI8_Median, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, HHI6_Median, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, HHI7_Median, left_index=True, right_index=True, how='left')
tempt_trans = tempt.T





# NEw tables organize as follows:
# Agency costs: leverage and market to book, Capex
# Governance: independent board (percentage independent directors > < median), managerial ownership, governance index
# Asymetric information: tangibility, RD, credit rating, SP500 index and NYSE listing, insitutional ownership
#Agency Costs
C = FUNDABS_desc_s1.groupby(['4ps'])[['HHI-C5', 'HHI-C8', 'BLEV_cut']].mean()
a = ['SBN', 'SUB', 'DLTO', 'CL', 'SHORT']


#leverage
a = ['BLEV_cut']
a = ['HHI-C5', 'HHI-C8']
lowlev = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'BLEV_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hilev = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'BLEV_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowlevIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'BLEV_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hilevIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'BLEV_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
tempt = pd.merge(lowlev, hilev, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowlevIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hilevIQ, left_index=True, right_index=True, how='left')
tempt_trans = tempt.T


tempt_trans.to_csv(os.path.join(tables_notregs, "lev.csv"), index=True)


# market to book capex
#market book
a = ['HHI-C5', 'HHI-C8']
lowmb = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'MB_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
himb = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'MB_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowmbIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'MB_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
himbIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'MB_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
tempt = pd.merge(lowmb, himb, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowmbIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, himbIQ, left_index=True, right_index=True, how='left')
tempt_trans = tempt.T

# market to book capex

a = ['HHI-C5', 'HHI-C8']
lowcapx = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'CAPEX_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hicapx = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'CAPEX_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowcapxIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'CAPEX_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hicapxIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'CAPEX_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowcapx, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hicapx, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowcapxIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hicapxIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "mbcapx.csv"), index=True)

# Tangibility, RD, Rating, NYSE membership, instituional ownership

a = ['HHI-C5', 'HHI-C8']
lowtang = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'TANG_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hitang= Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'TANG_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowtangIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'TANG_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hitangIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'TANG_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
tempt = pd.merge(lowtang, hitang, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowtangIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hitangIQ, left_index=True, right_index=True, how='left')

a = ['HHI-C5', 'HHI-C8']
lowRD = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'RD_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hiRD = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'RD_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowRDIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'RD_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hiRDIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'RD_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowRD, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hiRD, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowRDIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hiRDIQ, left_index=True, right_index=True, how='left')

a = ['HHI-C5', 'HHI-C8']
notnyse = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'NYSE_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
nyse = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'NYSE_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
notnyseIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'NYSE_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
nyseIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'NYSE_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, notnyse, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, nyse, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, notnyseIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, nyseIQ, left_index=True, right_index=True, how='left')



a = ['HHI-C5', 'HHI-C8']
lowinst = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'INSTOWN_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hiinst = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'INSTOWN_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowinstIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'INSTOWN_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hiinstIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'INSTOWN_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowinst, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hiinst, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowinstIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hiinstIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "asinf.csv"), index=True)

FUNDABS_desc['UR'] = np.where(FUNDABS_desc.fyear < 1986, np.isnan, FUNDABS_desc['UR'])
FUNDABS_desc['RATED']
FUNDABS_desc['RATED'] = np.where(FUNDABS_desc.fyear < 1986, np.isnan, FUNDABS_desc['RATED'])
FUNDIQ_desc['RATED'] = 1 - FUNDIQ_desc['UR']
a = ['HHI-C5', 'HHI-C8']
ur = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'UR', time_var='4YEARP',
                               count=0, sample_name='Compustat')
rated = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'RATED', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
urIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'UR', time_var='4YEARP',
                               count=0, sample_name='Compustat')
ratedIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'RATED', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(ur, rated, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, urIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, ratedIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "tated.csv"), index=True)

#GINDEX, Managerial onwership, board independence, hostility index
GIGRP_2
OWN_A_2
board-independence_2


a = ['HHI-C5', 'HHI-C8']
ginl = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'GIGRP_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
ginh = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'GIGRP_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
ginlIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'GIGRP_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
ginhIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'GIGRP_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(ginl, ginh, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, ginlIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, ginhIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "gindex.csv"), index=True)



a = ['HHI-C5', 'HHI-C8']
lowown = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'OWN_A_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hiown = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'OWN_A_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowownIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'OWN_A_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hiownIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'OWN_A_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(lowown, hiown, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowownIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hiownIQ, left_index=True, right_index=True, how='left')
tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "own.csv"), index=True)

a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'board-independence_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'board-independence_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'board-independence_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'board-independence_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(lowbi, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "board.csv"), index=True)

dual_ext
FUNDABS_desc['dual_ext'] = np.where(FUNDABS_desc['fyear'] < 1978, np.nan, FUNDABS_desc['dual_ext'])
FUNDABS_desc['NOTDUAL'] = 1 - FUNDABS_desc['dual_ext']
FUNDIQ_desc['NOTDUAL'] = 1 - FUNDIQ_desc['dual_ext']
FUNDABS_desc['DUALCLASS'] = FUNDABS_desc['dual_ext']
FUNDIQ_desc['DUALCLASS'] = FUNDIQ_desc['dual_ext']

a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'NOTDUAL', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'DUALCLASS', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'NOTDUAL', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'DUALCLASS', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(lowbi, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "dual.csv"), index=True)


#Accounts payable, inventories, accounts receivables, negative cashflow
negative_prof
FUNDABS_desc['neg_prof'] = np.where(FUNDABS_desc['PROF'] <= 0, 1, 0)
FUNDABS_desc['pos_prof'] = np.where(FUNDABS_desc['PROF'] > 0, 1, 0)
FUNDIQ_desc['neg_prof'] = np.where(FUNDIQ_desc['PROF'] <= 0, 1, 0)
FUNDIQ_desc['pos_prof'] = np.where(FUNDIQ_desc['PROF'] > 0, 1, 0)



a = ['HHI-C5', 'HHI-C8']
negprofc = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'neg_prof', time_var='4YEARP',
                               count=0, sample_name='Compustat')
posprofc = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'pos_prof', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
negprofq = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'neg_prof', time_var='4YEARP',
                               count=0, sample_name='Compustat')
posprofq = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'pos_prof', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(negprofc, posprofc, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, negprofq, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, posprofq, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "prof.csv"), index=True)


a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'AP_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'AP_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'AP_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'AP_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(lowbi, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')


a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'AR_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'AR_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'AR_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'AR_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowbi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')

a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'INV_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'INV_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'INV_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'INV_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowbi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')

a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'WCAP_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'WCAP_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'WCAP_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'WCAP_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowbi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')

a = ['HHI-C5', 'HHI-C8']
lowbi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'CFV_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibi = Functions.tempish(FUNDABS_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'CFV_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')
a = ['HHI-IQ7', 'HHI-IQ6']
lowbiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               ['Leverage'], [0,0], ['median'], 'CFV_1', time_var='4YEARP',
                               count=0, sample_name='Compustat')
hibiIQ = Functions.tempish(FUNDIQ_desc, a, ['Median'],
               [ 'Leverage'], [0,0], ['median'], 'CFV_2', time_var='4YEARP',
                               count=0, sample_name='Compustat')

tempt = pd.merge(tempt, lowbi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibi, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, lowbiIQ, left_index=True, right_index=True, how='left')
tempt = pd.merge(tempt, hibiIQ, left_index=True, right_index=True, how='left')

tempt_trans = tempt.T
tempt_trans.to_csv(os.path.join(tables_notregs, "lets.csv"), index=True)

AP AR INV WCAP CFV