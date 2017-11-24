import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-3.0, 3.0, 1000)
fig, ax = plt.subplots()
f = lambda alpha, mu, sigma : st.skewnorm.pdf(x, alpha, loc=mu, scale=sigma)
plot_pdf = lambda alpha, mu, sigma : ax.plot(x, f(alpha, mu, sigma), label=r'$\mu$={0}, $\sigma$={1}, $\alpha$={2}'.format(mu, sigma, alpha))
plot_pdf(-4.0,0.0,1.0)
plot_pdf(-1.0,0.0,1.0)
plot_pdf(0.0,0.0,1.0)
plot_pdf(1.0,0.0,1.0)
plot_pdf(4.0,0.0,1.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[-3,3], ylim=[0,0.7], xlabel='x', ylabel='f(x)')
plt.show()