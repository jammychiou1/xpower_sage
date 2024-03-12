from params import x
from ntt10 import ntt10_4x_nof34567, intt10_40x_nof3456, ntt10_ref, intt10_ref
from basemul import low_basemul, low_basemul_ref

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

    f8 = extract(in_poly, 0)
    f9 = extract(in_poly, 1)
    f0 = extract(in_poly, 2)
    f1 = extract(in_poly, 3)
    f2 = extract(in_poly, 4)

    h0, h1, h2, h3, h4, h5, h6, h7, h8, h9 = ntt10_4x_nof34567(f0, f1, f2, f8, f9)

    out_ntt[0] = h0
    out_ntt[1] = h1
    out_ntt[2] = h2
    out_ntt[3] = h3
    out_ntt[4] = h4
    out_ntt[5] = h5
    out_ntt[6] = h6
    out_ntt[7] = h7
    out_ntt[8] = h8
    out_ntt[9] = h9

    return out_ntt

def low_lay1_ref(in_poly):
    out_ntt = [0 for i in range(10)]

    f0 = extract(in_poly, 0)
    f1 = extract(in_poly, 1)
    f2 = extract(in_poly, 2)
    f3 = extract(in_poly, 3)
    f4 = extract(in_poly, 4)

    h0, h1, h2, h3, h4, h5, h6, h7, h8, h9 = ntt10_ref(f0, f1, f2, f3, f4, 0, 0, 0, 0, 0)

    out_ntt[0] = h0
    out_ntt[1] = h1
    out_ntt[2] = h2
    out_ntt[3] = h3
    out_ntt[4] = h4
    out_ntt[5] = h5
    out_ntt[6] = h6
    out_ntt[7] = h7
    out_ntt[8] = h8
    out_ntt[9] = h9

    return out_ntt

def ilow_lay1(in_ntt):
    out_poly = 0

    h0 = in_ntt[0]
    h1 = in_ntt[1]
    h2 = in_ntt[2]
    h3 = in_ntt[3]
    h4 = in_ntt[4]
    h5 = in_ntt[5]
    h6 = in_ntt[6]
    h7 = in_ntt[7]
    h8 = in_ntt[8]
    h9 = in_ntt[9]

    f0, f1, f2, f7, f8, f9 = intt10_40x_nof3456(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9)

    out_poly += insert(f7, 0)
    out_poly += insert(f8, 1)
    out_poly += insert(f9, 2)
    out_poly += insert(f0, 3)
    out_poly += insert(f1, 4)
    out_poly += insert(f2, 5)

    return out_poly

def ilow_lay1_ref(in_ntt):
    out_poly = 0

    h0 = in_ntt[0]
    h1 = in_ntt[1]
    h2 = in_ntt[2]
    h3 = in_ntt[3]
    h4 = in_ntt[4]
    h5 = in_ntt[5]
    h6 = in_ntt[6]
    h7 = in_ntt[7]
    h8 = in_ntt[8]
    h9 = in_ntt[9]

    f0, f1, f2, f3, f4, f5, f6, f7, f8, f9 = intt10_ref(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9)

    out_poly += insert(f0, 0)
    out_poly += insert(f1, 1)
    out_poly += insert(f2, 2)
    out_poly += insert(f3, 3)
    out_poly += insert(f4, 4)
    out_poly += insert(f5, 5)

    return out_poly

def lowmul(in1_poly, in2_poly):
    in1_lay1 = low_lay1(in1_poly)
    in2_lay1 = low_lay1(in2_poly)
    out_lay1 = low_basemul(in1_lay1, in2_lay1)
    out_low = ilow_lay1(out_lay1)
    out_low = out_low[:81] + 640 * (in1_poly[80] * in2_poly[0] + in1_poly[0] * in2_poly[80]) * x ** 80
    return out_low
