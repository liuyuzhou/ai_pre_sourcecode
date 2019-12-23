import matplotlib.gridspec as grid_spec
import matplotlib.pyplot as plt

gs0 = grid_spec.GridSpec(1, 2)

gs_1 = grid_spec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
gs_2 = grid_spec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[1])
ax_1 = plt.subplot(gs_1[:-1, :])
ax_2 = plt.subplot(gs_1[-1, :-1])
plt.show()
