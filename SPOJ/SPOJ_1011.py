"""
SPOJ 1011
kazdej tablicy oddaj jej polowe
"""

D = int(input())
for d in range(D):
    ciag = input()
    for i in range(len(ciag)//2):
        print(ciag[i], end = "")
    print("")
