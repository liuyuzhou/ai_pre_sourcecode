import numpy as np

nd_sh = np.array([[1, 2, 3], [4, 5, 6]])
print('调整数组大小前，nd_sh：\n{}'.format(nd_sh))
# 调整数组大小
nd_sh.shape = (3, 2)
print('调整数组大小后，nd_sh：\n{}'.format(nd_sh))
