from params import w, Rq, Zq, x
from sage.all import vector

w10 = w ** (4590 // 10)
w9 = w ** (4590 // 9)

# V16 = VectorSpace(Zq, 16)
# M16 = MatrixSpace(Zq, 16)
# V8 = VectorSpace(Zq, 8)
# M8 = MatrixSpace(Zq, 8)

def to_vec(f, dim):
    return vector(Zq, [f[i] for i in range(dim)])

def to_tpm(f, twiddle, dim):
    v = to_vec(f, dim)
    return twiddle * v, v

def mul_tpm_vec(m_col, m_row, v):
    l = len(v)
    res = 0
    for i, s in enumerate(v):
        col = vector([*m_row[l - i:], *m_col[:l - i]])
        res += s * col
    return res

def kara(col, row, v, n0):
    n = len(v)
    if n == n0:
        return mul_tpm_vec(col, row, v)

    v0, v1 = v[:n // 2], v[n // 2:]
    col0, col1 = col[:n // 2], col[n // 2:]
    row0, row1 = row[:n // 2], row[n // 2:]

    tmp = kara(col0, row1, v0 + v1, n0)
    c0 = tmp + kara(row1 - col0, row0 - row1, v1, n0)
    c1 = tmp - kara(col0 - col1, row1 - col0, v0, n0)

    return vector([*c0, *c1])

def radix2(a, b, i, j, n0):
    n = len(a)
    if n == n0:
        tw = w10 ** i * w9 ** j
        return mul_tpm_vec(b, tw * b, a)

    a0, a1 = a[:n // 2], a[n // 2:]
    b0, b1 = b[:n // 2], b[n // 2:]

    sqrt_tw = w10 ** (3 * i % 10) * w9 ** (5 * j % 9)
    a0, a1 = a0 + sqrt_tw * a1, a0 - sqrt_tw * a1
    b0, b1 = b0 + sqrt_tw * b1, b0 - sqrt_tw * b1

    c0 = radix2(a0, b0, 3 * i % 10, 5 * j % 9, n0)
    c1 = kara(b1, -sqrt_tw * b1, a1, n0)
    c0, c1 = (1 / Zq(2)) * (c0 + c1), (1 / Zq(2 * sqrt_tw)) * (c0 - c1)
    return vector([*c0, *c1])

def mixed(a, b, i, j, n0):
    if i % 2 == 1:
        tw = w10 ** i * w9 ** j
        return kara(b, tw * b, a, n0)
    else:
        return radix2(a, b, i, j, n0)

def main_basemul(in1_lay2, in2_lay2):
    out_lay2 = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        for j in range(9):
            tw = w10 ** i * w9 ** j
            a = to_vec(in1_lay2[i][j], 16)
            b = to_vec(in2_lay2[i][j], 16)
            c = mixed(a, b, i, j, 4)
            out_lay2[i][j] = Rq(list(c))
    return out_lay2

def low_basemul(in1_lay1, in2_lay1):
    out_lay1 = [0 for i in range(10)]
    for i in range(10):
        tw = w10 ** i
        a = to_vec(in1_lay1[i], 16)
        b = to_vec(in2_lay1[i], 16)
        c = mixed(a, b, i, 0, 4)
        out_lay1[i] = Rq(list(c))
        out_lay1[i] *= 72 * w10 ** i
    return out_lay1
