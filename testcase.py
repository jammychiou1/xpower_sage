from params import Zq, x
import random

def case1():
    poly = 0
    for i in range(761):
        poly += i * x ** i
    return poly

def case2():
    return x * sum([x ** (16 * i) for i in range(9)]) + sum([x ** (16 * i) for i in range(18)])

def case3():
    return 1 + x ** 16

def case_rand():
    poly = 0
    for i in range(761):
        poly += Zq(random.randrange(4591)) * x ** i
    return poly
#list(map(Zq, [1 if i == 1 else 0 for i in range(9)]))
