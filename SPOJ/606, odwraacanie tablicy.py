"""
SPOJ 606
wczytaj tablice i wypisz jej odwrotnosc
"""
D = int(input())
for d in range(D):

                                    #wczytanie danych
    s = input()
    licznik = 0                     #ilosc liczb
    l = [""]                        #l bede powiekszac o s

    for i in range(len(s)):
        if i == len(s)-1:           #dla ostatniej cyfry
            l[licznik] += s[i]
        elif s[i] == " ":           #gdy natrafisz na spacje
            licznik += 1            #przejdz do nastepnego indexu
            l.append("")            #i zwieksz tablice o nowy index
        else:
            l[licznik] += s[i]      #wydluz tablice o cyfre

    suma = 0
    for i in range(licznik, 0, -1): #od konca do pocaztku
        print(l[i], end = " ")      #wypisz l[i]
