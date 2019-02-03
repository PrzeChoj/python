def __usun_duplikaty_i_index(t, v):
    """
    funkcja dostaje liste t i zwraca taka, w ktorej sie nic nie powtarza i konkretnej liczby tez nie ma
    t - tablica
    v - liczba
    """
    # mozna to robic bez appenda dopisujac nowe elementy do tablicy o wielkosci len(t), a potem przepisac tablice bez elementow None na koncu
    # ale tak jest szybciej(dla programisty, nie dla komputera), ewentualne poprawki bede robic jak starczy czasu
    out_t = []
    for i in range(len(t)):
        if t[i] == v: continue
        i_unikalne = True
        for j in range(i + 1, len(t)):
            if t[i] == t[j]: i_unikalne = False
        if i_unikalne: out_t.append(t[i])  # dopisujesz do wyjsciowej tablicy tylko te, ktore sei pozniej nie powtarzaja, dlatego kazdy unikalny bedzie wpisany tylko raz
    return out_t

print(__usun_duplikaty_i_index([0,0,0,1,1,0,2,0],3))