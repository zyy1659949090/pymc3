import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-10.0, 10.0, 1000)
fig, ax = plt.subplots()
f = lambda mu, b : st.laplace.pdf(x, loc=mu, scale=b)
plot_pdf = lambda mu, b : ax.plot(x, f(mu, b), label=r'$\mu$={0}, $b$={1}'.format(mu, b))
plot_pdf(0.0, 1.0)
plot_pdf(0.0, 2.0)
plot_pdf(0.0, 4)
plot_pdf(-5.0, 4)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[-10,10], ylim=[0,0.5], xlabel='x', ylabel='f(x)')
plt.show()