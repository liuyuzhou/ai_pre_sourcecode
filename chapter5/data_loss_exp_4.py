import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 3),
                  index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e'])
print('df数组：\n{}'.format(df))
print("用0填充NaN后的数组:\n{}".format(df.fillna(0)))
print("用3填充NaN后的数组:\n{}".format(df.fillna(3)))
