import numpy as np

# 分隔符默认为空格
print(np.char.split('i like python'))
# 分隔符为 .
print(np.char.split('www.python.org', sep='.'))