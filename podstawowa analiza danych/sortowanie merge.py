def insertion_sort(t):
    """
    :param tablica:
    :return posortowana tablica:
    sortowanie przez wstawianie
    dziala w miejscu
    """
    n = len(t)
    for i in range(1, n):
        tcur = t[i]
        j = i
        while j > 0:
            if t[j-1] <= tcur: break
            t[j] = t[j-1]
            j -= 1
        t[j] = tcur
    return t

def insertion_arg_sort(t):
    """
    :param tablica:
    :return posortowana tablica:
    sortowanie przez wstawianie, permutacja sortujaca
    """
    n = len(t)
    o = list(range(n)) # 0, 1, 2, ...
    for i in range(1, n):
        ocur = t[o[i]]
        j = i
        while j > 0:
            if t[o[j-1]] <= t[ocur]: break
            o[j] = o[j-1]
            j -= 1
        t[o[j]] = ocur
    return o

#def algorytm_Shella(t):

def is_sorted(t):
    for i in range(len(t)-1):
        if not t[i] <= t[i+1]:
            return False
    return True


def mergesort(t):
    """ sortowanie przez scalanie (w miejscu)"""

    def _merge(t, i0, i1, i2):
        """
        t[i0]<=...<=t[i1-1]
        t[i1]<=...<=t[i2-1]
        --->
        t[i0]<=t[i0+1]<=...<=t[i2-1]
        """

        l = i0
        r = i1

        i = 0
        while l < i1 and r < i2:
            if t[l] <= t[r]:
                aux[i] = t[l]
                l += 1
            else:
                aux[i] = t[r]
                r += 1
            i += 1

        while l < i1:
            aux[i] = t[l]
            l += 1
            i += 1
        while r < i2:
            aux[i] = t[r]
            r += 1
            i += 1

        for i in range(i0, i2):
            t[i] = aux[i - i0]


    def _mergesort(t, i0, i2):
        # sortuje t[i0],t[i0+1],...,t[i2-1]
        if i2 - i0 <= 1:
            return
        else:
            i1 = (i2 + i0) // 2
            _mergesort(t, i0, i1)  # t[i0]<=...<=t[i1-1]
            _mergesort(t, i1, i2)  # t[i1]<=...<=t[i2]
            _merge(t, i0, i1, i2)

    aux = [0] * len(t)
    _mergesort(t, 0, len(t))
    return t

t = [None] * 100000

with open("Liczby.txt", "r") as Liczby:
    for i in range(100000):
        t[i] = float(Liczby.readline())

t = mergesort(t)

with open("sorted.txt", "w") as wynik:
    for i in range(100000):
        wynik.write(str(t[i]) + "\n")
