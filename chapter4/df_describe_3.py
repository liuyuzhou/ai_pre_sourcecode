import pandas as pd

dict_sr = {'Name': pd.Series(['meng', 'cai', 'zhang', 'wang', 'li', 'qiang', 'yang']),
           'Age': pd.Series([20, 21, 22, 21, 22, 19, 20]),
           'Rating': pd.Series([2.65, 3.51, 2.98, 3.22, 2.70, 3.6, 4.1])}
df = pd.DataFrame(dict_sr)
print('include为all的标准偏差：\n{}'.format(df.describe(include='all')))
