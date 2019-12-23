import numpy as np

a_np = np.array([1, 2, 3, 4, 5])
np.savetxt('out.txt', a_np)
b_np = np.loadtxt('out.txt')
print('b_np：{}'.format(b_np))

# 使用 delimiter 参数
x_np = np.arange(0, 10, 0.5).reshape(4, -1)
# 改为保存为整数，以逗号分隔
np.savetxt("out.txt", x_np, fmt="%d", delimiter=",")
# load 时也要指定为逗号分隔
y_np = np.loadtxt("out.txt", delimiter=",")
print('y_np：\n{}'.format(y_np))
