import numpy as np

num_np = np.arange(8).reshape(2, 4)
print('原数组：\n{}'.format(num_np))
print('调用ravel函数之后：\n{}'.format(num_np.ravel()))
print('以F风格顺序调用ravel函数之后：\n{}'.format(num_np.ravel(order='F')))