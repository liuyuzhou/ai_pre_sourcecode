import matplotlib.patches as m_patches
import matplotlib.pyplot as plt

black_patch = m_patches.Patch(color='black', label='The black data')
plt.legend(handles=[black_patch])

plt.show()
