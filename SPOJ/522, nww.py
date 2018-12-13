"""
SPOJ 522
Znajdz najmniejsza wspolna wielokrotnosc 2 liczb
"""
D = int(input())

for d in range(D):
    #Wczytanie danych
    ab = input()
    s = ab.index(" ")

    a = int(ab[0:s])
    b = int(ab[s+1:len(ab)])

    #potrzebne dla znalezienia nwd
    ad = a
    bd = b

    #znajdowanie nwd(a, b)
    while ad != 0:
        cd = bd % ad
        bd = ad
        ad = cd

    #znajdowanie nww(a, b)
    print(a//bd*b)