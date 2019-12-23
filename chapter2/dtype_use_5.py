import numpy as np

# 将数据类型应用于 ndarray 对象
dt_num = np.dtype([('number', np.int16)])
nd_num = np.array([(1001, ), (1002, ), (1003, )], dtype=dt_num)
print(nd_num)

dt_score = np.dtype([('score', np.float16)])
nd_score = np.array([(95.0, ), (90.0, ), (86.5, )], dtype=dt_score)
print(nd_score)
