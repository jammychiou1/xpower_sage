from params import w, x
from ntt9 import ntt9_qd, intt9_36x, ntt9_ref, intt9_ref
from ntt10 import ntt10_qd_nof3456, ntt10_qd_nof34567, intt10_40x, ntt10_ref, intt10_ref
from basemul import basemul, basemul_ref

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

def good_lay1_qd(in_poly):
    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for j in range(9):
        if j <= 2:
            f7 = extract(in_poly, (j + 5) % 10, j)
            f8 = extract(in_poly, (j + 6) % 10, j)
            f9 = extract(in_poly, (j + 7) % 10, j)
            f0 = extract(in_poly, (j + 8) % 10, j)
            f1 = extract(in_poly, (j + 9) % 10, j)
            f2 = extract(in_poly, j, j)
            h0, h1, h2, h3, h4, h5, h6, h7, h8, h9 = ntt10_qd_nof3456(f0, f1, f2, f7, f8, f9)
        else:
            f8 = extract(in_poly, (j + 6) % 10, j)
            f9 = extract(in_poly, (j + 7) % 10, j)
            f0 = extract(in_poly, (j + 8) % 10, j)
            f1 = extract(in_poly, (j + 9) % 10, j)
            f2 = extract(in_poly, j, j)
            h0, h1, h2, h3, h4, h5, h6, h7, h8, h9 = ntt10_qd_nof34567(f0, f1, f2, f8, f9)

        h0 = h0
        h1 = h1 * w10 ** (j + 8)
        h2 = h2 * w10 ** (2 * (j + 8))
        h3 = h3 * w10 ** (3 * (j + 8))
        h4 = h4 * w10 ** (4 * (j + 8))
        h5 = h5 * w10 ** (5 * (j + 8))
        h6 = h6 * w10 ** (6 * (j + 8))
        h7 = h7 * w10 ** (7 * (j + 8))
        h8 = h8 * w10 ** (8 * (j + 8))
        h9 = h9 * w10 ** (9 * (j + 8))

        out_ntt[0][j] = h0
        out_ntt[1][j] = h1
        out_ntt[2][j] = h2
        out_ntt[3][j] = h3
        out_ntt[4][j] = h4
        out_ntt[5][j] = h5
        out_ntt[6][j] = h6
        out_ntt[7][j] = h7
        out_ntt[8][j] = h8
        out_ntt[9][j] = h9
    return out_ntt

def igood_lay1_40x(in_ntt):
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

def good_lay1_ref(in_poly):
    out_ntt = [[0 for j in range(9)] for i in range(10)]
    for j in range(9):
        f0 = extract(in_poly, 0, j)
        f1 = extract(in_poly, 1, j)
        f2 = extract(in_poly, 2, j)
        f3 = extract(in_poly, 3, j)
        f4 = extract(in_poly, 4, j)
        f5 = extract(in_poly, 5, j)
        f6 = extract(in_poly, 6, j)
        f7 = extract(in_poly, 7, j)
        f8 = extract(in_poly, 8, j)
        f9 = extract(in_poly, 9, j)

        h0, h1, h2, h3, h4, h5, h6, h7, h8, h9 = ntt10_ref(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9)

        out_ntt[0][j] = h0
        out_ntt[1][j] = h1
        out_ntt[2][j] = h2
        out_ntt[3][j] = h3
        out_ntt[4][j] = h4
        out_ntt[5][j] = h5
        out_ntt[6][j] = h6
        out_ntt[7][j] = h7
        out_ntt[8][j] = h8
        out_ntt[9][j] = h9
    return out_ntt

def igood_lay1_ref(in_ntt):
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

        f0, f1, f2, f3, f4, f5, f6, f7, f8, f9 = intt10_ref(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9)

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

def good_lay2_qd(in_ntt):
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

        h0, h1, h2, h3, h4, h5, h6, h7, h8 = ntt9_qd(f0, f1, f2, f3, f4, f5, f6, f7, f8)

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

def igood_lay2_36x(in_ntt):
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

        f0, f1, f2, f3, f4, f5, f6, f7, f8 = intt9_36x(h0, h1, h2, h3, h4, h5, h6, h7, h8)

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

def good_lay2_ref(in_ntt):
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

        h0, h1, h2, h3, h4, h5, h6, h7, h8 = ntt9_ref(f0, f1, f2, f3, f4, f5, f6, f7, f8)

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

def igood_lay2_ref(in_ntt):
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

        f0, f1, f2, f3, f4, f5, f6, f7, f8 = intt9_ref(h0, h1, h2, h3, h4, h5, h6, h7, h8)

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
    lay1_qd = good_lay1_qd(in_poly)
    lay1_ref = good_lay1_ref(in_poly)
    # for j in range(9):
    #     for i in range(10):
    #         print(f"(i, j) = {(i, j)}")
    #         print(lay1_qd[i][j] / 4)
    #         print(lay1_ref[i][j])
    lay2_hxd = good_lay2_qd(lay1_qd)
    lay2_ref = good_lay2_ref(lay1_ref)
    # for i in range(10):
    #     for j in range(9):
    #         print(f"(i, j) = {(i, j)}")
    #         print(lay2_hxd[i][j] / 16)
    #         print(lay2_ref[i][j])
    return lay2_hxd

def backward(in_lay2):
    lay1_34x = igood_lay2_36x(in_lay2)
    lay1_ref = igood_lay2_ref(in_lay2)
    out_poly_1360x = igood_lay1_40x(lay1_34x)
    out_poly_ref = igood_lay1_ref(lay1_ref)
    return out_poly_1360x

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
        poly += random.randrange(4591) * x ** i
    return poly

# print([w10 ** i for i in range(10)])
# [1, 2981, 2776, 2274, 2478, 4590, 1610, 1815, 2317, 2113]
# print([w9 ** j for j in range(9)])
# [1, 2985, 3685, 4280, 3638, 1715, 310, 2559, 3782]

# in1_poly = case3()
# in2_poly = case3()
in1_poly = case_rand()
in2_poly = case_rand()

in1_lay2 = forward(in1_poly)
in2_lay2 = forward(in2_poly)
out_lay2 = basemul(in1_lay2, in2_lay2)
out_lay2_ref = basemul_ref(in1_lay2, in2_lay2)
# for i in range(10):
#     for j in range(9):
#         print(f"(i, j) = {(i, j)}")
#         print(out_lay2[i][j])
#         print(out_lay2_ref[i][j])
out_poly_1360x = backward(out_lay2)
out_poly_ref = in1_poly * in2_poly % (x ** 1440 - 1)

print(out_poly_1360x)
print(out_poly_ref)
print(out_poly_1360x / 1360 - out_poly_ref)
