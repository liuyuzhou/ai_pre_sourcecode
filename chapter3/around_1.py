import numpy as np

num_np = np.array([0.5, 1.0, 2.55, 13.321, 67.567, 125.132, 357.72])
print('原始数组：{}'.format(num_np))
print('正常舍入：{}'.format(np.around(num_np)))
print('舍入一位小数：{}'.format(np.around(num_np, decimals=1)))
print('舍入两位小数：{}'.format(np.around(num_np, decimals=2)))
print('舍入到十位：{}'.format(np.around(num_np, decimals=-1)))
print('舍入到百位：{}'.format(np.around(num_np, decimals=-2)))
