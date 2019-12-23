import pandas as pd

pd.options.display.max_rows = 5

read_data = pd.read_pickle('files/df_pickle')
print('read pickle结果：\n{}'.format(read_data))
