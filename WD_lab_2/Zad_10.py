# Zadanie nr 10

W = int(input("Podaj wysokość wieży:"))

while W > 10 :

    print("Podana wartość nie może być większa niż 10 !!!. Spróbuj jeszcze raz.")

    W = int(input("Podaj wysokość wieży:"))

i = int(0)

znak = ("")

while i < W:

    znak += "*"

    print(str(znak))

    i += 1 