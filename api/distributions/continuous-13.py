import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
x = np.linspace(0.0, 8.0, 1000)
fig, ax = plt.subplots()
f = lambda df : st.chi2.pdf(x, df)
plot_pdf = lambda df : ax.plot(x, f(df), label=r'$\nu$={0}'.format(df))
plot_pdf(1.0)
plot_pdf(2.0)
plot_pdf(3.0)
plot_pdf(4.0)
plot_pdf(6.0)
plot_pdf(9.0)
plt.legend(loc='upper right', frameon=False)
ax.set(xlim=[0,8], ylim=[0,0.5], xlabel='x', ylabel='f(x)')
plt.show()