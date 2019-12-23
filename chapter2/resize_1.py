import numpy as np

first_np = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：\n{}'.format(first_np))
print('第一个数组的形状：{}'.format(first_np.shape))

second_np = np.resize(first_np, (3, 2))

print('第二个数组：\n{}'.format(second_np))
print('第二个数组的形状：{}'.format(second_np.shape))

second_np = np.resize(first_np, (3, 3))
print('第二个数组修改大小后：\n{}'.format(second_np))
