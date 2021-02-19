# Zadanie nr 2

import sys


n = "Podaj dwie liczby:\n" 


x = sys.stdin.readline()

x = int(x)


y = sys.stdin.readline()

y = int(y)


z = x * y

z = str(z)


sys.stdout.write(z)