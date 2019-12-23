import numpy as np

np_ar = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('初始数组：\n{}'.format(np_ar))

# 获取初始数组中大于5的元素
bg_5 = np_ar[np_ar > 5]
print('初始数组中大于5的元素是：\n{}'.format(bg_5))
