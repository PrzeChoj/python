import fun_mac

A = fun_mac.random_randint_m(10, 20, 0, 10)

print(("A:"))
fun_mac.print_m(A)
V = fun_mac.average_vector_m(A)
Ar = fun_mac.expand_m(A, V, 0)

print("")

fun_mac.print_m(fun_mac.shifting_rows_by_avr(A))