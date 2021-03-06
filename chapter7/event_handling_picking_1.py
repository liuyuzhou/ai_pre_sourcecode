import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))


def onclick(event):
    print('发生点击操作：button={}, x={}, y={}, xdata={}, ydata={}'.
          format(event.button, event.x, event.y, event.xdata, event.ydata))


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
