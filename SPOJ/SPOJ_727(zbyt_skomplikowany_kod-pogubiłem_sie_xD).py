"""
SPOJ 727
podana jest liczba naturalna

nalezy wyznaczyc wszystkie niemalejace ciagi liczb naturalnych
ktorych wartosci sumuja sie do podanej na wejsciu liczby
"""

n = int(input())

tablica = [1] * n
liczba = 1

out = open("ciagi.txt", "w")

for i in range(1, n + 1):
    for j in range(n-i):
        print(tablica[j], end=" ", file = out)
    if liczba != 0:
        print(liczba, end=" ", file = out)

    liczba += 1

    print("", file = out)

out.close()

liczba = 1

for i in range(2 ** n):
    with open("ciagi.txt", "r") as out:
        for l in range(liczba):
            linia = out.readline()
    liczba += 1
    if linia == "\n": break

    linia = linia.split(" ")
    print(f"linia = {linia}")
    for j in range(len(linia) - 1):
        linia[j] = int(linia[j])

    l = None
    for c in range(1, len(linia)):
        if linia[c-1] == linia[c]:
            l = linia[c-1] + linia[c]
            break
    print(f"c = {c}")
    print(f"l = {l}")

    if l != None:
        nowy_ciag = [None] * (len(linia) - 1)
        for j in range(len(nowy_ciag)):
            if j == c:
                nowy_ciag[j] = l
            elif j == c-1: l = l
            else:
                nowy_ciag[j] = linia[j]
        print(f"nowy_ciag = {nowy_ciag}")

        dlugosc = 0
        for j in range(len(nowy_ciag)):
            if nowy_ciag[j] != None:
                dlugosc += 1

        sorted_ciag = [0] * dlugosc
        dlugosc = 0
        for j in range(len(nowy_ciag)):
            if nowy_ciag[j] != None:
                sorted_ciag[dlugosc] = nowy_ciag[j]
                dlugosc += 1

        sorted_ciag.sort()
        print(f"nowy_ciag = {sorted_ciag}")

        with open("ciagi.txt", "r") as inp:
            for line in inp:
                if line == "\n": break
                liczb = line.split(" ")
                liczby = [None] * (len(liczb)-1)
                czy_sa_to_samo = [False] * (len(liczb)-1)
                for i in range(len(liczb) - 1):
                    liczby[i] = int(liczb[i])

                    if i<len(sorted_ciag) and liczby[i] == sorted_ciag[i]:
                        czy_sa_to_samo[i] = False


        # tworzenie takich ciagow, ktore lacza nie 2, 3, 4, 5, ..., n/2 takich samych elementow


        # sprawdzanie, czy taki ciag juz byl


        with open("ciagi.txt", "a") as out:
            for j in range(len(sorted_ciag)):
                if sorted_ciag[j] != None:
                    print(sorted_ciag[j], end=" ", file = out)
            print("", file = out)