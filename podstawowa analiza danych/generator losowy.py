"""
Generuj liczby pseudolosowy na podstawie ziarna
"""

m = 2**31 - 1
a = 1103515245
c = 12345

s = int(input("Podaj ziarno: "))
n = int(input("Podaj ilosc liczb do wygenerowania: "))

with open("Liczby.txt", "w") as f:
    for i in range(n):
        s = (a*s + c) % m
        f.write(f"{10*s/m}\n")
