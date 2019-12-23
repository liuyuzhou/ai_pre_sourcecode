import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

fig = plt.figure()
ax = fig.add_subplot(111)

# Fixing random state for reproducibility
np.random.seed(19680801)

# histogram our data with numpy
data = np.random.randn(1000)
n, bins = np.histogram(data, 100)

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
n_rect_s = len(left)

n_vert_s = n_rect_s * (1 + 3 + 1)
vert_s = np.zeros((n_vert_s, 2))
codes = np.ones(n_vert_s, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
vert_s[0::5, 0] = left
vert_s[0::5, 1] = bottom
vert_s[1::5, 0] = left
vert_s[1::5, 1] = top
vert_s[2::5, 0] = right
vert_s[2::5, 1] = top
vert_s[3::5, 0] = right
vert_s[3::5, 1] = bottom

bar_path = path.Path(vert_s, codes)
patch = patches.PathPatch(bar_path, facecolor='green', edgecolor='yellow', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

plt.show()
