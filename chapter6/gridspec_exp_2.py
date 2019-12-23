import matplotlib.gridspec as grid_spec
import matplotlib.pyplot as plt

gs_1 = grid_spec.GridSpec(3, 3)
gs_1.update(left=0.05, right=0.48, wspace=0.05)
ax_1 = plt.subplot(gs_1[:-1, :])
ax_2 = plt.subplot(gs_1[-1, :-1])
ax_3 = plt.subplot(gs_1[-1, -1])

gs_2 = grid_spec.GridSpec(3, 3)
gs_2.update(left=0.55, right=0.98, hspace=0.05)
ax_4 = plt.subplot(gs_2[:, :-1])
ax_5 = plt.subplot(gs_2[:-1, -1])
ax_6 = plt.subplot(gs_2[-1, -1])
plt.show()
