import numpy as np

def sieve(hi=int(1e6)):
    if hi < 2:
        return np.zeros(hi, dtype=bool)
    is_prime = np.ones(hi, dtype=bool)
    is_prime[0] = False
    for p in range(3, int(hi**0.5) + 1, 2):
        if is_prime[p]:
            is_prime[p*p::2*p] = False
    return is_prime