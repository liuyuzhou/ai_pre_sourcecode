import numpy as np

# 类型字段名可以用于存取实际的number列
dt_num = np.dtype([('number', np.int16)])
nd_num = np.array([(1001, ), (1002, ), (1003, )], dtype=dt_num)
print('number:\n{}'.format(nd_num['number']))

# 类型字段名用于存取实际的score列
dt_score = np.dtype([('score', np.float16)])
nd_score = np.array([(95.0, ), (90.0, ), (86.5, )], dtype=dt_score)
print('score:\n{}'.format(nd_score['score']))
