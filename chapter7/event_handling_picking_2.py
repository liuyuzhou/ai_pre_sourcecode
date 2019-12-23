from matplotlib import pyplot as plt


class LineBuilder:
    def __init__(self, line_v):
        self.line = line_v
        self.xs = list(line_v.get_xdata())
        self.ys = list(line_v.get_ydata())
        self.cid = line_v.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('点击输出:{}'.format(event))
        if event.inaxes != self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])
line_builder = LineBuilder(line)

plt.show()
