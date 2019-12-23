import numpy as np

# 创建三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('\n')
# 将轴 2 滚动到轴 0（宽度到深度）

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2))
# 将轴 0 滚动到轴 1：（宽度到高度）
print('\n')

print('调用 rollaxis 函数：')
print(np.rollaxis(a, 2, 1))