def factors(n):
    d = 2
    while n >= d * d:
        if n % d == 0:
            n = n // d
            yield d
        else:
            d += 1
    if n > 1:
        yield n


def gcd(a, b):
    r = a % b
    while r > 0:
        a, b, r = b, r, b % r
    return b


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def crt(a, b, p, q):
    """
    Chinese Remainder Theorem

    https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    """
    if gcd(p, q) != 1:
        raise RuntimeError("p and q must be coprime")
    p_inv = mul_inv(p, q)
    q_inv = mul_inv(q, p)
    M = p * q
    return ((a * q * q_inv) + (b * p * p_inv)) % M
