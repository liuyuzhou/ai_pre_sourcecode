import numpy as np

a_np = np.array([[1, 2], [3, 4]])
print('a_np的行列式：{}'.format(np.linalg.det(a_np)))

b_np = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print('b_np初始数组：\n{}'.format(b_np))
print('b_np的行列式：{}'.format(np.linalg.det(b_np)))
str_b_np = '6 * (-2 * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - -2 * 2)'
cu_b_np = 6 * (-2 * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - -2 * 2)
print('b_np的行列式计算公式：\n{}={}'.format(str_b_np, cu_b_np))
