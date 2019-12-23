import numpy as np

num_np = np.arange(4).reshape(1, 4)
print('原数组：\n{}'.format(num_np))
br_to_np = np.broadcast_to(num_np, (4, 4))
print('调用 broadcast_to 函数之后：\n{}'.format(br_to_np))
