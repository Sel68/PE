#include <iostream>
using namespace std;
#define ll long long

// returns n and n+1
pair<ll, ll> fibPair(ll n, ll M) {
    if (n == 0) return {0,1};
    auto [a, b] = fibPair(n >> 1, M);
    ll c = a * ((b*2 - a + M) % M) % M;
    ll d = (a*a + b*b) % M;
    if (n & 1)
        return {d, ((c + d) % M)};
    else
        return {c, d};
}


// def fibPair(n, M):
//     if n == 0:
//         return (0, 1)
    
//     a, b = fibPair(n>>1, M)
//     c = (a * ((b * 2 - a + M) % M)) % M
//     d = (a * a + b * b) % M
    
//     if n % 2 == 1:
//         return (d, (c + d) % M)
//     else:
//         return (c, d)
