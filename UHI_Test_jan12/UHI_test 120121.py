# %%
import matplotlib.pyplot as plt
import supy as sp
import pandas as pd
import numpy as np
from pathlib import Path
from night import night 
from dict_legend import *
from supy_plot import supy_plot
sp.show_version()

# Sample Data
path_runcontrol_s = Path('SuPy/src/supy/sample_run')/ 'RunControl.nml'
df_state_init_s = sp.init_supy(path_runcontrol_s)
grid_s = df_state_init_s.index[0]
df_forcing_s = sp.load_forcing_grid(path_runcontrol_s, grid_s)

# Wisley Data
path_runcontrol_w = Path('SuPy/src/supy/sample_run')/ 'RunControl_wisley.nml'
df_state_init_w = sp.init_supy(path_runcontrol_w)
grid_w = df_state_init_w.index[0]
df_forcing_w = sp.load_forcing_grid(path_runcontrol_w, grid_w)

# Wisley Data
path_runcontrol_wu = Path('SuPy/src/supy/sample_run')/ 'RunControl_wisley_urban.nml'
df_state_init_wu = sp.init_supy(path_runcontrol_wu)
grid_wu = df_state_init_wu.index[0]
df_forcing_wu = sp.load_forcing_grid(path_runcontrol_wu, grid_wu)

sp.check_forcing(df_forcing_s)
sp.check_forcing(df_forcing_w)
sp.check_forcing(df_forcing_w)

# %% Sample Data Metological Conditions

df_plot_forcing_x = df_forcing_s.loc[:, list_var_forcing].copy().shift(
    -1).dropna(how='any')
df_plot_forcing = df_plot_forcing_x.resample('1h').mean()
df_plot_forcing['rain'] = df_plot_forcing_x['rain'].resample('1h').sum()

axes = df_plot_forcing.plot(
    subplots=True,
    figsize=(10, 12),
    legend=False,
)
fig = axes[0].figure
fig.tight_layout()
fig.autofmt_xdate(bottom=0.2, rotation=0, ha='center')
for ax, var in zip(axes, list_var_forcing):
    ax.set_ylabel(dict_var_label[var])

# %% Wisley Metological Conditions

df_plot_forcing_x = df_forcing_w.loc[:, list_var_forcing].copy().shift(
    -1).dropna(how='any')
df_plot_forcing = df_plot_forcing_x.resample('1h').mean()
df_plot_forcing['rain'] = df_plot_forcing_x['rain'].resample('1h').sum()

axes = df_plot_forcing.plot(
    subplots=True,
    figsize=(10, 12),
    legend=False,
)
fig = axes[0].figure
fig.tight_layout()
fig.autofmt_xdate(bottom=0.2, rotation=0, ha='center')
for ax, var in zip(axes, list_var_forcing):
    ax.set_ylabel(dict_var_label[var])

# %% Investigate Metreological conditions for London and Wisley
#df_forcing_si = df_forcing_s.add_suffix()
df_forcing_wi = df_forcing_w.add_suffix('_w')

df_forcing_m = pd.concat([df_forcing_s,df_forcing_wi], axis=1, join='inner')
df_forcing_m = df_forcing_m.rename(columns={'kdown': 'Kdown'})

# %% June Tair Sample Data
s = '2012 07 20'
e = '2012 07 29'
ax = sp.util.plot_day_clm(df_forcing_m.loc[s:e,['Tair', 'Tair_w']])

# %% June Tair Wisley Data 
s = '2012 07 20'
e = '2012 07 27'
ax_output = df_forcing_m.loc[s:e,['Tair','Tair_w']].plot(figsize=(9,7))
night(ax_output,df_forcing_m,s,e,s_alpha=0.1)

# %%  RH Selected days comparison

s = '2012 07 20'
e = '2012 07 27'
ax_output = df_forcing_m.loc[s:e,['RH','RH_w']].plot(figsize=(9,7))
night(ax_output,df_forcing_m,s,e,s_alpha=0.1)

# %%  U Selected days comparison

s = '2012 07 20'
e = '2012 07 27'
ax_output = df_forcing_m.loc[s:e,['U','U_w']].plot(figsize=(12,10))
night(ax_output,df_forcing_m,s,e,s_alpha=0.1)


# %% Set reasonable settings Wisley and WisleyUrban

#### Three scenario Used
# 1. Initial conditions used in sample data - Used Suffix: s


# 2. Building fraction = 0. grass = .41 - Population day/night = 0 - Used Suffix: _w         (Wisley Conditions)
# 3. London initial conditions with whisley met data - Used Suffix WU (Wisley Urban conditions with Building)

#pd.set_option("display.max_columns", 4600)

df_state_init_w.loc[:,'z'  ] = 49.1
# df_state_init_w.loc[:,'alt'] = 38
# df_state_init_w.loc[:,'lat'] = 51.3108
# df_state_init_w.loc[:,'lng'] = -0.47634
# df_state_init_w.loc[:,'z0m_in'] = 4
# df_state_init_w.loc[:,'zdm_in'] = 0.4  
# df_state_init_w.loc[:,'bldgh'] = 0.0000001
# df_state_init_w.loc[:,'dectreeh'] = 4
# df_state_init_w.loc[:,'evetreeh'] = 4

# %%


# df_state_init_wu = df_state_init_w.copy()

# df_state_init_w.loc[:, ('sfr', '(0,)')] = 0.10 # Paved
# df_state_init_w.loc[:, ('sfr', '(1,)')] = 0.10 # Building
# df_state_init_w.loc[:, ('sfr', '(2,)')] = 0.30 # Evergreen Trees
# df_state_init_w.loc[:, ('sfr', '(3,)')] = 0.30 # Decidous trees
# df_state_init_w.loc[:, ('sfr', '(4,)')] = 0.20 # Grass
# df_state_init_w.loc[:, ('sfr', '(5,)')] = 0.10 # Bare soil
# df_state_init_w.loc[:, ('sfr', '(6,)')] = 0 # Water

# df_state_init_w.loc.popdensdaytime = 10
# df_state_init_w.loc.popdensnighttime = 5
#     
sp.check_state(df_state_init_s)
sp.check_state(df_state_init_w)
sp.check_state(df_state_init_wu)

# %% Run Suews
# Run SuPy Sample data conditions
df_output_s, df_state_final_s = sp.run_supy(df_forcing_s, df_state_init_s)
df_output_suews_s = df_output_s['SUEWS']

# Run SuPy with Whisley add _w for recognition later on
df_output_w, df_state_final_w = sp.run_supy(df_forcing_w, df_state_init_w)
df_output_suews_w = df_output_w['SUEWS']
df_output_suews_w = df_output_suews_w.add_suffix('_w')
# 
# Run SuPy with Whisley met data and Sample data initial conditions add _wu for recognition later on
df_output_wu, df_state_final_wu = sp.run_supy(df_forcing_wu, df_state_init_wu)
df_output_suews_wu = df_output_wu['SUEWS']
df_output_suews_wu = df_output_suews_wu.add_suffix('_wu')
#%%
# Merge to one dataframe for easier plotting
df_output_suews_g_s  = df_output_suews_s.loc[grid_s]
df_output_suews_g_w  = df_output_suews_w.loc[grid_w]
df_output_suews_g_wu = df_output_suews_wu.loc[grid_wu]

df_merge = pd.concat([df_output_suews_g_s, df_output_suews_g_w,df_output_suews_g_wu],axis=1,join='inner')

# Add possibilites for investigating differences
init_col = list(df_output_suews_s)
w_col = list(df_output_suews_w)
wu_col = list(df_output_suews_wu)

# Visa på skillnader

for i, wd, w, wud, wu in zip(init_col,[sub + '_d' for sub in w_col],w_col,[sub + '_d' for sub in wu_col],wu_col):
    df_merge[wd] = df_merge[w] - df_merge[i]
    df_merge[wud] = df_merge[wu] - df_merge[i]


# %%

# %%
fsize=(8,10)
fig, axes = plt.subplots(6, 1, sharex=True)
clr= ('#ff7f0e','#2ca02c')
s='2012 07 10'
a = df_forcing_m.loc[s : e ,['Kdown']].plot(ax=axes[0],figsize=fsize,title= 'Incoming Solar\n Radiation ($ \mathrm{W \ m^{-2}}$)',color=clr)
b = df_forcing_m.loc[s : e ,['Tair','Tair_w']].plot(ax=axes[1],figsize=fsize,title='Air Temperature ($^{\circ}}$C)',color=clr)
c = df_forcing_m.loc[s : e ,['RH','RH_w']].plot(ax=axes[2],figsize=fsize,title='Relative Humidity (%)',color=clr)
d = df_forcing_m.loc[s : e ,['pres','pres_w']].plot(ax=axes[3],figsize=fsize,title='Air Pressure (hPa)',color=clr)
e1= df_forcing_m.loc[s : e ,['U','U_w']].plot(ax=axes[4],figsize=fsize,title='Wind Speed (m $\mathrm{s^{-1}}$)',color=clr)
f = df_forcing_m.loc[s : e ,['rain']].plot(ax=axes[5],figsize=fsize,title='Rainfall (mm)',color=clr)
for var in [a,b,c,d,e1,f]:
    night(var,df_forcing_m,s,e)
    var.get_legend().remove()
fig.tight_layout()

# %%
# Start and end date for comparison
s = '2012 07 22'
e = '2012 07 29'

# %% Net All Wave Radiation
var = 'QN'
supy_plot(var, df_merge,s,e)

# %% Storage Heat Flux
var = 'QS'
supy_plot(var, df_merge,s,e)

# %% Sensible Heat Flux
var = 'QH'
supy_plot(var, df_merge,s,e)

# %% Latent Heat Flux
var = 'QE'
supy_plot(var, df_merge,s,e)

# %%% Anthropogenic Heat flux
supy_plot('QF', df_merge,s,e)

# %% Air temp 2m
supy_plot('T2', df_merge,s,e)
# %% Wind Speed 10m
supy_plot('U10', df_merge,s,e)

# %% Soil Moisture Deficit
supy_plot('SMD', df_merge,s,e)

# %%
supy_plot('UStar', df_merge,s,e)

# %% 
def supy_plot(var, df_merge, s,e, size, clr):
    var_w =  var + '_w'
    var_wd = var +'_w_d'
    var_wu = var + '_wu'
    var_wud= var + '_wu_d'

    fig, axes = plt.subplots(2, 1, sharex=True)
    a = df_merge.loc[s:e,[var, var_w, var_wu]].rename(columns=dict_var_disp)\
        .plot(ax=axes[0],figsize=(size),title=dict_var_title[var])
    b = df_merge.loc[s:e,[var_wd, var_wud]].rename(columns=dict_var_disp)\
        .plot(ax=axes[1],figsize=(size),title=('Difference ' + dict_var_title[var]),color=clr)
    plt.hlines(0,s,'2012 08',linestyles='--',colors='grey')

    for i in [a,b]:
        night(i,df_merge,s,e)
        i.legend()
        i.set_ylabel(dict_var_ylabel[var])
        i.set_xlabel('')
    fig.tight_layout()

#%% RSL Kolla over thetta
# df_output_rsl_s = df_output_s['RSL']
# df_output_rsl_s_g = df_output_rsl_s.loc[grid]
# df_output_rsl_s = df_output_rsl_w.add_suffix('_w')

# df_output_rsl_w = df_output_w['RSL']
# df_output_rsl_w = df_output_rsl_w.add_suffix('_w')
# df_output_rsl_w_g = df_output_rsl_w.loc[grid]
# df_output_rsl_rb = df_rb_out
# put['RSL']

# df_output_rsl_rb = df_output_rsl_rb.add_suffix('_rb')
# df_output_rsl_rb_g = df_output_rsl_rb.loc[grid]
# Kolla over detta
# df_rsl = pd.concat([df_output_rsl_g,df_output_rsl_r_g,df_output_rsl_rb_g],axis=1,join='inner')
# %%
# Choose variable to plot as var
var = 'QN'
var_w =  var + '_w'
var_wd = var +'_w_d'
var_wu = var + '_wu'
var_wud= var + '_wu_d'

fig, axes = plt.subplots(2, 1, sharex=True)
a = df_merge.loc[s:e,[var, var_w, var_wu]].rename(columns=dict_var_disp)\
    .plot(ax=axes[0],figsize=(size),title=dict_var_title[var])
b = df_merge.loc[s:e,[var_wd, var_wd]].rename(columns=dict_var_disp)\
    .plot(ax=axes[1],figsize=(size),title=('Difference ' + dict_var_title[var]),color=clr)
plt.hlines(0,s,'2012 08',linestyles='--',colors='grey')

for i in [a,b]:
    night(i,df_merge,s,e)
    i.legend()
    i.set_ylabel(dict_var_ylabel[var])
    i.set_xlabel('')
fig.tight_layout()

