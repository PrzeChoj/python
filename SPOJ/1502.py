"""
SPOJ 1502
eazy mnozenie
"""

l = input()
l = l.split(" ")
for i in range(len(l)):
    l[i] = int(l[i])

print(l[0]*l[1] + l[2]*l[3])
