import numpy as np

a_np = np.array([[1, 2], [3, 4]])
print('数组a_np：\n{}'.format(a_np))

b_np = np.array([[11, 12], [13, 14]])
print('数组b_np：\n{}'.format(b_np))

print('数组a_np和数组b_np的内积：\n{}'.format(np.inner(a_np, b_np)))
