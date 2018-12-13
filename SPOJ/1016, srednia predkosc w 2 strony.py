"""
SPOJ 1016
policz srodnia predkosc w 2 strony
"""
D = int(input())
for d in range(D):

    s  = input()                #wczytanie predkosci czesciowych
    ss = s.index(" ")           #znalezienie indexu spacji

    v1 = int(s[0:ss])           #wygrzebanie pierwszej predkosci
    v2 = int(s[ss+1:len(s)])    #wygrzebanie drugiej   predkosci

    print(int(2*v1*v2/(v1+v2))) #druk wyniku