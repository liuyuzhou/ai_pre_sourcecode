import numpy as np

# 等价于 1*0+2*1+3*0
inner_np = np.inner(np.array([1, 2, 3]), np.array([0, 1, 0]))
print('向量内积：{}'.format(inner_np))

