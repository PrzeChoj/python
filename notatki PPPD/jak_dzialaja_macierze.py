def drukuj_macierz(t):
    for i in range(len(t)):
        for j in range(len(t[0])):
            print(t[i][j], end=" ")
        print("")

def wczytanie_do_macierzy(m):
    for i in range(len(m)):
        liczby = input()
        liczby = liczby.split(" ")

        for j in range(len(m[0])):
            m[i][j] = int(liczby[j])


n = 3
m = 4
t = [[0]*n for i in range(m)]
print(t)

for i in range(m):
    for j in range(n):
        t[i][j] = str(i+1)+str(j+1)

drukuj_macierz(t)


