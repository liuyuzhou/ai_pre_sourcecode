import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t_1 = np.arange(0.0, 5.0, 0.1)
t_2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t_1, f(t_1), 'bo', t_2, f(t_2), 'k')

plt.subplot(212)
plt.plot(t_2, np.cos(2 * np.pi * t_2), 'r--')
plt.show()
