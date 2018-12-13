"""
SOPJ 708
Podaj pierwszy index dla ktorego wyracem ciagu jest 1
"""
D = int(input())
for d in range(D):
    s = int(input())
    x = s
    ilosc = 0

    while x != 1:
        if x % 2 == 1:
            x = 3*x + 1
        else:
            x = x/2
        ilosc += 1

    print(ilosc)