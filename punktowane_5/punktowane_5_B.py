"""
Labolarotia punktowane wersion 5B
"""

import math
import random

def dist(A):
    D = [ [0]*len(A) for i in range(len(A)) ]
    for i in range(len(D)):
        for j in range(len(D[0])):
            D[i][j] = math.sqrt((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)
    return D

def medioids(D, c):
    """
    c = [ 0, 0, 1, 0, 2, 1, ... ]
    D:
    0 2 4 1 ...
    2 0 1 3 ...
    4 1 0 2 ...
    1 3 2 0 ...
    . . . .
    """
    if len(D) != len(c) or len(D[0]) != len(c): raise Exception("Rozne dlugosci tablic!")

    grupy = []
    for i in range(len(c)):
        czy_byl = False
        for j in range(len(grupy)):
            if c[i] == grupy[j]:
                czy_byl = True
                break
        if not(czy_byl):
            grupy.append(c[i])
    #grupy = [0, 1]

    suma = [0] * len(D)
    medioid = [math.inf] * len(grupy)
    for g in range(len(grupy)):
        for i in range(len(c)):
            if c[i] != grupy[g]: continue
            for j in range(len(c)):
                if c[j] != grupy[g]: continue
                suma[i] += D[i][j]

        for i in range(len(c)):
            if c[i] != grupy[g]: continue
            if suma[i] < medioid[g]:
                medioid[g] = suma[i]
                index = i
        medioid[g] = index

    #print("suma: ", suma)
    #print("grupy: ", grupy)

    return medioid

def updateGroups(D, M):
    """
    M == [ 0, 6 ]
    D:
    0 1    3    1    0 ...
    1 0    2    1.14 1 ...
    3 2    0    3.16 3 ...
    1 1.41 3.16 0    1 ...
    0 1    3    1    0 ...
    . .    .    .    .
    """

    c = [None] * len(D[0])
    for d in range(len(D[0])):
        min_m = math.inf
        for m in range(len(M)):
            if D[d][m] < min_m:
                min_m = D[d][m]
                index = m
        c[d] = index

    return c

def kmedions(A, K, maxiter = 50):
    c = [ random.randint(0, K - 1) for i in range(len(A)) ]

    dystans = dist(A)
    mediony = medioids(dystans, c)

    for i in range(maxiter):
        dystans = dist(A)
        mediony = medioids(dystans, c)
        c = updateGroups(dystans, mediony)

    return c, mediony


A = []
f = open("forest.txt", "r")
for line in f:
    A.append([float(e) for e in str.split(line)])
f.close()
"""
A:
1 3
4 2
2 3
4 3
. .
. .
. .
"""


K = 2

G = kmedions(A, K, 25)

print(G)

zielonych = 0
czerwonych = 0
for i in range(len(G[0])):
    if G[0][i] == 0: zielonych += 1
    if G[0][i] == 1: czerwonych += 1

print("Czerwonych: ", czerwonych)
print("zielonych: ", zielonych)

kolory = ["green", "red"]
#            0      1

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-3, 2.5])
ax.set_ylim([-2, 1.5])

for g in range(K):
    for i in range(len(A)):
        if G[0][i] != g: continue
        plt.scatter(A[i][0], A[i][1], color=kolory[g])


    plt.scatter(A[G[1][g]][0], A[G[1][g]][1], color='black', marker='x')

fig.savefig("rysunek_punktow.png", dpi=90)
