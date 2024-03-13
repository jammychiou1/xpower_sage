from params import w

w3 = w ** (4590 // 3)
w9 = w ** (4590 // 9)
red = w3 - w3 ** 2
green = w9 ** 8 / 2
blue = w9 / 2

def ntt3_2xh12(f0, f1, f2):
    v0, v1, v2 = f0, f1, f2
    v1, v2 = v1 + v2, v1 - v2
    v0, v1 = v0 + v1, 2 * v0 - v1
    v2 = red * v2
    v1, v2 = v1 + v2, v1 - v2
    h0, h1, h2 = v0, v1, v2
    return h0, h1, h2

def ntt3_2xf12(f0, f1, f2):
    v0, v1, v2 = f0, f1, f2
    v1, v2 = v1 + v2, v1 - v2
    v0, v1 = v0 + 2 * v1, v0 - v1
    v2 = red * v2
    v1, v2 = v1 + v2, v1 - v2
    h0, h1, h2 = v0, v1, v2
    return h0, h1, h2

def ntt9_2x(f0, f1, f2, f3, f4, f5, f6, f7, f8):
    v0, v1, v2 = f0, f3, f6
    v0, v1, v2 = ntt3_2xh12(v0, v1, v2)
    v0 = 2 * v0

    v3, v4, v5 = f1, f7, f4
    v3, v4, v5 = ntt3_2xh12(v3, v4, v5)
    v4, v5 = green * v4, blue * v5

    v6, v7, v8 = f8, f2, f5
    v6, v7, v8 = ntt3_2xh12(v6, v7, v8)
    v7, v8 = green * v7, blue * v8

    v1, v3 = v3, v1
    v2, v6 = v6, v2
    v4, v7 = v7, v4

    v0, v1, v2 = ntt3_2xf12(v0, v1, v2)
    v3, v4, v5 = ntt3_2xf12(v3, v4, v5)
    v6, v7, v8 = ntt3_2xf12(v6, v7, v8)

    h0, h3, h6 = v0, v1, v2
    h1, h7, h4 = v3, v4, v5
    h8, h2, h5 = v6, v7, v8

    return h0, h1, h2, h3, h4, h5, h6, h7, h8

def intt9_18x(h0, h1, h2, h3, h4, h5, h6, h7, h8):
    return ntt9_2x(h0, h8, h7, h6, h5, h4, h3, h2, h1)

