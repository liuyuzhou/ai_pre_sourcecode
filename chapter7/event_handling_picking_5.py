import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(100, 1000)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=5)


def on_pick(event):
    if event.artist!=line: return True

    ind_len = len(event.ind)
    if not ind_len: return True

    fi_gi = plt.figure()
    for sub_plot_num, data_ind in enumerate(event.ind):
        ax = fi_gi.add_subplot(ind_len, 1, sub_plot_num+1)
        ax.plot(X[data_ind])
        ax.text(0.05, 0.9, 'mu=%1.3f\nsigma=%1.3f' % (xs[data_ind], ys[data_ind]),
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    fi_gi.show()
    return True


fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
