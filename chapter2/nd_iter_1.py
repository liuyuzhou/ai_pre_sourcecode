import numpy as np

np_ar = np.arange(6).reshape(2, 3)
print('原始数组：\n{}'.format(np_ar))
print('迭代输出元素：')
for x in np.nditer(np_ar):
    print(x, end=", ")
