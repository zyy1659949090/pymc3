import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(-5.0, 5.0, 1000)
fig, ax = plt.subplots()
f = lambda a, b : st.cauchy.pdf(x, loc=a, scale=b)
plot_pdf = lambda a, b : ax.plot(x, f(a, b), label=r'$\alpha$={0}, $\beta$={1}'.format(a, b))
plot_pdf(0.0, 0.5)
plot_pdf(0.0, 1.0)
plot_pdf(0.0, 2.0)
plot_pdf(-2.0, 1.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[-5,5], ylim=[0,0.7], xlabel='x', ylabel='f(x)')
plt.show()