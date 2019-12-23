import pandas as pd

df = pd.read_json('files/basic_info.json')
print('pandas读取json文件结果：\n{}'.format(df))
