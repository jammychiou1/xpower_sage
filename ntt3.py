from params import w

w3 = w ** (4590 // 3)

def ntt3_db(f0, f1, f2):
    red = w3 - w3 ** 2

    t0i = f1 + f2
    t0o = -t0i
    t1i = f1 - f2
    t1o = red * t1i

    g1 = t0o + t1o
    g2 = t0o - t1o

    g0 = 2 * t0i
    db_f0 = 2 * f0

    h0 = g0 + db_f0
    h1 = g1 + db_f0
    h2 = g2 + db_f0
    return h0, h1, h2

def ntt3_db_noh0(f0, f1, f2):
    red = w3 - w3 ** 2

    t0i = f1 + f2
    t0o = -t0i
    t1i = f1 - f2
    t1o = red * t1i

    g1 = t0o + t1o
    g2 = t0o - t1o

    db_f0 = 2 * f0

    h1 = g1 + db_f0
    h2 = g2 + db_f0
    return h1, h2

def intt3_sx_noh0(h1, h2):
    red = w3 ** 2 - w3

    t0i = h1 + h2
    t0o = -t0i
    t1i = h1 - h2
    t1o = red * t1i

    g1 = t0o + t1o
    g2 = t0o - t1o

    g0 = 2 * t0i

    h0 = g0
    h1 = g1
    h2 = g2
    return h0, h1, h2
