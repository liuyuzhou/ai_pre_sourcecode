import pandas as pd
import numpy as np

str_list = ['meng', 'Zhi', 'MI', 'w@y', np.nan, '123', 'LiXiao']
pd_str = pd.Series(str_list)
print(pd_str.str.upper())
