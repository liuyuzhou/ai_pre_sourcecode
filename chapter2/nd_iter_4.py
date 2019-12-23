import numpy as np

np_ar = np.arange(0, 60, 5)
np_ar = np_ar.reshape(3, 4)
print('原始数组：\n{}'.format(np_ar))

print('以 C 风格顺序排序：')
for x in np.nditer(np_ar, order='C'):
    print(x, end=", ")
print('\n')

print('以 F 风格顺序排序：')
for x in np.nditer(np_ar, order='F'):
    print(x, end=", ")
