import numpy as np

num_np = np.array([[3, 7], [9, 1]])
print('初始数组：\n{}'.format(num_np))
print('调用 sort() 函数：\n{}'.format(np.sort(num_np)))
print('按列排序：\n{}'.format(np.sort(num_np, axis=0)))
print('按行排序：\n{}'.format(np.sort(num_np, axis=1)))

# 在 sort 函数中自定义排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
num_np = np.array([("meng", 21), ("zhi", 25), ("li", 17), ("zhang", 27)], dtype=dt)
print('初始数组：\n{}'.format(num_np))
print('按 name 排序：\n{}'.format(np.sort(num_np, order='name')))
