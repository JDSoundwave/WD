import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sciezka = r'C:\Users\ASUS\Desktop\GitHub\index\Test\Zestaw1\wyksz.csv'

dane = pd.read_csv(sciezka)

print(dane)

wyzsze = dane[dane["Wykształcenie"] == "wyższe"]

sred = dane[dane["Wykształcenie"] == "średnie"]

podst = dane[dane["Wykształcenie"] == "podstawowe"]

x = np.arange(0, len(wyzsze))

plt.bar(x - 0.25, wyzsze["Liczebność"], label="Wyższe", width=0.25, color="blue")

plt.bar(x, sred["Liczebność"], label="Średnie", width=0.25, color="green")

plt.bar(x + .25, podst["Liczebność"], label="podstawowe", width=0.25, color="brown")

plt.legend(loc=7)

plt.ylabel("Liczebność")

plt.xlabel("Przedział wiekowy")

plt.title("Wykształcenie a wiek")

plt.xticks(x, wyzsze["Wiek"])

plt.show()