# plot supy variables
from night import night
import matplotlib.pyplot as plt
import pandas as pd
from dict_legend import dict_var_title, dict_var_ylabel
from dict_legend import dict_var_disp_TS as dict_var_disp
from datetime import date, datetime
import datetime

def supy_plot_old(var, df_merge, s,e, size=False, clr=False):
    var_w =  var + '_fWS_sWS'
    var_wd = var +'_fWS_sWS_d'
    var_wu = var + '_fWS_sKC'
    var_wud= var + '_fWS_sKC_d'

    if size:   
        size=size
    else:
        size = 10, 6

    if clr:
        clr=clr
    else:
        clr = ('#ff7f0e','#2ca02c')

    fig, axes = plt.subplots(2, 1, sharex=True)
    a = df_merge.loc[s:e,[var, var_w, var_wu]].rename(columns=dict_var_disp)\
        .plot(ax=axes[0],figsize=(size),title=dict_var_title[var])
    plt.hlines(0,'2011 01 01','2012 12 30',linestyles='--',colors='grey')

    b = df_merge.loc[s:e,[var_wd, var_wud]].rename(columns=dict_var_disp)\
        .plot(ax=axes[1],figsize=(size),title=('Difference ' + dict_var_title[var]),color=clr)
    plt.hlines(0,'2011 01 01','2012 12 30',linestyles='--',colors='grey')

    for i in [a,b]:
        night(i,df_merge,s,e)
        i.legend()
        i.set_ylabel(dict_var_ylabel[var])
        i.set_xlabel('')
    fig.tight_layout()

def supy_plot(var, df_in, s,e, size=False, clr=False):

    if size:   
        size=size
    else:
        size = 10, 6

    if clr:
        clr=clr
    else:
        clr = ('#ff7f0e','#2ca02c')
    
    fig, axes = plt.subplots(2, 1, sharex=True)
    a = df_in.loc[s:e,[var]]\
        .plot(ax=axes[0],figsize=(size),title=dict_var_title[var])

    f_date = (date(int(s[0:4]),int(s[5:7]),int(s[7:10])))
    l_date = (date(int(e[0:4]),int(e[5:7]),int(e[7:10])))
    f_date - datetime.timedelta(days=2)    
    l_date + datetime.timedelta(days=2)
    
    plt.hlines(0,f_date - datetime.timedelta(days=2),l_date + datetime.timedelta(days=2),\
        linestyles='--',colors='grey');
    a.legend(['fKC_sKC','fWS_sKC','fWS_sWS',])

    b = df_diff_m=pd.concat([df_in.loc[s:e,(var,'fWS_sWS')]-df_in.loc[s:e,(var,'fKC_sKC')],\
        (df_in.loc[s:e,(var,'fWS_sKC')]-df_in.loc[s:e,(var,'fKC_sKC')])],\
        axis=1,join='inner',keys=['fWS_sWS','fWS_sKC']).sort_index(axis=1).\
        plot(ax=axes[1], figsize=(size), title = ('Difference ' + dict_var_title[var]), color=clr)

    plt.hlines(0,f_date - datetime.timedelta(days=2),l_date + datetime.timedelta(days=2),\
        linestyles='--',colors='grey');


    for i in [a,b]:
        night(i,df_in,s,e)
        i.set_ylabel(dict_var_ylabel[var])
        i.set_xlabel('')
        if var == 'Lob':
            i.set_yscale('symlog')

    fig.tight_layout()

def zeroline(s,e, value=False):
    f_date = (date(int(s[0:4]),int(s[5:7]),int(s[7:10])))
    l_date = (date(int(e[0:4]),int(e[5:7]),int(e[7:10])))
    f_date - datetime.timedelta(days=2)    
    l_date + datetime.timedelta(days=2)

    if value:
        value = value
    else:
        value = 0
        
    plt.hlines(value,f_date - datetime.timedelta(days=2),l_date + datetime.timedelta(days=2),\
    linestyles='--',colors='grey');