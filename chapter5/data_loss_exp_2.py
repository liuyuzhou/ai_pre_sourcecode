import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 3),
                  index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e'])
print(df)
# 对应元素是否为NaN，为NaN，结果为True，否则为False
print(df['one'].isnull())
# 对应元素不为NaN，不为NaN，结果为True，否则为False
print(df['one'].notnull())
