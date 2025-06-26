def mobius_upto(n):
    mo = [1]*(n+1)
    primes = [True]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            mo[i]*=-1
            for j in range(2*i, n+1, i):
                primes[j]=0
                mo[j]*=-1
            for j in range(i*i, n+1, i*i):
                mo[j]=0
    return mo