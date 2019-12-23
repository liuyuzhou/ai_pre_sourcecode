import numpy as np

# 最开始 a 是个 3X2 的数组
a_np = np.arange(6).reshape(3, 2)
print('数组：\n{}'.format(a_np))

b_np = a_np.view()
print('创建a_np的视图：\n{}'.format(b_np))

print('两个数组的 id()不同：')
print('a_np的id()：{}'.format(id(a_np)))
print('b_np的id()：{}'.format(id(b_np)))

# 修改 b 的形状，并不会修改 a
b_np.shape = 2, 3
print('b_np的形状：\n{}'.format(b_np))
print('a_np的形状：\n{}'.format(a_np))
