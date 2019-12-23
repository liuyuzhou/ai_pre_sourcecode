import numpy as np

num_np = np.arange(9.).reshape(3, 3)
print('初始数组：\n{}'.format(num_np))

# 定义条件, 选择偶数元素
condition = np.mod(num_np, 2) == 0
print('按元素的条件值：\n{}'.format(condition))

print('使用条件提取元素：{}'.format(np.extract(condition, num_np)))
