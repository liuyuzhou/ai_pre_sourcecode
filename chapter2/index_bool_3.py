import numpy as np

np_ar = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print('初始数组：{}'.format(np_ar))

filter_nr = np_ar[np.iscomplex(np_ar)]
print('过滤非复数后的数组：{}'.format(filter_nr))