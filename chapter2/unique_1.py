import numpy as np

num_np = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print('初始数组：\n{}'.format(num_np))

unique_np = np.unique(num_np)
print('数组去重：\n{}'.format(unique_np))

print('去重数组的索引数组：')
unique_np, indices = np.unique(num_np, return_index=True)
print(indices)

print('每个和原数组下标对应的数值：')
print(num_np)

print('去重数组的下标：')
unique_np, indices = np.unique(num_np, return_inverse=True)
print(unique_np)
print('下标为：\n{}'.format(indices))

print('使用下标重构原数组：')
print(unique_np[indices])

print('返回去重元素的重复数量：')
unique_np, indices = np.unique(num_np, return_counts=True)
print(unique_np)
print(indices)
