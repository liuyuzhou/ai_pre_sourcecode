import pandas as pd

s = pd.Series(pd.date_range('2019-1-23', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3, 6)])
df = pd.DataFrame(dict(A=s, B=td))
print('初始日期：\n{}'.format(df))

df['C'] = df['A'] + df['B']
print('日期相加：\n{}'.format(df))

df['C'] = df['A'] - df['B']
print('日期相减：\n{}'.format(df))
