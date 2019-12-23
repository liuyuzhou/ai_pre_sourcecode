import numpy as np

x_np = np.arange(9.).reshape(3, 3)
print('初始数组：\n{}'.format(x_np))

y_np = np.where(x_np > 3)
print('大于 3 的元素的索引：\n{}'.format(y_np))

print('使用索引获取满足条件的元素：{}'.format(x_np[y_np]))