import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 5.0, 1000)
fig, ax = plt.subplots()
f = lambda m, alpha : st.pareto.pdf(x, alpha, scale=m)
plot_pdf = lambda m, alpha : ax.plot(x, f(m, alpha), label=r'm={0}, $\alpha$={1}'.format(m, alpha))
plot_pdf(1.0,1.0)
plot_pdf(1.0,2.0)
plot_pdf(1.0,3.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,5], ylim=[0,3.0], xlabel='x', ylabel='f(x)')
plt.show()