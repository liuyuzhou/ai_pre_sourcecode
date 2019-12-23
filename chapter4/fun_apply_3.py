import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())
print('调用apply函数后的数组：\n{}'.format(df))
