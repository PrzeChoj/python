import random
import math
import matplotlib.pyplot as plt

def los(K):
    l = 0
    for k in range(K):
        r = random.uniform(0, 1)
        if r > 1/(math.fabs(l/1000)+2):
            if l < 0:
                l += 1
            elif l > 0:
                l -= 1
            else:
                r = random.randint(0, 1)
                if r:
                    l += 1
                else:
                    l -= 1
        else:
            if l > 0:
                l += 1
            else:
                l -= 1
    return l

fig = plt.figure()
ax = fig.add_subplot(111)

# ustal zakresy na osiach:
#ax.set_xlim([-100, 100]) # zakres wartości na osi OX
#ax.set_ylim([-10, 10]) # zakres wartości na osi OY


K = 1000
D = 10000
dic = {}
dic2 = {}

for d in range(D):
    l = los(K)
    try:
        dic[l] += 1
    except:
        dic[l] = 1
        dic2[l] = l

print(dic)


# rysuje punkty
plt.bar(range(len(dic)), list(dic.values()), align = 'center')
plt.xticks(range(len(dic)), list(dic.keys()))


#ax.axis("equal") # OX i OY proporcjonalne
plt.show()


