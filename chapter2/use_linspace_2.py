import numpy as np

# 设置元素全部是5的等差数列，默认为浮点数
ln_np = np.linspace(5, 5, 10)
print(ln_np)

# 设置dtype为int
ln_np = np.linspace(5, 5, 10, dtype=int)
print(ln_np)
