#include <bits/stdc++.h>
#define fli(i,fc,n) for(int i=fc;i<n;i++)
#define rli(i,n,rc) for(int i=n;i>rc;i--)
#define sz(a) a.size()
#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define nl "\n"
using namespace std;
#define M2 998244353
#define M 1e9+7
#define ff first
#define ss second
#define N 100005


vector<vector<set<int>>> generateKDisjointSubsetGroups(vector<int> v, int k) {
    vector<vector<set<int>>> result;
    int n = sz(v);
    int limit = 1 << n;

    vector<int> masks;
    fli(mask, 1, limit) masks.pb(mask);


    function<void(int, vector<int>&)> dfs = [&](int idx, vector<int>& chosen) {
        if (sz(chosen) == k) {
            int combined = 0;
            bool valid = true;

            for (int m : chosen) {
                if (combined & m) {
                    valid = false;
                    break;
                }
                combined |= m;
            }

            if (valid) {
                vector<set<int>> groups(k);
                fli(i, 0, k) {
                    fli(j, 0, n) {
                        if (chosen[i] & (1 << j)) groups[i].insert(v[j]);
                    }
                }
                result.pb(groups);
            }
            return;
        }

        fli(i, idx, sz(masks)) {
            chosen.pb(masks[i]);
            dfs(i + 1, chosen);
            chosen.pop_back();
        }
    };

    vector<int> selected;
    dfs(0, selected);

    return result;
}

void printingSubsetsTuples(const vector<vector<set<int>>> &partitions){
    for (auto& group : partitions) {
        for (auto& s : group) {
            cout << "{ ";
            for (int x : s) cout << x << " ";
            cout << "} ";
        }
        cout << nl;
    }
    if (partitions.empty()) cout<<"Required number of Disjoint Subsets exceed cardinality of original set.\n";
    else cout << "Total partitions into " << sz(partitions[0]) << " disjoint subsets: " << sz(partitions) << nl;
}

void solve() {

}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    clock_t s = clock();
    solve();
    cout << "Execution Time: " << double(clock() - s) / CLOCKS_PER_SEC << " seconds" << endl;
}
