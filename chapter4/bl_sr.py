import pandas as pd

bl_s = pd.Series(5, index=[0, 1, 2, 3])
print('从标量创建：\n{}'.format(bl_s))
