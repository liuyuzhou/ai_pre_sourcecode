import pandas as pd
import numpy as np

df_1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
print('初始数组：\n{}'.format(df_1))

print("重命名行和列后：\n{}".format(df_1.rename(columns={'col1': 'c1', 'col2': 'c2'},
                                        index={0: 'apple', 1: 'banana', 2: 'durian'})))
