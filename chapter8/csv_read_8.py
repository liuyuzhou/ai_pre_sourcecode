import pandas as pd

df = pd.read_csv('files/basic_info_1.csv', nrows=4)
print('读取的指定行数的文本内容如下：\n{}'.format(df))
