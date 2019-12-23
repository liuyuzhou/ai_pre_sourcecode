import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(2, 4),
                  index=pd.date_range('1/1/2019', periods=2),
                  columns=['A', 'B', 'C', 'D'])
print('初始数组：\n{}'.format(df))

rl_df = df.rolling(window=3, min_periods=1)
print('聚合结果：\n{}'.format(rl_df.aggregate(np.sum)))
