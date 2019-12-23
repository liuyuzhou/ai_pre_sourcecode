import matplotlib.pyplot as plt
import numpy as np

n_steps, n_walkers = 100, 250
t = np.arange(n_steps)

S1 = 0.002 + 0.01*np.random.randn(n_steps, n_walkers)
S2 = 0.004 + 0.02*np.random.randn(n_steps, n_walkers)

X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)

mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='mean population 1', color='blue')
ax.plot(t, mu2, lw=2, label='mean population 2', color='yellow')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='blue', alpha=0.5)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='yellow', alpha=0.5)
ax.set_title('random walkers empirical $\mu$ and $\pm \sigma$ interval')
ax.legend(loc='upper left')
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()

plt.show()
