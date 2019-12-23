import numpy as np

num_np = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print('初始数组：\n{}'.format(num_np))

print('调用 argmax() 函数：{}'.format(np.argmax(num_np)))
print('展开数组：{}'.format(num_np.flatten()))

max_index = np.argmax(num_np, axis=0)
print('沿轴 0 的最大值索引：{}'.format(max_index))

max_index = np.argmax(num_np, axis=1)
print('沿轴 1 的最大值索引：{}'.format(max_index))

min_index = np.argmin(num_np)
print('调用 argmin() 函数：{}'.format(min_index))

print('展开数组中的最小值：{}'.format(num_np.flatten()[min_index]))

min_index = np.argmin(num_np, axis=0)
print('沿轴 0 的最小值索引：{}'.format(min_index))

min_index = np.argmin(num_np, axis=1)
print('沿轴 1 的最小值索引：{}'.format(min_index))
