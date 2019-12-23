import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': np.random.randn(100)})
frame.to_hdf('files/my_data.h5', 'obj_3', format='table')

read_result = pd.read_hdf('files/my_data.h5', 'obj_3', where=['index < 5'])
print('执行结果：\n{}'.format(read_result))
