import numpy as np

num_np = np.array([10, 100, 1000])
print('初始数组：{}'.format(num_np))
print('调用power函数：{}'.format(np.power(num_np, 2)))

second_np = np.array([1, 2, 3])
print('第二个数组：{}'.format(second_np))
print('调用power函数：{}'.format(np.power(num_np, second_np)))
