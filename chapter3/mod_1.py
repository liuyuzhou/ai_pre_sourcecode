import numpy as np

first_np = np.array([10, 25, 50])
second_np = np.array([3, 5, 9])
print('第一个数组：{}'.format(first_np))
print('第二个数组：{}'.format(second_np))

print('调用mod()函数：{}'.format(np.mod(first_np, second_np)))
print('调用remainder()函数：{}'.format(np.remainder(first_np, second_np)))
