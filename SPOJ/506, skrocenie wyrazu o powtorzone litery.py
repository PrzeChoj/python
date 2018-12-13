"""
SPOJ 506
wczytac ciag liter
przerobic napis: przy wiecej niz 2 literach obok siebie, wypisz tylko jedna i cyfre oznaczajaca ilosc wystapien
"""

D = int(input())        #zapetlanie
for d in range(D):      #d-krotne

    #wczytuje napis pierwotny
    n = input()
    w = "" #w to napis wyjsciowy, bede go z czasem przedluzal



    licznik = 1 #liczy powtorzenia
    for i in range(1, len(n)):
        if licznik == 2 and n[i-1] != n[i]: #w przypadku 2 liter obok sibie
            w = w + n[i-2] + n[i-1]         #nie zacufrowywuj ich
            licznik = 1
        elif n[i-1] == n[i]:                #jesli sa takie same,
            licznik += 1                    #podlicz je
        elif licznik != 1:                  #jesli sa inne
            w = w + n[i-1] + str(licznik)   #dodaj wielkosc do w
            licznik = 1                     #i wyzeruj licznik
        else:
            w = w + n[i-1]                  #albo po prostu dodaj to do w



    #poprawka dla ostatniej literki
    if licznik == 1:
        w += n[len(n)-1]
    elif licznik == 2:
        w = w + n[len(n)-1] + n[len(n)-1]
    else:
        w = w + n[len(n)-1] + str(licznik)



    print(w)