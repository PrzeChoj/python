"""
SPOJ 496
wczytac liczbe n;
policzyc 2 ostatnie liczby rozwiniecia dzisietnego n!
"""

D = int(input())

for c in range(0, D):

    n = int(input())

    d = 1

    if n > 12:
        print(0, 0)
    else:
        for i in range(1, n+1):
            d *= i
            if d > 99:
                d %= 100

        print((d-d%10)//10, d%10)