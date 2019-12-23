import numpy as np

a = np.arange(4).reshape(2, 2)
print('原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)