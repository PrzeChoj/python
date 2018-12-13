"""
SPOJ 804
policzyc wyjscie po odejmowaniu 2 liczb na zmiane
"""
D = int(input())            #zapetlenie D razy
for d in range(D):

    s  = input()            #wczytanie danych
    ss = s.index(" ")       #znalezienie spacji

    a = int(s[0:ss])        #wyciagniecie a z danych
    b = int(s[ss+1:len(s)]) #wyciagniecie b z danych

    while a != b:           #petli sie, dopuki sa inne
        if a > b:
            a -= b
        else:
            b -= a

    print(a + b)            #wypisanie wyniku
