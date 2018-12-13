"""
gra losowa:
2 graczy gra miedzy soba. Wynik jest losowy 50%.
Gdy graczy wygrywa-zdobywa punkt
Gdy gracz z wieksza iloscia punktow sie zmienia, nawywamy to przebiciem.
Policz wartosc oczekiwana ilosci przebic w zaleznosci od n-ilosci rozegranych gier
"""
import random

def ile_przebic(n):
    punkty_pierwszego = 0
    punkty_drugiego = 0
    przewaga = 0
    przewaga_poprzednia = 0
    przebicia = 0

    for i in range(n):
        r = random.randint(0, 1)
        if r == 0:
            punkty_pierwszego += 1
        else:
            punkty_drugiego += 1

        if przewaga == 0 and ((punkty_drugiego - punkty_pierwszego > 0 and przewaga_poprzednia == 1) or (punkty_drugiego - punkty_pierwszego < 0 and przewaga_poprzednia == 2)):
            przebicia += 1

        przewaga_poprzednia = przewaga

        if punkty_pierwszego > punkty_drugiego:
            przewaga = 1
        elif punkty_pierwszego < punkty_drugiego:
            przewaga = 2
        else:
            przewaga = 0

    return przebicia

sredni = [0] * 100
M = 10000
out = open("prawdopodobienstwo.txt", "w")

for j in range(1, len(sredni), 2):
    for i in range(M):
        sredni[j] += ile_przebic(j)
    sredni[j] = sredni[j]/M

    print(sredni[j], file = out)

    print(f"dla j = {j}: {sredni[j]}")

out.close()

print(sredni)
