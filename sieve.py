def sieve(hi = int(1e6)):
    num = [1 for i in range(hi)]
    num[0] = num[1] = 0
    for i in range(2, hi):
        if num[i]:
            for j in range(i*i, hi, i):
                num[j] = 0
    return num