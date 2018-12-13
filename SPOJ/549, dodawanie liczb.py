"""
SPOJ 549
dodaje liczby oddzielone spacja
"""
D = int(input())

for j in range(D):

    #wczytanie danych
    n = int(input())  #Niepotrzebna informacja
    l = input()

    tablica = l.split(" ")  #tablica liczb calkkowitych

    s = 0 #definiowanie sumy

    for i in range(len(tablica)):
        s += int(tablica[i])  #dodawanie wszystkich int z tablicy

    print(s) #wypisanie wyniku