class Data:
    def __init__(self, rok, miesiac, dzien):
        """
        assert type(rok) == int or type(miesiac) == int or type(dzien) == int
        assert not(miesiac > 12 or miesiac < 1 or rok < 0 or dzien < 0)
        if miesiac in (1, 3, 5, 7, 8, 10, 12):
            assert dzien < 31
        elif miesiac in (4, 6, 9, 11):
            assert dzien < 31
        else:
            if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0):
                assert dzien < 30
            else:
                assert dzien < 29
        """
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok

    def __repr__(self):
        return ( "Data to: " + str(self.rok) + ", " + str(self.miesiac) + ", " + str(self.dzien) )

    def dodaj_n_dni(self, n):
        def korekta_dnia(dzien, miesiac, rok):
            if miesiac == 2:
                if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0):
                    if dzien > 29:
                        dzien -= 29
                        miesiac += 1
                        __korekta_miesiaca(miesiac, rok)
                else:
                    dzien -= 28
                    miesiac += 1
                    m = __korekta_miesiaca(miesiac, rok)
                    miesiac = m[0]
                    rok = m[1]
            elif miesiac in (1, 3, 5, 7, 8, 10, 12):
                if dzien > 31:
                    dzien -= 31
                    miesiac += 1
                    m = __korekta_miesiaca(miesiac, rok)
                    miesiac = m[0]
                    rok = m[1]
            elif miesiac in (4, 6, 9, 11):
                if dzien > 30:
                    dzien -= 30
                    miesiac += 1
                    m = __korekta_miesiaca(miesiac, rok)
                    miesiac = m[0]
                    rok = m[1]
            return dzien, miesiac, rok

        def __korekta_miesiaca(miesiac, rok):
            if miesiac > 12:
                miesiac -= 12
                rok += 1
            return miesiac, rok

        assert type(n) == int

        self.dzien += n
        while self.dzien > 31:
            kor = korekta_dnia(self.dzien, self.miesiac, self.rok)
            self.dzien = kor[0]
            self.miesiac = kor[1]
            self.rok = kor[2]
        kor = korekta_dnia(self.dzien, self.miesiac, self.rok)
        self.dzien = kor[0]
        self.miesiac = kor[1]
        self.rok = kor[2]

    def __sub__(self, other):
        """
        nie dziala :(
        """
        roznica = Data(self.rok - other.rok, self.miesiac - other.miesiac, self.dzien - other.dzien)
        while roznica.rok < 0:
            roznica.rok += 1
            roznica.miesiac -= 12
        while roznica.rok > 0:
            roznica.rok -= 1
            roznica.miesiac += 12
        while roznica.miesiac > 0:
            if (roznica.miesiac - other.miesiac - 1) in (1, 3, 5, 7, 8, 10, 12):
                roznica.miesiac -= 1
                roznica.dzien += 31
            if (roznica.miesiac - other.miesiac - 1) in (4, 6, 9, 11):
                roznica.miesiac -= 1
                roznica.dzien += 30
            if (roznica.miesiac - other.miesiac - 1) == 2:
                if ((other.rok + roznica.miesiac//12) % 4 == 0) and ((other.rok + roznica.miesiac//12) % 100 != 0) or ((other.rok + roznica.miesiac//12) % 400 == 0):
                    roznica.miesiac -= 1
                    roznica.dzien += 29
                else:
                    roznica.miesiac -= 1
                    roznica.dzien += 28
        while roznica.miesiac < 0:
            if -(roznica.miesiac - other.miesiac - 1) in (1, 3, 5, 7, 8, 10, 12):
                roznica.miesiac += 1
                roznica.dzien -= 31
            if -(roznica.miesiac - other.miesiac - 1) in (4, 6, 9, 11):
                roznica.miesiac += 1
                roznica.dzien -= 30
            if -(roznica.miesiac - other.miesiac - 1) == 2:
                if ((other.rok + roznica.miesiac//12) % 4 == 0) and ((other.rok + roznica.miesiac//12) % 100 != 0) or ((other.rok + roznica.miesiac//12) % 400 == 0):
                    roznica.miesiac += 1
                    roznica.dzien -= 29
                else:
                    roznica.miesiac -= 1
                    roznica.dzien += 28


        return roznica

dzis = Data(2019, 2, 28)
print(dzis)

dzis.dodaj_n_dni(31)
print(dzis)
dzis.dodaj_n_dni(1)
print(dzis)
dzis.dodaj_n_dni(230)
print(dzis)
dzis.dodaj_n_dni(44)
print(dzis)
dzis.dodaj_n_dni(1)
print(dzis)
dzis.dodaj_n_dni(55)
print(dzis)
dzis.dodaj_n_dni(4)
print(dzis)
dzis.dodaj_n_dni(1)
print(dzis)
teraz = Data(2019, 3, 28)
print("XD")
print(teraz - dzis)


pozniej = teraz
wczesniej = Data(2019, 1, 28)
print(f"{pozniej} - {wczesniej}:")
print(pozniej - wczesniej)

