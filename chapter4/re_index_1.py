import pandas as pd
import numpy as np

df_1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df_2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])
print('初始数组：\n{}'.format(df_1))

df_1 = df_1.reindex_like(df_2)
print('重建对象对齐索引后的数组：\n{}'.format(df_1))
