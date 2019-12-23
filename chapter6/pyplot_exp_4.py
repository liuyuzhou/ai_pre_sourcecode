import numpy as np
import matplotlib.pyplot as plt

# 平均采样时间为200ms
pt = np.arange(0., 5., 0.2)

# 输出红色的破折号，蓝色的正方形和绿色的三角形
plt.plot(pt, pt, 'r--', pt, pt ** 2, 'bs', pt, pt ** 3, 'g^')
plt.show()
