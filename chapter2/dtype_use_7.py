import numpy as np

# 定义一个结构化数据类型student_info
student_info = np.dtype([('name', 'U20'), ('number', 'i2'), ('score', 'f2')])
print(student_info)
