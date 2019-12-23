import numpy as np

# 首先创建结构化数据类型
dt_num = np.dtype([('number', np.int16)])
print(dt_num)

dt_score = np.dtype([('score', np.float16)])
print(dt_score)
