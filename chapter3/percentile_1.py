import numpy as np

num_np = np.array([[10, 7, 4], [3, 2, 1]])
print('初始数组：\n{}'.format(num_np))

# 50% 的分位数，就是 num_np 里排序之后的中位数
print('调用percentile()函数：{}'.format(np.percentile(num_np, 50)))

# axis 为 0，在纵列上求
print('沿轴0调用percentile()函数：{}'.format(np.percentile(num_np, 50, axis=0)))

# axis 为 1，在横行上求
print('沿轴1调用percentile()函数：{}'.format(np.percentile(num_np, 50, axis=1)))

# 保持维度不变
percentile_np = np.percentile(num_np, 50, axis=1, keepdims=True)
print('沿轴1调用percentile()函数，保持维度不变：\n{}'.format(percentile_np))
