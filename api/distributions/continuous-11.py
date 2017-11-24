import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-5.0, 5.0, 200)
fig, ax = plt.subplots()
f = lambda sigma, nu : st.t.pdf(x, df=nu, loc=0, scale=sigma)
plot_pdf = lambda sigma, nu : ax.plot(x, f(sigma, nu), label=r'$\sigma$={}, $\nu$={}'.format(sigma, nu))
plot_pdf(1, 0.5)
plot_pdf(1, 1)
plot_pdf(2, 1)
plot_pdf(1, 30)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,5], ylim=[0, 0.4], xlabel='x', ylabel='f(x)')
plt.show()