import fun_mac

print(fun_mac.track_m(fun_mac.make_m(5, 5, 5)))

"""
ile = 100000
suma = 0
C = fun_mac.make_m(5, 5, 0)
for i in range(ile):
    R = fun_mac.random_randint_m(5, 5)
    suma += (fun_mac.track_m(R))
    C = fun_mac.sum_m(C, R)

print(suma/ile)
fun_mac.print_m(C)
"""