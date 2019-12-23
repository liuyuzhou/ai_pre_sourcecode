import matplotlib.pyplot as plt

plt.title(r'mathematical', fontsize=20)
# 字体编写
plt.text(0.3, 0.8, r'$s(t) = \mathcal{A}\mathrm{sin}(2 \omega t)$', fontsize=20)
# 字体编写
plt.text(0.3, 0.5, r'$s(t) = \mathcal{A}\/\sin(2 \omega t)$', fontsize=20)
# 创建重音符号
plt.text(0.4, 0.2, r"$\hat i\ \ \hat \imath$", fontsize=20)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
