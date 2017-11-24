import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-np.pi, np.pi, 1000)
fig, ax = plt.subplots()
f = lambda mu, kappa : st.vonmises.pdf(x, kappa, loc=mu)
plot_pdf = lambda mu, kappa : ax.plot(x, f(mu, kappa), label=r'$\mu$={0}, $\kappa$={1}'.format(mu, kappa))
plot_pdf(0.0,0.001)
plot_pdf(0.0,0.5)
plot_pdf(0.0,1.0)
plot_pdf(0.0,2.0)
plot_pdf(0.0,4.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[-np.pi,np.pi], ylim=[0,1.0], xlabel='x', ylabel='f(x)')
plt.show()