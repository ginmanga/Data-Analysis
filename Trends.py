

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
holder_par = []
holder_std = []

holder_par, holder_std = Functions.trend_parameters(compIQ, trend, periods)
holder_list = Functions.list_maker_deluxe(holder_par, holder_std)
for i in holder_list:
    Functions.really_short_latex(i)




trend = ['Average HHI-C5', 'Average HHI-C8',
         'Median HHI-C5', 'Median HHI-C8']
b1 = Functions.run_regressions_4(data=[compIQ.loc[1972.0:1979.0]], endog=[trend], exog=['New_ID'], options=2, clusterfirm=2)
Functions.prep_params(b1)

exog_2 = ['trend']

Functions.write_file_latex_style(tables,
                                 "cc.txt",
                                 Functions.prep_latex_table(Functions.print_reg(trend, exog_2, Functions.prep_params(b1))),
                                 'w')