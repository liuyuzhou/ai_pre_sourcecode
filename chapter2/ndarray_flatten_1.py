import numpy as np

num_np = np.arange(8).reshape(2, 4)
print('原数组：\n{}'.format(num_np))
# 默认按行
print('展开的数组：\n{}'.format(num_np.flatten()))
print('以F风格顺序展开的数组：\n{}'.format(num_np.flatten(order='F')))
