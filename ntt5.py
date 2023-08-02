from params import w

w5 = w ** (4590 // 5)

def ntt5_qd_nof14(f0, f2, f3):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    ci1 = f2 + f3
    ct0i = ci1
    h0 = 4 * (f0 + ct0i)
    ct0i -= 4 * f0
    ct0o = -ct0i
    ct1i = -ci1
    ct1o = red * ct1i
    co0 = ct0o + ct1o
    co1 = ct0o - ct1o

    ni1 = f2 - f3
    nt1i = ni1
    nt1o = blue * nt1i
    nt2i = ni1
    nt2o = yellow * nt2i
    no0 = -nt2o
    no1 = nt1o - nt2o

    h1 = co0 + no0
    h3 = co1 + no1
    h4 = co0 - no0
    h2 = co1 - no1

    return h0, h1, h2, h3, h4

def ntt5_qd_nof023(f1, f4):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    ci0 = f1 + f4
    ct0i = ci0
    h0 = 4 * ct0i
    ct0o = -ct0i
    ct1i = ci0
    ct1o = red * ct1i
    co0 = ct0o + ct1o
    co1 = ct0o - ct1o

    ni0 = f1 - f4
    nt0i = ni0
    nt0o = green * nt0i
    nt1i = ni0
    nt1o = blue * nt1i
    no0 = nt0o
    no1 = nt1o - nt0o

    h1 = co0 + no0
    h3 = co1 + no1
    h4 = co0 - no0
    h2 = co1 - no1

    return h0, h1, h2, h3, h4

def ntt5_qd_nof03(f1, f2, f4):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    ci0 = f1 + f4
    ci1 = f2
    ct0i = ci0 + ci1
    h0 = 4 * ct0i
    ct0o = -ct0i
    ct1i = ci0 - ci1
    ct1o = red * ct1i
    co0 = ct0o + ct1o
    co1 = ct0o - ct1o

    ni0 = f1 - f4
    ni1 = f2
    nt0i = ni0
    nt1i = ni0 + ni1
    nt2i = ni1
    nt0o = green * nt0i
    nt1o = blue * nt1i
    nt2o = yellow * nt2i
    no0 = nt0o - nt2o
    no1 = nt1o - nt0o - nt2o

    h1 = co0 + no0
    h3 = co1 + no1
    h4 = co0 - no0
    h2 = co1 - no1

    return h0, h1, h2, h3, h4

def ntt5_qd(f0, f1, f2, f3, f4):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    ci0 = f1 + f4
    ci1 = f2 + f3
    ct0i = ci0 + ci1
    h0 = 4 * (f0 + ct0i)
    ct0i -= 4 * f0
    ct0o = -ct0i
    ct1i = ci0 - ci1
    ct1o = red * ct1i
    co0 = ct0o + ct1o
    co1 = ct0o - ct1o

    ni0 = f1 - f4
    ni1 = f2 - f3
    nt0i = ni0
    nt1i = ni0 + ni1
    nt2i = ni1
    nt0o = green * nt0i
    nt1o = blue * nt1i
    nt2o = yellow * nt2i
    no0 = nt0o - nt2o
    no1 = nt1o - nt0o - nt2o

    h1 = co0 + no0
    h3 = co1 + no1
    h4 = co0 - no0
    h2 = co1 - no1

    return h0, h1, h2, h3, h4

'''
def ntt5_qd_noh14(f0, f1, f2, f3, f4):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    co0 = f2 + f3
    ci1 = f2 + f3
    ct0 = -ci1
    ct1 = -red * ci1
    co0 = ct0 + ct1
    co1 = ct0 - ct1

    ni1 = f2 - f3
    nt1 = blue * ni1
    nt2 = yellow * ni1
    no0 = -nt2
    no1 = nt1 - nt2

    g1 = co0 + no0
    g3 = co1 + no1
    g4 = co0 - no0
    g2 = co1 - no1

    g0 = 4 * ci1

    qd_f0 = 4 * f0
    h0 = qd_f0 + g0
    h1 = qd_f0 + g1
    h2 = qd_f0 + g2
    h3 = qd_f0 + g3
    h4 = qd_f0 + g4
    return h0, h1, h2, h3, h4
'''
