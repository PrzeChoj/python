"""
SPOJ 609
Znajdz pole kola na przecieciu 2 identycznych sfer
"""
import math

#wczytanie danych
s = input()

#wskazanie spacji w s
ss = s.index(" ")
r = float(s[0:ss])        #wyznaczenie 1 liczby
d = float(s[ss+1:len(s)]) #wyznaczenie 2 liczby

#wzor na promien tego kola - pitagoras
rd = math.sqrt(r ** 2 - (d/2) ** 2)

#wypisanie pola tego kola
print(math.pi * ((rd) ** 2))