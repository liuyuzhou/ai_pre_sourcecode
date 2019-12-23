import numpy as np

num_np = np.arange(12).reshape(3, 4)
print('初始数组：\n{}'.format(num_np))

print('未传递 Axis 参数。在删除之前输入数组会被展开：')
print(np.delete(num_np, 5))

print('删除第二列：\n{}'.format(np.delete(num_np, 1, axis=1)))

print('包含从数组中删除的替代值的切片：')
num_np = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(num_np, np.s_[::2]))
