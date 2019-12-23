import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on points')

line, = ax.plot(np.random.rand(100), 'o', picker=5)


def on_pick(event):
    this_line = event.artist
    x_data = this_line.get_xdata()
    y_data = this_line.get_ydata()
    ind = event.ind
    points = tuple(zip(x_data[ind], y_data[ind]))
    print('onpick points:', points)


fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
