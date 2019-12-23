import pandas as pd

df = pd.read_csv('files/basic_info_1.csv', index_col='product_code')
print('指定索引位置，从csv文件中读取的文本内容如下：\n{}'.format(df))

df_2 = pd.read_csv('files/basic_info_2.csv', names=['a', 'b', 'c', 'updt'], index_col='b')
print('指定索引位置，读取的文本内容如下（自定义列名）：\n{}'.format(df_2))
