import numpy as np

num_list = [[1, 2, 3], [4, 5, 6]]
"""
指定创建数组的样式，order的可选值有：'K', 'A', 'C', 'F'四个，C为行
方向，F为列方向，A为任意方向
"""
mat_np = np.array(num_list, order='A')
print(mat_np)
