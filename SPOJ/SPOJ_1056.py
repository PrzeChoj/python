"""
SOPJ 1056
macierz o podanej wielkosci
nalezy elementy na jej brzegach przesunac o jeden
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

def spin_macierzy(m):
    pocz = m[0][0]

    for i in range(len(m[0])-1):
        m[0][i] = m[0][i+1]

    for i in range(len(m)-1):
        m[i][len(m[0])-1] = m[i+1][len(m[0])-1]

    for i in range(len(m[0]) - 1):
        m[len(m)-1][len(m[0])-1-i] = m[len(m)-1][len(m[0])-1-(i+1)]

    for i in range(len(m) - 2):
        m[len(m)-1-i][0] = m[len(m)-1-(i+1)][0]

    if len(m) > 1: m[1][0] = pocz

D = int(input())
for d in range(D):
    wymiary = input()
    wymiary = wymiary.split(" ")

    macierz = [[None] * int(wymiary[1]) for i in range(int(wymiary[0]))]

    wczytanie_do_macierzy(macierz)

    spin_macierzy(macierz)

    drukuj_macierz(macierz)