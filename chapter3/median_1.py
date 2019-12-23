import numpy as np

num_np = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
print('初始数组：\n{}'.format(num_np))

print('调用 median() 函数：{}'.format(np.median(num_np)))
print('沿轴 0 调用 median() 函数：{}'.format(np.median(num_np, axis=0)))
print('沿轴 1 调用 median() 函数：{}'.format(np.median(num_np, axis=1)))
