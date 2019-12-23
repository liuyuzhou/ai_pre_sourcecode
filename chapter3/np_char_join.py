import numpy as np

# 操作字符串
print(np.char.join(':', 'numpy'))

# 指定多个分隔符操作数组元素
print(np.char.join([':', '-'], ['numpy', 'pandas']))
