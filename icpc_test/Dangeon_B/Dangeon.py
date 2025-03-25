#!/usr/bin/env python3
import sys
from collections import deque

sys.setrecursionlimit(10000)
limit = 10
data = []
line_count = 0
    
for line in sys.stdin:
    if line_count >= limit:
        break
    data.extend(line.split())
    line_count += 1
    
it = iter(data)
def ni():
    return int(next(it))

# Read the tree
n = ni()
q = ni()
adj = [[] for _ in range(n)]
sumW = 0
for _ in range(n - 1):
    u = ni() - 1
    v = ni() - 1
    w = ni()
    adj[u].append((v, w))
    adj[v].append((u, w))
    sumW += w
total = 2 * sumW

# Precompute, for each starting room s:
#   dist_all[s][v] = distance from s to v
#   next_all[s][v] = first neighbor of s on the unique path from s to v (for v != s)
dist_all = [None] * n
next_all = [None] * n

INF = 10**9
for s in range(n):
    dist = [10**9] * n
    nxt = [-1] * n
    dist[s] = 0
    # We'll use a stack for DFS; each element is (current, parent)
    stack = [(s, -1)]
    while stack:
        u, parent = stack.pop()
        for v, w in adj[u]:
            if v == parent:
                continue
            nd = dist[u] + w
            # Since it's a tree, the first time we see v is the unique path
            if nd < dist[v]:
                dist[v] = nd
                # For direct neighbor of s, the first step is v; else inherit from u.
                nxt[v] = v if u == s else nxt[u]
                stack.append((v, u))
    dist_all[s] = dist
    next_all[s] = nxt

# For each s, build for each neighbor u of s (i.e. each possible "first step"):
#   comp[s][u] = set of vertices v (v != s) such that next_all[s][v] == u
#   maxComp[s][u] = maximum distance from s among v in comp[s][u]
comp = [dict() for _ in range(n)]
maxComp = [dict() for _ in range(n)]
for s in range(n):
    for v in range(n):
        if v == s:
            continue
        u = next_all[s][v]
        if u < 0:
            continue
        if u not in comp[s]:
            comp[s][u] = set()
            maxComp[s][u] = 0
        comp[s][u].add(v)
        if dist_all[s][v] > maxComp[s][u]:
            maxComp[s][u] = dist_all[s][v]

# Process queries. For each query (s, k, t) (1-indexed), let:
#   u = next_all[s][t]
# Then, if key k is in comp[s][u] and dist_all[s][k] >= dist_all[s][t],
# the route is impossible (trap is reached before key). Otherwise, answer = total - maxComp[s][u].
out_lines = []
for _ in range(q):
    s = ni() - 1
    key = ni() - 1
    trap = ni() - 1
    u = next_all[s][trap]  # first neighbor on path from s to trap
    # It is guaranteed that trap != s, so u is defined.
    D = maxComp[s][u]
    # If the key is in the branch of u (i.e. next_all[s][key] == u) and key is reached no sooner than trap,
    # then the key would be visited after trap, making it impossible.
    if u in comp[s] and key in comp[s][u]:
        if dist_all[s][key] >= dist_all[s][trap]:
            out_lines.append("impossible")
            continue
    ans = total - D
    out_lines.append(str(ans))
sys.stdout.write("\n".join(out_lines))
