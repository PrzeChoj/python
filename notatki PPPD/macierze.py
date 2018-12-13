n = 5

A = [None] * n
for i in range(n):
    A[i] = [i] * n

print(A)

m = 2
n = 3
B = [ [0] * m ] * n
print(B[0][0])

C = [ [0] * m for i in range(n)]
print(f"{C}\n{B}")

D = [[i+j for j in range(5)] for i in range(4)]
print(D)

print(f"len(D) = {len(D)}")
print(f"len(D)[0] = {len(D[0])}")

