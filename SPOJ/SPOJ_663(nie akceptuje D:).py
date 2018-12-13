"""
SPOJ 663
posortuj punkty pod wzgledem odleglosci od 0 0
"""
def drukuj_macierz(t):
    for i in range(len(t)):
        print(t[i][0], end=" ")
        for j in range(1, len(t[0])-1):
            print(int(t[i][j]), end=" ")
        print("")

import math

def odleglosc_euklidesa(x, y):
    return math.sqrt(x**2 + y**2)

def sortowanie(t):
    for i in range(len(t)-1):
        for j in range(i, len(t)-1):
            if t[j][3] > t[j+1][3]:
                for k in range(4):
                    t[j][k], t[j+1][k] = t[j+1][k], t[j][k]

D = int(input())
for d in range(D):

    T = int(input())
    macierz = [ [0] * 4 for t in range(T) ]
    for t in range(T):
        lista = input()
        lista = lista.split(" ")

        macierz[t][0] = lista[0]
        for i in range(1, 3):
            macierz[t][i] = int(lista[i])

        macierz[t][3] = odleglosc_euklidesa(macierz[t][1], macierz[t][2])

    sortowanie(macierz)

    drukuj_macierz(macierz)


    T = input()
    assert T == "\n"

    print("")
