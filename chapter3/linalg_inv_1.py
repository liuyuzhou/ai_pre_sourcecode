import numpy as np

x_np = np.array([[1, 2], [3, 4]])
y_inv = np.linalg.inv(x_np)
print('数组x_np：\n{}'.format(x_np))
print('数组y_np：\n{}'.format(y_inv))
print('数组x_np与y_np的点积:\n{}'.format(np.dot(x_np, y_inv)))

a_np = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
print('数组a_np：\n{}'.format(a_np))

a_inv = np.linalg.inv(a_np)
print('a_np的逆：\n{}'.format(a_inv))

b_np = np.array([[6], [-4], [27]])
print('矩阵b_np：\n{}'.format(b_np))

x_inv = np.linalg.solve(a_np, b_np)
print('计算：A^(-1)B：\n{}'.format(x_inv))