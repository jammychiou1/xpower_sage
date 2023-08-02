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

# in1_poly = case3()
# in2_poly = case3()
in1_poly = case_rand()
in2_poly = case_rand()

out_main_1360x = mainmul(in1_poly, in2_poly)
out_main_ref = in1_poly * in2_poly % (x ** 1440 - 1)
print(out_main_1360x)
print(out_main_ref)
print(out_main_1360x / 1360 - out_main_ref)

# out_low = lowmul(in1_poly, in2_poly)
# out_low_ref = in1_poly * in2_poly % (x ** 81)
# print(out_low)
# print(out_low_ref)
# print(out_low - out_low_ref)

def crt(main, low):
    coefs = [0 for i in range(1521)]
    for i in range(81):
        coefs[i] = low[i]
    for i in range(81, 1440):
        coefs[i] = main[i]
    for i in range(1440, 1521):
        coefs[i] = main[i - 1440] - low[i - 1440]
    return Rq(coefs)

# out_poly_ref = in1_poly * in2_poly
# out_poly = crt(out_main_1360x / 1360, out_low)
# print(out_poly_ref)
# print(out_poly)
# print(out_poly - out_poly_ref)
