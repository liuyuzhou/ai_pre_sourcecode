import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.01)

plt.plot(t)
plt.title(r'mathematical', fontsize=20)
# 制作下标和上标
plt.text(10, 4, r'$\alpha_i > \beta_i$', fontsize=20)
# 编写 0 到无穷的x
plt.text(120, 4, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
# 创建分数
plt.text(220, 4, r'$\frac{3}{4} \binom{3}{4} \stackrel{3}{4}$', fontsize=20)
# 创建二项式
plt.text(320, 4, r'$\frac{5 - \frac{1}{x}}{4}$', fontsize=20)
# 创建堆叠数字
plt.text(110, 0.5, r'$(\frac{5 - \frac{1}{x}}{4})$', fontsize=20)
# 创建堆叠数字
plt.text(220, 0.5, r'$\left(\frac{5 - \frac{1}{x}}{4}\right)$', fontsize=20)
# 创建根式
plt.text(350, 0.5, r'$\sqrt{2}$', fontsize=20)
# 创建根式
plt.text(440, 0.5, r'$\sqrt[3]{x}$', fontsize=20)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
