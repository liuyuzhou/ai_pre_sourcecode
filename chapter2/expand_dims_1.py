import numpy as np

x_np = np.array(([1, 2], [3, 4]))
print('数组x_np：\n{}'.format(x_np))

y_np = np.expand_dims(x_np, axis=0)
print('数组y_np：\n{}'.format(y_np))

print('数组x_np和y_np的形状：\n{},{}'.format(x_np.shape, y_np.shape))

# 在位置 1 插入轴
y_np = np.expand_dims(x_np, axis=1)
print('在位置1插入轴之后的数组y_np：\n{}'.format(y_np))
print('x_np.ndim和y_np.ndim：\n{},{}'.format(x_np.ndim, y_np.ndim))
print('x_np.shape 和 y_np.shape：\n{},{}'.format(x_np.shape, y_np.shape))