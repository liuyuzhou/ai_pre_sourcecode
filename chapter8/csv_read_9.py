import pandas as pd

df = pd.read_csv('files/basic_info_1.csv', chunksize=100)
print('读取的文本内容如下：\n{}'.format(df))

tot = pd.Series([])
for piece in df:
    tot = tot.add(piece['product_code'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)
print('对product_code聚合结果如下：\n{}'.format(tot))
