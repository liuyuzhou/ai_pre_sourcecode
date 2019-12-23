import numpy as np

num_np = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('初始数组：\n{}'.format(num_np))

print('调用amin()函数：{}'.format(np.amin(num_np, 1)))
print('再次调用amin()函数：{}'.format(np.amin(num_np, 0)))

print('调用amax()函数：{}'.format(np.amax(num_np)))
print('再次调用amax()函数：{}'.format(np.amax(num_np, axis=0)))
