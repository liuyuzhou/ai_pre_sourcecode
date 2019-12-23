import numpy as np

# 数组的 dtype 为 int64（八个字节）
int_size = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print('int_size的itemsize为：{}'.format(int_size.itemsize))

# 数组的 dtype 现在为 float16（两个字节）
float_size = np.array([1, 2, 3, 4, 5], dtype=np.float16)
print('float_size的itemsize为：{}'.format(float_size.itemsize))
