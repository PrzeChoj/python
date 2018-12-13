import fun_mac

A = fun_mac.random_randint_m(5, 6, 0)
fun_mac.print_m(A)
print("")

D = fun_mac.delete_r_c_m(A, 3, 2)

fun_mac.print_m(D)



print("\n\n")



W = fun_mac.make_m(8, 7)
fun_mac.read_m(W, "inp.txt")

fun_mac.print_m(W)
print("")

fun_mac.print_m( fun_mac.delete_r_c_m(W, 5, 4) )
