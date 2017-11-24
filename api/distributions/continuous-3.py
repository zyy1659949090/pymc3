import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 1.0, 1000)
fig, ax = plt.subplots()
f = lambda a, b : st.beta.pdf(x, a, b)
plot_pdf = lambda a, b : ax.plot(x, f(a,b), label=r'$\alpha$={0}, $\beta$={1}'.format(a,b))
plot_pdf(0.5, 0.5)
plot_pdf(5.0, 1.0)
plot_pdf(1.0, 3.0)
plot_pdf(2.0, 2.0)
plot_pdf(2.0, 5.0)
plt.legend(loc='upper center', frameon=False)
ax.set(xlim=[0,1], ylim=[0,2.5], xlabel='x', ylabel='f(x)')
plt.show()