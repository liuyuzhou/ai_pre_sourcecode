import numpy as np

# 使用range函数创建列表对象
num_list = range(5)
iter_obj = iter(num_list)

# 使用迭代器创建ndarray,dtype可由自己指定
nd_int = np.fromiter(iter_obj, dtype=int)
print(nd_int)
