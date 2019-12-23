import numpy as np

a_np = np.arange(8).reshape(2, 2, 2)
b_np = np.arange(4).reshape(2, 2)
print('多维矩阵乘积：\n{}'.format(np.matmul(a_np, b_np)))
