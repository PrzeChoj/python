"""
Nie bardzo dziala
Po odhashowaniu 26 i 33 linijki na wykresie powinny pojawiac sie
    proste najleprzego dopasowania, ale z jakiegos powodu
    cos tam sie ewidentnie spierdolilo.
"""
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

def druk_do_pliku(table):
    import matplotlib.pyplot as plt
    plt.figure(figsize=[16, 16], dpi=72)

    #prost = proste(table)

    for n in range(4):
        for m in range(4):

            plt.subplot(4, 4, n * 4 + m + 1)

            for i in range(len(table[0])):
                plt.scatter(table[m][i], table[n][i], color = "green", alpha=0.3)

            #plt.plot(prost[n][m][1] + prost[n][m][0] * min(table[m]), prost[n][m][1] + prost[n][m][0] * max(table[m]), color="red")

    plt.suptitle('Irysy')
    plt.savefig("output.png")

def korelacja_pearsona(dane1, dane2):
    sr1 = srednia(dane1)

    sr2 = srednia(dane2)

    sumx = 0
    sumy = 0
    sum2 = 0
    for i in range(len(dane1)):
        sumx += (dane1[i] - sr1) ** 2
        sumy += (dane2[i] - sr2) ** 2
        sum2 += (dane1[i] - sr1) * (dane2[i] - sr2)

    return sum2 / (math.sqrt(sumx) * math.sqrt(sumy))

def srednia(list):
    sr = 0
    for i in range(len(list)):
        sr += list[i]
    sr /= (i + 1)
    return sr

def mac_kor(dane):
    out = [ [None] * len(dane) for i in range(len(dane)) ]

    for i in range(len(out)):
        for j in range(len(out[0])):
            out[i][j] = korelacja_pearsona(dane[i], dane[j])

    return out

def proste(dane):
    out = [[ ["b", "a"] ] * len(dane) for i in range(len(dane))]

    for i in range(len(out)):
        for j in range(len(out[0])):
            srx = srednia(dane[i])
            sry = srednia(dane[j])

            sum2 = 0
            sumx = 0
            for k in range(len(dane[i])):
                sumx += (dane[i][k] - srx) ** 2
                sum2 += (dane[i][k] - srx) * (dane[j][k] - sry)

            out[i][j][0] = sum2/sumx
            out[i][j][1] = sry - out[i][j][0] * srx

    return out

t = wczytanie()
druk_do_pliku(t)

"""
fun_mac.print_m(mac_kor(t), 6)
print("")
fun_mac.print_m(proste(t))
"""

