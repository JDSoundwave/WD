import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sciezka = r'C:\Users\ASUS\Desktop\GitHub\index\Test\Zestaw1\sport.xlsx'

dane = pd.read_excel(sciezka, header=None)

print(dane)

x = dane.iloc[:, 1]

etykiety = dane.iloc[:, 0]

plt.pie(x, labels=etykiety, autopct="%1.0f%%", explode=(0.1, 0, 0, 0, 0, 0))

plt.title("Popularność sportu w grupie nastolatków")

plt.annotate("12345", [-1, 1])

plt.savefig("zad2.jpg")

plt.show()