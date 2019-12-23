import pandas as pd

date_list = pd.date_range('2019/01/23', periods=5)
print(date_list)

# 更改日期频率
date_list = pd.date_range('2019/01/23', periods=5, freq='M')
print('最大日期频率：\n{}'.format(date_list))
