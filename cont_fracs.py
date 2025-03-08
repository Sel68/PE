from math import floor

def cont_frac(n):
    m, d, a0 =0, 1, int(n**0.5)
    if a0**2 == n:
        return []

    a, expansion = a0, [a0]
    while True:
        m = d*a - m
        d = (n-m**2)//d
        a = (a0+m)//d
        expansion.append(a)
        if a == 2*a0:
            break
    return expansion
