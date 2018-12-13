import fun_mac

A = fun_mac.random_randint_m(5, 5, 1)
B = fun_mac.make_m(5, 1, 0)
fun_mac.print_m(A)
print("")
fun_mac.print_m(B)
print("")

C = fun_mac.expand_m(A, B, 3)
fun_mac.print_m(C)
print("")

C = fun_mac.expand_m(C, B, 0)

fun_mac.print_m(C)


