import pandas as pd
import numpy as np

sr_1 = pd.Series(np.random.randn(20))
sr_2 = pd.Series(np.random.randn(30))
print('Series.cov() 可用于计算序列之间的协方差:\n{}'.format(sr_1.cov(sr_2)))

df = pd.DataFrame(np.random.randn(100, 5), columns=['a', 'b', 'c', 'd', 'e'])
print('DataFrame.cov()计算DataFrame中的序列之间的协方差:\n{}'.format(df.cov()))

df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
df.loc[df.index[:5], 'a'] = np.nan
df.loc[df.index[5:10], 'b'] = np.nan
print('DataFrame.cov支持可选min_periods关键字:\n{}'.format(df.cov(min_periods=2)))
