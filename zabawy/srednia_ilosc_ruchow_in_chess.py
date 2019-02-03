import random

class place:
    """
    Klasa przechowujaca wspolrzedne punktu na szachownicy w formie:
        quarter - nuper cwiartki jak w ukladzie wspolrzednych
        place - miejsce jakby w pierwszej cwiardce
    Dzięki takiemu zapisowi i faktowi, ze szachownica jest
        symetryczna mozemy pracowac na jednej cwiardce i opisywac
        4 razy mniej sytuacji
    """
    def __init__(self, origin=[1, 0], orq = 3):
        assert origin[0] >= 1
        assert origin[0] <= 8
        assert origin[1] >= 1
        assert origin[1] <= 8
        assert orq > 0
        assert orq < 5

        if orq != 3:
            if orq == 1:
                origin[0] = 9 - origin[0]
                origin[1] = 9 - origin[1]
            elif orq == 2:
                origin[1] = 9 - origin[1]
            else:
                origin[0] = 9 - origin[0]

        if origin[0] > 4:
            if origin[1] > 4:
                self.quarter = 1
                self.place = [ 9 - origin[0], 9 - origin[1] ]
            else:
                self.quarter = 4
                self.place = [ 9 - origin[0], origin[1] ]
        else:
            if origin[1] > 4:
                self.quarter = 2
                self.place = [ origin[0], 9 - origin[1] ]
            else:
                self.quarter = 3
                self.place = [ origin[0], origin[1] ]

    def __repr__(self):
        outp = ""
        if self.quarter == 1:
            outp += str(9 - self.place[0])
            outp += " "
            outp += str(9 - self.place[1])
        elif self.quarter == 2:
            outp += str(self.place[0])
            outp += " "
            outp += str(9 - self.place[1])
        elif self.quarter == 4:
            outp += str(9 - self.place[0])
            outp += " "
            outp += str(self.place[1])
        else:
            outp += str(self.place[0])
            outp += " "
            outp += str(self.place[1])

        return outp

class knight:
    def __init__(self, origin=[1, 0], orq = 3):
        assert origin[0] >= 1
        assert origin[0] <= 8
        assert origin[1] >= 1
        assert origin[1] <= 8

        self.current = place(origin, orq)

    def __repr__(self):
        return self.current.__repr__()

    def move(self):
        if self.current.place[0] > 2 and self.current.place[1] > 2:
            r = random.randint(1, 8)
        elif self.current.place[0] == 2 and self.current.place[1] > 2:
            r = random.randint(1, 6)
        elif self.current.place[0] == 2 and self.current.place[1] == 2:
            r = random.randint(1, 4)
        elif self.current.place[0] == 2 and self.current.place[1] == 1:
            r = random.randint(1, 3)
        elif self.current.place[0] == 1 and self.current.place[1] > 2:
            r = random.randint(2, 5)
        elif self.current.place[0] == 1 and self.current.place[1] == 2:
            r = random.randint(2, 4)
        elif self.current.place[0] == 1 and self.current.place[1] == 1:
            r = random.randint(2, 3)
        elif self.current.place[0] > 2 and self.current.place[1] == 2:
            r = random.randint(1, 6)
            if r > 4:
                r += 2
        elif self.current.place[0] > 2 and self.current.place[1] == 1:
            r = random.randint(1, 4)
            if r == 4:
                r = 8
        else: raise Exception("Cos tu sie ewidentnie spierdolilo w wyborze punktow!")

        if r == 1:
            self.current = place([ self.current.place[0] - 1, self.current.place[1] + 2 ], self.current.quarter)
        elif r == 2:
            self.current = place([self.current.place[0] + 1, self.current.place[1] + 2], self.current.quarter)
        elif r == 3:
            self.current = place([self.current.place[0] + 2, self.current.place[1] + 1], self.current.quarter)
        elif r == 4:
            self.current = place([self.current.place[0] + 2, self.current.place[1] - 1], self.current.quarter)
        elif r == 5:
            self.current = place([self.current.place[0] + 1, self.current.place[1] - 2], self.current.quarter)
        elif r == 6:
            self.current = place([self.current.place[0] - 1, self.current.place[1] - 2], self.current.quarter)
        elif r == 7:
            self.current = place([self.current.place[0] - 2, self.current.place[1] - 1], self.current.quarter)
        else:
            self.current = place([self.current.place[0] - 2, self.current.place[1] + 1], self.current.quarter)





sum = 0
D = 10000
start = [1, 2]
for d in range(D):
    k = knight(start)
    i = 1
    k.move()
    while not (k.current.place == start and k.current.quarter == 3):
        k.move()
        i += 1
    sum += i
print(sum/D)

