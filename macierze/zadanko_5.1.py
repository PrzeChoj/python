
n = int(input("Podaj wymiar:"))

m = [ [0] * n for i in range(n) ]

for i in range(len(m)):
    for j in range(len(m[0])):
        m[i][j] = 1/((i+1) + (j+1) - 1)

for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j], end = " ")
    print("")
