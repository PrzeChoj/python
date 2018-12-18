import fun_mac

def wczytanie():
    table = []
    with open("iris.csv", "r") as dane:
        for line in dane:
            table.append(line.split(","))
            for i in range(4):
                table[len(table) - 1][i] = float(table[len(table) - 1][i])

    table = fun_mac.transpose_m(table)
    return table

def zapis(A, C, C2):
    import matplotlib.pylab as plt
    plt.figure(figsize=[8, 4], dpi=72)
    plt.subplot(1, 3, 1)
    for i in range(len(A)):
        plt.scatter(A[i][0], A[i][1], color="green")
    plt.subplot(1, 3, 2)
    for i in range(len(C)):
        plt.scatter(C[i][0], C[i][1], color="green")
    plt.subplot(1, 3, 3)
    for i in range(len(C2)):
        plt.scatter(C2[i][0], C2[i][1], color="green")
    plt.savefig("output1.png")

def mnoz(A, B):
    C = [ [0] * len(A[0]) for i in range(len(A)) ]

    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]

    return C

def wycentrowanie(A):
    srx = 0
    sry = 0
    for i in range(len(A)):
        srx += A[i][0]
        sry += A[i][1]
    srx, sry = srx/i, sry/i

    for i in range(len(A)):
        A[i][0] -= srx
        A[i][1] -= sry

t = fun_mac.transpose_m(wczytanie())
A = [ [0, 0] for i in range(len(t)) ]

for i in range(len(t)):
    for j in range(2):
        A[i][j] = t[i][2*j]

wycentrowanie(A)

B = [ [1, 5], [1, 0] ]

C = mnoz(A, B)

B = [ [1, 0], [1, 5] ]
C2 = mnoz(A, B)

zapis(A, C, C2)
