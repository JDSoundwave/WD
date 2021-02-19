# Zadanie nr 11

x = (" ")

y = ("*")

W = int(input("Podaj wysokość diamentu:"))

while (W > 9 or W < 3):

    print("Wysokość nie może być większa niż 9 i mniejsza niż 3 !!!.")

    W = int(input("Podaj wysokość diamentu:"))


if (W % 2 == 0):

    i = 1

    while i < (W - 1) / 2:

        x += " "

        i += 1 
   
    i = 1

    while i < W / 2 + 1:

        print(x + y)
        
        "\n"

        y += "**"

        x = x[:-1]

        i += 1 

    i = W - 1

    while i > W / 2 - 1:

        y = y[:-2]

        print(" " + x + y)

        "\n"

        x += " "

        i -= 1 

else:

    i = 1

    while i < (W - 1) / 2:

        x += " "

        i += 1 
   
    i = 1

    while i < (W - 1) / 2 + 1:

        print(x + y)

        "\n"

        y += "**"

        x = x[:-1]

        i += 1 

    i = W

    while i > W / 2:

        print(x + y)

        "\n"

        x += " "

        y = y[:-2]

        i -= 1 






