import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)

# c 使用了关键字参数 sin_array
np.savez("numpy.npz", a, b, sin_array=c)
r = np.load("numpy.npz")
print(r.files)
# 数组 a
print(r["arr_0"])
# 数组 b
print(r["arr_1"])
# 数组 c
print(r["sin_array"])
