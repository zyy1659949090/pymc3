import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 5.0, 1000)
fig, ax = plt.subplots()
f = lambda b : st.cauchy.pdf(x, scale=b)
plot_pdf = lambda b : ax.plot(x, f(b), label=r'$\beta$={0}'.format(b))
plot_pdf(0.5)
plot_pdf(1.0)
plot_pdf(2.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,5], ylim=[0,0.7], xlabel='x', ylabel='f(x)')
plt.show()