import numpy as np

num_np = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('初始数组：\n{}'.format(num_np))

print('调用 ptp() 函数：{}'.format(np.ptp(num_np)))
print('沿轴 1 调用 ptp() 函数：{}'.format(np.ptp(num_np, axis=1)))
print('沿轴 0 调用 ptp() 函数：{}'.format(np.ptp(num_np, axis=0)))
