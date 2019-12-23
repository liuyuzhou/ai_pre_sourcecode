import numpy as np

np_ar = np.array([[1, 2], [3, 4], [5, 6]])
# 获取坐标轴为(0,0)，(1,1)和(2,0)的元素
point_ar = np_ar[[0, 1, 2], [0, 1, 0]]
print(point_ar)
