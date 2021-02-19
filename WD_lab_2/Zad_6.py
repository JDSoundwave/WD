
# Zadanie nr 6

od = input("Początek zakresu liczb:")

od = int(od)

do = input("Koniec zakresu liczb:")

do = int(do)

for i in range(od, do):

    i = int(i)

    if i % 5 == 0:

        print("Liczba podzielna przez 5 to:", i)