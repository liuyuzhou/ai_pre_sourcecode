import pandas as pd

str_list = [' meng', 'Zhi ', 'MI', ' Li Xiao']
pd_sr = pd.Series(str_list)
print('before split:\n{}'.format(pd_sr))
print("after split:\n{}".format(pd_sr.str.split()))
