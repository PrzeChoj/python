import fun_mac

A = fun_mac.make_m(3)
fun_mac.read_m(A, "magic_sq1.txt")

fun_mac.print_m(A)

print(fun_mac.is_magic_sq_m(A))


print("")


B = fun_mac.make_m(3)
fun_mac.read_m(B, "magic_sq2.txt")

fun_mac.print_m(B)

print(fun_mac.is_magic_sq_m(B))

print("")


C = fun_mac.make_m(7)
fun_mac.read_m(C, "magic_sq3.txt")

fun_mac.print_m(C, 6)

print(fun_mac.is_magic_sq_m(C))

print("")



#2

import fun_mac

A = fun_mac.random_uniform_m(5, 600, -50, 50)

V = fun_mac.average_vector_m(A)

#fun_mac.print_m(A)
#print("")

fun_mac.print_m(fun_mac.expand_m(A, V, 0), 4)



