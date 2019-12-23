import numpy as np

num_np = np.arange(12).reshape(3, 4)
print('原数组：\n{}'.format(num_np))
print('对换数组：\n{}'.format(np.transpose(num_np)))
