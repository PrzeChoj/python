"""
SPOJ 499
wczytac a, b
policzyc ostatnia cyfre liczby a**b
"""

#wczytuje ile razy sie wykona
D = int(input())

#petluje D razy
for c in range(D):
    s = input() #wczytuje s w postaci s = "15 67"
    index = s.index(" ") #index to numer indeksu spacji

    w = 1
    a = int(s[0:index]) #wczytuje a jako pierwsza czesc napisu(przed spacja)
    b = int(s[index+1:len(s)]) #wczytuje b jako druga czesc napisu(za spacja)

    #przedefiniowanie a do jednosci z pierwotnej liczby
    if a > 9:
        a = a%10

    #dla 0, 1, 5 i 6 wynik jest taki sam
    if a == 0 or a == 1 or a == 5 or a == 6:
        w = a
    elif a == 2 or a == 3 or a == 7 or a == 8: #przypadek czterookresowy
        for i in range(b%4):
            w *= a
    else: #przypadek dwuokresowy(dla 4, 9)
        for i in range(b%2):
            w *= a

    #przedefiniowanie w do jednosci
    if w > 9:
       w = w % 10

    print(w)