"""
SPOJ 1042
Ztransponuj macierz
"""
def drukuj_macierz(t):
    for i in range(len(t)):
        for j in range(len(t[0])):
            print(t[i][j], end=" ")
        print("")

def wczytanie_do_macierzy(m):
    for i in range(len(m)):
        liczby = input()
        liczby = liczby.split(" ")

        for j in range(len(m[0])):
            m[i][j] = int(liczby[j])

def transponowanie(m):
    t = [ [None] * len(m) for i in range(len(m[0])) ]

    for i in range(len(m[0])):
        for j in range(len(m)):
            t[i][j] = m[j][i]

    return t

wymiar = input()
wymiar = wymiar.split()
for i in range(len(wymiar)):
    wymiar[i] = int(wymiar[i])

macierz_d = [ [None] * wymiar[1] for i in range(wymiar[0]) ]


wczytanie_do_macierzy(macierz_d)

macierz_t = transponowanie(macierz_d)

drukuj_macierz(macierz_t)

