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
    out_ntt = [[0 for j in range(9)] for i in range(10)]

    lut = [[w10 ** (i * (j + 8)) for j in range(9)] for i in range(10)]

    for j in range(9):
        if j <= 2:
            f7, f8, f9, f0, f1, f2 = [extract(in_poly, (j + t) % 10, j) for t in range(5, 11)]
            hi_s = ntt10_4x_nof3456(f0, f1, f2, f7, f8, f9)
        else:
            f8, f9, f0, f1, f2 = [extract(in_poly, (j + t) % 10, j) for t in range(6, 11)]
            hi_s = ntt10_4x_nof34567(f0, f1, f2, f8, f9)

        for i in range(10):
            out_ntt[i][j] = hi_s[i] * lut[i][j]

    return out_ntt

def imain_lay1(in_ntt):
    out_poly = 0
    for j in range(9):
        h0 = in_ntt[0][j]
        h1 = in_ntt[1][j]
        h2 = in_ntt[2][j]
        h3 = in_ntt[3][j]
        h4 = in_ntt[4][j]
        h5 = in_ntt[5][j]
        h6 = in_ntt[6][j]
        h7 = in_ntt[7][j]
        h8 = in_ntt[8][j]
        h9 = in_ntt[9][j]

        f0, f1, f2, f3, f4, f5, f6, f7, f8, f9 = intt10_40x(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9)

        out_poly += insert(f0, 0, j)
        out_poly += insert(f1, 1, j)
        out_poly += insert(f2, 2, j)
        out_poly += insert(f3, 3, j)
        out_poly += insert(f4, 4, j)
        out_poly += insert(f5, 5, j)
        out_poly += insert(f6, 6, j)
        out_poly += insert(f7, 7, j)
        out_poly += insert(f8, 8, j)
        out_poly += insert(f9, 9, j)

    return out_poly

def main_lay2(in_ntt):
    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        f0 = in_ntt[i][0]
        f1 = in_ntt[i][1]
        f2 = in_ntt[i][2]
        f3 = in_ntt[i][3]
        f4 = in_ntt[i][4]
        f5 = in_ntt[i][5]
        f6 = in_ntt[i][6]
        f7 = in_ntt[i][7]
        f8 = in_ntt[i][8]

        h0, h1, h2, h3, h4, h5, h6, h7, h8 = ntt9_2x(f0, f1, f2, f3, f4, f5, f6, f7, f8)

        out_ntt[i][0] = h0
        out_ntt[i][1] = h1
        out_ntt[i][2] = h2
        out_ntt[i][3] = h3
        out_ntt[i][4] = h4
        out_ntt[i][5] = h5
        out_ntt[i][6] = h6
        out_ntt[i][7] = h7
        out_ntt[i][8] = h8
    return out_ntt

def imain_lay2(in_ntt):
    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        h0 = in_ntt[i][0]
        h1 = in_ntt[i][1]
        h2 = in_ntt[i][2]
        h3 = in_ntt[i][3]
        h4 = in_ntt[i][4]
        h5 = in_ntt[i][5]
        h6 = in_ntt[i][6]
        h7 = in_ntt[i][7]
        h8 = in_ntt[i][8]

        f0, f1, f2, f3, f4, f5, f6, f7, f8 = intt9_18x(h0, h1, h2, h3, h4, h5, h6, h7, h8)

        out_ntt[i][0] = f0
        out_ntt[i][1] = f1
        out_ntt[i][2] = f2
        out_ntt[i][3] = f3
        out_ntt[i][4] = f4
        out_ntt[i][5] = f5
        out_ntt[i][6] = f6
        out_ntt[i][7] = f7
        out_ntt[i][8] = f8
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
