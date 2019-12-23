import numpy as np

num_np = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('初始数组：\n{}'.format(num_np))

print('调用 mean() 函数：{}'.format(np.mean(num_np)))
print('沿轴 0 调用 mean() 函数：{}'.format(np.mean(num_np, axis=0)))
print('沿轴 1 调用 mean() 函数：{}'.format(np.mean(num_np, axis=1)))
