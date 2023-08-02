from params import w, Rq, Zq, x
from sage.all import vector

w9 = w ** (4590 // 9)
w10 = w ** (4590 // 10)

# V16 = VectorSpace(Zq, 16)
# M16 = MatrixSpace(Zq, 16)
# V8 = VectorSpace(Zq, 8)
# M8 = MatrixSpace(Zq, 8)

def to_vec(f, dim):
    return vector(Zq, [f[i] for i in range(dim)])

def to_tpm(f, twiddle, dim):
    v = to_vec(f, dim)
    return twiddle * v, v

def mla_tpm_vec(m_col, m_row, v, acc):
    l = len(v)
    for i, s in enumerate(v):
        col = vector([*m_row[l - i:], *m_col[:l - i]])
        acc += s * col
    return acc

def main_basemul(in1_lay2, in2_lay2):
    out_lay2 = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        for j in range(9):
            tw = w10 ** i * w9 ** j
            a = to_vec(in1_lay2[i][j], 16)
            b = to_vec(in2_lay2[i][j], 16)
            if i % 2 == 0:
                # ntt 2
                sqrt_tw = w10 ** (i // 2) * w9 ** (5 * j)

                a0, a1 = a[:8], a[8:]
                b0, b1 = b[:8], b[8:]

                a0, a1 = a0 + sqrt_tw * a1, a0 - sqrt_tw * a1
                b0, b1 = b0 + sqrt_tw * b1, b0 - sqrt_tw * b1

                c0 = 0
                b0_col = b0
                b0_row = sqrt_tw * b0
                c0 = mla_tpm_vec(b0_col, b0_row, a0, c0)

                c1 = 0
                b1_col = b1
                b1_row = -sqrt_tw * b1
                c1 = mla_tpm_vec(b1_col, b1_row, a1, c1)

                c0, c1 = (1 / Zq(2)) * (c0 + c1), (1 / Zq(2 * sqrt_tw)) * (c0 - c1)
                c = vector([*c0, *c1])
            else:
                # karatsuba
                a0, a1 = a[:8], a[8:]
                b0, b1 = b[:8], b[8:]

                c0 = 0
                m1_col = b0
                m1_row = tw * b1
                c0 = mla_tpm_vec(m1_col, m1_row, a0 + a1, c0)
                c1 = c0

                m2_col = tw * b1 - b0
                m2_row = tw * b0 - tw * b1
                c0 = mla_tpm_vec(m2_col, m2_row, a1, c0)

                m3_col = b1 - b0
                m3_row = b0 - tw * b1
                c1 = mla_tpm_vec(m3_col, m3_row, a0, c1)

                c = vector([*c0, *c1])
            out_lay2[i][j] = Rq(list(c))
    return out_lay2

def main_basemul_ref(in1_lay2, in2_lay2):
    out_lay2 = [[0 for j in range(9)] for i in range(10)]
    for i in range(10):
        for j in range(9):
            out_lay2[i][j] = in1_lay2[i][j] * in2_lay2[i][j] % (x ** 16 - w10 ** i * w9 ** j)
    return out_lay2

def low_basemul(in1_lay1, in2_lay1):
    out_lay1 = [0 for i in range(10)]
    for i in range(10):
        out_lay1[i] = in1_lay1[i] * in2_lay1[i] % (x ** 16 - w10 ** i)
        out_lay1[i] *= w10 ** i
    return out_lay1

def low_basemul_ref(in1_lay1, in2_lay1):
    out_lay1 = [0 for i in range(10)]
    for i in range(10):
        out_lay1[i] = in1_lay1[i] * in2_lay1[i] % (x ** 16 - w10 ** i)
    return out_lay1
