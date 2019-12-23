import numpy as np

first_np = np.arange(9, dtype=np.float_).reshape(3, 3)
print('第一个数组：\n{}'.format(first_np))

second_np = np.array([10, 10, 10])
print('第二个数组：\n{}'.format(second_np))

print('两个数组相加：\n{}'.format(np.add(first_np, second_np)))
print('两个数组相减：\n{}'.format(np.subtract(first_np, second_np)))
print('两个数组相乘：\n{}'.format(np.multiply(first_np, second_np)))
print('两个数组相除：\n{}'.format(np.divide(first_np, second_np)))
