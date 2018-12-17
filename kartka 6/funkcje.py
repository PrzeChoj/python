def konkatenacja(A, B):
    """
    Funkcja laczy 2 listy w jedna, dluzsza
    """
    C = [None] * (len(A) + len(B))

    for i in range(len(A)):
        C[i] = A[i]
    for i in range(len(B)):
        C[i+len(A)] = B[i]

    return C

def rep_times(t, d = 2):
    """
    Funkcja zwraca tablice z elementami danej tablicy
        powturzone ilosc razy rowna wartosci 2-go parametru
    """
    T = [None] * (len(t) * d)

    for i in range(d):
        for j in range(len(t)):
            T[i*len(t) + j] = t[j]

    return T

def rep_each(t, d = 2):
    """
    Funkcja zwraca tablice w ktorej kazdy element z danej tablicy
        jest powtorzony d razy
    """
    T = [None] * (len(t)*d)

    for i in range(len(t)):
        for j in range(d):
            T[i * d + j] = t[i]

    return T
