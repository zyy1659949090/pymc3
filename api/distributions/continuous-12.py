import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 3.0, 1000)
fig, ax = plt.subplots()
f = lambda mu, sd : st.lognorm.pdf(x, sd, scale=np.exp(mu))
plot_pdf = lambda mu, sd : ax.plot(x, f(mu, sd), label=r'$\mu$={0}, $\sigma$={1}'.format(mu, sd))
plot_pdf(0.0, 0.25)
plot_pdf(0.0, 0.5)
plot_pdf(0.0, 1.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,3], ylim=[0,1.8], xlabel='x', ylabel='f(x)')
plt.show()