

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
tps = [[1969,1974], [1975,1979], [1980,1984], [1985,1989], [1990,1994], [1995,1999], [2000,2004],
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


build_period_var(FUNDABS_desc, tps)
build_period_var(FUNDIQ_desc, tps)
build_period_var(FUNDABS_desc_s1, tps)

C = FUNDABS_desc_s1.groupby(['4ps'])[['HHI-C5', 'HHI-C8', 'BLEV_cut']].mean()

small_comp = Functions.tempish(FUNDABS_desc, ['HHI-C5', 'HHI-C8', 'BLEV_cut'], ['Average', 'Median'],
               ['Small', 'Small', 'Leverage Compustat'], [3,3,1], ['mean', 'median'], 'S_1', time_var='4YEARP')
med_comp = Functions.tempish(FUNDABS_desc, ['HHI-C5', 'HHI-C8', 'BLEV_cut'], ['Average', 'Median'],
               ['Medium','Medium', 'Leverage Compustat'],  [3,3,1], ['mean', 'median'], 'S_2', time_var='4YEARP')
lar_comp = Functions.tempish(FUNDABS_desc, ['HHI-C5', 'HHI-C8', 'BLEV_cut'], ['Average', 'Median'],
               ['Large','Large', 'Leverage Compustat'],  [3,3,1], ['mean', 'median'], 'S_3', time_var='4YEARP')

small_iq = Functions.tempish(FUNDIQ_desc, ['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut'], ['Average', 'Median'],
               ['Small', 'Small', 'Leverage Capital IQ'], [3,3,1], ['mean', 'median'], 'S_1', time_var='4YEARP')

med_iq = Functions.tempish(FUNDIQ_desc, ['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut'], ['Average', 'Median'],
               ['Medium','Medium', 'Leverage Capital IQ'], [3,3,1], ['mean', 'median'], 'S_2', time_var='4YEARP')
lar_iq = Functions.tempish(FUNDIQ_desc, ['HHI-IQ7', 'HHI-IQ6', 'BLEV_cut'], ['Average', 'Median'],
               ['Large','Large', 'Leverage Capital IQ'], [3,3,1], ['mean', 'median'], 'S_3', time_var='4YEARP')

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