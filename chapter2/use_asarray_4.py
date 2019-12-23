import numpy as np

num_list = [1, 2, 3]
# 设置dtype参数为int
nd_int = np.asarray(num_list, dtype=int)
print('设置dtype参数为int：\n{}'.format(nd_int))

# 设置dtype参数为float
nd_ft = np.asarray(num_list, dtype=float)
print('设置dtype参数为float：\n{}'.format(nd_ft))
