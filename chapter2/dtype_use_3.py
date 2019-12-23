import numpy as np

# 字节顺序标注
dt = np.dtype('>i1')
print(dt)

dt = np.dtype('<i4')
print(dt)

dt = np.dtype('<i8')
print(dt)
