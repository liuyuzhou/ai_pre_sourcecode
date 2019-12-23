import pandas as pd

df_1 = pd.read_csv('files/basic_info_1.csv')
print('读取的完整文本内容如下：\n{}'.format(df_1))

df_2 = pd.read_csv('files/basic_info_1.csv', skiprows=[1, 3])
print('跳过文件的第二和第四行后，读取的文本内容如下：\n{}'.format(df_2))
