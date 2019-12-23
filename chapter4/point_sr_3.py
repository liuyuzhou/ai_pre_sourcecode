import pandas as pd

pd_sr = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('获取系列最后三个元素：\n{}'.format(pd_sr[-3:]))
