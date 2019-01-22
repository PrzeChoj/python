import numpy as np

x = np.random.rand(10)

print(np.sqrt(np.sum((x-np.mean(x))**2)/x.shape[0]))




y = {"jabuszko", "gruszka"}
y2 = {"gruszka", "gruszka"}

print("jabuszko" in y)

print(y & y2)
print(y | y2)
print(y - y2)
print(y.issubset(y2))
print(y.issubset(y2|y))

import fun_mac as fm
#t = [ i**2 for i in range(10) if x % 2 == 1 ]
t = [ [i*j for i in range(10)] for j in range(10) ]

fm.print_m(t)

#dict comprehensions
s = { str(i%2):i**2 for i in range(7) }
print(s)



print(help(list))
krotka = 1,2,3,4
print(krotka)
print(4 in krotka)
print(krotka[-1])

napis = "123456789"
print("78" in napis)
print(napis[::-1])

#to byly typy sekwencyjne, czyli maja te same operacje

#sa tez typy iterowalne
#wszystkie seksencyjne sa iterowalne

obiekt_iterowalny = [1,2,3,4]
obiekt_iterowalny = "abc"
obiekt_iterowalny = range(1, 10, 2) #range jest sekwencyjny
obiekt_iterowalny = reversed(obiekt_iterowalny)
for e in obiekt_iterowalny:
    print(e)

print(obiekt_iterowalny)
print(list("abc"))

obiekt_iterowalny = (enumerate("abc"))
print(obiekt_iterowalny)
for e in obiekt_iterowalny:
    print(e)

help(zip)

a = 0
b = 1
a, b = b, a
print(a, b)

x, y, z = 3, 4, 5
print(y)

x, y, z = range(3)
print(x, y, z)

x, *y, z = reversed(range(10))
print(x, y, z)

for ind, val in enumerate("napis"):
    print("(%d)=<%s>"%(ind, val))

print(round(3142.421, -2))

def test(a, *b, c=5):
    print(a, b, c)

test(1, 2, 3, 4, 5, 6, 7, 8, c=50)

def test2(a, *b, c=5, **kwargs):
    print(a, b, c, kwargs)

test2(2, 3, 4, 5, 2, "xD", color="red", nextColor="bloue")

x = list(range(10))
import matplotlib.pyplot as plt
plt.plot(x, [ xi**2 for xi in x ], "r-", label="$x^2$")
plt.plot(x, [ xi**3 for xi in x ], "b:", label="$x^3$")
#plt.show()


args = [3,4,5, "xDDDD"] # iterowalne
test(1, 2, *args)

styl = {"color":"red", "linestyle": "-."}
# ...
styl["alpha"] = 0.6
#plt.


pliki = [ "plik1", "plik2", ... ]
for plik in pliki:
    try:
        ...
    except:
        ...
    finally:
        ...
