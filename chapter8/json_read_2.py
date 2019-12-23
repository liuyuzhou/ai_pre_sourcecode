import pandas as pd

df = pd.read_json('files/basic_info.json')
print('pandas数据转json格式结果：\n{}'.format(df.to_json()))
