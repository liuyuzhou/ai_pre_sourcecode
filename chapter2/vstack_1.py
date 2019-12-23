import numpy as np

first_np = np.array([[1, 2], [3, 4]])
print('第一个数组：\n{}'.format(first_np))

second_np = np.array([[5, 6], [7, 8]])
print('第二个数组：\n{}'.format(second_np))

print('竖直堆叠：\n{}'.format(np.vstack((first_np, second_np))))
