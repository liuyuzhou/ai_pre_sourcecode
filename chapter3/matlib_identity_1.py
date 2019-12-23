import numpy.matlib
import numpy as np

# 大小为2，类型为整型
print('整型单位矩阵：\n{}'.format(np.matlib.identity(2, dtype=int)))

# 大小为3，类型为浮点型
print('浮点型单位矩阵：\n{}'.format(np.matlib.identity(3, dtype=float)))
