import datetime, csv
#from sas7bdat import SAS7BDAT
import pandas as pd
import pandasql as ps
import numpy as np
import gzip, os, csv
import datetime
import matplotlib.pyplot as plt
#want a function to get me a gvkey

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


def plot_maker(a, c, b=[], save=[0], year=1986, method='mean', label=0):
    """Functions takes and makes plots"""
    #a = variable to plot
    #b = group by, list with the columns want to use to group by
    #c = dataset
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'black', 'palegreen']
    color_code = 0
    #print(a)
    if len(a) > 1:
        main_vars = ['fyear']
        main_vars.extend(a)
        series_temp = c[main_vars]
        series_temp = series_temp[series_temp.fyear >= year]
        series_temp = series_temp.astype({'fyear': 'int64'})
        for i in a:
            #print(i)
            #print(c[i])
            o = getattr(series_temp.groupby(['fyear'])[[i]], method) #calls method given by user
            #print(o)
            #series_temp_1 = series_temp.groupby(['fyear'])[[i]].mean().reset_index()
            series_temp_1 = o().reset_index()
            plt.plot(series_temp_1['fyear'], series_temp_1[i], color=colors[color_code], label=i)
            color_code +=1

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
            #series_temp_1 = series_temp[o == 1].groupby(['fyear'])[[a[0]]].mean().reset_index()
            plt.plot(series_temp_1['fyear'], series_temp_1[a], color=colors[color_code], label=i)
            color_code +=1

    if save[0] == 1 and label == 0:
        plt.savefig(os.path.join(save[1], save[2]))
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
    print("hello")
    for index, elem in enumerate(list1):
        if options == 0:
            data.rename(columns={elem: list2[index]}, inplace=True)
        else:
            data.rename(index={elem: list2[index]}, inplace=True)
    return data

def winsor(data, column=[], cond_list=[], cond_num=[], quantiles=[0.99, 0.01], year=1968, freq='annual'):
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