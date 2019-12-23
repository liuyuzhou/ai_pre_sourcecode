import matplotlib.gridspec as grid_spec
import matplotlib.pyplot as plt

gs = grid_spec.GridSpec(3, 3)
ax_1 = plt.subplot(gs[0, :])
ax_2 = plt.subplot(gs[1, :-1])
ax_3 = plt.subplot(gs[1:, -1])
ax_4 = plt.subplot(gs[-1, 0])
ax_5 = plt.subplot(gs[-1, -3])
plt.show()
