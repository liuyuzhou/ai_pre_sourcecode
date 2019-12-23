import pandas as pd

df_1 = pd.read_table('files/basic_info_1.csv', sep=',')
print('指定逗号（，）为分割符，从csv文件中读取到的文本内容如下：\n{}'.format(df_1))

df_2 = pd.read_table('files/basic_info_1.csv', sep='/')
print('指定斜杠（/）为分割符，从csv文件中读取到的文本内容如下：\n{}'.format(df_2))
