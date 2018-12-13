"""
SPOJ 8090
Dzielenie pizzy

12.3456 > 2 > 5 >
1.23456 > 1 > 4 >
0.12345 > 1 > 4 >

"""
def drukuj_wynik(t):
    t[0] = int(t[0] * 10**3) / 10**3

    print("{0} {1}".format(t[0], t[1]))

D = input()
for d in range(int(D)):

    dane = input()
    dane = dane.split(" ")
    for i in range(len(dane)):
        dane[i] = int(dane[i])


    import math

    if dane[1] % 2 == 0:
        dane[0] *= math.pi/dane[1]
        dane[1] //= 2
    else:
        dane[0] *= math.pi/dane[1]/2



    drukuj_wynik(dane)