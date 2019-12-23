import numpy as np

x_np = np.arange(9).reshape(1, 3, 3)
print('数组x_np：\n{}'.format(x_np))

y_np = np.squeeze(x_np)
print('数组y_np：\n{}'.format(y_np))

print('数组x_np和y_np的形状：\n{},{}'.format(x_np.shape, y_np.shape))
