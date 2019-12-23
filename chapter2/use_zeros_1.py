import numpy as np

# 默认为浮点数
zr_df = np.zeros(5)
print('默认类型：\n{}'.format(zr_df))

# 设置类型为整数
zr_int = np.zeros((5,), dtype=np.int)
print('设置为int类型：\n{}'.format(zr_int))

# 自定义类型
zr_sf = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'f4')])
print('自定义类型：\n{}'.format(zr_sf))
