# Zadanie nr 14

import math  

x = float(input("Podaj liczbę:"))

while x < 0:

	print("Podana liczba nie może być ujemna !!!. Proszę spróbuj jeszcze raz.")

	x = float(input("Podaj liczbę: "))

z = (math.sqrt(x))

print(z)