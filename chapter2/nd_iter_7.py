import numpy as np

first_ar = np.arange(0, 60, 5)
first_ar = first_ar.reshape(3, 4)
print('第一个数组：\n{}'.format(first_ar))

second_ar = np.array([1, 2, 3, 4], dtype=int)
print('第二个数组：\n{}'.format(second_ar))

print('修改后的数组：')
for x, y in np.nditer([first_ar, second_ar]):
    print("%d:%d" % (x, y), end=", ")
