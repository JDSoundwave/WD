# Zadanie nr 7

while True:

    x = input("Podaj liczbę:")

    x = int(x)

    kwadrat = (x ** 2)

    print("Podana liczba podniesiona do kwadratu wynosi:", kwadrat)

    print("Czy chcesz opuścić program: T/N ?")

    z = input()

    if (z == 'T' or z == 't'):

        print("EXIT")
        
        break

    else:
        
        continue