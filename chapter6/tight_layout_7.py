import matplotlib.pyplot as plt
import matplotlib.gridspec as grid_spec


def draw_plot(ax_p, font_size=12):
    ax_p.plot([1, 2])
    ax_p.locator_params(nbins=3)
    ax_p.set_xlabel('x-label', fontsize=font_size)
    ax_p.set_ylabel('y-label', fontsize=font_size)
    ax_p.set_title('Title', fontsize=font_size)


plt.close('all')
fig = plt.figure()

gs_1 = grid_spec.GridSpec(2, 1)
gs_2 = grid_spec.GridSpec(3, 1)
ax_1 = fig.add_subplot(gs_1[0])
ax_2 = fig.add_subplot(gs_1[1])

for ss in gs_2:
    ax = fig.add_subplot(ss)
    draw_plot(ax)
    ax.set_title("")
    ax.set_xlabel("")

ax.set_xlabel("x-label", fontsize=12)

gs_1.tight_layout(fig, rect=[0, 0, 0.5, 1])
gs_2.tight_layout(fig, rect=[0.5, 0, 1, 1], h_pad=0.5)

top = min(gs_1.top, gs_2.top)
bottom = max(gs_1.bottom, gs_2.bottom)

gs_1.tight_layout(fig, rect=[None, 0 + (bottom - gs_1.bottom),
                             0.5, 1 - (gs_1.top - top)])
gs_2.tight_layout(fig, rect=[0.5, 0 + (bottom - gs_2.bottom),
                             None, 1 - (gs_2.top - top)], h_pad=0.5)
plt.show()
