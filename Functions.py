import datetime, csv
#from sas7bdat import SAS7BDAT
import pandas as pd
import pandasql as ps
import numpy as np
import gzip, os, csv
import datetime
#want a function to get me a gvkey

def hhi_calculator(x, y, c, df):
    tt = [i + '_temp' for i in x]
    for i in x:
        df[i + '_temp'] = (df[i]/df[y])**2
    df[c] = df[tt].sum(axis=1)
    df[c] = (df[c]-(1/len(tt)))/(1-(1/len(tt)))
    return df.drop(tt, axis=1)

def pct_calculator(x, y, name, df):
    for i in x:
        df[i + name] = (df[i]/df[y])
    return df




def plot_maker(a, c, b=[], save=[0], year=1986, method='mean'):
    """Functions takes and makes plots"""
    #a = variable to plot
    #b = group by, list with the columns want to use to group by
    #c = dataset
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b', 'w']
    color_code = 0

    if len(a) > 1:
        main_vars = ['fyear']
        main_vars.extend(a)
        series_temp = c[main_vars]
        series_temp = series_temp[series_temp.fyear >= year]
        series_temp = series_temp.astype({'fyear': 'int64'})
        for i in a:
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

    if save[0] == 1:
        plt.savefig(os.path.join(save[1], save[2]))
    plt.legend()
    plt.show()
    plt.close()
    del series_temp
    del series_temp_1
    return None
