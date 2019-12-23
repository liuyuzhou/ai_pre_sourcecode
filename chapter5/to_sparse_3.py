import pandas as pd
import numpy as np

sr = pd.Series([1, np.nan, np.nan])
print('初始序列：\n{}'.format(sr))
print('稀疏处理后：\n{}'.format(sr.to_sparse()))
