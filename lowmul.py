from params import x
from ntt10 import ntt10_4x_nof34567, intt10_40x_nof3456
from basemul import low_basemul

def extract(poly, i):
    res = 0
    base = 16 * i
    for k in range(16):
        res += poly[base + k] * x ** k
    return res

def insert(f, i):
    base = 16 * i
    return x ** base * f

def low_lay1(in_poly):
    out_ntt = [0 for i in range(10)]
    f8, f9, f0, f1, f2 = (extract(in_poly, i) for i in range(5))
    hi_s = ntt10_4x_nof34567(f0, f1, f2, f8, f9)
    for i in range(10):
        out_ntt[i] = hi_s[i]
    return out_ntt

def ilow_lay1(in_ntt):
    out_poly = 0
    hi_s = (in_ntt[i] for i in range(10))
    f0, f1, f2, f7, f8, f9 = intt10_40x_nof3456(*hi_s)
    for i, f in enumerate((f7, f8, f9, f0, f1, f2)):
        out_poly += insert(f, i)
    return out_poly

def lowmul(in1_poly, in2_poly):
    in1_lay1 = low_lay1(in1_poly)
    in2_lay1 = low_lay1(in2_poly)
    out_lay1 = low_basemul(in1_lay1, in2_lay1)
    out_low = ilow_lay1(out_lay1)
    out_low = out_low[:81] + 170 * (in1_poly[80] * in2_poly[0] + in1_poly[0] * in2_poly[80]) * x ** 80
    return out_low
