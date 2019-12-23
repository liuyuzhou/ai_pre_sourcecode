import numpy as np

arr = np.arange(12)
print('初始数组：\n{}'.format(arr))
print('创建切片：')
a_np = arr[3:]
b_np = arr[3:]
a_np[1] = 123
b_np[2] = 234
print(arr)
print(id(a_np), id(b_np), id(arr[3:]))
