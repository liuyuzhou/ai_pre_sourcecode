import pandas as pd

df = pd.read_csv('files/basic_info_1.csv')
df.to_pickle('files/df_pickle')
