import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3.0, 3.0, 1000)
a, b = 0.0, 2.0
y = np.zeros(1000)
y[(x<b) & (x>a)] = 1.0/(b-a)
fig, ax = plt.subplots()
ax.plot(x, y, label='lower=1, upper=2')
a, b = -2.0, 1.0
y = np.zeros(1000)
y[(x<b) & (x>a)] = 1.0/(b-a)
ax.plot(x, y, label='lower=-2, upper=1')
ax.legend(loc='upper right')
ax.set(ylim=[-0.2,1.2], xlabel='x', ylabel='f(x)')
plt.show()