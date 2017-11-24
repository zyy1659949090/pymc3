import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 3.0, 1000)
fig, ax = plt.subplots()
f = lambda alpha, beta : st.invgamma.pdf(x, alpha, scale=beta)
plot_pdf = lambda alpha, beta : ax.plot(x, f(alpha, beta), label=r'$\alpha$={0}, $\beta$={1}'.format(alpha, beta))
plot_pdf(1.0,1.0)
plot_pdf(2.0,1.0)
plot_pdf(3.0,1.0)
plot_pdf(3.0,0.5)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,3], ylim=[0,5], xlabel='x', ylabel='f(x)')
plt.show()