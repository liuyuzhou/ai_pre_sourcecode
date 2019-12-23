import numpy as np

ar_np = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('初始数组：\n{}'.format(ar_np))

print('第2列元素：{}'.format(ar_np[..., 1]))
print('第2行元素：{}'.format(ar_np[1, ...]))
print('第2列及剩下的所有元素：\n{}'.format(ar_np[..., 1:]))
