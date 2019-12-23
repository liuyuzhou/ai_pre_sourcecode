import matplotlib.pyplot as plt

plt.rcParams['savefig.facecolor'] = "0.8"


def draw_plot(ax_p, font_size=12):
    ax_p.plot([1, 2])
    ax_p.locator_params(nbins=3)
    ax_p.set_xlabel('x-label', fontsize=font_size)
    ax_p.set_ylabel('y-label', fontsize=font_size)
    ax_p.set_title('Title', fontsize=font_size)


plt.close('all')
fig, ax = plt.subplots()
draw_plot(ax, font_size=24)
# plt.tight_layout()
plt.show()
