import numpy as np

num_np = np.arange(6).reshape(3, 2)
print('初始数组：\n{}'.format(num_np))

wt = np.array([3, 5])
print('修改后的数组：{}'.format(np.average(num_np, axis=1, weights=wt)))
print('修改后的数组：{}'.format(np.average(num_np, axis=1, weights=wt, returned=True)))
