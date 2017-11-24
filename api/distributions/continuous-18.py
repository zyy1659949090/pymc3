import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-6.0, 6.0, 1000)
fig, ax = plt.subplots()
f = lambda mu, sigma, nu : st.exponnorm.pdf(x, nu/sigma, loc=mu, scale=sigma)
plot_pdf = lambda mu, sigma, nu : ax.plot(x, f(mu, sigma, nu), label=r'$\mu$={0}, $\sigma$={1}, $\nu$={2}'.format(mu, sigma, nu))
plot_pdf(0.0,1.0,1.0)
plot_pdf(-2.0,1.0,1.0)
plot_pdf(0.0,3.0,1.0)
plot_pdf(-3.0,1.0,4.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[-6,6], ylim=[0,0.4], xlabel='x', ylabel='f(x)')
plt.show()