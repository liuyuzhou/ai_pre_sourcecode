import pandas as pd

print('当前时间：{}'.format(pd.datetime.now()))

pd_time = pd.Timestamp('2019-01-23')
print('创建一个时间戳：{}'.format(pd_time))

pd_time = pd.Timestamp(1588686880, unit='s')
print('时间戳转时间:{}'.format(pd_time))

pd_time = pd.date_range("12:00", "23:59", freq="30min").time
print('创建一个时间范围：\n{}'.format(pd_time))

pd_time = pd.date_range("12:00", "23:59", freq="H").time
print('改变时间的频率:\n{}'.format(pd_time))

pd_time = pd.to_datetime(pd.Series(['Jul 31, 2009', '2019-10-10', None]))
print('转换为时间戳:\n{}'.format(pd_time))

pd_time = pd.to_datetime(['2019/01/23', '2019.12.31', None])
print('时间转换:{}'.format(pd_time))
