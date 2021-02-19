# Zadanie nr 5

print("Podaj liczbę a:")

a = input()
a = int(a)

print("Podaj liczbę b:")

b = input()
b = int(b)

print("Podaj liczbę c:")

c = input()
c = int(c)

if (a >= 0 and a <= 10):
    
    print("Liczba a zawiera się w przedziale od 1 do 10.")

    if (a > b):

        print("Liczba a jest większa od liczby b.")

    elif (b > c):

        print("Liczba b jest większa od liczby c.")

    elif (a == b and b == c):

        print("Wszystkie wprowadzone liczby są sobie równe.")

    else:

        print("Liczba c ma największą wartość.")
   
else:

    print("Liczba a nie należy do przedziału od 1 do 10")