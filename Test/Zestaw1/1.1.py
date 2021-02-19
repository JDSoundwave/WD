import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.arange(-5, 10, step=0.01)

y = (4 - x + x ** 3) / (6 + x - 4 * x ** 2 + x ** 3)

plt.plot(x, y, color="lightblue", label="Funkcja")

plt.ylim(-30, 30) # optyka - pole widzenia

# asympotota pozioma

av = np.ones(len(x))

plt.plot(x, av, color="orange", linestyle="--", label="y=1")

# asymptota pionowa

x1 = [-1, -1]

y1 = [-30, 30]

plt.plot(x1, y1, color="red", linestyle="--", label="x=-1")

x2 = [2, 2]

y2 = [-30, 30]

plt.plot(x2, y2, color="green", linestyle="--", label="x=2")

x3 = [3, 3]

y3 = [-30, 30]

plt.plot(x3, y3, color="violet", linestyle="--", label="x=3")

plt.title("Wykres funkcji")

plt.legend()

plt.savefig("zad1.pdf", format="pdf")

plt.show()