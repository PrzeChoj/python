import csv
import math
import copy

A = []
f = open("train_wine.csv", "r")
for row in csv.reader(f):
    for i in range(len(row)):
        row[i] = float(row[i])
    list.append(A, row)     
f.close()

c = []
g = open("train_class.txt", "r")
while True:
	line = g.readline()
	if line == "": 
		break
	x = int(line)
	c.append(x)
g.close()

#sprawdzenie poprawnosci wczytanych zbiorów

def poprawna_macierz(A, k = 2):
	assert type(A) == list
	for i in range(len(A)):
		assert type(A[i]) == list
		assert len(A[i]) == k

poprawna_macierz(A)

def poprawnosc_listy(C, A):
	for i in range(len(C)):
		assert C[i] == 1 or C[i] == 0
	assert len(C) == len(A)

poprawnosc_listy(c, A)

def distance(u, v):
	assert len(u) == len(v)
	m = len(u)
	suma = 0
	for i in range(m):
		suma += (u[i] - v[i])**2
	return math.sqrt(suma)

#2 

def nearest_neighbor_class(A, c, z):
	min_odl = math.inf
	for i in range(len(A)):
		x = distance(A[i], z)
		if min_odl > x:
			klasa = c[i]
			min_odl = x
	return klasa

def knn(A, c, Z):
	l = [0]*len(Z)
	for i in range(len(Z)):
		l[i] = nearest_neighbor_class(A, c, Z[i])	
	return l

#3
def transpozycja(A):
    n = len(A)
    m = len(A[0])
    At = [[None]*n for i in range(m)] 
    for i in range(n):
        for j in range(m):
            At[j][i] = A[i][j]    
    return At

B = copy.deepcopy(A)
B = transpozycja(B)

def wyznacz_ciag(a, b, n):
	r = (b - a)/(n -1)
	ciag = [0]*n
	for i in range(n):
		ciag[i] = a + i*r
	return ciag

a0 = min(B[0])
a1 = max(B[0])
b0 = min(B[1])
b1 = max(B[1])
x = wyznacz_ciag(a0, a1, 20) #N to długość ciągu
y = wyznacz_ciag(b0, b1, 20)

#siatka x, y jako macierz, l to klasy [x[i],y[i]]
C = [x, y]
C = transpozycja(C)
l = knn(A, c, C)

import matplotlib.pyplot as plt
plt.figure(figsize = [6, 6])

plt.subplot(1, 1, 1)
B = copy.deepcopy(A)
B = transpozycja(B)
"""
c to lista klas, tworzymy liste kolorow dla klas 
"""
def kolor(x):
	kolor = [None]*len(x)
	for i in range(len(x)):
		if x[i] == 0:
			kolor[i] = "red"
		else:
			kolor[i] = "blue"
	return kolor

Z = copy.deepcopy(C)
Z = transpozycja(Z)

plt.scatter(B[0], B[1], color = kolor(c))
import fun_mac
fun_mac.print_m(Z)
dupa = [None] * len(Z[0])
for i in range(len(Z[0])):
	dupa[i] = (Z[0][i] - Z[0][0]) #* (Z[0][len(Z[0])-1]/6)
print(kolor(l))
plt.scatter(Z[0], dupa, marker = ".", color = kolor(l), alpha = "0.9")

plt.savefig("output.png", dpi=90)

#4 ocena jakości klasyfikatora
#4.6
T = []
f = open("test_wine.csv", "r")
for row in csv.reader(f):
    for i in range(len(row)):
        row[i] = float(row[i])
    list.append(T, row)     
f.close()

poprawna_macierz(T)
c_t = knn(A, c, T)

#4.7

c_p = []
g = open("test_class.txt", "r")
while True:
	line = g.readline()
	if line == "": 
		break
	x = int(line)
	c_p.append(x)
g.close()

def licz(x, y):
	"""
	sprawdza i zlicza wartości z dwóch list
	z czego pierwsza jest testowa, a druga prawdziwa
	funkcja zwraca listę zawierającą odpowiednio TN, FP, FN, TP
	"""
	assert len(x) == len(y)
	TN = 0
	FP = 0
	FN = 0
	TP = 0
	for i in range(len(x)):	
		if x[i] == 0 and y[i] == 0:	 
			TN += 1
		if x[i] == 1 and y[i] == 0:	 
			FP += 1
		if x[i] == 0 and y[i] == 1:	 
			FN += 1
		if x[i] == 1 and y[i] == 1:	 
			TP += 1
	return [TN, FP, FN, TP]

def dokladnosc(x, y):
	lista = licz(x, y)
	suma = 0
	for i in range(len(lista)):
		suma += lista[i]
	A = (lista[3] + lista[0])/(suma)
	return A

def precyzja(x, y):
	lista = licz(x, y)
	P = lista[3]/(lista[3] + lista[1])
	return P

def czulosc(x, y):
	lista = licz(x, y)
	R = lista[3]/(lista[3] + lista[2])
	return R

def miara(x, y):
	lista = licz(x, y)
	F = 2*lista[3]/(2*lista[3] + lista[1] + lista[2])
	return F

lista = licz(c_t, c_p)
with open("output.txt", "w") as f:
	print(str.format(" "*2+"|"+"{0:^7d}"+"|"+"{1:^7d}", 0, 1), file = f)
	print("-"*18, file = f)
	print(str.format("0 |"+"{0:^7d}"+"|"+"{1:^7d}", lista[0], lista[1]), file = f)
	print(str.format("1 |"+"{0:^7d}"+"|"+"{1:^7d}"+"\n", lista[2], lista[3]), file = f)
	print(str.format("Dokladnosc = {0:0.2f}", dokladnosc(c_t, c_p)), file = f)
	print(str.format("Precyzja   = {0:0.2f}", precyzja(c_t, c_p)), file = f)
	print(str.format("Czulosc    = {0:0.2f}", czulosc(c_t, c_p)), file = f)
	print(str.format("Miara F1   = {0:0.2f}", miara(c_t, c_p)), file = f)

