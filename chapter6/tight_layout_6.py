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
ax_1 = fig.add_subplot(gs_1[0])
ax_2 = fig.add_subplot(gs_1[1])
draw_plot(ax_1)
draw_plot(ax_2)

gs_1.tight_layout(fig)
# plt.show()
