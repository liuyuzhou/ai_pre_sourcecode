import pandas as pd

pd_sr = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('检索多个元素：\n{}'.format(pd_sr[['a', 'c', 'd']]))
