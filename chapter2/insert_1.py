import numpy as np

num_np = np.array([[1, 2], [3, 4], [5, 6]])
print('初始数组：\n{}'.format(num_np))
print('未传递Axis参数。 在插入之前输入数组会被展开:')
print(np.insert(num_np, 3, [11, 12]))

print('传递了 Axis 参数。 会广播数组来配输入数组。')
print('沿轴0广播：\n{}'.format(np.insert(num_np, 1, [11],axis=0)))
print('沿轴 1 广播：\n{}'.format(np.insert(num_np, 1, [11], axis=1)))
