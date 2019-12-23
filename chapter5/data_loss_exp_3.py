import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 3),
                  index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c'])
print('df数组：\n{}'.format(df))
print('df数组求和：{}'.format(df['one'].sum()))

pd_df = pd.DataFrame(index=[0, 1, 2, 3, 4, 5], columns=['one', 'two'])
print('pd_df数组：\n{}'.format(pd_df))
print('pd_df数组求和：{}'.format(pd_df['one'].sum()))
