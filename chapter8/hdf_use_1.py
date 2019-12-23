import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('files/my_data.h5')
store['obj_1'] = frame
store['obj_1_col'] = frame['a']
print('执行结果：\n{}'.format(store))
