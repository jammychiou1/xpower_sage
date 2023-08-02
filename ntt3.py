from params import w

w3 = w ** (4590 // 3)

def ntt3_db(f0, f1, f2):
    red = w3 - w3 ** 2

    t0i = f1 + f2
    h0 = 2 * (f0 + t0i)
    t0i -= 2 * f0
    t0o = -t0i
    t1i = f1 - f2
    t1o = red * t1i

    h1 = t0o + t1o
    h2 = t0o - t1o

    return h0, h1, h2

def ntt3_db_noh0(f0, f1, f2):
    red = w3 - w3 ** 2

    t0i = f1 + f2
    t0i -= 2 * f0
    t0o = -t0i
    t1i = f1 - f2
    t1o = red * t1i

    h1 = t0o + t1o
    h2 = t0o - t1o

    return h1, h2

def ntt3_db_nof0(f1, f2):
    red = w3 - w3 ** 2

    t0i = f1 + f2
    h0 = 2 * t0i
    t0o = -t0i
    t1i = f1 - f2
    t1o = red * t1i

    h1 = t0o + t1o
    h2 = t0o - t1o

    return h0, h1, h2

def intt3_sx_noh0(h1, h2):
    return ntt3_db_nof0(h2, h1)
