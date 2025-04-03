# Precompute smallest prime factors up to 100,000
MAX = 100001
spf = [0] * MAX
for i in range(2, MAX):
    if spf[i] == 0:
        spf[i] = i
        if i * i < MAX:
            for j in range(i * i, MAX, i):
                if spf[j] == 0:
                    spf[j] = i
# For 0 and 1
spf[0] = spf[1] = 1

def largest_component_size(A):
    from collections import defaultdict

    # Union-Find implementation
    parent = list(range(len(A)))
    size = [1] * len(A)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if size[u_root] < size[v_root]:
            parent[u_root] = v_root
            size[v_root] += size[u_root]
        else:
            parent[v_root] = u_root
            size[u_root] += size[v_root]

    factor_map = {}
    for idx, num in enumerate(A):
        x = num
        factors = set()
        while x > 1:
            factor = spf[x]
            factors.add(factor)
            while x % factor == 0:
                x //= factor
        for factor in factors:
            if factor in factor_map:
                union(idx, factor_map[factor])
            else:
                factor_map[factor] = idx

    # Count the size of each connected component
    count = defaultdict(int)
    for i in range(len(A)):
        root = find(i)
        count[root] +=1
    return max(count.values()) if count else 0

def run_tests():
    tests = [
        ([4,6,15,35], 4),
        ([20,50,9,63], 2),
        ([2,3,6,7,4,12,21,39], 8)
    ]
    correct = 0
    total = len(tests)
    for input_A, expected in tests:
        output = largest_component_size(input_A)
        result = (output == expected)
        print(result)
        if result:
            correct +=1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()