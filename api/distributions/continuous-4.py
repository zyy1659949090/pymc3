import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 5.0, 1000)
fig, ax = plt.subplots()
f = lambda lam : st.expon.pdf(x, scale=1.0/lam)
plot_pdf = lambda lam : ax.plot(x, f(lam), label=r'$\lambda$={0}'.format(lam))
plot_pdf(0.5)
plot_pdf(1.0)
plot_pdf(1.5)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,5], ylim=[0,1.6], xlabel='x', ylabel='f(x)')
plt.show()