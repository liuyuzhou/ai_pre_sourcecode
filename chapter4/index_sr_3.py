import pandas as pd

pd_sr = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('检索不存在的元素：\n{}'.format(pd_sr['w']))
