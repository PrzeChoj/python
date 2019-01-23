class Polynomian:
    def __init__(self, *war):
        self.st = len(war)
        self.wsp = [0] * self.st
        for i in range(self.st):
            self.wsp[i] = war[i]

    def __repr__(self):
        napis = ""
        for i in range(self.st):
            if self.wsp[i] == 0: continue
            elif self.wsp[i] == 1:
                napis += "+ "
                napis += "x^"
                napis += str(self.st - i - 1)
                napis += " "
            elif self.wsp[i] == -1:
                napis += "- "
                napis += "x^"
                napis += str(self.st - i - 1)
                napis += " "
            elif self.wsp[i] > 0:
                napis += "+ "
                napis += str(self.wsp[i])
                napis += "x^"
                napis += str(self.st - i - 1)
                napis += " "
            elif self.wsp[i] < 0:
                napis += "- "
                napis += str(-self.wsp[i])
                napis += "x^"
                napis += str(self.st - i - 1)
                napis += " "
        return napis

    def __call__(self, x):
        c = self.wsp[0]
        for i in range(1, self.st):
            c = x * c + self.wsp[i]
        return c

w = Polynomian(1, -4, 3, -5)
print(w)
print(w(2))