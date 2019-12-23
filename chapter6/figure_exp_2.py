import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
line, = ax2.plot(t, s, color='blue', lw=2)
plt.show()
