from params import Rq, Zq, x
from mainmul import mainmul
from lowmul import lowmul

def case1():
    poly = 0
    for i in range(761):
        poly += i * x ** i
    return poly

def case2():
    return x * sum([x ** (16 * i) for i in range(9)]) + sum([x ** (16 * i) for i in range(18)])

def case3():
    return 1 + x ** 16

import random
def case_rand():
    poly = 0
    for i in range(761):
        poly += Zq(random.randrange(4591)) * x ** i
    return poly

in1_poly = case_rand()
in2_poly = case_rand()

#list(map(Zq, [1 if i == 1 else 0 for i in range(9)]))

out_main = mainmul(in1_poly, in2_poly)

out_low = lowmul(in1_poly, in2_poly)

def crt(main, low):
    coefs = [0 for i in range(1521)]
    for i in range(81):
        coefs[i] = low[i]
    for i in range(81, 1440):
        coefs[i] = main[i]
    for i in range(1440, 1521):
        coefs[i] = main[i - 1440] - low[i - 1440]
    return Rq(coefs)

out_poly = crt(out_main, out_low) / 170
out_poly_ref = in1_poly * in2_poly
print(out_poly_ref)
print(out_poly)
print(out_poly - out_poly_ref)
