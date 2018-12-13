"""
SPOJ 751
5, 6,   55, 56, 65, 66,   555, 556, 565, 566, 655, 656, 665, 666,   5555, 5556, 5565, 5566, 5655, 5656, 5665, 5666, 6555, ...
"""

n = int(input())  #23
ilosc = 0
licznik = 1

while True:
    if ilosc >= n: break

    ilosc_przed = ilosc
    ilosc += 2**licznik
    licznik += 1
licznik -= 1

print(f"ilosc liczb krotrzych od {n}-tej: {ilosc_przed}\n{n}-ta liczba ma {licznik} cyfr\n{n}-ta liczba jest {n-ilosc_przed}-ta liczba swojej dlugosci")
print(ilosc_przed, 2**(licznik-1))