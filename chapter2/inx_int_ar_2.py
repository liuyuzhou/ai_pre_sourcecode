import numpy as np

np_ar = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('初始数组：\n{}'.format(np_ar))

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
target_ar = np_ar[rows, cols]
print('初始数组np_ar的四个角元素是：\n{}'.format(target_ar))
