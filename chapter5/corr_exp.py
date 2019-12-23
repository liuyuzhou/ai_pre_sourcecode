import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
print(df['a'].corr(df['b']))
print(df.corr())

df.loc[df.index[:4], 'a'] = np.nan
df.loc[df.index[4:10], 'b'] = np.nan
print(df.corr(min_periods=2))
