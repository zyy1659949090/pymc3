import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 3.0, 1000)
fig, ax = plt.subplots()
f = lambda mu, lam : st.invgauss.pdf(x, mu/lam, scale=lam)
plot_pdf = lambda a, b : ax.plot(x, f(a,b), label=r'$\mu$={0}, $\lambda$={1}'.format(a,b))
plot_pdf(1.0,1.0)
plot_pdf(1.0,0.2)
plot_pdf(1.0,3.0)
plot_pdf(3,1)
plot_pdf(3,0.2)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,3], ylim=[0,3.0], xlabel='x', ylabel='f(x)')
plt.show()