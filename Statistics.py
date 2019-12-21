#statiscs and tables for printing
#correct erase later#


FUNDABS['income_std_12_at'] = FUNDABS['income_std_12']/FUNDABS['at']
FUNDABS['income_std_9_at'] = FUNDABS['income_std_9']/FUNDABS['at']
FUNDIQ['income_std_12_at'] = FUNDIQ['income_std_12']/FUNDIQ['at']
FUNDIQ['income_std_9_at'] = FUNDIQ['income_std_9']/FUNDIQ['at']

FUNDABSIQ = FUNDABS[FUNDABS.fyear>2001]
FUNDABSN = FUNDABS[FUNDABS.fyear>=1969]

sample_stats = ['MVBook', 'PROF','CASH', 'TANG', 'CAPEX', 'ADVERT', 'RD', 'MLEV', 'BLEV', 'AP','income_std_12']

sample_stats = ['AT','MVBook', 'PROF', 'DIVP','CASH', 'TANG', 'CAPEX', 'MLEV','income_std_12_at',
                'sale_std_12','sale_std_ff48_12_2', 'AGE']

i = FUNDABSIQ[sample_stats].mean()
ii = FUNDABSIQ[sample_stats].median()
iii = FUNDIQ[sample_stats].mean()
iv = FUNDIQ[sample_stats].median()

FUNDABSIQ[sample_stats].count()
FUNDIQ[['MLEV']].describe()
combo = [i,ii,iii,iv]
result = pd.concat(combo, axis=1)

sample_stats_re = ['Size','M/B', 'Profitability', 'Dividend payer','Cash', 'Tangibility', 'Capital Expenditures',
                   'Market leverage','CF Vol 1', 'Sale Vol 1','Sale Vol FF', 'AGE']

list1 = [0, 1, 2, 3]
list2 = ['Mean','Median','Mean','Median']
result = Functions.rename(result, list1, list2)
result = Functions.rename(result, sample_stats, sample_stats_re, options=1)

result = result.round(3)
result.to_csv(os.path.join(datadirectory, "table1.csv"))


z=result.to_latex(index=False)

result.rename(columns={0: 'Mean'}, inplace=True)
result.rename(columns={1: 'Median'}, inplace=True)
result.rename(columns={2: 'Mean'}, inplace=True)
result.rename(columns={3: 'Median'}, inplace=True)

sample_stats = ['AT','MVBook', 'PROF', 'DIVP','CASH', 'TANG', 'CAPEX', 'MLEV','income_std_12_at',
                'sale_std_12','sale_std_ff48_12_2', 'AGE']
sample_stats_re = ['Size','M/B', 'Profitability', 'Dividend payer','Cash', 'Tangibility', 'Capital Expenditures',
                   'Market leverage','CF Vol 1', 'Sale Vol 1','Sale Vol FF', 'AGE']

sample_stats = ['HH1','HH2','HH1_IQ']
sample_stats_co =['HH1','HH2']

iii = FUNDABSIQ[sample_stats_co].mean()
iv = FUNDABSIQ[sample_stats_co].median()
i = FUNDIQ[sample_stats].mean()
ii = FUNDIQ[sample_stats].median()
combo = [i,ii,iii,iv]
result = pd.concat(combo, axis=1)
result.to_csv(os.path.join(datadirectory, "table2.csv"))
combo = [iii,iv]
result = pd.concat(combo, axis=1)

list1 = [0, 1, 2, 3]
list2 = ['Mean','Median','Mean','Median']
result = Functions.rename(result, list1, list2)
result = Functions.rename(result, sample_stats, sample_stats_re, options=1)

#Entire sample

#Descriptive stats full sample
sample_stats = ['AT','MVBook', 'PROF', 'DIVP','CASH', 'TANG', 'CAPEX', 'MLEV','income_std_12_at',
                'sale_std_12','sale_std_ff48_12_2', 'AGE','HH1','HH2']
sample_stats_re = ['Size','M/B', 'Profitability', 'Dividend payer','Cash', 'Tangibility', 'Capital Expenditures',
                   'Market leverage','CF Vol 1', 'Sale Vol 1','Sale Vol FF', 'AGE','HH1','HH2']
i = FUNDABSN[sample_stats].mean()
ii = FUNDABSN[sample_stats].median()
FUNDABSN[sample_stats].count()
combo = [i,ii]
result2 = pd.concat(combo, axis=1)
list1 = [0, 1]
list2 = ['Mean','Median']
result2 = Functions.rename(result, list1, list2)
result2 = Functions.rename(result, sample_stats, sample_stats_re, options=1)
#result = result.round(3)
result2.to_csv(os.path.join(datadirectory, "table3.csv"))





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





mod = PanelOLS(FUNDIQ.HH1_IQ, FUNDIQ.AT, entity_effects=True)







FUNDABS[['PROF']].describe()

FUNDABS['PROF'].quantile(0.99)