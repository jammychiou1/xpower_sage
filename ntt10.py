from params import w
from ntt5 import ntt5_4x_nof14, ntt5_4x_nof03, ntt5_4x_nof023, ntt5_4x, ntt5_4x_noh23, ntt5_4x_noh04

w10 = w ** (4590 // 10)

def ntt10_4x_nof3456(f0, f1, f2, f7, f8, f9):
    h0, h2, h4, h6, h8 = ntt5_4x_nof14(f0, f2, f8)
    h5, h7, h9, h1, h3 = ntt5_4x_nof03(f1, f7, f9)
    h0, h5 = h0 + h5, h0 - h5
    h2, h7 = h2 + h7, h2 - h7
    h4, h9 = h4 + h9, h4 - h9
    h6, h1 = h6 + h1, h6 - h1
    h8, h3 = h8 + h3, h8 - h3
    return h0, h1, h2, h3, h4, h5, h6, h7, h8, h9

def ntt10_4x_nof34567(f0, f1, f2, f8, f9):
    h0, h2, h4, h6, h8 = ntt5_4x_nof14(f0, f2, f8)
    h5, h7, h9, h1, h3 = ntt5_4x_nof023(f1, f9)
    h0, h5 = h0 + h5, h0 - h5
    h2, h7 = h2 + h7, h2 - h7
    h4, h9 = h4 + h9, h4 - h9
    h6, h1 = h6 + h1, h6 - h1
    h8, h3 = h8 + h3, h8 - h3
    return h0, h1, h2, h3, h4, h5, h6, h7, h8, h9

def ntt10_4x_noh3456(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9):
    h0, h2, h8 = ntt5_4x_noh23(f0 + f5, f6 + f1, f2 + f7, f8 + f3, f4 + f9)
    h7, h9, h1 = ntt5_4x_noh04(f0 - f5, f6 - f1, f2 - f7, f8 - f3, f4 - f9)
    return h0, h1, h2, h7, h8, h9

def ntt10_4x(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9):
    h0, h2, h4, h6, h8 = ntt5_4x(f0, f6, f2, f8, f4)
    h5, h7, h9, h1, h3 = ntt5_4x(f5, f1, f7, f3, f9)
    h0, h5 = h0 + h5, h0 - h5
    h2, h7 = h2 + h7, h2 - h7
    h4, h9 = h4 + h9, h4 - h9
    h6, h1 = h6 + h1, h6 - h1
    h8, h3 = h8 + h3, h8 - h3
    return h0, h1, h2, h3, h4, h5, h6, h7, h8, h9

def intt10_40x(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9):
    return ntt10_4x(h0, h9, h8, h7, h6, h5, h4, h3, h2, h1)

def intt10_40x_nof3456(h0, h1, h2, h3, h4, h5, h6, h7, h8, h9):
    return ntt10_4x_noh3456(h0, h9, h8, h7, h6, h5, h4, h3, h2, h1)
