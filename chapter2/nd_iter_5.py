import numpy as np

np_ar = np.arange(0, 60, 5)
np_ar = np_ar.reshape(3, 4)
print('原始数组：\n{}'.format(np_ar))

for x in np.nditer(np_ar, op_flags=['readwrite']):
    # 数组所有元素值翻倍
    x[...] = 2 * x

print('修改后的数组：\n{}'.format(np_ar))
