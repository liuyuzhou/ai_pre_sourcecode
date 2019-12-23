import pandas as pd

df = pd.read_csv('files/basic_info_1.csv', nrows=4)
df.to_csv('files/write_1.csv', index=False)

df_1 = pd.read_csv('files/write_1.csv')
print('读取的文本内容如下：\n{}'.format(df_1))
