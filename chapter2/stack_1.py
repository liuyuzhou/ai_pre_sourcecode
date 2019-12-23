import numpy as np

first_np = np.array([[1, 2], [3, 4]])
print('第一个数组：\n{}'.format(first_np))

second_np = np.array([[5, 6], [7, 8]])
print('第二个数组：\n{}'.format(second_np))

print('沿轴 0 堆叠两个数组：\n{}'.format(np.stack((first_np, second_np), 0)))
print('沿轴 1 堆叠两个数组：\n{}'.format(np.stack((first_np, second_np), 1)))
