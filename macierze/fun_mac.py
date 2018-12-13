"""
error in print_m

try code:

import fun_mac
macroyal jalapenio
mac = fun_mac.make_m(5, 3)
fun_mac.read_m(mac)
fun_mac.print_m(mac, None, "inp.txt.txt")
"""
def print_m(t, d = None, f = None):
    """
    Funkcja dostaje macierz t
    Funkcja wydrukuje macierz na terminal, lub do pliku
        podanego jako 3 argument funkcji
    Jesli podamy funkcji liczbe jako 2 argument,
         wydrukuje maksymalnie taka ilosc znakow w kazdej komurce
    Funkcja dostosowuje dlugosci wartosci w macierzy
    """
    if d != None:
        for i in range(len(t)):
            for j in range(len(t[0])):
                t[i][j] = (int(t[i][j] * 10**d)/10**d)
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
                    print(" " * (length[j] - len(str(t[i][i]))), end = "")
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
                    m[i][j] = int(liczby[j])

def random_uniform_m(m, n = None, a = 0, b = 1):
    """
    returns a matrix m X n
    with a random float values x so that: a(=0) <= x <= b(=1).
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
    Returns a sum of 2 matrix
    If matrixes are unaddable, returns None
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
    Returns changed matrix with all the values turned into minus itself
    """
    nA = make_m(len(A), len(A[0]))
    for i in range(len(nA)):
        for j in range(len(nA[0])):
            nA[i][j] = -A[i][j]
    return nA

def sub_m(A, B):
    """
    Returns a matrix C that for every i, j: C[i][j] = A[i][j] - B[i][j]
    If matrixes are unsubstractable, returns None
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
    Returns matrix transposed to A
    """
    if type(A[0]) != type([0, 0]):
        At = make_m(1, len(A))
        for i in range(len(A)):
            At[0][i] = A[i]

    else:
        At = make_m(1, len(A))
        for i in range(len(A)):
            for j in range(len(A[0])):
                At[j][i] = A[i][j]

    return At

def track_m(A):
    """
    Function returns track of matrix.
    If matrix is not squared, returns None
    """
    if len(A) != len(A[0]):
        return None

    tr = 0
    for i in range(len(A)):
        tr += A[i][i]

    return tr

def is_symetric_m(A):
    """
    Function returns True, when given matrix is symetrical
    """
    if len(A) != len(A[0]): return False

    for i in range(len(A)):
        for j in range(len(A[0]) - i):
            if A[i][j] != A[len(A) - i - 1][len(A[0]) - j - 1]: return False
    return True


def diagonal_m(A):
    """
    Function returns array that has values of given matrix on diagonal in itself
    Returns None if matrix is not squared
    """
    if len(A) != len(A[0]): return None
    d = [None] * len(A)

    for i in range(len(A)):
        d[i] = A[i][i]

    return d

def multiplication_m(A, k = None):
    """
    Function is returning a multiplication of matrix and matrix
        or matrix and scalar.
    If 2nd argument is missing, multiplies matrix by itself.
    If multiplication is impossible, returns None
    """
    if k == None: k = A

    if type([[0], [0]]) == type(k):

        #multiplication of 2 vectors
        if type(A[0]) != type([0, 0]):
            if len(k[0]) != len(A): return None
            C = make_m(len(A), len(k[0]))
            for i in range(len(C)):
                for j in range(len(C[0])):
                    C[i][j] = A[i] * k[0][j]
            return C

        #both arguments are matrixes
        if len(A[0]) != len(k): return None
        C = make_m(len(A), len(k[0]))
        for i in range(len(C)):
            for j in range(len(C[0])):
                sum = 0
                for m in range(len(k)):
                    sum += A[i][m] * k[m][j]

                C[i][j] = sum
        return C

    #multiplication of matrix by scalar
    if str(type(3)) == str(type(k)) or str(type(3.3)) == str(type(k)):
        B = [ [None] * len(A[0]) for i in range(len(A)) ]
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[i][j] = A[i][j] * k
        return B
    else: return None

def expand_m(A, b, t = None):
    """
    Function makes new matrix that is matrix A expanded by vector b
        placed on place t(in case of lack of this parameter
        it is placed on the end)
    If vector is in inappropriate length, function returns None
    If vector if in such a form: [a, b, c, ...]: where a, b, c,... are numbers,
        matrix is expanded by row.
        If vector is in form: [ [a, b, c,... ] ], it is expanded by column.
    """
    #expanding by row
    if type(b[0]) == type([0, 0]) and len(b[0]) != 1:
        if t == None: t = len(A)
        if len(b[0]) != len(A[0]): return None

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


    #expanding by column
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
    Function returns matrix without some of the rows or columns
        (1 in conjecture)
    If 3rd parameter is missing - conjecture same as 2nd
    If 2nd parameter is missing - conjecture last
    Remember that columns and rows are numbered from 0, 1, 2,...
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
    Function returns True if matrix is magic square and
        returns False otherwise
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

def average_vector_m(A, o = 0):
    """
    Function returns vector that i-value contain average value for
        numbers in i-row(o = 0), or i-colum(o = 1)
    """
    if o ==0:
        V = make_m(len(A), 1)

        for i in range(len(A)):
            sum = 0
            for j in range(len(A[0])):
                sum += A[i][j]
            V[i] = sum/len(A[0])
        return V

def statistic_m(A, d = None):
    """
    Function returns matrix which for every raw gives 5 atributes:
        minimum, 1ts quartile, median, 3rd quartile, max
    Gives it with precision of d
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
