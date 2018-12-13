"""
SPOJ 439
wykonaj mnozenie 2 liczb
"""

D = int(input())            #Petla dla zadania
for d in range(D):

    s  = input()            #wczytanie liczb
    ss = s.index(" ")       #znalezienie przerwy miedzy nimi

    a = int(s[0:ss])        #wyznaczenie pierwszej
    b = int(s[ss+1:len(s)]) #wyznaczenie drugiej

    print(a)
    print(b)

    print(a*b)              #wypisanie wyniku mnozenia