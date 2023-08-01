from params import w
from ntt5 import ntt5_qd_nof14, ntt5_qd_nof03, ntt5_qd_nof023, ntt5_qd

w10 = w ** (4590 // 10)

def ntt10_qd_nof3456(f0, f1, f2, f7, f8, f9):
    h0, h2, h4, h6, h8 = ntt5_qd_nof14(f0, f2, f8)
    h5, h7, h9, h1, h3 = ntt5_qd_nof03(f1, f7, f9)
    h0, h5 = h0 + h5, h0 - h5
    h2, h7 = h2 + h7, h2 - h7
    h4, h9 = h4 + h9, h4 - h9
    h6, h1 = h6 + h1, h6 - h1
    h8, h3 = h8 + h3, h8 - h3
    return h0, h1, h2, h3, h4, h5, h6, h7, h8, h9

def ntt10_qd_nof34567(f0, f1, f2, f8, f9):
    h0, h2, h4, h6, h8 = ntt5_qd_nof14(f0, f2, f8)
    h5, h7, h9, h1, h3 = ntt5_qd_nof023(f1, f9)
    h0, h5 = h0 + h5, h0 - h5
    h2, h7 = h2 + h7, h2 - h7
    h4, h9 = h4 + h9, h4 - h9
    h6, h1 = h6 + h1, h6 - h1
    h8, h3 = h8 + h3, h8 - h3
    return h0, h1, h2, h3, h4, h5, h6, h7, h8, h9

def ntt10_qd(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9):
    h0, h2, h4, h6, h8 = ntt5_qd(f0, f6, f2, f8, f4)
    h5, h7, h9, h1, h3 = ntt5_qd(f5, f1, f7, f3, f9)
    h0, h5 = h0 + h5, h0 - h5
    h2, h7 = h2 + h7, h2 - h7
    h4, h9 = h4 + h9, h4 - h9
    h6, h1 = h6 + h1, h6 - h1
    h8, h3 = h8 + h3, h8 - h3
    return h0, h1, h2, h3, h4, h5, h6, h7, h8, h9

def intt10_40x(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9):
    return ntt10_qd(h0, h9, h8, h7, h6, h5, h4, h3, h2, h1)

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