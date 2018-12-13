"""
SPOJ 978
Zapelnij tablice liczbami i ja wyzeruj
"""
t = [None] * 10
ile = 0

while True:
    kontroler = input()

    if kontroler == "+":
        if ile < 10:
            t[ile] = int(input())
            print(":)")
            ile += 1
        else: print(":(")

    elif kontroler == "-":
        if ile > -1:
            ile -= 1
            print(t[ile])
        else: print(":(")

    if ile == 0:
        break
