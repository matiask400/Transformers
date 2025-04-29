#include <bits/stdc++.h>
using namespace std;
 
// Tamaño máximo (n ≤ 2000)
const int MAXN = 2100;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, q;
    cin >> n >> q;
    vector<vector<pair<int,int>>> adj(n);
    long long sumW = 0;
    for (int i = 0; i < n - 1; i++){
        int u, v, w;
        cin >> u >> v >> w;
        u--; v--;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
        sumW += w;
    }
    // El coste total sin ahorro es 2·(suma de pesos)
    long long total = 2 * sumW;
 
    // Pre-computación: para cada vértice s, se calcula
    //  – distAll[s][v]: la distancia de s a v
    //  – nextStepAll[s][v]: el primer vértice (vecino de s) en la ruta única de s a v.
    vector<vector<int>> distAll(n, vector<int>(n, INT_MAX));
    vector<vector<int>> nextStepAll(n, vector<int>(n, -1));
    for (int s = 0; s < n; s++){
        vector<int> dist(n, INT_MAX), nxt(n, -1);
        queue<int> qu;
        dist[s] = 0;
        qu.push(s);
        while(!qu.empty()){
            int u = qu.front();
            qu.pop();
            for (auto &edge : adj[u]){
                int v = edge.first, w = edge.second;
                if(dist[v] > dist[u] + w){
                    dist[v] = dist[u] + w;
                    // Si u es s, el primer paso para v es v; de lo contrario, se hereda el de u.
                    nxt[v] = (u == s ? v : nxt[u]);
                    qu.push(v);
                }
            }
        }
        distAll[s] = dist;
        nextStepAll[s] = nxt;
    }
 
    // Para cada s y para cada posible vecino u de s, se pre-computa:
    //   comp[s][u]: un bitset que marca los vértices v (v ≠ s) tales que el primer paso en la ruta de s a v es u.
    //   maxComp[s][u]: = max { distAll[s][v] : v con primer paso u }.
    vector<vector<bitset<MAXN>>> comp(n, vector<bitset<MAXN>>(n));
    vector<vector<int>> maxComp(n, vector<int>(n, -1));
    for (int s = 0; s < n; s++){
        for (int v = 0; v < n; v++){
            if(v == s) continue;
            int u = nextStepAll[s][v];
            if(u >= 0){
                comp[s][u].set(v, true);
                maxComp[s][u] = max(maxComp[s][u], distAll[s][v]);
            }
        }
    }
 
    // Para cada consulta se utiliza la siguiente estrategia:
    //   - Sea u = nextStepAll[s][t]: es el primer paso en la ruta única de s a t.
    //   - Sea D = maxComp[s][u] = max { d(s,v) : v con primer paso u }.
    //   - Si k ∈ comp[s][u] y d(s,k) ≥ d(s,t) entonces no es posible (se visitaría t antes que k).
    //   - En caso contrario, la respuesta es total − D.
    for (int i = 0; i < q; i++){
        int s, k, t;
        cin >> s >> k >> t;
        s--; k--; t--;
        int u = nextStepAll[s][t]; // primer paso en la ruta de s a t
        int D = maxComp[s][u];
        if(comp[s][u].test(k)){
            if(distAll[s][k] >= distAll[s][t]){
                cout << "impossible" << "\n";
                continue;
            }
        }
        long long ans = total - D;
        cout << ans << "\n";
    }
 
    return 0;
}
