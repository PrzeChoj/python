"""
Ktore z podanych liczb sa pierwsze?
"""
import math

def pierwsze(k):
    gr = math.sqrt(k)
    out = [True] * k
    gr = math.ceil(gr)

    for i in range(2, gr):
        if out[i]:
            for j in range(2, k):
                try:
                    out[i*j] = False
                except: continue

    out[1] = " "
    for i in range(2, k):
        if out[i]: out[i] = "O"
        else: out[i] = "."

    return out

liczby = []
D = int(input())
for d in range(D):
    liczby.append(int(input()))

maks = max(liczby)

pierwsze_do_maks = pierwsze(maks + 2)

for i in range(D):
    if pierwsze_do_maks[liczby[i]] == "O":
        print("TAK")
    else:
        print("NIE")
