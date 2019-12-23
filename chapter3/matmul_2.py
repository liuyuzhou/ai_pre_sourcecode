import numpy as np

a_np = [[1, 0], [0, 1]]
b_np = [1, 2]
print('二维和一维矩阵乘积：{}'.format(np.matmul(a_np, b_np)))
print('一维和二维矩阵乘积：{}'.format(np.matmul(b_np, a_np)))
