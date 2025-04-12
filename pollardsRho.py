from math import gcd
import sympy as sp


def pollards_rho(n, c=1):
    if n % 2 == 0:
        return 2
    x = y = 2
    f = lambda x: (x*x + c) % n
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    if d == n:
        return None
    return d

def PFD(n):
    if n == 1:
        return []
    if sp.isprime(n):
        return [n]
    d, c = None, 1
    while d is None:
        d = pollards_rho(n, c)
        c += 1
    return PFD(d) + PFD(n // d)

