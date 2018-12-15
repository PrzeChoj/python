import fun_mac
n = int(input("Podaj wymiar:"))

m = fun_mac.make_m(n)

for i in range(len(m)):
    for j in range(len(m[0])):
        m[i][j] = 1/((i+1) + (j+1) - 1)

fun_mac.print_m(m, 4)