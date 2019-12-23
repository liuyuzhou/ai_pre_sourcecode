import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

fig = plt.figure()
ax = fig.add_subplot(111)

# 做一个简单的正弦波
x = np.arange(0., 2., 0.01)
y = np.sin(2 * np.pi * x)
line, = ax.plot(x, y, lw=3, color='blue')

# 移动物体2个点，向下2个点
dx, dy = 2/72., -2/72.
offset = transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)
shadow_transform = ax.transData + offset

# 现在用偏移变换绘制相同的数据,使用zorder来确保在线下
ax.plot(x, y, lw=3, color='gray', transform=shadow_transform, zorder=0.5 * line.get_zorder())

# 使用偏移变换创建阴影效果
ax.set_title('creating a shadow effect with an offset transform')
plt.show()
