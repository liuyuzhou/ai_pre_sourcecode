import numpy as np

nd_one = np.arange(12)
# nd_one现只有一个维度
# print(nd_one)
print('nd_one的维度为：{}维'.format(nd_one.ndim))
# 现在调整其大小
nd_three = nd_one.reshape(2, 3, 2)
# nd_three现在拥有三个维度
# print(nd_three)
print('nd_three的维度为：{}维'.format(nd_three.ndim))
