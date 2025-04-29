def solve():
    def can_split_groups(N, dislikes):
        adj = [[] for _ in range(N + 1)]
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * (N + 1)

        def is_bipartite_dfs(u, c):
            color[u] = c
            for v in adj[u]:
                if color[v] == -1:
                    if not is_bipartite_dfs(v, 1 - c):
                        return False
                elif color[v] == c:
                    return False
            return True

        for i in range(1, N + 1):
            if color[i] == -1:
                if not is_bipartite_dfs(i, 0):
                    return False
        return True

    test_cases = [
        (4, [[1,2],[1,3],[2,4]], True),
        (3, [[1,2],[1,3],[2,3]], False),
        (5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False),
        (1, [], True),
        (2, [], True),
        (2, [[1,2]], True),
        (3, [[1,2]], True),
        (3, [[1,2],[2,3]], True),
        (4, [[1,2],[3,4]], True),
        (4, [[1,2],[1,3],[1,4]], False),
        (4, [[1,2],[1,3],[3,4],[2,4]], False),
    ]

    correct_count = 0
    for i, (N, dislikes, expected) in enumerate(test_cases):
        result = can_split_groups(N, dislikes)
        if result == expected:
            print(True)
            correct_count += 1
        else:
            print(False)
        # print(f"Test {i+1}: Input N={N}, dislikes={dislikes}, Expected={expected}, Result={result}")

    print(f"{correct_count}/{len(test_cases)}")

solve()