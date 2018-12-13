def ilosc_liczb(s = "Liczby.txt"):
    with open(s, "r") as p:
        licznik = 0
        for line in p:
            if line == "\n": break
            if line != "0.0\n": licznik += 1

    return(licznik)


def najmniejsza(s = "Liczby.txt"):
    with open(s, "r") as p:
        lowest = float(p.readline())
        n_linii = 1
        i = 1
        for line in p:
            n_linii += 1
            if line == "\n": break
            if float(line) < lowest and line != "0.0\n":
                lowest = float(line)
                i = n_linii

    return(lowest, i)


def najwieksza(s = "Liczby.txt"):
    with open(s, "r") as p:
        highest = float(p.readline())
        n_linii = 1
        i = 1
        for line in p:
            n_linii += 1
            if line == "\n": break
            if float(line) > highest:
                highest = float(line)
                i = n_linii
    return(highest, i)


def srednia_a(s = "Liczby.txt"):
    with open(s, "r") as p:
        suma = float(p.readline())
        n_linii = 1
        for line in p:
            if line == "\n": break
            n_linii += 1
            suma += float(line)

    return(suma/n_linii)


def wariancja(s = "Liczby.txt"):
    with open(s, "r") as p:
        suma = float(p.readline())**2
        n_linii = 1
        for line in p:
            if line == "\n": break
            n_linii += 1
            suma += float(line)**2

    return((suma/n_linii)-(srednia_a(s))**2)


def srednia_bez1(s = "Liczby.txt"):
    with open(s, "r") as p:
        n_linii = 1
        for line in p:
            if line == "\n": break
            n_linii += 1
    return((srednia_a()*n_linii-najmniejsza()[0]-najwieksza()[0])/(n_linii-2))


def usuwanie_n_najmniejszych(n = 3, liczby = "Liczby.txt", pomocniczy = "pomocniczyMin.txt", pomocniczy2 = "pomocniczyMin2.txt"):
    i_min = najmniejsza(liczby)[1]
    with open(liczby, "r") as data:
        with open(pomocniczy, "w") as pomoc:
            n_linii = 0
            for line in data:
                n_linii += 1
                if n_linii == i_min:
                    pomoc.write("0.0\n")
                else:
                    pomoc.write(line)
    for i in range(1, n):
        if ((100 * i) % n) < ((100 * (i - 1)) % n):
            print(f"usuwanie min: {(100 * i // n):2} %")
        if i % 2 == 0:
            i_min = najmniejsza(pomocniczy2)[1]
            with open(pomocniczy2, "r") as pomoc2:
                with open(pomocniczy, "w") as pomoc:
                    n_linii = 0
                    for line in pomoc2:
                        n_linii += 1
                        if n_linii == i_min:
                            pomoc.write("0.0\n")
                        else:
                            pomoc.write(line)
        else:
            i_min = najmniejsza(pomocniczy)[1]
            with open(pomocniczy2, "w") as pomoc2:
                with open(pomocniczy, "r") as pomoc:
                    n_linii = 0
                    for line in pomoc:
                        n_linii += 1
                        if n_linii == i_min:
                            pomoc2.write("0.0\n")
                        else:
                            pomoc2.write(line)
    if n % 2 == 0: return pomocniczy2
    else: return pomocniczy

def usuwanie_n_najwiekszych(n = 3, liczby = "Liczby.txt", pomocniczy = "pomocniczyMax.txt", pomocniczy2 = "pomocniczyMax2.txt"):
    i_min = najwieksza(liczby)[1]
    with open(liczby, "r") as data:
        with open(pomocniczy, "w") as pomoc:
            n_linii = 0
            for line in data:
                n_linii += 1
                if n_linii == i_min:
                    pomoc.write("0.0\n")
                else:
                    pomoc.write(line)
    for i in range(1, n):
        if ((100 * i) % n) < ((100 * (i - 1)) % n): print(f"usuwanie max: {(100 * i // n):2} %")
        if i % 2 == 0:
            i_min = najwieksza(pomocniczy2)[1]
            with open(pomocniczy2, "r") as pomoc2:
                with open(pomocniczy, "w") as pomoc:
                    n_linii = 0
                    for line in pomoc2:
                        n_linii += 1
                        if n_linii == i_min:
                            pomoc.write("0.0\n")
                        else:
                            pomoc.write(line)
        else:
            i_min = najwieksza(pomocniczy)[1]
            with open(pomocniczy2, "w") as pomoc2:
                with open(pomocniczy, "r") as pomoc:
                    n_linii = 0
                    for line in pomoc:
                        n_linii += 1
                        if n_linii == i_min:
                            pomoc2.write("0.0\n")
                        else:
                            pomoc2.write(line)
    if n % 2 == 0: return pomocniczy2
    else: return pomocniczy

def laczenie_Min_Max(min = "pomocniczyMin.txt", max = "pomocniczyMax.txt", polaczony = "polaczony.txt"):
    p  = open(polaczony, "w")
    mx = open(max, "r")
    mn = open(min, "r")

    while True:
        linex = mx.readline()
        linen = mn.readline()
        if linex == "": break
        if linex == linen:
            p.write(linex)
        else:
            p.write("0.0\n")

    p.close()
    mx.close()
    mn.close()



import math

print("Liczb jest:", ilosc_liczb())
print("Najwieksza z liczb to: :", najwieksza()[0])
print("Najmniejsza z liczb to: :", najmniejsza()[0])
print("Ich srednia arytmetyczna to :", srednia_a())
print("Wariancja to :", wariancja())
print("Odchylenie standardowe :", math.sqrt(wariancja()))
print("Srednia bez 1: ", srednia_bez1())


laczenie_Min_Max(usuwanie_n_najmniejszych(100), usuwanie_n_najwiekszych(100))
print(f"Ilosc liczb po wyrzuceniu: ", ilosc_liczb("polaczony.txt"))
print("Srednia po wyrzuceniu: ", srednia_a("polaczony.txt"))
print("Wariancja po wyrzuceniu: ", wariancja("polaczony.txt"))
