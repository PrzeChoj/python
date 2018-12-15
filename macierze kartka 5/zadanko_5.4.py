def diagonal_matrix(A):
    if len(A) != len(A[0]): return None
    d = [None] * len(A)

    for i in range(len(A)):
        d[i] = A[i][i]

    return d

import fun_mac
mat = fun_mac.make_m(5, 5, 3)
rand = fun_mac.random_randint_m(5)

fun_mac.print_m(mat)
print("")
fun_mac.print_m(rand)
print("")

print(diagonal_matrix(mat))
print("")
print(diagonal_matrix(rand))
