def multiplication_m(A, k):
    if str(type([[0], [0]])) == str(type(k)):
        k = "macierz"
    if str(type(3)) == str(type(k)) or str(type(3.3)) == str(type(k)):
        B = [ [None] * len(A[0]) for i in range(len(A)) ]
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[i][j] = A[i][j] * k
        return B
    else: return None

import fun_mac
fun_mac.print_m(multiplication_m(fun_mac.make_m(5, 6, 1/5), 1/5), 4)
