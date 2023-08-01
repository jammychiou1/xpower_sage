from sage.all import Zmod, PolynomialRing

Q = 4591
Zq = Zmod(Q)
Rq, x = PolynomialRing(Zq, "x").objgen()

w = Zq(11)
