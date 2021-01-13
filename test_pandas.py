# %%
import pandas as pd
import numpy as np
# %%
countries = ['USA','Nigeria','France','Ghana']
my_data = [100, 200, 300, 400]
# %%
my_series = pd.Series(my_data,countries)
my_series
# %%
np_arr = np.array(my_data)
pd.Series(np_arr)
# %%
my_dict = {'USA':50,'Nigeria':60,'France':70,'Ghana':80}
my_dict
# %%
pd.Series(my_dict)
# %%
my_dict['USA']
# %%
my_series['USA']
# %%  DATAFRAME

df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df

# %%
data = {'name': ['George','Ann', 'Tino', 'Charles','Phil'],
        'age' : [40, 24, 31, 21, 23],
        'year': [2012, 2012, 2013, 2014, 2014]
    }
my_df = pd.DataFrame(data, index = ['Lagos', 'Dubai', 'Mumbai', 'Accra', 'Yuma'])
my_df
# %%
type(my_df[['name', 'year']])
# %%
my_df
# %%
df = {  'Name' : pd.Series(['Jon', 'Aaron', 'Todd'], index = ['a','b','c']),
        'Age' : pd.Series(['39','34', '32', '33'],   index = ['a','b','c','d']),
        'Nationality':pd.Series(['US', 'China','US'], ['a','b','c'])
        }
pd.DataFrame(df)
# %%
df['Year'] = pd.Series(['2016','2017','2018','2015'], ['a','b','c','d'])
pd.DataFrame(df)
# %%
df = pd.DataFrame(df)
# %%
df.loc['a']
# %%
df.iloc[0]
# %%
df.iloc[[0,2]]
# %%
df.loc['c',['Name','Year']]
# %%
df.loc[['c','b'],['Name','Year']]
# %%
for i in ['Jon', 'Aaron', 'Todd']:
    df[df['Name']==i]
# %%
df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df[df['W']>0]['X']
# %%
df
df2 = df
df2.reset_index(inplace=True)
df2.loc[1]
# %%
df2.loc[2:4]['Y']
# %% Lägg till ny column som heter ID
df['ID'] = ['df1', 'df2','df3','df4','df5']
df = df.set_index('ID')
# %%¨
grej = ['df1','df2','df3']
print([grej])
df.loc[grej]
# %% MULTIINDEX

outside = ['O Level','O Level','O Level','A Level','A Level','A Level', ]
inside  = [21, 22, 23, 24, 24, 25]

my_index = list(zip(outside, inside))
my_index
#%%
my_index = pd.MultiIndex.from_tuples(my_index)
my_index
# %%
df = pd.DataFrame(np.random.randn(6,2),index = my_index, columns=['A','B'])
df
# %%
df.loc['O Level'].loc[22]
# %%
df.index.names = ['Levels', 'Num']
df
# %%
df.xs(24, level = 'Num')
# %%
