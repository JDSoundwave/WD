# Zadanie nr 1 lab 4

plik = open("zad_1.txt", "a+")

for x in range(1, 51):

    if x % 4 == 0:

        print(x, end=" ")

    plik.write(str(x))

plik.close()