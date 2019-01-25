import math
class Ulamek:
    def __init__(self, licznik, mianownik):
        assert mianownik != 0
        if math.gcd(mianownik, licznik) != 1:
            self.mianownik = mianownik//math.gcd(mianownik, licznik)
            self.licznik = licznik//math.gcd(mianownik, licznik)
            return
        self.licznik = licznik
        self.mianownik = mianownik
        return

    def __repr__(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def __add__(self, other):
        if type(other) == int:
            liczba = other * self.mianownik
            suma = Ulamek(self.licznik+liczba, self.mianownik)

        elif type(other) == float:
            dokladnosc = 1000
            liczba = Ulamek(int(other*dokladnosc), 1000)
            suma = self + liczba

        elif type(other) == Ulamek:
            suma = Ulamek(self.licznik*other.mianownik + self.mianownik*other.licznik, self.mianownik * other.mianownik)

        else:
            raise Exception("Dodawane sa nieprawidlowe dane")

        return suma

    def __radd__(self, other):
        return (self + other)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return (self + (-other))

        elif type(other) == Ulamek:
            return (self + Ulamek(-other.licznik, other.mianownik))

    def __rsub__(self, other):
        if other == 0:
            return Ulamek(-self.licznik, self.mianownik)
        else:
            return (0-(self - other))

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Ulamek(other * self.licznik, self.mianownik)
        elif type(other) == Ulamek:
            return  Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __rmul__(self, other):
        return (self * other)

    """
    # jak nadpisac dzielenie?
    # bo __div__() nie dziala :(
    def __div__(self, other):
        if type(other) == int or type(other) == float:
            return Ulamek(self.licznik/other, self.mianownik)
    """


l = Ulamek(21, 2)
print(l)
k = Ulamek(13, 3)

print(l-k)

print(3 - l)
print(l - 3)
print("dupa")
print(l*3)
print(2*l)
#print(l/2)