"""
SPOJ 541
sprawdz, czy czwarty punkt jest w trojkacie o rogach
pierwszych 3 punktow
"""
def czy_jest_w_pol(xa, ya, xb, yb, xc, yc, xp, yp):
    """
    ya = a1 xa + b1
    yb = a1 xb + b1
    ya - yb = a1 (xa - xb)
    a1 = (ya - yb) / (xa - xb)
    :param xa:
    :param ya:
    :param xb:
    :param xc:
    :param yc:
    :param xp:
    :param yp:
    :return:
    """
    if (xa - xb) == 0:
        if ((xc - xa) < 0 and (xp - xa) < 0) or ((xc - xa) > 0 and (xp - xa) > 0):
            return True
        else:
            return False

    a = (ya - yb) / (xa - xb)
    b = ya - a*xa

    if ((yc < xc * a + b) and (yp < xp * a + b)) or ((yc > xc * a + b) and (yp > xp * a + b)):
        return True
    else:
        return False

def czy_jest_na_brzegu(xa, ya, xb, yb, xp, yp):
    # 0, 0, 0, 10, 1, 1
    if (xa - xb) == 0:
        if (xp - xa) == 0 and ((yp <= ya and yp >= yb) or (yp >= ya and yp <= yb)):
            return True
        else:
            return False

    a = (ya - yb) / (xa - xb)
    b = ya - a * xa

    if (yp == xp * a + b) and ((xp <= xa and xp >= xb) or (xp >= xa and xp <= xb)):
        return True
    else:
        return False

I = 0
O = 0
E = 0
for j in range(100000):
    """
    s = input()
    points = s.split(" ")
    
    for i in range(8):
        points[i] = int(points[i])
    """
    import random
    points = [None] * 8
    for i in range(8):
        points[i] = random.randint(1, 1000)

    if points[0] == points[1] and points[0] == points[2] and points[0] == points[3] and points[0] == points[4] and points[0] == points[5] and points[0] == points[6] and points[0] == points[7] and points[0] == 0:
        break

    if (czy_jest_w_pol(points[0], points[1], points[2], points[3], points[4], points[5], points[6], points[7])) and (czy_jest_w_pol(points[4], points[5], points[0], points[1], points[2], points[3], points[6], points[7])) and (czy_jest_w_pol(points[2], points[3], points[4], points[5], points[0], points[1], points[6], points[7])):
        I += 1
        continue
    if (czy_jest_na_brzegu(points[0], points[1], points[2], points[3], points[6], points[7])) or (czy_jest_na_brzegu(points[0], points[1], points[4], points[5], points[6], points[7])) or (czy_jest_na_brzegu(points[4], points[5], points[2], points[3], points[6], points[7])):
        E += 1
        continue
    O += 1

print(I, E, O, sep="\n")