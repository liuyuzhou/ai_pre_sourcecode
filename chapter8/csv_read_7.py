import pandas as pd

pd.options.display.max_rows = 5

df = pd.read_csv('files/basic_info_1.csv')
print('读取的文本内容如下：\n{}'.format(df))
