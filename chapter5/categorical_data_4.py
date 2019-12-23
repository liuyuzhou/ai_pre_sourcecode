import pandas as pd
import numpy as np

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print('对象类别：{}'.format(s.categories))

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print('对象顺序：{}'.format(cat.ordered))
