class Human:
    """
    Human xD
    """
    ...
    def __init__(self, imie, nazwisko, wiek):
        """
        Metoda specialna,
        kontruktor
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"I'm {self.imie} {self.nazwisko} i mam {self.wiek} lat xD")

    def __repr__(self):
        return(f"Human {self.imie}, {self.nazwisko}, {self.wiek}")

    def __le__(self, other):
        """
        self <= other
        """
        return self.wiek >= other.wiek

    def __lt__(self, other):
        """
        self < other
        """
        return self.wiek > other.wiek

Romek = Human("Rom", "AT", 31)
print(Romek.imie)

Romek.przedstaw_sie()

print(Romek)

Antek = Human("Ant", "TA", 40)

print(Antek >= Romek)

#print(sorted(Romek, Antek))

"""
import Pandas as pd

x = pd.DataFrame([
    [1,2,3]
    [4,5,6]
])
print(x)

"""

class DynaicArray:
    """
    Dynamiczna tablica
    """
    def __init__(self, ile = 0, co = 0):
        self.data = [co] * ile

    def __repr__(self):
        return f"Tabliczka: {self.data}"

    def __getitem__(self, item):







