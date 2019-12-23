import matplotlib.gridspec as grid_spec
import matplotlib.pyplot as plt

gs = grid_spec.GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])

ax_1 = plt.subplot(gs[0])
ax_2 = plt.subplot(gs[1])
ax_3 = plt.subplot(gs[2])
ax_4 = plt.subplot(gs[3])
plt.show()
