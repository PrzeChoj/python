import fun_mac

A = fun_mac.random_randint_m(5, 5, 1)
B = fun_mac.make_m(1, 5, 0)
fun_mac.print_m(A)
print("")
fun_mac.print_m(B)
print("")

C = fun_mac.expand_m(A, B, 3)
fun_mac.print_m(C)
print("")

C = fun_mac.expand_m(C, B)

fun_mac.print_m(C)

print("\n")
D = fun_mac.random_randint_m(6, 8)
E = fun_mac.make_m(6, 1, 0)


EX = fun_mac.expand_m(D, E)
fun_mac.print_m(EX)
