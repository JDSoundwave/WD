# Zadanie nr 1 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import openpyxl 
import xlrd

sciezka = r'ludnosc.xlsx'

odczyt = pd.ExcelFile(sciezka)

plik = pd.read_excel(odczyt, 'Arkusz1')

# Odczyt pierwotnej tabeli #


print(plik)


# Wyciąganie kolumn z pliku #


wyciagnij_dane = pd.DataFrame(plik, columns = ['Kraj', 2006, 2017])

print(wyciagnij_dane)


# Wyliczenie różnicy bezwzględnej -->> abs <<-- między rokiem 2006 a 2017 #


roznica = pd.DataFrame(abs(plik[2006] - plik[2017]))


# Dołączenie kolumny różnica #


plik['Roznica'] = roznica

plik = plik[['Kraj', 2006, 2017, 'Roznica']]


# Sortowanie malejące względem wartości w kolumnie różnica # 


sortowanie = plik.sort_values(by = 'Roznica', ascending = False)

print(sortowanie[0:10])

posortowane = (sortowanie[0:10])

rezultat = posortowane[['Kraj', 2006, 2017]]


# Etykiety, wielkość fontów #


rezultat.plot.bar('Kraj', figsize = (10, 6))

plt.xticks(rotation = 10)

plt.ylabel('Populacja w miliardach', fontsize = 14)

plt.xlabel('Kraj', fontsize = 3)


# Legenda #


plt.legend(loc = 2)


# Tytuł #


plt.title('Różnica w liczbie ludności pomiędzy 2006 a 2017 rokiem.', fontsize = 14)

plt.show()