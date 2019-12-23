import numpy as np

num_np = np.invert(np.array([13], dtype=np.uint8))
print('13的位反转，其中ndarray的dtype是uint8：{}'.format(num_np))

num_13_bin = np.binary_repr(13, width=8)
print('13的二进制表示：{}'.format(num_13_bin))

num_242_bin = np.binary_repr(242, width=8)
print('242的二进制表示：{}'.format(num_242_bin))
