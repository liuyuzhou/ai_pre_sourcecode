import numpy as np

# 默认数据类型
ft_np = np.logspace(0, 9, 10, base=2)
print(ft_np)

# 设置数据类型为int
int_np = np.logspace(0, 9, 10, base=2, dtype=int)
print(int_np)
