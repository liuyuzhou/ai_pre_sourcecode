import pandas as pd
import numpy as np

pd_sr = pd.Series([1, 2, 3, 4, 5, 4])
pct_ch = pd_sr.pct_change()
print('系列：\n{}'.format(pd_sr))
print('系列前后元素变化百分比：\n{}'.format(pct_ch))

df = pd.DataFrame(np.random.randn(5, 2))
print('数据帧前后元素变化百分比：\n{}'.format(df.pct_change()))
