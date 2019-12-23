import numpy as np

a_np = np.array([[1, 2], [3, 4]])
b_np = np.array([[11, 12], [13, 14]])

# vdot 将数组展开计算内积
print('a_np和b_np的向量点积：{}'.format(np.vdot(a_np, b_np)))
