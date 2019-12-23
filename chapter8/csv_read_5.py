import pandas as pd

df_1 = pd.read_csv('files/basic_info_1.csv', index_col=['product_code', 'image_id'])
print('指定索引列表，从csv文件中读取的文本内容如下：\n{}'.format(df_1))

df_2 = pd.read_csv('files/basic_info_1.csv', index_col=[1, 0])
print('指定索引编号，从csv文件中读取的文本内容如下：\n{}'.format(df_2))
