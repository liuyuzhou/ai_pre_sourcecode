import pandas as pd
import numpy as np

# pd.options.display.max_rows = 10

df = pd.read_csv('D:/privatefile/files/basic_info.csv', nrows=2)
print(df)
# df.head()
# print(df.head())

df.to_csv('D:/privatefile/files/out_info.csv')
# for i in range(0, 20):
#     df2 = df.iloc[i:i + 2].applymap(lambda s: str(s))
#     nan_df = df.notnull()
#     df2 = df2.where(nan_df, None)  # 转成空字符串或空值
#     # 将df转成list-tuple格式，才能导入数据库
#     param = df2.to_records(index=False).tolist()
#     print(param)
#
# readcsv = pd.read_table('D:/privatefile/files/basic_info.csv', sep=',')
# print(readcsv)
