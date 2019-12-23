import numpy as np

first_np = np.array([[1, 2], [3, 4]])
print('第一个数组：\n{}'.format(first_np))

second_np = np.array([[5, 6], [7, 8]])
print('第二个数组：\n{}'.format(second_np))

# 两个数组的维度相同
print('沿轴0连接两个数组：\n{}'.format(np.concatenate((first_np, second_np))))
print('沿轴 1 连接两个数组：\n{}'.format(np.concatenate((first_np, second_np), axis=1)))
