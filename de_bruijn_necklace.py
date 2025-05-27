def de_bruijn_necklace(k, n):
#Eulerian circuit appraoch
    N = k**n
    m = N//k

    adj = {u: list(range(k)) for u in range(m)}
    used = {u: [0]*k for u in range(m)}
    seq = []  #only edge labels along current path
    seen = set() 

    def dfs(u):
        if len(seq) == N:
            s = "0"*(n-1) + "".join(str(a) for a in seq)
            s = s[:N]
            # normalize by minimal rotation
            minrot = min(s[i:]+s[:i] for i in range(N))
            if minrot not in seen:
                seen.add(minrot)
                yield minrot
            return

        for i in range(k):
            if not used[u][i]:
                used[u][i] = True
                v = (u * k + i) % m
                seq.append(i)
                yield from dfs(v)
                seq.pop()
                used[u][i] = False

    yield from dfs(0)


