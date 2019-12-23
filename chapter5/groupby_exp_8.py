import pandas as pd

df_data = {'Team': ['ABCA', 'BD', 'ABCA', 'BD', 'AE', 'ABDCA', 'CA'],
           'Rank': [1, 2, 2, 3, 3, 4, 1],
           'Year': [2018, 2019, 2020, 2019, 2018, 2020, 2021],
           'Points': [187.5, 181, 186, 179.5, 176, 189, 175]}
df = pd.DataFrame(df_data)
filter = df.groupby('Team').filter(lambda x: len(x) >= 2)
print(filter)
