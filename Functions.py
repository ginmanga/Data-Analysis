import datetime, csv
#from sas7bdat import SAS7BDAT
import pandas as pd
import pandasql as ps
import numpy as np
import gzip, os, csv
import datetime
import matplotlib.pyplot as plt
from linearmodels.panel import PanelOLS
from linearmodels.panel import compare
from linearmodels.panel import PooledOLS
import statsmodels.api as sm



def write_file_latex_style(path_file, filename, data, write_type):
    """Writes all data to file"""
    #first tells if it writtes or appends
    #write_type 'w' or 'a'
    print(data)
    path_to_2 = os.path.join(path_file, filename)
    with open(path_to_2, write_type, encoding='utf-8') as file:
        #file.writelines('&'.join(i) + r"\\" for i in data)
        file.writelines('&'.join(i) + " \n" for i in data)
    file.close()


def hhi_calculator(x, y, c, df, options=0, denominators=[],selection=[]):
    tt = [i + '_temp' for i in x]
    for i in x:
        df[i + '_temp'] = (df[i]/df[y])**2
    df[c] = df[tt].sum(axis=1)
    df[c] = (df[c]-(1/len(tt)))/(1-(1/len(tt)))
    return df.drop(tt, axis=1)


def pct_calculator(x, y, name, df, options=0, denominators=[], selection=[]):
    for i in x:
        df[i + name] = (df[i]/df[y])
    return df


def plot_maker(a, c, b=[], save=[0], year=1986, method='mean', label=0, sep_label=0):
    """Functions takes and makes plots"""
    #a = variable to plot
    #b = group by, list with the columns want to use to group by
    #c = dataset
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'black', 'palegreen']
    color_code = 0
    print(len(a))
    figData = plt.figure()
    ax = plt.gca()
    if len(a) > 1:
        main_vars = ['fyear']
        main_vars.extend(a)
        series_temp = c[main_vars]
        series_temp = series_temp[series_temp.fyear >= year]
        series_temp = series_temp.astype({'fyear': 'int64'})
        for i in a:
            o = getattr(series_temp.groupby(['fyear'])[[i]], method) #calls method given by user
            series_temp_1 = o().reset_index()
            plt.plot(series_temp_1['fyear'], series_temp_1[i], color=colors[color_code], label=i)
            color_code += 1
    if (len(a) == 1) and (len(b) == 0):
        main_vars = ['fyear']
        main_vars.extend(a)
        series_temp = c[main_vars]
        series_temp = series_temp[series_temp.fyear >= year]
        series_temp = series_temp.astype({'fyear': 'int64'})
        for i in a:
            print(i)
            o = getattr(series_temp.groupby(['fyear'])[[i]], method) #calls method given by user
            series_temp_1 = o().reset_index()
            plt.plot(series_temp_1['fyear'], series_temp_1[i], color=colors[color_code], label=i)
            color_code += 1
    if len(b) > 0:
        main_vars = ['fyear', a[0]]
        main_vars.extend(b)
        series_temp = c[main_vars]
        series_temp = series_temp[series_temp.fyear >= year]
        series_temp = series_temp.astype({'fyear': 'int64'})
        for i in b:
            o = getattr(series_temp, i)
            get_meth = getattr(series_temp[o == 1].groupby(['fyear'])[[a[0]]], method)
            series_temp_1 = get_meth().reset_index()
            plt.plot(series_temp_1['fyear'], series_temp_1[a], color=colors[color_code], label=i)
            color_code += 1

    if save[0] == 1 and label == 0:
        plt.savefig(os.path.join(save[1], save[2]))
        if sep_label == 1:
            #figData = plt.figure()
            #ax = plt.gca()
            figLegend = plt.figure(figsize=(1.5, 1.3))
            # produce a legend for the objects in the other figure
            plt.figlegend(*ax.get_legend_handles_labels(), loc='upper left')
            # save the two figures to files
            figLegend.savefig(os.path.join(save[1], "legend.png"))

    if save[0] == 1 and label == 1:
        plt.legend()
        plt.savefig(os.path.join(save[1], save[2]))

    plt.legend()
    plt.show()
    plt.close()
    del series_temp
    del series_temp_1
    return None


def rating_grps(data):
    ratings = ['AAA+', 'AAA', 'AAA-', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'A-', 'BBB+', 'BBB', 'BBB-',
               'BB+', 'BB', 'BB-', 'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC+', 'CC', 'CC-', 'C']
    ig = ['AAA+', 'AAA', 'AAA-', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'BBB+', 'BBB', 'BBB-']
    hig = ['AAA+', 'AAA', 'AAA-', 'AA+', 'AA', 'AA-']
    lig = ['A+', 'A', 'A-', 'A-''BBB+', 'BBB', 'BBB-']
    hjunk = ['BB+', 'BB', 'BB-']
    lj = ['B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC+', 'CC', 'CC-', 'C']
    junk = ['BB+', 'BB', 'BB-', 'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC+', 'CC', 'CC-', 'C']
    D = ['D', 'SD']
    rated = ['rated', 'INVGRADE', 'JUNK', 'HJUNK', 'LJUNK', 'HIG', 'LIG', 'D']

    AAA = ['AAA+', 'AAA', 'AAA-']
    AA = ['AA+', 'AA', 'AA-']
    A = ['A+', 'A', 'A-']
    BBB = ['BBB+', 'BBB', 'BBB-']
    BB = ['BB+', 'BB', 'BB-']
    B = ['B+', 'B', 'B-']
    C = ['CCC+', 'CCC', 'CCC-', 'CC+', 'CC', 'CC-', 'C']
    groups = [ratings, ig, hig, lig, junk, hjunk, lj, AAA, AA, A, BBB, BB, B, C, D]
    names = ['RATED', 'INVGRADE', 'HIG', 'LIG', 'JUNK', 'HJUNK', 'LJUNK', 'AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'C', 'D']
    groups = [AAA, AA, A, BBB, BB, B, C, D]
    names = ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'C']

    for index, elem in enumerate(names):
        print(elem)
        print(index)
        print(groups[index])
        data[elem] = [1 if x in groups[index] else 0 for x in data['splticrm']]
        data[elem] = [np.nan if x in groups[index] else 0 for x in data['splticrm']]
    return data


def rename(data, list1, list2, options=0):
    print("Renaming data")
    """Renames elements of list1 to list2"""
    for index, elem in enumerate(list1):
        if options == 0:
            data.rename(columns={elem: list2[index]}, inplace=True)
        else:
            data.rename(index={elem: list2[index]}, inplace=True)
    return data


def winsor_old(data, column=[], cond_list=[], cond_num=[], quantiles=[0.99, 0.01], year=1968, freq='annual'):
    """function to winsorize"""
    # print(year)
    # print(cond_list)
    # print(cond_num)
    # print(len(data))
    if freq == 'annual':
        data_temp = data[data['fyear'] >= year]
    if freq == 'qtr':
        data_temp = data[data['fyearq'] >= year]

    for index, elem in enumerate(cond_list):
        data_temp = data_temp[data_temp[elem] == cond_num[index]]
        print(len(data_temp))

    for i in column:
        print(i)
        data['temp1'] = data_temp[i].quantile(quantiles[0])
        data['temp2'] = data_temp[i].quantile(quantiles[1])
        new_var = i + '_cut'
        data[new_var] = np.where(data[i] > data['temp1'], data['temp1'], data[i])
        data[new_var] = np.where(data[new_var] < data['temp2'], data['temp2'], data[new_var])
        data = data.drop('temp1', axis=1)
        data = data.drop('temp2', axis=1)
    return data



def winsor(data, column=[], cond_list=[], cond_num=[], quantiles=[0.99, 0.01], year=1968, freq='annual', options=1):
    """function to winsorize"""
    # print(year)
    # print(cond_list)
    # print(cond_num)
    # print(len(data))
    data_temp = data
    if options == 1:
        if freq == 'annual':
            data_temp = data[data['fyear'] >= year]
        if freq == 'qtr':
            data_temp = data[data['fyearq'] >= year]
        for index, elem in enumerate(cond_list):
            data_temp = data_temp[data_temp[elem] == cond_num[index]]
            print(len(data_temp))

    for i in column:
        print(i)
        data['temp1'] = data_temp[i].quantile(quantiles[0])
        data['temp2'] = data_temp[i].quantile(quantiles[1])
        print(data_temp[i].describe())
        new_var = i + '_cut'
        data[new_var] = np.where(data[i] > data['temp1'], data['temp1'], data[i])
        data[new_var] = np.where(data[new_var] < data['temp2'], data['temp2'], data[new_var])
        data = data.drop('temp1', axis=1)
        data = data.drop('temp2', axis=1)
    return data


def rol_vars(data, var, newname, group, onn, window, levels, mp1=None, group1=[], group2=[], mp=3, options=0):
    """Calculates rolling statistic given parameters"""
    if levels == 1:
        get_meth = getattr(data.groupby('gvkey').rolling(window, min_periods=mp1, on=onn)[[var]], 'std')
    if levels == 2:
        get_meth = getattr(data.groupby('gvkey').rolling(window, min_periods=mp, on=onn)[[var]], 'std')
    c = get_meth().reset_index()
    print(c.columns)
    if levels == 2:
        c = winsor(c, column=[var], cond_list=[], cond_num=[], quantiles=[0.99, 0.01], options=0)
        print(c[var + '_cut'].describe())
        c = pd.merge(c, data[group1],
                     left_on=group,
                     right_on=group, how='left')
        c = c.dropna(subset=[var])
        # get_meth = getattr(c.groupby(group2)[[var]], 'mean')
        if options == 0:
            get_meth = getattr(c.groupby(group2)[[var + '_cut']], 'mean')
        if options == 1:
            get_meth = getattr(c.groupby(group2)[[var + '_cut']], 'median')
        c = get_meth().reset_index()
    #c.rename(columns={var: newname}, inplace=True)
    c.rename(columns={var + '_cut': newname}, inplace=True)
    groups = [newname, 'FF48', 'fyear']
    if levels == 2:
        data = pd.merge(data, c[groups], left_on=group2, right_on=group2, how='left')
    if levels == 1:
        data = pd.merge(data, c, left_on=group, right_on=group, how='left')
    return data, c


def run_regressions(dataa, datab, endog1, endog2, exog1, exog2, options=0):
    results = []
    print(endog1)
    for index, elem in enumerate(endog1):
        name = 'endog1' + '_' + str(index)
        if options == 0:
            mod = PanelOLS(dataa[elem], dataa[exog1], entity_effects=True, time_effects=True)
        if options == 1:
            mod = PanelOLS(dataa[elem], dataa[exog1], entity_effects=False, time_effects=True)
        results.append(mod.fit(cov_type='clustered', clusters=dataa.gvkey))
    for index, elem in enumerate(endog2):
        name = 'endog2' + '_' + str(index)
        if options == 0:
            mod = PanelOLS(datab[elem], datab[exog2], entity_effects=True, time_effects=True)
        if options == 1:
            mod = PanelOLS(datab[elem], datab[exog2], entity_effects=False, time_effects=True)
        results.append(mod.fit(cov_type='clustered', clusters=datab.gvkey))
    return results


def run_regressions_2(data, endog=[], exog=[], options=0):
    results = []
    print(endog)
    for index, elem in enumerate(endog):
        name = 'endog' + '_' + str(index)
        if options == 0:
            for i, e in enumerate(endog):
                mod = PanelOLS(data[elem], data[e], entity_effects=True, time_effects=True)
        if options == 1:
                mod = PanelOLS(data[elem], data[e], entity_effects=False, time_effects=True)
        results.append(mod.fit(cov_type='clustered', clusters=data.gvkey))
    return results


def check_pvalues(t, pvalue):
    """takes a parameter and pvalue and adds asterix"""
    if pvalue <= 0.01:
       s = str(t) + '***'
    if (pvalue <= 0.05) & (pvalue > 0.01):
       s = str(t) + '**'
    if (pvalue <= 0.1) & (pvalue > 0.05):
       s = str(t) + '*'
    if pvalue > 0.1:
        s = str(t)
    return s


def re_parameters(t):
    #t = str(round(e, 3))
    tt = t.split('.')
    t1 = tt[0].strip("-")
    if len(t1) >= 3:
        t = round(float(t), 1)
    if len(t1) == 2:
        #print(t1)
        t = round(float(t), 2)
    if len(t1) < 2:
        res = tt[1].ljust(3, '0')
        t = tt[0] + '.' + res
    return t


def prep_params(reg_results, endog=[], exog=[], param=[], pvalues=[], stderrors=[]):
    """Function to take a list of endog, exog variables, estimated PARAMETERS, pvalues and t-stats"""
    list_para = []
    list_std = []
    list_obs = []
    list_r2 = []
    for index, elem in enumerate(reg_results):
        new_para = []
        new_std = []
        for i, e in enumerate(elem.params.values):
            """Resize parameters and add asterix"""
            t = str(round(e, 3))
            t = re_parameters(t)
            s = check_pvalues(t, elem.pvalues.values[i])
            std = "(" + str(round(elem.std_errors.values[i], 3)).ljust(5, '0') + ")"
            new_para.append(s)
            new_std.append(std)
        new_para = ['\ ' + i if i[0] != '-' else i for i in new_para ]
        list_para.append(new_para)
        list_std.append(new_std)
        list_obs.append(elem.nobs)
        list_r2.append(str(round(elem.rsquared, 3)).ljust(5, '0'))
    return [list_para, list_std, list_obs, list_r2]


def print_reg(endog, exog, reg_results, fixed=['year', 'industry'], model='OLS'):
    if len(endog) != len(reg_results[0]):
        print("Model number incorrect")
        return None
    if len(exog) != len(reg_results[0][0]):
        print("Number of parameters does not match")
        return None
    rows = len(reg_results[0][0]) +  len(reg_results) - 2 + 2
    second_line = [" "]
    second_line.extend(["(" + str(i) + ")" for i in range(1, len(endog) + 1)])
    second_line = ["\\multicolumn{1}{c}{" + i + "}" for i in second_line]
    second_line[0] = " "
    second_line[-1] = second_line[-1] + r"\\" + " \hline"
    first_line = [" "]
    first_line.extend(endog)
    first_line = ["\\multicolumn{1}{l}{"+i+"}" for i in first_line]
    first_line[0] = " "
    first_line[-1] = first_line[-1] + r"\\"
    nobs = ["Obs."]
    model = ["Model"]
    rs = ["R2"]
    fe = [r"\begin{tabular}[c]{@{}l@{}}Industry and \\ Year FEs\end{tabular}"]
    parameters = []
    std_errors =[]
    line_holder = []
    line_holder.append(first_line)
    line_holder.append(second_line)
    for index, elem in enumerate(exog):
        temp = [elem]
        temp1 = [" "]
        for index1, elem1 in enumerate(endog):
            temp.extend([reg_results[0][index1][index]])
            temp1.extend([reg_results[1][index1][index]])
        temp[-1] = temp[-1] + r"\\"
        temp1[-1] = temp1[-1] + r"\\"
        line_holder.append(temp)
        line_holder.append(temp1)
    for index1, elem1 in enumerate(endog):
        fe.extend(["YES"])
        nobs.extend([str(reg_results[2][index1])])
        model.extend(["OLS"])
        rs.extend([reg_results[3][index1]])
    fe[-1] = fe[-1] + r"\\" #add backslashes for latex
    nobs[-1] = nobs[-1] + r"\\" #add backslashes for latex
    model[-1] = model[-1] + r"\\" #add backslashes for latex
    rs[-1] = rs[-1] + r"\\" + " \hline" #add backslashes for latex
    toapp = [fe, nobs, model, rs]
    line_holder.extend(toapp)
    return line_holder



def print_reg_2(endog, exog, reg_results, fixed=['year', 'industry'], model='OLS'):
    if len(endog) != len(reg_results[0]):
        print("Model number incorrect")
        return None
    if len(exog) != len(reg_results[0][0]):
        print("Number of parameters does not match")
        return None
    rows = len(reg_results[0][0]) +  len(reg_results) - 2 + 2
    second_line = [" "]
    second_line.extend(["(" + str(i) + ")" for i in range(1, len(endog) + 1)])
    second_line = ["\\multicolumn{1}{c}{" + i + "}" for i in second_line]
    second_line[0] = " "
    second_line[-1] = second_line[-1] + r"\\" + " \hline"
    first_line = [" "]
    first_line.extend(endog)
    first_line = ["\\multicolumn{1}{l}{"+i+"}" for i in first_line]
    first_line[0] = " "
    first_line[-1] = first_line[-1] + r"\\"
    nobs = ["Obs."]
    model = ["Model"]
    rs = ["R2"]
    fe = [r"\begin{tabular}[c]{@{}l@{}}Industry and \\ Year FEs\end{tabular}"]
    parameters = []
    std_errors =[]
    line_holder = []
    line_holder.append(first_line)
    line_holder.append(second_line)
    for index, elem in enumerate(exog):
        temp = [elem]
        temp1 = [" "]
        for index1, elem1 in enumerate(endog):
            temp.extend([reg_results[0][index1][index]])
            temp1.extend([reg_results[1][index1][index]])
        temp[-1] = temp[-1] + r"\\"
        temp1[-1] = temp1[-1] + r"\\"
        line_holder.append(temp)
        line_holder.append(temp1)
    for index1, elem1 in enumerate(endog):
        fe.extend(["YES"])
        nobs.extend([str(reg_results[2][index1])])
        model.extend(["OLS"])
        rs.extend([reg_results[3][index1]])
    fe[-1] = fe[-1] + r"\\" #add backslashes for latex
    nobs[-1] = nobs[-1] + r"\\" #add backslashes for latex
    model[-1] = model[-1] + r"\\" #add backslashes for latex
    rs[-1] = rs[-1] + r"\\" + " \hline" #add backslashes for latex
    toapp = [fe, nobs, model, rs]
    line_holder.extend(toapp)
    return line_holder



def prep_latex_table(a):
    list_all = []
    begin1 = [r"\begin{table}[]"]
    begin2 = [r"\centering"]
    begin3 = [r'\begin{tabular}'+ "{l" + 'l'*(len(a[0])-1) + "}"]
    begin4 = [r'\hline']
    end1 = [r'\end{tabular}']
    end2 = [r'\end{table}']
    begin = [begin1, begin2, begin3, begin4]
    end = [end1, end2]
    list_all.extend(begin)
    list_all.extend(a)
    list_all.extend(end)
    return list_all