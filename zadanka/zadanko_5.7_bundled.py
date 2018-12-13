import fun_mac

x = [1, 2, 3]
y = [[4, 5, 6]]

#W = fun_mac.multiplication_m( x, fun_mac.transpose_m(y) ) #nie dziala, bo to wektorki,trzeba poprawic z portfolio
W = fun_mac.multiplication_m(x, y)

fun_mac.print_m(W)
