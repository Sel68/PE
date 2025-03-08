def ephi(hi = int(1e6)):
    phi = [i for i in range(hi)]

    for j in range(2,hi):
        if phi[j] == j:
            for k in range(j,hi,j):
                phi[k]  = phi[k]*(j-1)//j
    return phi
        
print(ephi(10)[:10])