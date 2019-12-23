import numpy as np

num_np = np.arange(8)
print('原始数组：\n{}'.format(num_np))

mod_np = num_np.reshape(4, 2)
print('修改后的数组：\n{}'.format(mod_np))
