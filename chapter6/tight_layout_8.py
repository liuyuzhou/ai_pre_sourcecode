import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Grid


def draw_plot(ax_p, font_size=12):
    ax_p.plot([1, 2])
    ax_p.locator_params(nbins=3)
    ax_p.set_xlabel('x-label', fontsize=font_size)
    ax_p.set_ylabel('y-label', fontsize=font_size)
    ax_p.set_title('Title', fontsize=font_size)


plt.close('all')
fig = plt.figure()

grid = Grid(fig, rect=111, nrows_ncols=(2, 2), axes_pad=0.25, label_mode='L',)

for ax in grid:
    draw_plot(ax)
    ax.title.set_visible(False)

plt.tight_layout()
plt.show()
