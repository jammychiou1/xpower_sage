from params import w, x
from ntt9 import ntt9_2x, intt9_18x
from ntt10 import ntt10_4x_nof3456, ntt10_4x_nof34567, intt10_40x
from basemul import main_basemul

w10 = w ** (4590 // 10)

def extract(poly, i, j):
    res = 0
    base = (81 * i + 10 * j) % 90 * 16
    for k in range(16):
        res += poly[base + k] * x ** k
    return res

def insert(f, i, j):
    base = (81 * i + 10 * j) % 90 * 16
    return x ** base * f

def main_lay1(in_poly):
    lut = [[w10 ** (i * (j + 8)) for j in range(9)] for i in range(10)]

    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for j in range(9):
        if j <= 2:
            f7, f8, f9, f0, f1, f2 = (extract(in_poly, (j + t) % 10, j) for t in range(5, 11))
            hi_s = ntt10_4x_nof3456(f0, f1, f2, f7, f8, f9)
        else:
            f8, f9, f0, f1, f2 = (extract(in_poly, (j + t) % 10, j) for t in range(6, 11))
            hi_s = ntt10_4x_nof34567(f0, f1, f2, f8, f9)

        for i in range(10):
            out_ntt[i][j] = hi_s[i] * lut[i][j]
    return out_ntt

def imain_lay1(in_ntt):
    out_poly = 0
    for j in range(9):
        hi_s = (in_ntt[i][j] for i in range(10))
        fi_s = intt10_40x(*hi_s)
        for i in range(10):
            out_poly += insert(fi_s[i], i, j)
    return out_poly

def main_lay2(in_ntt):
    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        fj_s = (in_ntt[i][j] for j in range(9))
        hj_s = ntt9_2x(*fj_s)
        for j in range(9):
            out_ntt[i][j] = hj_s[j]
    return out_ntt

def imain_lay2(in_ntt):
    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        hj_s = (in_ntt[i][j] for j in range(9))
        fj_s = intt9_18x(*hj_s)
        for j in range(9):
            out_ntt[i][j] = fj_s[j]
    return out_ntt

def forward(in_poly):
    lay1 = main_lay1(in_poly) # 1 -> 4
    lay2 = main_lay2(lay1) # 4 -> 8
    return lay2

def backward(in_lay2):
    lay1 = imain_lay2(in_lay2) # 64 -> 1152
    out_poly = imain_lay1(lay1) # 1152 -> 170
    return out_poly

def mainmul(in1_poly, in2_poly):
    in1_lay2 = forward(in1_poly) # 1 -> 8
    in2_lay2 = forward(in2_poly) # 1 -> 8
    out_lay2 = main_basemul(in1_lay2, in2_lay2) # 8, 8 -> 64
    out_main = backward(out_lay2) # 64 -> 170

    return out_main
