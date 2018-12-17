def is_symetric_m(A):
    if len(A) != len(A[0]): return False

    for i in range(len(A)):
        for j in range(i, len(A[0])):
            if A[i][j] != A[j][i]: return False
    return True