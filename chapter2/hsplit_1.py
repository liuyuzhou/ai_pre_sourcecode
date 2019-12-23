import numpy as np

num_np = np.floor(10 * np.random.random((2, 6)))
print('原始数组：\n{}'.format(num_np))
print('水平分割后：\n{}'.format(np.hsplit(num_np, 3)))
