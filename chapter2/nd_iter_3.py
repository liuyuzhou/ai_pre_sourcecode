import numpy as np

np_ar = np.arange(0, 60, 5)
np_ar = np_ar.reshape(3, 4)
print('原始数组：\n{}'.format(np_ar))

t_ar = np_ar.T
print('原始数组的转置：\n{}'.format(t_ar))

c_order_np = t_ar.copy(order='C')
print('以 C 风格顺序排序：\n{}'.format(c_order_np))
for x in np.nditer(c_order_np):
    print(x, end=", ")
print('\n')

f_order_np = t_ar.copy(order='F')
print('以 F 风格顺序排序：\n{}'.format(f_order_np))
for x in np.nditer(f_order_np):
    print(x, end=", ")