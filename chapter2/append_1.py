import numpy as np

num_np = np.array([[1, 2, 3], [4, 5, 6]])
print('初始数组：\n{}'.format(num_np))
print('向数组添加元素：\n{}'.format(np.append(num_np, [7, 8, 9])))
print('沿轴0添加元素：\n{}'.format(np.append(num_np, [[7, 8, 9]], axis=0)))
print('沿轴1添加元素：\n{}'.format(np.append(num_np, [[5, 5, 5], [7, 8, 9]], axis=1)))
