import random
k = 150
t = [None] * k
for i in range(k):
    t[i] = random.uniform(0, 1)
print(t)

wartownik = k-1

for i in range(k-1, 0, -1):
    for j in range(wartownik):
        if t[j] > t[j+1]:
            t[j], t[j+1] = t[j+1], t[j]
            wartownik = j

print(t)
