"""
SPOJ 806
wiatraczki rekurencyjne
"""

def wiatraczki(r):
    kierunek = False

    if r > 0: kierunek = True
    else: r = -r

    wiatrak = [[None]*(2*r) for i in range(2*r)]
    if r == 1:
        for i in range(2*r):
            for j in range(2*r):
                wiatrak[i][j] = "*"
        return wiatrak

    wiatrak_last = wiatraczki(r-1)

    for i in range(1, 2*r-1):
        for j in range(1, 2*r-1):
            wiatrak[i][j] = wiatrak_last[i-1][j-1]

    if not(kierunek):
        for i in range(1, r):
            wiatrak[i][0] = "."
            wiatrak[2*r-1][i] = "."
            wiatrak[2*r-i-1][2*r-1] = "."
            wiatrak[0][2*r-i-1] = "."

        for i in range(r, 2*r):
            wiatrak[i][0] = "*"
            wiatrak[2*r-1][i] = "*"
            wiatrak[2 * r - i - 1][2 * r - 1] = "*"
            wiatrak[0][2 * r - i - 1] = "*"

    else:
        for i in range(1, r):
            wiatrak[0][i] = "."
            wiatrak[i][2*r-1] = "."
            wiatrak[2*r-1][2*r-i-1] = "."
            wiatrak[2*r-i-1][0] = "."

        for i in range(r, 2*r):
            wiatrak[0][i] = "*"
            wiatrak[i][2*r-1] = "*"
            wiatrak[2 * r - 1][2 * r - i - 1] = "*"
            wiatrak[2 * r - i - 1][0] = "*"

    return wiatrak

def drukuj(t):
    for i in range(len(t[0])):
        for j in range(len(t)):
            print(t[i][j], end="")
        print("")

while True:
    r = int(input())

    if r == 0: break

    drukuj(wiatraczki(r))
