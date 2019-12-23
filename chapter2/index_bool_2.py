import numpy as np

np_ar = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print('初始数组：{}'.format(np_ar))

filter_nr = np_ar[~np.isnan(np_ar)]
print('过滤nan后的数组：{}'.format(filter_nr))
