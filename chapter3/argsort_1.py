import numpy as np

x_np = np.array([3, 1, 2])
print('初始数组：{}'.format(x_np))

y_np = np.argsort(x_np)
print('对x_np调用 argsort() 函数：{}'.format(y_np))

print('以排序后的顺序重构原数组：{}'.format(x_np[y_np]))

print('使用循环重构原数组：')
for i in y_np:
    print(x_np[i], end=" ")
