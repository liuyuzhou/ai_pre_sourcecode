import numpy as np

# 创建三维的 ndarray
num_np = np.arange(8).reshape(2, 2, 2)
print('原数组：\n{}'.format(num_np))
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
print('调用swapaxes函数后的数组：\n{}'.format(np.swapaxes(num_np, 2, 0)))
