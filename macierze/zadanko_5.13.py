import fun_mac

A = fun_mac.random_uniform_m(5, 600, -50, 50)

V = fun_mac.average_vector_m(A)

#fun_mac.print_m(A, 4)
#print("")

fun_mac.print_m(fun_mac.expand_m(A, V, 0), 4)