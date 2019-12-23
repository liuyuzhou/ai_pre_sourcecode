import numpy as np

num_np = np.array([1, 256, 8755], dtype=np.int16)
print('初始数组：{}'.format(num_np))

print('以十六进制表示内存中的数据：{}'.format(map(hex, num_np)))

# byteswap() 函数通过传入 True 来原地交换
print('调用 byteswap() 函数：{}'.format(num_np.byteswap(True)))
print('十六进制形式：{}'.format(hex, num_np))
