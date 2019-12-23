import numpy as np

# 定义一个结构化数据类型student_info
student_info = np.dtype([('name', 'U20'), ('number', 'i2'), ('score', 'f2')])
# 将dtype应用到adarray对象
detail_info = np.array([('小智', 1002, 82.5), ('小萌', 1001, 99.0)], dtype=student_info)
print(detail_info)
