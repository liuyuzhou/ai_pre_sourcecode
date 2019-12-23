import numpy as np

# 移除字符串头尾的指定字符
print(np.char.strip('hHello worldh', 'h'))
# 头尾有多个满足条件的指定字符也移除
print(np.char.strip('hhHello worldhh', 'h'))

# 移除数组元素头尾的指定字符
print(np.char.strip(['detail', 'good', 'world', 'deed'], 'd'))
