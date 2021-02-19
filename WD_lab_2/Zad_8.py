# Zadanie nr 8

liczba = input("Z ilu elementów ma się składać lista:")

liczba = int(liczba)

lista = []

i = 0

while i < liczba:

    i += 1

    print("Wprowadź", i, "element do listy:")

    a = input()

    a = int(a)

    lista.append(int(a))

print("Lista składa się z następujących elementów:", lista)