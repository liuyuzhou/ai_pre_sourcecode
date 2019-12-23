import pandas as pd

str_list = ['123', 'Zhi ', 'MI', ' Li Xiao']
pd_sr = pd.Series(str_list)
print(pd_sr.str.isnumeric())
