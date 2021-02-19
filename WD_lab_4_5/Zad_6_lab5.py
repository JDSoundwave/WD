# Zadanie nr 6 lab 5

class Wspak:

    """Iterator zwracający wartości w odwróconym porządku"""

    def __init__(self, data):

        self.data = data

        self.index = len(data)

    def __iter__(self):

        return self

    def __next__(self):

        if self.index == 0:

            raise StopIteration

        self.index = self.index - 1

        return self.data[self.index]

    def odwroc(data):

        for x in data:

            print(x)       

jeden = Wspak("Reks")

jeden.odwroc()

dwa = Wspak("Jakis napis")

dwa.odwroc()
