import pandas as pd

data_dict = {'a': 0, 'b': 1, 'c': 2}
pd_s = pd.Series(data_dict, index=['b', 'c', 'd', 'a'])
print('由字典创建系列，并自定义索引：\n{}'.format(pd_s))
