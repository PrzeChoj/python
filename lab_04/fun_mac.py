"""
error in print_m

try code:
    import fun_mac
    macroyal jalapenio
    mac = fun_mac.make_m(5, 3)
    fun_mac.read_m(mac)
    fun_mac.print_m(mac, None, "inp.txt.txt")

    standarization_m
    I don't know if it works ¯\_(ツ)_/¯


statistic_m does not gives answer with given precision
"""
def print_m(A, d = None, f = None):
    """
    Funkcja dostaje macierz t
    Funkcja wydrukuje macierz na terminal, lub do pliku
        podanego jako 3 argument funkcji
    Jesli podamy funkcji liczbe jako 2 argument,
         wydrukuje maksymalnie taka ilosc znakow w kazdej komurce
    Funkcja dostosowuje dlugosci wartosci w macierzy
    """
    t = copy_m(A)

    if d != None:
        for i in range(len(A)):
            for j in range(len(A[0])):
                t[i][j] = (int(A[i][j] * 10**d)/10**d)


    if type(t) != type([ [0, 0], [0, 0] ]):
        print("It's not a matrix!\nIt is:")
        print(t)
        return

    length = [0] * len(t[0])
    for j in range(len(t[0])):
        for i in range(len(t)):
            if len(str(t[i][j])) > length[j]: length[j] = len(str(t[i][j]))

    if f == None:
        for i in range(len(t)):
            for j in range(len(t[0])):
                print(t[i][j], end=" ")
                print(" " * (length[j] - len(str(t[i][j]))), end = "")
            print("")

    else:
        with open(f, "a") as out:
            for i in range(len(t)):
                for j in range(len(t[0])):
                    print(" " * (length[j] - len(str(t[i][i]))), end = "", file = out)
                    print(t[i][j], end=" ", file = out)
                print("", file = out)

def read_m(m, f = None, l = 0):
    """
    Funkcja dostaje macierz m
    Funkcja wczyta z klawiatury (badz z pliku jesli podany na 2 argument)
        wardosci i wpisze je do macierzy
    Jesli wczytujesz z pliku nie od poczadku, jako 3 argument
        podaj linijke od ktorej zaczyna sie plik
    """
    if f == None:
        for i in range(len(m)):
            liczby = input()
            liczby = liczby.split(" ")

            for j in range(len(m[0])):
                m[i][j] = int(liczby[j])
    else:
        with open(f, "r") as inpu:
            for i in range(l):
                liczby = inpu.readline()

            for i in range(len(m)):
                liczby = inpu.readline()
                liczby = liczby.split(" ")

                for j in range(len(m[0])):
                    m[i][j] = float(liczby[j])

def random_uniform_m(m, n = None, a = 0, b = 1):
    """
    returns a matrix m X n
        with a random float values x so that: a(=0) <= x <= b(=1).
    Zwraca macierz wielkosci m na n wypelniona wartosciami
        float z przedzialu <a, b>
    Jesli pominiemy 2 wspolrzedna, tworzy macierz kwadratowa.
    """
    if n == None: n = m

    import random
    t = make_m(m, n)
    for i in range(m):
        for j in range(n):
            x = random.uniform(a, b)
            t[i][j] = x
    return t

def random_randint_m(m, n = None, a = -10, b = 10):
    """
    returns a matrix m X n
        with a random integer values x so that: a(=0) <= x <= b(=1)
    Zwraca macierz wielkosci m na n wypelniona losowymi intami
        z przedzialu <a, b>
    Jesli pominiemy 2 wspolrzedna, tworzy macierz kwadratowa.
    """
    if n == None: n = m

    import random
    t = make_m(m, n)
    for i in range(m):
        for j in range(n):
            x = random.randint(a, b)
            t[i][j] = x
    return t

def make_m(m, n = None, w = None):
    """
    Funkcja zwraca macierz o m kolumnach i n wierszach.
    Jesli pominiemy 2 wspolrzedna, tworzy macierz kwadratowa.
    Macierz jest Wypelniona 3. argumentem, domyslnie None
    """
    if n == None: n = m

    return [ [w] * n for i in range(m) ]

def sum_m(A, B):
    """
    Zwraca sume 2 macierzy
    Jesli macierze sa niedodawalne, zwraca None
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None

    C = make_m(len(A), len(A[0]), 0)

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]

    return C

def negativ_m(A):
    """
    Zwraca macierz z wartosciami przeciwnymi do macierzy podanej
    """
    nA = make_m(len(A), len(A[0]))
    for i in range(len(nA)):
        for j in range(len(nA[0])):
            nA[i][j] = -A[i][j]
    return nA

def sub_m(A, B):
    """
    Zwraca macierz C ktorej dla kazdego elementu i, j: C[i][j] = A[i][j] - B[i][j]
    Jesli macierze sa nieodejmowalne, zwraca None
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    C = make_m(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def transpose_m(A):
    """
    Zwraca macierz transponowana do podanej
    """

    #Jesli podana macierz to vektor
    if type(A[0]) != type([0, 0]) or len(A[0]) == 1:
        At = make_m(1, len(A))
        for i in range(len(A)):
            At[0][i] = A[i]

    else:
        At = make_m(len(A[0]), len(A))
        for i in range(len(A)):
            for j in range(len(A[0])):
                At[j][i] = A[i][j]

    return At

def copy_m(A):
    """
    Zwraca kopie macierzy A
    """
    return transpose_m(transpose_m(A))

def track_m(A):
    """
    Zwraca slad podanej macierzy
    Jesli macierz nie jest kwadratowa, zwraca None
    """
    if len(A) != len(A[0]):
        return None

    tr = 0
    for i in range(len(A)):
        tr += A[i][i]

    return tr

def is_symetric_m(A):
    """
    Zwraca True, jesli macierz jest symetryczna
    """
    if len(A) != len(A[0]): return None

    for i in range(len(A)):
        for j in range(i, len(A[0])):
            if A[i][j] != A[j][i]: return False
    return True


def diagonal_m(A):
    """
    Zwraca tablice o wartosciach z diagonali danej macierzy
    Jesli macierz nie jest kwadratowa, zwraca None
    """
    if len(A) != len(A[0]): return None
    d = [0] * len(A)

    for i in range(len(A)):
        d[i] += A[i][i]

    return d

def multiplication_m(A, k = None):
    """
    Zwraca wynik mnozenia macierzy z macierza, albo macierzy ze skalarem
    Jesli nie podajemy przez co pomnozyc, mnozy maciez przez sama siebie
    Jesli mnozenie jest niemozliwe, zwraca None
    """
    if k == None: k = A

    if type([[0], [0]]) == type(k):

        #mnozenie 2 vektorow
        if type(A[0]) != type([0, 0]):
            if len(k[0]) != len(A): return None
            C = make_m(len(A), len(k[0]))
            for i in range(len(C)):
                for j in range(len(C[0])):
                    C[i][j] = A[i] * k[0][j]
            return C

        #mnozenie 2 macierzy
        if len(A) != len(k[0]): return None
        C = make_m(len(A), len(k[0]))
        for i in range(len(C)):
            for j in range(len(C[0])):
                sum = 0
                for m in range(len(k)):
                    sum += A[i][m] * k[m][j]

                C[i][j] = sum
        return C

    #mnozenie macierzy przez skalar
    if str(type(3)) == str(type(k)) or str(type(3.3)) == str(type(k)):
        B = [ [None] * len(A[0]) for i in range(len(A)) ]
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[i][j] = A[i][j] * k
        return B
    else: return None

def expand_m(A, b, t = None):
    """
    Funkcja tworzy nowa macierz, ktora jest dana macierza rozszezona o
        wektor b postawiony na t-tym miejscy(jesli nie podany jest ten
        parametr, wstawiany jest na koniec)
    Jesli wektor jest nieodpowiedniej dlugosci, zwraca None
    Jesli wektor jest w formie: [a, b, c, ...]: gdzie a, b, c,... to liczby,
        macierz jest powiekrzana o wiersz
    Jesli wektor jest w formie [ [a, b, c,... ] ],
        macierz jest rozszezana o kolumne
    """
    #rozszezanie o wiersz
    if type(b[0]) == type([0, 0]) and len(b[0]) != 1:
        if t == None: t = len(A)
        if len(b[0]) != len(A[0]): return "Rozne dlugosci macierzy!", b

        Ar = make_m(len(A) + 1, len(A[0]))

        for i in range(t):
            for j in range(len(A[0])):
                Ar[i][j] = A[i][j]

        for j in range(len(A[0])):
            Ar[t][j] = b[0][j]

        for i in range(t + 1, len(A) + 1):
            for j in range(len(A[0])):
                Ar[i][j] = A[i - 1][j]

        return Ar


    #rozszezanie o kolumne
    if t == None: t = len(A[0])
    if len(b) != len(A): return None

    Ar = make_m(len(A), len(A[0]) + 1)
    for i in range(len(A)):
        for j in range(t):
            Ar[i][j] = A[i][j]

    for i in range(len(A)):
        Ar[i][t] = b[i]

    for i in range(len(A)):
        for j in range(t + 1, len(A[0]) + 1):
            Ar[i][j] = A[i][j - 1]

    return Ar

def delete_r_c_m(A, n = None, m = None, amount_n = None, amount_m = None):
    """
    Funkcja zwraca dana macierz pomniejszona o niektore z wierszy
        albo kolumn (jedna jesli nie podane)
    Jesli 3. parametr jest pominiety - usuwany jest ten sam, co 2.
    Jesli 2. jest pominiety - usuwa odtatni
    Pamietaj, ze kolumny i wiersze sa numerowane od 0
    """
    if n == None: n = len(A)
    if m == None: m = n
    if amount_n == None: amount_n = 1
    if amount_m == None: amount_m = 1

    Ad = make_m(len(A) - amount_n, len(A[0]) - amount_m)

    for i in range(n):
        for j in range(m):
            Ad[i][j] = A[i][j]

    for i in range(n, len(A) - amount_n):
        for j in range(m, len(A[0]) - amount_m):
            Ad[i][j] = A[i+amount_n][j+amount_m]

    for i in range(n):
        for j in range(m, len(Ad[0])):
            Ad[i][j] = A[i][j + amount_m]

    for i in range(n, len(Ad)):
        for j in range(m):
            Ad[i][j] = A[i + amount_n][j]

    return Ad

def is_magic_sq_m(M):
    """
    Funkcja zwraca True, jesli podana macierz to kwarat magiczny
        False w przeciwnym przypadku
    """
    if len(M) != len(M[0]): return False

    sum = 0
    for i in range(len(M)):
        sum += M[i][i]
    sumt = 0
    for i in range(len(M)):
        sumt += M[i][len(M[0]) - i - 1]

    if sumt != sum: return False

    for i in range(len(M)):
        sumt = 0
        for j in range(len(M[0])):
            sumt += M[i][j]

        if sumt != sum: return False

    for j in range(len(M[0])):
        sumt = 0
        for i in range(len(M)):
            sumt += M[i][j]

        if sumt != sum: return False

    return True

def average_vector_m(A):
    """
    Funkcja zwraca wektor, ktory zawiera srednie wartosci w i-tym wierszu
    """
    V = make_m(len(A), 1)
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[0])):
            sum += A[i][j]
        V[i] = sum/len(A[0])
    return V

def statistic_m(A, d = None):
    """
    Funkcja zwraca macierz, ktora w karzdym wierszu zawiera 5 elementow:
        minimum, 1. kwartyl, mediane, 3. kwartyl, maximum
    Daje je z dokladnoscia d #niegotowe
    """

    if len(A[0]) < 6: return None

    As = make_m(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            As[i][j] = A[i][j]

    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(1, len(A[0])):
                if As[i][k-1] > As[i][k]:
                    As[i][k-1], As[i][k] = As[i][k], As[i][k-1]

    B = make_m(len(A), 5)
    for i in range(len(A)):
        B[i][0] = As[i][0]
        B[i][1] = As[i][len(As[i])//4]
        B[i][2] = As[i][len(As[i]) // 2]
        B[i][3] = As[i][3 * len(As[i]) // 4]
        B[i][4] = As[i][len(As[i])-1]

    return B

def min_m(A):
    import math
    mini = math.inf
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] < mini: mini = A[i][j]
    return mini

def max_m(A):
    import math
    maxi = - math.inf
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > maxi: maxi = A[i][j]
    return maxi

def negative_avr(A, Row = True):
    """
    Funkcja zwraca macierz, ktora zawiera tylko te wiersze z podanej
        macierzy, ktorych srednia arytmetyczna jest nieujemna
    """
    if not Row:
        C = transpose_m(A)
    else:
        C = copy_m(A)
    B = []
    for i in range(len(C)):
        suma = 0
        for j in range(len(C[0])):
            suma += C[i][j]
        if suma >= 0:
            B.append(C[i])
    if Row:
        return B
    else:
        return transpose_m(B)

def standarization_m(A):
    def average(a):
        suma = 0
        for j in range(len(a)):
            suma += a[j]
        return suma/len(a)

    def sd(a, s):
        suma = 0
        for j in range(len(a)):
            suma += (a[j] - s)**2

        return suma/len(a)

    for i in range(len(A)):
        av = average(A[i])
        o = sd(A[i], av)
        for j in range(len(A[0])):
            A[i][j] -= av
            A[i][j] /= o

def shifting_rows_by_avr(A):
    """
    Does work
    Plz do use
    """
    V = average_vector_m(A)
    V = expand_m(A, V, 0)
    I = [ [i] for i in range(len(A)) ]
    V = expand_m(V, I, 1)



    wartownik = len(V) - 1

    for i in range(len(V) - 1, 0, -1):
        for j in range(wartownik):
            if V[j][0] > V[j + 1][0]:
                V[j][0], V[j + 1][0] = V[j + 1][0], V[j][0]
                V[j][1], V[j + 1][1] = V[j + 1][1], V[j][1]
                wartownik = j

    J = make_m(1, len(V[0]), 0)

    V = expand_m(V, J, 0)
    V = delete_r_c_m(V, 0)

    V = expand_m(V, I, 1)

    for i in range(len(V)):
        if V[i][0][0] == V[i][1][0]: continue
        for j in range(i, len(V)):
            if V[j][1][0] == V[i][0][0]:
                for k in range(1, len(V[0])):
                    V[i][k], V[j][k] = V[j][k], V[i][k]


    J = make_m(1, len(V[0]), 0)
    V = expand_m(V, J, 0)
    V = delete_r_c_m(V, 0)
    J = make_m(1, len(V[0]), 0)
    V = expand_m(V, J, 0)
    V = delete_r_c_m(V, 0)


    return V

"""
Ni chy=uja nie wiem, jak to zrobic :(
def how_many_same_m(A):
    ""
    Funkcja zwraca liczbe:
        |{ (i1, ..., im): A[i1][1] = A[i2][i] = ... = A[im][m] }|
        gdzie m = len(A[0)
    ""
    def dla_kazdej_wartosci_w kolumnie(liczik):
        for i1 in range(len(A)):
            if A[i1][j1] == A[i][j]:
                licznik[i1] += 1
                    
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            licznik = [0] * len(A[0])
            for j1 in range(len(A[0])):
                dla_kazdej_wartosci_w_kolumnie(licznik)
                    
    
    
"""
