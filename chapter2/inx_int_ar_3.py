import numpy as np

np_ar = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s_s_ar = np_ar[1:3, 1:3]
print(s_s_ar)

s_l_ar = np_ar[1:3, [1, 2]]
print(s_l_ar)

e_s_ar = np_ar[..., 1:]
print(e_s_ar)