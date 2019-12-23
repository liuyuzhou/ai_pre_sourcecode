import matplotlib.pyplot as plt


def draw_plot(ax_p, font_size=12):
    ax_p.plot([1, 2])
    ax_p.locator_params(nbins=3)
    ax_p.set_xlabel('x-label', fontsize=font_size)
    ax_p.set_ylabel('y-label', fontsize=font_size)
    ax_p.set_title('Title', fontsize=font_size)


plt.close('all')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
draw_plot(ax1)
draw_plot(ax2)
draw_plot(ax3)
draw_plot(ax4)
# plt.tight_layout()
plt.show()
