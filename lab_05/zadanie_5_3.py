import math

def table(T, d):
    output = [0] * d
    for t in T:
        output[t] += 1
    return output

def piechrt(t, f):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])

    def kolo(l, r):
        """
        Wzraca wierzcholki l-konta foremnego o "promieniu" r
        """
        # l > 2; r > 0
        Output = [  ]
        for i in range(l + 1):
            Output.append([r * math.sin((i/l)*math.pi*2), r * math.cos((i/l)*math.pi*2)])

        #print(Output)

        return Output


    suma = 0
    for i in range(len(t)):
        suma += t[i]

    ball = kolo(suma*10, 1)

    kolor = [ "red", "green" , "black"]

    # suma == 3
    # len(ball) = 31

    last = 0
    for i in range(len(f)):
        wykres = [ [0, 0] ]
        for j in range((t[i]*10)):
            wykres.append(ball[last])
            last += 1
        wykres.append(ball[last])
        ax.add_patch(patches.Polygon(wykres, facecolor=kolor[i]))

    """
    xy = [[0, -1], [-1, 0], [0, 1], [-0.5, 2], [-1.1, 0]]
    """

    ax.axis("equal")

    fig.savefig("wykres_kolowy.png", dpi=90)


x = [0, 1, 2, 0]
f = ["mezczyzna", "kobieta", "lol"]

t = table(x, 3) # t == [ 2, 1, 1 ]

piechrt(t, f)