#-------------------------------------------------------------------------------
# Name:        Codigos Básicos Py
# Purpose:
#
# Author:      Odenir Gomes
#
# Created:     07/02/2019
# Copyright:   (c) Odenir Gomes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    #Entrada
    x = int(input("X: "))

    #Saida
    print(x)

    #Decisão
    if (x == 0):
        print("X é igual a zero!")

    elif (x > 0):
        print("X é maior que zero!")

    else:
        print("X é menor que zero!")

    #Laços

    #for
    print()
    for i in range(0, x):
        print("X")

    #while
    print()
    i = 0
    while i < x:
        print("Y")
        i = i + 1

    #Função
    def func():
        print("\nFunction")
        return

    func()

    class Classe:

        def __init__(self):
            self.y = x

        def print_Y(self):
            print("Classe Y: ", self.y)

    z = Classe()

    z.print_Y()

if __name__ == '__main__':
    main()
