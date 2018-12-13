"""
SOPJ 978
"""

s = input()

liczby = s.split(" ")
for i in range(len(liczby)):
    print(liczby[len(liczby)-i-1], end = " ")

