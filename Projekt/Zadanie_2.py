# Zadanie nr 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import openpyxl 
import xlrd

sciezka = r'ludnosc.xlsx'

odczyt = pd.ExcelFile(sciezka)

plik = pd.read_excel(odczyt, 'Arkusz1')

# Sortowanie #

sortowanie = plik.sort_values(by = 2017, ascending = False)

posortowane = (sortowanie[0:10])

# Grupowanie #

grupowanie = posortowane.groupby(['Kraj']).agg({2017:['sum']})

wykres = grupowanie.plot.pie(fontsize = 10, figsize = (15, 6), subplots = True, autopct = '%.2f %%', )

# Tytuł, Legenda #

plt.legend(loc = 2, bbox_to_anchor = (-0.1, 1.05), fontsize = 6)

plt.title('Najbardziej zaludnione kraje i regiony')

plt.show()