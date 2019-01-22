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

def rm_dup(x):
    """
    funksja przyjmuje liste i zwraca ja z usunietym
        duplikatami-sasiadami
    """
    y = [None] * len(x)

    y[0] = x[0]
    iy = 1
    for i in range(1, len(x)):
        if x[i-1] != x[i]:
            y[iy] = x[i]
            iy += 1

    y2 = [None] * iy

    for i in range(len(y2)):
        y2[i] = y[i]

    return y2

def dominanta(t, a, b):
    """
    Przyjmuje tablice i wartosci a i b
    Tablica musi skladac sie z wartosci calkowitych miedzy a i b
    Funkcja zwracawartosc najczesciej wystepujaca
    Jesli wartosciwystepuja tyle samo razy-zwraza ich srednia rytmetyczna
    """
    assert type(a) == int
    assert type(b) == int
    assert type(t) == list
    assert a <= b

    pomocnicza = [0] * (b-a+1)

    for i in range(len(t)):
        pomocnicza[t[i]] += 1

    max = 0
    index = None
    for i in range(len(pomocnicza)):
        if pomocnicza[i] > max:
            max = pomocnicza[i]
            index = i

    wynik = 0
    ilosc = 0
    for i in range(len(pomocnicza)):
        if pomocnicza[i] == max:
            wynik += a+i
            ilosc += 1

    return wynik/ilosc

def split_codes(x, f):
    """
    2 listy: x-wartosci i f-indexy (0, 1, 2, .., k-1)
    zwraca liste o dlugosci len(f) taka, ze
    o[i] == [ x[i1], x[i2], ... ] tak, ze wszytskie f[in]==i
    """
