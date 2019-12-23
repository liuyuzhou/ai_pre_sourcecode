import numpy as np

num_np = np.arange(16).reshape(4, 4)

print('原始数组：\n{}'.format(num_np))
print('竖直分割后：\n{}'.format(np.vsplit(num_np, 2)))
