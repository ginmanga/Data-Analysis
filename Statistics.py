import pandas as pd
import numpy as np
import os
import Functions
import scipy.stats as scistats

datadirectory = " "
tables = 0

FUNDIQ_desc_old = pd.read_csv(os.path.join(datadirectory, "FUNDIQDESC-DEC30.csv.gz"))
# FUNDABS_desc = pd.read_csv(os.path.join(datadirectory, "FUNDABSDESC-DEC31.csv.gz"))

# FUNDIQ_desc = pd.read_csv(os.path.join(datadirectory, "FUNDIQDESC-Jan29.csv.gz"))
# FUNDABS_desc = pd.read_csv(os.path.join(datadirectory, "FUNDABSDESC-Jan29.csv.gz"))

# FUNDIQ_desc = pd.read_csv(os.path.join(datadirectory, "FUNDIQDESC-Jan30.csv.gz"))
# FUNDABS_desc = pd.read_csv(os.path.join(datadirectory, "FUNDABSDESC-Jan30.csv.gz"))

FUNDIQ_desc = pd.read_csv(os.path.join(datadirectory, "FUNDIQDESC-Feb1.csv.gz"))
FUNDABS_desc = pd.read_csv(os.path.join(datadirectory, "FUNDABSDESC-Feb1.csv.gz"))


FUNDABS_desc['C/B'] = FUNDABS_desc['LJUNK']
FUNDABS_desc['BBB/A'] = FUNDABS_desc['LIG']
FUNDABS_desc['AA/AAA'] = FUNDABS_desc['HIG']
FUNDABS_desc['HHI-C8'] = FUNDABS_desc['HH1']
FUNDABS_desc['HHI-C5'] = FUNDABS_desc['HH2']
FUNDABS_desc['HH1_IQ'] = np.nan
FUNDABS_desc['HH2_IQ'] = np.nan


FUNDIQ_desc['C/B'] = FUNDIQ_desc['LJUNK']
FUNDIQ_desc['BBB/A'] = FUNDIQ_desc['LIG']
FUNDIQ_desc['AA/AAA'] = FUNDIQ_desc['HIG']
FUNDIQ_desc['HHI-C8'] = FUNDIQ_desc['HH1']
FUNDIQ_desc['HHI-C5'] = FUNDIQ_desc['HH2']
FUNDIQ_desc['HHI-IQ7'] = FUNDIQ_desc['HH1_IQ']
FUNDIQ_desc['HHI-IQ6'] = FUNDIQ_desc['HH2_IQ']
FUNDIQ_desc['HHI-IQ7B'] = FUNDIQ_desc['HH1_IQB']
FUNDIQ_desc['HHI-IQ6B'] = FUNDIQ_desc['HH2_IQB']

FUNDIQ_desc_old['C/B'] = FUNDIQ_desc_old['LJUNK']
FUNDIQ_desc_old['BBB/A'] = FUNDIQ_desc_old['LIG']
FUNDIQ_desc_old['AA/AAA'] = FUNDIQ_desc_old['HIG']
FUNDIQ_desc_old['HHI-C8'] = FUNDIQ_desc_old['HH1']
FUNDIQ_desc_old['HHI-C5'] = FUNDIQ_desc_old['HH2']
FUNDIQ_desc_old['HHI-IQ7'] = FUNDIQ_desc_old['HH1_IQ']
FUNDIQ_desc_old['HHI-IQ6'] = FUNDIQ_desc_old['HH2_IQ']


FUNDABS_desc['NDIVP'] = 1-FUNDABS_desc['DIVP']
FUNDABS_desc['UR'] = 1-FUNDABS_desc['RATED']
FUNDIQ_desc['NDIVP'] = 1-FUNDIQ_desc['DIVP']

FUNDABSIQ = FUNDIQ_desc

FUNDABS_desc = FUNDABS_desc.drop_duplicates(subset=['gvkey', 'fyear'])
FUNDIQ_desc = FUNDIQ_desc.drop_duplicates(subset=['gvkey', 'fyear'])
FUNDABSIQ = FUNDABSIQ.drop_duplicates(subset=['gvkey', 'fyear'])

FUNDABSIQ = FUNDABSIQ[FUNDABSIQ.BLEV <= 1]
FUNDIQ_desc = FUNDIQ_desc[FUNDIQ_desc.BLEV <= 1]
FUNDABS_desc = FUNDABS_desc[FUNDABS_desc.BLEV <= 1]
FUNDABSN = FUNDABS_desc[FUNDABS_desc.fyear >= 2002]
print(len(FUNDABSN))  # 39864 40442
print(len(FUNDABSIQ))  # 35449 35928

FUNDABS_desc = FUNDABS_desc[FUNDABS_desc.fyear >= 1969]
print(len(FUNDABSN))  # 39864 39864
print(len(FUNDABSIQ))  # 35449 35449
print(len(FUNDABS_desc))  # 151602

mean_fyear = FUNDABS_desc.groupby(['fyear'])[['HHI-C5']].mean()
median_fyear = FUNDABS_desc.groupby(['fyear'])[['HHI-C5']].median()

FUNDABS_desc.groupby(['fyear'])[['HHI-C8']].mean()
FUNDABS_desc.groupby(['fyear'])[['HHI-C8']].median()

FUNDABS_desc.groupby(['fyear'])[['PROF']].mean()
FUNDABS_desc.groupby(['fyear'])[['PROF']].median()

FUNDABS_desc['PROF'].describe()
FUNDABS_desc['PROF_cut'].describe()

FUNDABS_desc['cut_income_std_10_FF48'].describe()
FUNDABS_desc['income_std_10_FF48'].describe()

FUNDABS_desc['income_std_4_cut'].describe()
FUNDABS_desc['AP_cut'].describe()
FUNDABS_desc['AP'].describe()
FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].mean()
FUNDABS_desc.groupby(['fyear'])[['cut_income_std_10_FF48']].median()

FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].mean()
FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].mean()
FUNDABS_desc.groupby(['fyear'])[['income_std_10_FF48']].median()

FUNDABS_desc.groupby(['fyear'])[['AP_cut']].median()
FUNDABS_desc.groupby(['fyear'])[['AP_cut']].mean()
FUNDABS_desc.groupby(['fyear'])[['AP']].median()

compare = FUNDABS_desc[FUNDABS_desc.fyear <= 1994]

compare['cut_income_std_10_FF48'].describe()
compare['income_std_10_FF48'].describe()

print(len(FUNDABSN))  # 39864
print(len(FUNDABSIQ))  # 35449
# Get the median firm and show the 5 categories in 1979 and then 2018
median_79 = FUNDABS_desc[(FUNDABS_desc['HHI-C5'] <= median_fyear.loc[1979][0] + 0.0009) &
                         (FUNDABS_desc['HHI-C5'] >= median_fyear.loc[1979][0] - 0.0009) &
                         (FUNDABS_desc.fyear == 1979)]

median_18 = FUNDABS_desc[(FUNDABS_desc['HHI-C5'] <= median_fyear.loc[2018][0] + 0.0001) &
                         (FUNDABS_desc['HHI-C5'] >= median_fyear.loc[2018][0] - 0.0001) &
                         (FUNDABS_desc.fyear == 2018)]
check_list = ['gvkey', 'fyear', 'at', 'TOTALDEBT_C', 'AT', 'RATED', 'SUB_C', 'SBN_C', 'BD_C', 'CL_C', 'SHORT_C',
              'HHI-C8', 'HHI-C5']

checki = FUNDABS_desc[check_list]
check = checki[checki.gvkey == 6845]

FUNDABSIQ['SSS'] = 1
FUNDABSNI = pd.merge(FUNDABSN, FUNDABSIQ[['gvkey', 'datadate', 'SSS']], left_on=['gvkey', 'datadate'],
                     right_on=['gvkey', 'datadate'], how='left')

i = FUNDABSNI['SSS'].sum() #34313

FUNDABSNI = FUNDABSNI[FUNDABSNI.SSS.isnull()]
print(len(FUNDABSNI))  # 5551

# FUNDABSN['SSSS'] = 1
FUNDABSIQI = pd.merge(FUNDABSIQ, FUNDABSN[['gvkey', 'datadate', 'SSSS']], left_on=['gvkey', 'datadate'],
                      right_on=['gvkey', 'datadate'], how='left')

i = FUNDABSIQI['SSSS'].sum()  # 34313

FUNDABSIQI = FUNDABSIQI[FUNDABSIQI.SSSS.isnull()]
print(len(FUNDABSIQI))  # 1136

# Simple statas by CR
UR = FUNDABS_desc[FUNDABS_desc.UR == 1]
LJ = FUNDABS_desc[FUNDABS_desc.LJUNK == 1]
BB = FUNDABS_desc[FUNDABS_desc.BB == 1]
LIG = FUNDABS_desc[FUNDABS_desc.LIG == 1]
HIG = FUNDABS_desc[FUNDABS_desc.HIG == 1]
UR.groupby(['fyear'])[['HHI-C5']].mean()
UR.groupby(['fyear'])[['HHI-C5']].median()
LJ.groupby(['fyear'])[['HHI-C5']].mean()
LJ.groupby(['fyear'])[['HHI-C5']].median()

########## Median Junk firms  ##########

median_fyearLJ = LJ.groupby(['fyear'])[['HHI-C5']].median()

median_LJ86 = LJ[(LJ['HHI-C5'] <= median_fyearLJ.loc[1986][0] + 0.005) &
                 (LJ['HHI-C5'] >= median_fyearLJ.loc[1986][0] - 0.005) &
                 (LJ.fyear == 1986)]

median_LJ86 = LJ[(LJ['HHI-C5'] <= median_fyearLJ.loc[1986][0] + 0.01) &
                 (LJ['HHI-C5'] >= median_fyearLJ.loc[1986][0] - 0.01)]

median_LJ95 = LJ[(LJ['HHI-C5'] <= median_fyearLJ.loc[1995][0] + 0.001) &
                 (LJ['HHI-C5'] >= median_fyearLJ.loc[1995][0] - 0.001) &
                 (LJ.fyear == 1995)]

median_LJ16 = LJ[(LJ['HHI-C5'] <= median_fyearLJ.loc[2016][0] + 0.0125) &
                 (LJ['HHI-C5'] >= median_fyearLJ.loc[2016][0] - 0.0125) &
                 (LJ.fyear == 2016)]

check_list = ['gvkey', 'fyear', 'at', 'TOTALDEBT_C', 'AT', 'RATED', 'SUB_C', 'SBN_C', 'BD_C', 'CL_C', 'SHORT_C',
              'HHI-C8', 'HHI-C5', 'splticrm',  'SUB_CPCT', 'SBN_CPCT', 'BD_CPCT', 'CL_CPCT', 'SHORT_CPCT']

checki = median_LJ86[check_list]
checki2 = median_LJ95[check_list]
checki3 = median_LJ16[check_list]
check = checki[checki.gvkey == 4535]


#################
sample_stats = ['MVBook', 'PROF', 'CASH', 'TANG', 'CAPEX', 'ADVERT', 'RD', 'MLEV', 'BLEV', 'AP', 'income_std_12']

sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'TANG_cut', 'MLEV_cut', 'BLEV_cut',
                'income_std_12_cut', 'income_std_9_cut', 'income_std_4_cut', 'AGE']

sample_stats = ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1']
sample_stats1 = ['HH1_IQ', 'HH2_IQ', 'HH2', 'HH1']
sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut']
sample_stats = ['AT', 'MVBook', 'PROF', 'DIVP', 'CASH']

sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'RD_cut', 'UR', 'income_std_12_cut']

FUNDABSIQ[sample_stats].describe()
FUNDABSN[sample_stats].describe()
FUNDABSNI['PROF_cut'].describe()

i = FUNDABSIQ[sample_stats1].mean()
ii = FUNDABSIQ[sample_stats1].median()
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

#merge and find stats of missing from CAPIQ


sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'RD_cut', 'UR',
                'income_std_12_cut', 'income_std_4_cut', 'AGE', 'HH2', 'HH1', 'HH1_IQ', 'HH2_IQ']

sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'TANG_cut', 'RD_cut', 'UR',
                'MLEV_cut', 'BLEV_cut', 'income_std_12_cut', 'income_std_4_cut', 'AGE',
                'HH2', 'HH1', 'HH1_IQ', 'HH2_IQ']

i = FUNDABSIQ[sample_stats].mean()
ii = FUNDABSIQ[sample_stats].median()
iii = FUNDABSN[sample_stats].mean()
iv = FUNDABSN[sample_stats].median()
v = FUNDABSNI[sample_stats].mean()
vi = FUNDABSNI[sample_stats].median()

vii = FUNDABSIQI[sample_stats].mean()
viii = FUNDABSIQI[sample_stats].median()

combo = [i, ii, iii, iv, v, vi]
result3 = pd.concat(combo, axis=1)
print(result3)

combo = [i, ii, iii, iv]
result4 = pd.concat(combo, axis=1)
print(result4)

combo = [i, ii, v, vi]
result5 = pd.concat(combo, axis=1)
print(result5)

combo = [v, vi, vii, viii]
result6 = pd.concat(combo, axis=1)
print(result6)

for i in result3[0]:
    print(Functions.re_parameters(str(round(i, 3))))

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
list_test = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'TANG_cut', 'RD_cut', 'UR',
                'income_std_12_cut', 'income_std_4_cut', 'AGE', 'HH2', 'HH1', 'HH1_IQ', 'HH2_IQ']
#list_test = ['AT', 'MVBook', 'PROF', 'DIVP', 'CASH']
list_test = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'TANG_cut', 'RD_cut', 'UR',
                'MLEV_cut', 'income_std_12_cut', 'income_std_4_cut', 'AGE', 'HH2', 'HH1', 'HH1_IQ', 'HH2_IQ']

s = tests(FUNDABSIQ, FUNDABSN, list_test)
s1 = tests(FUNDABSIQ, FUNDABSNI, list_test)
s2 = tests(FUNDABSN, FUNDABSIQI, list_test)
s3 = tests(FUNDABSNI, FUNDABSIQI, list_test)
def check_pvalues_diffmean(a, options=0):
    """takes a parameter and pvalue and adds asterix"""
    s = a
    check = str(a).split(".")[0]
    digits = 3
    if len(check) >= 3:
        digits = 1
    if len(check) == 2:
        digits = 2
    if a <= 0.01:
        s = str(round(a, digits)).ljust(5, '0')
        if options == 1:
            s = str(round(a,digits)).ljust(5, '0') + '***'
    if (a <= 0.05) & (a > 0.01):
        s = str(round(a, digits)).ljust(5, '0')
        if options == 1:
            s = str(round(a,digits)).ljust(5, '0') + '**'
    if (a <= 0.1) & (a > 0.05):
        s = str(round(a, digits)).ljust(5, '0')
        if options == 1:
            s = str(round(a,digits)).ljust(5, '0') + '*'
    if a > 0.1:
        s = str(round(a, digits)).ljust(5, '0')
        if options == 1:
            s = str(round(a,digits)).ljust(5, '0')
    if a == 0:
        s = '0.000'
        if options == 1:
            s = '0.000' + '***'
    return s

for i in range(4):
    s[i] = s[i].apply(check_pvalues_diffmean)

s['ttest'] = s['ttest'].apply(check_pvalues_diffmean, options=1)
s['wilcox'] = s['wilcox'].apply(check_pvalues_diffmean, options=1)

def run_clear_all(a, options=0):
    for i in range(4):
        a[i] = a[i].apply(check_pvalues_diffmean)
    a['ttest'] = a['ttest'].apply(check_pvalues_diffmean, options=1)
    a['wilcox'] = a['wilcox'].apply(check_pvalues_diffmean, options=1)
    if (options == 1) | (options == 4):
        a.loc['HH1_IQ', 'wilcox'] = np.nan
        a.loc['HH2_IQ', 'wilcox'] = np.nan
    if (options == 2) | (options == 4):
        a.loc['HH1', 2] = np.nan
        a.loc['HH1', 3] = np.nan
        a.loc['HH2', 2] = np.nan
        a.loc['HH2', 3] = np.nan
        a.loc['HH1', 'wilcox'] = np.nan
        a.loc['HH2', 'wilcox'] = np.nan
    return a
s = run_clear_all(s, options=1)
s1 = run_clear_all(s1, options=1)
s2 = run_clear_all(s2, options=4)
s3 = run_clear_all(s3, options=4)
print(FUNDABSIQ['AT_cut'].count())  # 35449
print(FUNDABSN['AT_cut'].count())   # 39864
print(FUNDABSNI['AT_cut'].count())  # 5551
print(FUNDABSIQI['AT_cut'].count())  # 1136

print(FUNDABSIQ['income_std_12_cut'].count())  # 31999
print(FUNDABSN['income_std_12_cut'].count())   # 35876
print(FUNDABSNI['income_std_12_cut'].count())  # 4875
print(FUNDABSIQI['income_std_12_cut'].count())  #998

print(FUNDABSIQ['income_std_4_cut'].count())  # 33775
print(FUNDABSN['income_std_4_cut'].count())   # 37955
print(FUNDABSNI['income_std_4_cut'].count())  # 5238
print(FUNDABSIQI['income_std_4_cut'].count()) # 1058


sample_stats = ['AT_cut', 'MVBook_cut', 'PROF_cut', 'DIVP', 'CASH_cut', 'TANG_cut', 'RD_cut', 'UR',
                'MLEV_cut', 'income_std_12_cut', 'income_std_4_cut', 'AGE', 'HH2', 'HH1', 'HH1_IQ', 'HH2_IQ']

sample_stats_re = ['Size', 'M/B', 'Profitability', 'Div.payer', 'Cash holdings', 'Tagibility', 'R&D exp.',
                   'Unrated', 'Market Leverage', 'CFV_Q', 'CFV_A', 'AGE', 'HHI-C5', 'HHI-C8', 'HHI-IQ7', 'HHI-IQ6']


list1 = [0, 1, 2, 3, 'ttest', 'wilcox']
list2 = ['Mean','Median','Mean','Median', 't-test', 'Wilcoxon Test']
s = Functions.rename(s, list1, list2)
s = Functions.rename(s, sample_stats, sample_stats_re, options=1)
s1 = Functions.rename(s1, list1, list2)
s1 = Functions.rename(s1, sample_stats, sample_stats_re, options=1)
s2 = Functions.rename(s2, list1, list2)
s2 = Functions.rename(s2, sample_stats, sample_stats_re, options=1)
s3 = Functions.rename(s3, list1, list2)
s3 = Functions.rename(s3, sample_stats, sample_stats_re, options=1)

s.to_csv(os.path.join(tables, "table1.txt"))
s1.to_csv(os.path.join(tables, "table2.txt"))
s2.to_csv(os.path.join(tables, "table3.txt"))
s3.to_csv(os.path.join(tables, "table4.txt"))




FUNDABSIQ['BLEV'].describe()
ss = FUNDABSIQ[FUNDABSIQ.BLEV > 1]
FUNDABSNI['BLEV'].describe()
FUNDABSNI['MLEV'].describe()

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

a = scistats.ttest_ind(FUNDABSIQ['AGE'].dropna(), FUNDABSN['AGE'].dropna())
print(a)
b = scistats.mannwhitneyu(FUNDABSIQ['AGE'].dropna(), FUNDABSN['AGE'].dropna())
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

