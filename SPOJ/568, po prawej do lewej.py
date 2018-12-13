"""
SPOJ 568
jesli liczbe czytasz od prawej i od lewej tak samo, to ja zostaw
jesli  inaczej, dodaj ja do tej odwroconej i powtorz procedure
wypisz ostateczny wynik i ilosc operacji
"""
D = int(input())
for d in range(D):

    #wczytanie liczby pierwotnej
    n  = input()
    no = ""     #no bede powiekszac o n od konca
    licznik = 0 #liczy iteracje dodawania

    for i in range(len(n)-1, -1, -1):
        no += n[i]



    while no != n:                  #gdy n nie jest palindromem
        licznik += 1
        n = str(int(n) + int(no))   #nowe n jest suma n i no
        no = ""

        for i in range(len(n)-1, -1, -1): #nowe no to nowe n od konca
            no += n[i]



    print(no, licznik)

