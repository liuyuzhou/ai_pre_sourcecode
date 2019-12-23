import numpy as np

num_np = np.arange(9)
print('原始数组：\n{}'.format(num_np))
print('将数组分为三个大小相等的子数组：\n{}'.format(np.split(num_np, 3)))
print('将数组在一维数组中表明的位置分割：\n{}'.format(np.split(num_np, [4, 7])))
