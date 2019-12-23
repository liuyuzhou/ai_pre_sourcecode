import numpy as np

num_np = np.arange(6)
print('初始数组：{}'.format(num_np))

print('调用id()函数：{}'.format(id(num_np)))

b_np = num_np
print('num_np赋值给b_np：{}'.format(b_np))
print('b_np拥有和num_np相同的id：{}'.format(id(b_np)))

b_np.shape = 3, 2
print('修改b_np的形状：\n{}'.format(b_np))
print('num_np的形状也修改了：\n{}'.format(num_np))
