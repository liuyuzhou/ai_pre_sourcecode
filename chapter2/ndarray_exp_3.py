import numpy as np

minimum_dimension = [[1, 2, 3], [4, 5, 6]]
# 最小维度，指定为两维
md_np_two = np.array(minimum_dimension, ndmin=2)
print('最小维度两维结果：\n{}'.format(md_np_two))

# 最小维度，指定为三维
md_np_three = np.array(minimum_dimension, ndmin=3)
print('最小维度三维结果：\n{}'.format(md_np_three))
