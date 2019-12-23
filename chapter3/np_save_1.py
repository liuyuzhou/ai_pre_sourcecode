import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)

# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('outfile2', a)
