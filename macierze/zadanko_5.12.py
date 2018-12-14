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




