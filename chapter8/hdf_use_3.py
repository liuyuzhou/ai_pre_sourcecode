import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('files/my_data.h5')

store.put('obj_2', frame, format='table')
store.select('obj_2', where=['index >= 10 and index <= 15'])
print('执行结果：\n{}'.format(store))