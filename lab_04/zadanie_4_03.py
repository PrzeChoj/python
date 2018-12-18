import fun_mac
import math

def wczytanie():
    table = []
    with open("iris.csv", "r") as dane:
        for line in dane:
            table.append(line.split(","))
            for i in range(4):
                table[len(table) - 1][i] = float(table[len(table) - 1][i])

    table = fun_mac.transpose_m(table)
    return table

def zapis(A, C):
    import matplotlib.pylab as plt
    plt.figure(figsize=[8, 4], dpi=72)
    plt.subplot(1, 2, 1)
    for i in range(len(A[0])):
        plt.scatter(A[0][i], A[1][i], color="green")
    plt.subplot(1, 2, 2)
    for i in range(len(C[0])):
        plt.scatter(C[0][i], C[1][i], color="green")

    plt.savefig("output1.png")

def mnoz(B, A):
    C = [ [0] * len(A[0]) for i in range(len(B)) ]

    for i in range(len(B)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                C[i][j] += B[i][k]*A[k][j]
    return C

def wycentrowanie(A):
    srx = 0
    sry = 0
    for i in range(len(A[0])):
        srx += A[0][i]
        sry += A[1][i]
    srx, sry = srx/i, sry/i

    for i in range(len(A[0])):
        A[0][i] -= srx
        A[1][i] -= sry

def obrot(theta):
    return [ [math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)] ]

def obrazek():
    B = obrot(math.pi / 3)

    C = mnoz(B, A)

    B1 = [[5, 0], [0, 5]]
    C1 = mnoz(B1, A)

    zapis(A, C, C1)

def wariancja(x):
    sr = 0
    for i in range(len(x)):
        sr += x[i]
    sr /= (i+1)

    war = 0
    for i in range(len(x)):
        war += (x[i]-sr)**2
    war /= len(x)

    return war

t = wczytanie()

A = [ [0] * len(t[0]) for i in range(2) ]

for i in range(2):
    for j in range(len(t[0])):
        A[i][j] = t[2*i][j]

wycentrowanie(A)

#obrazek()

k = 100
war = []
for i in range(k):
    the = i*math.pi/k

    B = obrot(the)

    C = mnoz(B, A)
    war.append(wariancja(C[0]))

zapis(A, war)
