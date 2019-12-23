import numpy as np

np_ar = np.arange(0, 60, 5)
np_ar = np_ar.reshape(3, 4)
print('原始数组：\n{}'.format(np_ar))

print('修改后的数组是：')
for x in np.nditer(np_ar, flags=['external_loop'], order='F'):
    print(x, end=", ")
