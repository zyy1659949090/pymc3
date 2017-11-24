import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-5.0, 5.0, 1000)
fig, ax = plt.subplots()
f = lambda mu, lam, df : st.t.pdf(x, df, loc=mu, scale=1.0/np.sqrt(lam))
plot_pdf = lambda mu, lam, df : ax.plot(x, f(mu, lam, df), label=r'$\mu$={0}, $\lambda$={1}, $\nu$={2}'.format(mu, lam, df))
plot_pdf(0.0, 1.0, 1.0)
plot_pdf(0.0, 1.0, 2.0)
plot_pdf(0.0, 1.0, 5)
plot_pdf(-1.0, 1.0, 5)
plot_pdf(-1.0, 2.0, 5)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[-5,5], ylim=[0,0.6], xlabel='x', ylabel='f(x)')
plt.show()