import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 20.0, 1000)
fig, ax = plt.subplots()
f = lambda a, b : st.gamma.pdf(x, a, scale=1.0/b)
plot_pdf = lambda a, b : ax.plot(x, f(a, b), label=r'$\alpha$={0}, $\beta$={1}'.format(a, b))
plot_pdf(1.0, 0.5)
plot_pdf(2.0, 0.5)
plot_pdf(3.0, 1.0)
plot_pdf(7.5, 1.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,20], ylim=[0,0.5], xlabel='x', ylabel='f(x)')
plt.show()