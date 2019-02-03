"""
SPOJ 17132
dla ciagu liczb zamienic powtarzajace sie na nowe
"""
D = int(input())
for d in range(D):
    n = int(input())
    c = input()
    ciag = c.split(" ")

    tablica_bedacych = [False] * (1000000)
    czy = True
    for i in range(len(ciag)):
        ciag[i] = int(ciag[i])
        if tablica_bedacych[ciag[i]] == True:
            czy = False
        tablica_bedacych[ciag[i]] = True

    if czy:
        print("OK")
    else:

        flaga = 1

        nowa_tablica_bedacych = [False] * (1000000)
        for i in range(len(ciag)):
            if nowa_tablica_bedacych[ciag[i]] == True:
                for j in range(flaga, len(tablica_bedacych)):
                    if tablica_bedacych[j] == False:
                        flaga = j + 1
                        ciag[i] = j
                        break
            else:
                nowa_tablica_bedacych[ciag[i]] = True

        for i in range(len(ciag)):
            print(ciag[i], end = " ")

"""
To rozwiazanie zabiiera zbyt duzo pamieci,
    podjalem probe uproszcznia go, ale bezskutecznie :(
"""

"""
#SPOJ 17132
#dla ciagu liczb zamienic powtarzajace sie na nowe

D = int(input())
for d in range(D):
    n = int(input())
    c = input()
    ciag = c.split(" ")

    for i in range(len(ciag)):
        ciag[i] = int(ciag[i])

    tablica_bedacych = []

    for i in range(len(ciag)):
        jest_nowy = True
        for j in range(i):
            if ciag[j] == ciag[i]: jest_nowy = False
        if jest_nowy:
            tablica_bedacych.append(ciag[i])
        
    print(tablica_bedacych)
    tablica_bedacych.sort()
    # 1 3 4 5 14
    flaga = 1
    
    czy_byl = [False] * len(tablica_bedacych)
    for i in range(len(ciag)):
        for j in range(len(tablica_bedacych)):
            if ciag[i] == tablica_bedacych[j]:
                if czy_byl[j] == False:
                    czy_byl[j] = True
                else:
                    for k in range(flaga, len(ciag)):
"""