from params import w

w5 = w ** (4590 // 5)

def ntt5_4x_nof14(f0, f2, f3):
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

def ntt5_4x_nof023(f1, f4):
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

def ntt5_4x_nof03(f1, f2, f4):
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

def ntt5_4x(f0, f1, f2, f3, f4):
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

def ntt5_4x_noh04(f0, f1, f2, f3, f4):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    ci0 = f1 + f4
    ci1 = f3 + f2
    ct0i = ci0 + ci1
    # h0 = 4 * (f0 + ct0i)
    ct0i -= 4 * f0
    ct0o = - ct0i
    ct1i = ci0 - ci1
    ct1o = red * ct1i
    co0 = ct0o + ct1o
    co1 = ct0o - ct1o

    ni0 = f1 - f4
    ni1 = f3 - f2
    nt0i = ni0 - ni1
    nt1i = ni1
    nt2i = -ni0 - ni1
    nt0o = green * nt0i
    nt1o = blue * nt1i
    nt2o = yellow * nt2i
    no0 = nt0o + nt1o
    no1 = nt1o + nt2o

    h1 = co0 + no0
    h2 = co1 + no1
    # h4 = co0 - no0
    h3 = co1 - no1

    return h1, h2, h3

def ntt5_4x_noh23(f0, f1, f2, f3, f4):
    red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
    green = 2 * (w5 - w5 ** 4)
    blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
    yellow = 2 * (w5 ** 3 - w5 ** 2)

    ci0 = f1 + f4
    ci1 = f3 + f2
    ct0i = ci0 + ci1
    h0 = 4 * (f0 + ct0i)
    ct0i -= 4 * f0
    ct0o = - ct0i
    ct1i = ci0 - ci1
    ct1o = red * ct1i
    co0 = ct0o + ct1o
    # co1 = ct0o - ct1o

    ni0 = f1 - f4
    ni1 = f3 - f2
    nt0i = ni0 - ni1
    nt1i = ni1
    # nt2i = -ni0 - ni1
    nt0o = green * nt0i
    nt1o = blue * nt1i
    # nt2o = yellow * nt2i
    no0 = nt0o + nt1o
    # no1 = nt1o + nt2o

    h1 = co0 + no0
    # h2 = co1 + no1
    h4 = co0 - no0
    # h3 = co1 - no1

    return h0, h1, h4

def intt5_20x_nof04(h0, h1, h2, h3, h4):
    return ntt5_4x_noh04(h0, h4, h3, h2, h1)

def intt5_20x_nof23(h0, h1, h2, h3, h4):
    return ntt5_4x_noh23(h0, h4, h3, h2, h1)
