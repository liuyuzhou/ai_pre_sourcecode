import pandas as pd

str_list = [' meng', 'Zhi ', 'MI', ' Li Xiao']
pd_sr = pd.Series(str_list)
print(pd_sr.str.count('i'))
