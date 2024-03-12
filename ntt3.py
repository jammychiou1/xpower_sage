from params import w

w3 = w ** (4590 // 3)
red = w3 - w3 ** 2

def ntt3_2xh12(f0, f1, f2):
    v0, v1, v2 = f0, f1, f2
    v1, v2 = v1 + v2, v1 - v2
    v0, v1 = v0 + v1, 2 * v0 - v1
    v2 *= red
    v1, v2 = v1 + v2, v1 - v2
    h0, h1, h2 = v0, v1, v2
    return h0, h1, h2

def intt3_6x(h0, h1, h2):
    return ntt3_2x(h0, h2, h1)
