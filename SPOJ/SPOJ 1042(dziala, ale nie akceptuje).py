"""
SPOJ 1042
Ztransponuj macierz
"""

wymiar = input()
wymiar = wymiar.split(" ")
for i in range(len(wymiar)):
    wymiar[i] = int(wymiar[i])

wartosci = [0] * (wymiar[0] * wymiar[1])

for m in range(wymiar[0]):
    war = input()
    war = war.split(" ")
    for i in range(len(war)):
        war[i] = int(war[i])

    for n in range(wymiar[1]):
        wartosci[m*wymiar[1] + n] = war[n]

print(wartosci)