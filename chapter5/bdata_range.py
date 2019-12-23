import pandas as pd

date_list = pd.bdate_range('2019/01/23', periods=5)
print('指定开始日期的商业日期：\n{}'.format(date_list))

# 指定起始日期
start = pd.datetime(2019, 1, 23)
end = pd.datetime(2019, 1, 28)
b_dates = pd.bdate_range(start, end)
print('指定起始日期的商业日期：\n{}'.format(b_dates))
