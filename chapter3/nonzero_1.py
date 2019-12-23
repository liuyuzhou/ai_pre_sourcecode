import numpy as np

num_np = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
print('初始数组：\n{}'.format(num_np))
print('调用 nonzero() 函数：\n{}'.format(np.nonzero(num_np)))
