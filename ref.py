from params import Rq, Zq, x

def mainmul_ref(in1_poly, in2_poly):
    return in1_poly * in2_poly % (x ** 1440 - 1)

def lowmul_ref(in1_poly, in2_poly):
    return in1_poly * in2_poly % (x ** 81)

def main_lay1_ref(in_poly):
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

def imain_lay1_ref(in_ntt):
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

def main_lay2_ref(in_ntt):
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

def imain_lay2_ref(in_ntt):
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

def ntt10_ref(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9):
    fis = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9]
    his = [0 for i in range(10)]
    for i in range(10):
        for ii in range(10):
            his[i] += w10 ** (i * ii) * fis[ii]
    return his[0], his[1], his[2], his[3], his[4], his[5], his[6], his[7], his[8], his[9]

def intt10_ref(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9):
    f0, f1, f2, f3, f4, f5, f6, f7, f8, f9 = ntt10_ref(h0, h9, h8, h7, h6, h5, h4, h3, h2, h1)
    return f0 / 10, f1 / 10, f2 / 10, f3 / 10, f4 / 10, f5 / 10, f6 / 10, f7 / 10, f8 / 10, f9 / 10

def ntt9_ref(f0, f1, f2, f3, f4, f5, f6, f7, f8):
    fjs = [f0, f1, f2, f3, f4, f5, f6, f7, f8]
    hjs = [0 for j in range(9)]
    for j in range(9):
        for jj in range(9):
            hjs[j] += w9 ** (j * jj) * fjs[jj]
    return hjs[0], hjs[1], hjs[2], hjs[3], hjs[4], hjs[5], hjs[6], hjs[7], hjs[8]

def intt9_ref(h0, h1, h2, h3, h4, h5, h6, h7, h8):
    f0, f1, f2, f3, f4, f5, f6, f7, f8 = ntt9_ref(h0, h8, h7, h6, h5, h4, h3, h2, h1)
    return f0 / 9, f1 / 9, f2 / 9, f3 / 9, f4 / 9, f5 / 9, f6 / 9, f7 / 9, f8 / 9

def main_basemul_ref(in1_lay2, in2_lay2):
    out_lay2 = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        for j in range(9):
            out_lay2[i][j] = in1_lay2[i][j] * in2_lay2[i][j] % (x ** 16 - w10 ** i * w9 ** j)
    return out_lay2

def low_basemul_ref(in1_lay1, in2_lay1):
    out_lay1 = [0 for i in range(10)]
    for i in range(10):
        out_lay1[i] = in1_lay1[i] * in2_lay1[i] % (x ** 16 - w10 ** i)
    return out_lay1
