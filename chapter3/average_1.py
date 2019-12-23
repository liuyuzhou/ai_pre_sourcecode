import numpy as np

num_np = np.array([1, 2, 3, 4])
print('初始数组：{}'.format(num_np))
print('调用 average() 函数：{}'.format(np.average(num_np)))

# 不指定权重时相当于 mean 函数
wts = np.array([4, 3, 2, 1])
print('再次调用 average() 函数：{}'.format(np.average(num_np, weights=wts)))

# 如果 returned 参数设为 true，则返回权重的和
print('权重的和：{}'.format(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True)))
