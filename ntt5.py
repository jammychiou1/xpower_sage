from params import w

w5 = w ** (4590 // 5)
red = w5 + w5 ** 4 - w5 ** 3 - w5 ** 2
green = 2 * (w5 - w5 ** 4)
blue = 2 * (w5 - w5 ** 4 + w5 ** 3 - w5 ** 2)
yellow = 2 * (w5 ** 3 - w5 ** 2)

def ntt5_4x(f0, f1, f2, f3, f4):
    v0, v1, v2, v3, v4 = f0, f1, f2, f4, f3
    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    v1, v2 = v1 + v2, v1 - v2
    v0, v1 = v0 + v1, 4 * v0 - v1
    v2 = red * v2
    v0 = 4 * v0
    v1, v2 = v1 + v2, v1 - v2

    v3, v4, v5 = v3, v3 + v4, v4
    v3, v4, v5 = green * v3, blue * v4, yellow * v5
    v3, v4 = v3 - v5, v4 - v3 - v5

    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    h0, h1, h3, h4, h2 = v0, v1, v2, v3, v4

    return h0, h1, h2, h3, h4

def ntt5_4x_nof14(f0, f2, f3):
    v0, v2, v4 = f0, f2, f3
    v2, v4 = v2 + v4, v2 - v4

    v1, v2 = v2, -v2
    v0, v1 = v0 + v1, 4 * v0 - v1
    v2 = red * v2
    v0 = 4 * v0
    v1, v2 = v1 + v2, v1 - v2

    v4, v5 = v4, v4
    v4, v5 = blue * v4, yellow * v5
    v3, v4 = -v5, v4 - v5

    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    h0, h1, h3, h4, h2 = v0, v1, v2, v3, v4

    return h0, h1, h2, h3, h4

def ntt5_4x_nof023(f1, f4):
    v1, v3 = f1, f4
    v1, v3 = v1 + v3, v1 - v3

    v1, v2 = v1, v1
    v0, v1 = v1, -v1
    v2 = red * v2
    v0 = 4 * v0
    v1, v2 = v1 + v2, v1 - v2

    v3, v4 = v3, v3
    v3, v4 = green * v3, blue * v4
    v3, v4 = v3, v4 - v3

    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    h0, h1, h3, h4, h2 = v0, v1, v2, v3, v4

    return h0, h1, h2, h3, h4

def ntt5_4x_nof03(f1, f2, f4):
    v1, v2, v3 = f1, f2, f4
    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2, v2

    v1, v2 = v1 + v2, v1 - v2
    v0, v1 = v1, -v1
    v2 = red * v2
    v0 = 4 * v0
    v1, v2 = v1 + v2, v1 - v2

    v3, v4, v5 = v3, v3 + v4, v4
    v3, v4, v5 = green * v3, blue * v4, yellow * v5
    v3, v4 = v3 - v5, v4 - v3 - v5

    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    h0, h1, h3, h4, h2 = v0, v1, v2, v3, v4

    return h0, h1, h2, h3, h4

def ntt5_4x_noh04(f0, f1, f2, f3, f4):
    v0, v1, v2, v3, v4 = f0, f1, f2, f4, f3
    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    v1, v2 = v1 + v2, v1 - v2
    v1 = 4 * v0 - v1
    v2 = red * v2
    v1, v2 = v1 + v2, v1 - v2

    v3, v4, v5 = v3, v3 + v4, v4
    v3, v4, v5 = green * v3, blue * v4, yellow * v5
    v3, v4 = v3 - v5, v4 - v3 - v5

    v1 = v1 + v3
    v2, v4 = v2 + v4, v2 - v4

    h1, h3, h2 = v1, v2, v4

    return h1, h2, h3

def ntt5_4x_noh23(f0, f1, f2, f3, f4):
    v0, v1, v2, v3, v4 = f0, f1, f2, f4, f3
    v1, v3 = v1 + v3, v1 - v3
    v2, v4 = v2 + v4, v2 - v4

    v1, v2 = v1 + v2, v1 - v2
    v0, v1 = v0 + v1, 4 * v0 - v1
    v2 = red * v2
    v0 = 4 * v0
    v1 = v1 + v2

    v3, v5 = v3, v4
    v3, v5 = green * v3, yellow * v5
    v3 = v3 - v5

    v1, v3 = v1 + v3, v1 - v3

    h0, h1, h4 = v0, v1, v3

    return h0, h1, h4
