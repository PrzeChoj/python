
m = [ [1] * 5 for i in range(5) ]


tr = 0
for i in range(len(m)):
    tr += m[i][i]

print(tr)