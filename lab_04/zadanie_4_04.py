import fun_mac
import math
import matplotlib.pylab as plt

def wczytanie():
    table = []
    with open("iris.csv", "r") as dane:
        for line in dane:
            table.append(line.split(","))
            for i in range(4):
                table[len(table) - 1][i] = float(table[len(table) - 1][i])

    table = fun_mac.transpose_m(table)
    return table

def druk_do_pliku(table, av):
    plt.figure(figsize=[12, 6], dpi=72)

    plt.subplot(1, 2, 1)
    for i in range(50):
        plt.scatter(table[0][i], table[2][i], color = "green", alpha=0.3)
    for i in range(50, 100):
        plt.scatter(table[0][i], table[2][i], color = "blue", alpha=0.3)
    for i in range(100, 150):
        plt.scatter(table[0][i], table[2][i], color="red", alpha=0.3)

    for i in range(3):
        plt.plot(av[0][i], av[2][i], markersize=25, color="#00000055", marker='o', linestyle='')

    plt.subplot(1, 2, 2)
    for i in range(50):
        plt.scatter(table[1][i], table[3][i], color="green", alpha=0.3)
    for i in range(50, 100):
        plt.scatter(table[1][i], table[3][i], color="blue", alpha=0.3)
    for i in range(100, 150):
        plt.scatter(table[1][i], table[3][i], color="red", alpha=0.3)

    for i in range(3):
        plt.plot(av[1][i], av[3][i], markersize=25, color="#00000055", marker='o', linestyle='')


    plt.suptitle('Irysy')
    plt.savefig("output3.png")

def srednie(T):
    out = [ [0] * 3 for i in range(4) ]

    for i in range(4):
        for j in range(3):
            sr = 0
            for k in range(50):
                sr += T[i][k + j*50]
            out[i][j] = sr/50
    return out

def euk(zero, p):
    suma = 0
    for i in range(4):
        suma += (p[i]-zero[i])**2
    return math.sqrt(suma)



iris = wczytanie()
t_iris = fun_mac.transpose_m(iris)
"""
iris:
5.1 4.9 ...
3.5 3.0 ...
1.4 1.4 ...
0.2 0.2 ...
"""

sr_m = srednie(iris)
t_sr_m = fun_mac.transpose_m(sr_m)
"""
sr_m:
5.0059 5.936 6.5879
3.428  2.77  2.9739
1.462  4.26  5.5519
0.2459 1.325 2.0259
"""
#sr_m[0] = [5, 3.4, 1.4, 0.25]
d = [[ [0]*50 for i in range(3) ] for j in range(3)]
"""
d:
Sa takie 3:
0.14 0.44 0.41 ...
3.98 3.57 4.13 ...
5.23 4.13 5.26 ...
"""
for k in range(3):
    for i in range(3):
        for j in range(50):
            d[k][i][j] = euk(t_sr_m[k], t_iris[i*50 + j])

jaki_kwiat = [ [None]*50 for i in range(3) ]

for k in range(3):
    for j in range(50):
        mini = math.inf
        kwiat = None
        for i in range(3):
            if d[k][i][j] < mini:
                mini = d[k][i][j]
                jaki_kwiat[k][j] = i


fun_mac.print_m(jaki_kwiat)


#druk_do_pliku(iris, sr_m)


