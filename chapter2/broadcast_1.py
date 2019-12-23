import numpy as np

x_np = np.array([[1], [2], [3]])
y_np = np.array([4, 5, 6])

# 对 y_np 广播 x_np
b_np = np.broadcast(x_np, y_np)

# 它拥有 iterator 属性，基于自身组件的迭代器元组
print('对 y_np 广播 x_np：')
r, c = b_np.iters

# Python3.x 为 next(context) ，Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))
print('\n')

# shape 属性返回广播对象的形状
print('广播对象的形状：\n{}'.format(b_np.shape))

# 手动使用 broadcast 将 x_np 与 y_np 相加
b_np = np.broadcast(x_np, y_np)
c = np.empty(b_np.shape)

print('手动使用 broadcast 将x_np与y_np相加：\n{}'.format(c.shape))

c.flat = [u + v for (u, v) in b_np]
print('调用 flat 函数：\n{}'.format(c))

print('x_np与y_np的和：\n{}'.format(x_np + y_np))
