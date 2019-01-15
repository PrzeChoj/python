# doctionary = zbior par (klucz, wartosc)
s = {
    "ala": [1, 2, 3],
    "jola": 7,
    "zenek": sum,
    7: 'XD'
}

print(s)

t = dict(ala=1, zosia=8, janek=3)

print(t)

s1 = s["ala"]

print(s1)

print("ala" in s)

s["x"] = dict(a=1, b=2, c=3)

print(s["x"])

print(s["x"]["a"])

del s["x"]

print("x" in s)

print(s.values())

for x in s.values():
    print(x)

y = 1,2,3,4
print(y)

print(hash("xD"))