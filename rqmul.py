from params import Rq
from mainmul import mainmul
from lowmul import lowmul
from testcase import case_rand

def crt(main, low):
    coefs = [0 for i in range(1521)]
    for i in range(81):
        coefs[i] = low[i]
    for i in range(81, 1440):
        coefs[i] = main[i]
    for i in range(1440, 1521):
        coefs[i] = main[i - 1440] - low[i - 1440]
    return Rq(coefs)

def rqmul(in1_poly, in2_poly):
    out_main = mainmul(in1_poly, in2_poly)
    out_low = lowmul(in1_poly, in2_poly)
    out_poly = crt(out_main, out_low) / 170
    return out_poly

if __name__ == '__main__':
    in1_poly = case_rand()
    in2_poly = case_rand()
    out_poly = rqmul(in1_poly, in2_poly)
    out_poly_ref = in1_poly * in2_poly
    print(out_poly_ref)
    print(out_poly)
    print(out_poly - out_poly_ref)
