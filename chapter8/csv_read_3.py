import pandas as pd

df_1 = pd.read_csv('files/basic_info_2.csv')
print('从csv文件中读取的文本内容如下（分配默认的列名）：\n{}'.format(df_1))

df_2 = pd.read_csv('files/basic_info_2.csv', names=['a', 'b', 'c', 'updt'])
print('从csv文件中读取的文本内容如下（自定义列名列名）：\n{}'.format(df_2))
