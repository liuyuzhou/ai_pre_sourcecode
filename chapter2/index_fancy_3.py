import numpy as np

np_ar = np.arange(32).reshape((8, 4))
fancy_ar = np_ar[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
print('花式结果：\n{}'.format(fancy_ar))
