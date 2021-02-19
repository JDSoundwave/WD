

def otoczka():

    tekst = input("Podaj tekst do otoczenia: ")

    if len(tekst) <= 76:

        print('#' * 80)

        print('# ' + tekst + ' ' * (76 - (len(tekst))) + ' #')

        print('#' * 80)

otoczka()