#statiscs and tables for printing
#correct erase later#
import scipy.stats as scistats


FUNDABSIQ = FUNDIQ_desc
FUNDABSN = FUNDABS_desc[FUNDABS_desc.fyear >= 2002]
print(len(FUNDABSN))  # 40442
print(len(FUNDABSIQ))  # 35928
FUNDABSN['HH1_IQ'] = np.nan
FUNDABSN['HH2_IQ'] = np.nan
sample_stats = ['MVBook', 'PROF','CASH', 'TANG', 'CAPEX', 'ADVERT', 'RD', 'MLEV', 'BLEV', 'AP','income_std_12']

sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'TANG_cut', 'MLEV_cut', 'BLEV_cut',
                'income_std_12_cut', 'income_std_9_cut', 'income_std_4_cut', 'AGE']

sample_stats = ['HH1_IQ', 'HH3_IQ', 'HH2_IQ', 'HH4_IQ']
sample_stats = ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1']
sample_stats1 = ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1']
sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut']
sample_stats = ['AT', 'MVBook', 'PROF', 'DIVP', 'CASH']


FUNDABSIQ[sample_stats].describe()
FUNDABSN[sample_stats].describe()


i = FUNDABSIQ[sample_stats].mean()
ii = FUNDABSIQ[sample_stats].median()
iii = FUNDABSN[sample_stats1].mean()
iv = FUNDABSN[sample_stats1].median()

combo = [i, ii, iii, iv]
result1 = pd.concat(combo, axis=1)
print(result1)

i = FUNDABSIQ[sample_stats].mean()
ii = FUNDABSIQ[sample_stats].median()
iii = FUNDABSN[sample_stats].mean()
iv = FUNDABSN[sample_stats].median()
combo = [i, ii, iii, iv]
result2 = pd.concat(combo, axis=1)
print(result2)

combo = [i, ii, iii, iv]
result = pd.concat(combo, axis=1)

scistats.mannwhitneyu(FUNDABSIQ['AT_cut'], FUNDABSN['AT_cut'], alternative='two-sided')
scistats.mannwhitneyu(FUNDABSIQ['DIVP'], FUNDABSN['DIVP'], alternative='two-sided')
scistats.mannwhitneyu(FUNDABSIQ['AT'], FUNDABSN['AT'])

loc = FUNDABSIQ['HH2'].dropna()

a = scistats.ttest_ind(loc, FUNDABSN['HH2'])
print(a)
b = scistats.mannwhitneyu(loc, FUNDABSN['HH2'])
print(b)

a = scistats.ttest_ind(FUNDABSIQ['AT_cut'], FUNDABSN['AT_cut'])
print(a)
b = scistats.mannwhitneyu(FUNDABSIQ['AT_cut'], FUNDABSN['AT_cut'])
print(b)


a = scistats.ttest_ind(FUNDABSIQ['MVBook_cut'].dropna(), FUNDABSN['MVBook_cut'].dropna())
print(a)
b = scistats.mannwhitneyu(FUNDABSIQ['MVBook_cut'], FUNDABSN['MVBook_cut'])
print(b)


a = scistats.ttest_ind(FUNDABSIQ['DIVP'].dropna(), FUNDABSN['DIVP'].dropna())
print(a)
b = scistats.mannwhitneyu(FUNDABSIQ['DIVP'].dropna(), FUNDABSN['DIVP'].dropna())
print(b)

'CASH_cut'

a = scistats.ttest_ind(FUNDABSIQ['CASH_cut'].dropna(), FUNDABSN['CASH_cut'].dropna())
print(a)
b = scistats.mannwhitneyu(FUNDABSIQ['CASH_cut'].dropna(), FUNDABSN['CASH_cut'].dropna())
print(b)

a = scistats.ttest_ind(FUNDABSIQ['TANG_cut'].dropna(), FUNDABSN['TANG_cut'].dropna())
print(a)
b = scistats.mannwhitneyu(FUNDABSIQ['TANG_cut'].dropna(), FUNDABSN['TANG_cut'].dropna())
print(b)


def tests(data1, data2, list_test):
    i = data1[list_test].mean()
    ii = data1[list_test].median()
    iii = data2[list_test].mean()
    iv = data2[list_test].median()
    combo = [i, ii, iii, iv]
    # result2 = pd.concat(combo, axis=1)
    ser = pd.DataFrame(columns=['ttest', 'wilcox'])
    for i in list_test:
        a = scistats.ttest_ind(data1[i].dropna(), data2[i].dropna())
        b = scistats.mannwhitneyu(data1[i].dropna(), data2[i].dropna())
        x = [a[1], b[1]]
        x = [0 if i < 0.00001 else i for i in x]
        df2 = pd.DataFrame({"ttest": [x[0]],
                            "wilcox": [x[1]]}, index=[i])
        ser = ser.append(df2)
    return pd.concat(combo, axis=1).join(ser)
list_test = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut']
#list_test = ['AT', 'MVBook', 'PROF', 'DIVP', 'CASH']
print(tests(FUNDABSIQ, FUNDABSN, list_test))




t_statistic, p_value = scistats.ttest_ind(group1, group2)








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

