import numpy as np

str_v = np.char.encode('numpy', 'cp500')
print('解码前：{}'.format(str_v))
print('解码后：{}'.format(np.char.decode(str_v, 'cp500')))
