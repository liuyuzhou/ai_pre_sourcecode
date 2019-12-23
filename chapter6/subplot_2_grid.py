import matplotlib.pyplot as plt

ax_1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax_2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax_3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax_4 = plt.subplot2grid((3, 3), (2, 0))
ax_5 = plt.subplot2grid((3, 3), (2, 1))
plt.show()
