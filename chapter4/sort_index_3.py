import pandas as pd
import numpy as np

un_sorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
sorted_df = un_sorted_df.sort_index(axis=1)
print(sorted_df)