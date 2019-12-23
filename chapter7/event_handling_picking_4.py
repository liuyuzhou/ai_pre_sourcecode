import matplotlib.pyplot as plt


def enter_axes(event):
    print('enter_axes:{}'.format(event.inaxes))
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()


def leave_axes(event):
    print('leave_axes:{}'.format(event.inaxes))
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()


def enter_figure(event):
    print('enter_figure{}'.format(event.canvas.figure))
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()


def leave_figure(event):
    print('leave_figure:{}'.format(event.canvas.figure))
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()


fig1 = plt.figure()
fig1.suptitle('mouse hover over figure or axes to trigger events')
ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)

fig1.canvas.mpl_connect('figure_enter_event', enter_figure)
fig1.canvas.mpl_connect('figure_leave_event', leave_figure)
fig1.canvas.mpl_connect('axes_enter_event', enter_axes)
fig1.canvas.mpl_connect('axes_leave_event', leave_axes)

plt.show()
