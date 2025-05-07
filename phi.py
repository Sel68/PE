import numpy as np

def ephi(hi = int(1e6)):
    phi = np.arange(hi, dtype=int)
    primes = np.ones(hi, dtype=bool)
    primes[0] = primes[1] = 0
    for j in range(2, int(np.sqrt(hi)) + 1):
        if primes[j]:
            phi[j::j] -= phi[j::j] // j
            primes[j*j::j] = 0
    return phi

