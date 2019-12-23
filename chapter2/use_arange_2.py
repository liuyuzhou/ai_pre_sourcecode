import numpy as np

# 生成指定长度数组，并指定dtype为float类型
ft_ar = np.arange(5, dtype=float)
print('float结果数组：{}'.format(ft_ar))

# 生成指定长度数组，并指定dtype为complex类型
cp_ar = np.arange(5, dtype=complex)
print('complex结果数组：{}'.format(cp_ar))
