def is_symetric_m(A):
    if len(A) != len(A[0]): return False

    for i in range(len(A)):
        for j in range(len(A[0]) - i):
            if A[i][j] != A[len(A) - i - 1][len(A[0]) - j - 1]: return False
    return True