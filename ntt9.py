from params import w
from ntt3 import ntt3_db, intt3_sx_noh0

w9 = w ** (4590 // 9)

# TODO: revisit add g0/g3/g6 timing
def ntt9_qd(f0, f1, f2, f3, f4, f5, f6, f7, f8):
    f0, f3, f6 = ntt3_db(f0, f3, f6)
    g3 = 2 * f3
    g6 = 2 * f6

    f1, f7, f4 = ntt3_db(f1, f7, f4)
    f7 *= w9 ** 8
    f4 *= w9

    f8, f2, f5 = ntt3_db(f8, f2, f5)
    f2 *= w9 ** 8
    f5 *= w9

    h0, h3, h6 = ntt3_db(f0, f1, f8)

    f7, f2 = f2, f7

    g1, g7, g4 = intt3_sx_noh0(f7, f4)
    g8, g2, g5 = intt3_sx_noh0(f2, f5)

    h1 = g1 + g3
    h5 = g2 + g6
    h7 = g4 + g3
    h8 = g8 + g6
    h4 = g7 + g3
    h2 = g5 + g6

    return h0, h1, h2, h3, h4, h5, h6, h7, h8

def intt9_36x(h0, h1, h2, h3, h4, h5, h6, h7, h8):
    return ntt9_qd(h0, h8, h7, h6, h5, h4, h3, h2, h1)

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
