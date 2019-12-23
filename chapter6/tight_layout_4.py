import matplotlib.pyplot as plt


def draw_plot(ax_p, font_size=12):
    ax_p.plot([1, 2])
    ax_p.locator_params(nbins=3)
    ax_p.set_xlabel('x-label', fontsize=font_size)
    ax_p.set_ylabel('y-label', fontsize=font_size)
    ax_p.set_title('Title', fontsize=font_size)


plt.close('all')
fig = plt.figure()

ax_1 = plt.subplot2grid((3, 3), (0, 0))
ax_2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
ax_3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
ax_4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

draw_plot(ax_1)
draw_plot(ax_2)
draw_plot(ax_3)
draw_plot(ax_4)

plt.tight_layout()
plt.show()
