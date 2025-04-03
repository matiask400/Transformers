def solve():
    def can_split_groups(N, dislikes):
        adj = [[] for _ in range(N + 1)]
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        group = [0] * (N + 1)

        def is_bipartite(node, current_group):
            group[node] = current_group
            for neighbor in adj[node]:
                if group[neighbor] == 0:
                    if not is_bipartite(neighbor, 3 - current_group):
                        return False
                elif group[neighbor] == current_group:
                    return False
            return True

        for i in range(1, N + 1):
            if group[i] == 0:
                if not is_bipartite(i, 1):
                    return False
        return True

    def run_test(N, dislikes, expected_output):
        actual_output = can_split_groups(N, dislikes)
        if actual_output == expected_output:
            print('True')
        else:
            print('False')

    # Example 1
    run_test(4, [[1,2],[1,3],[2,4]], True)

    # Example 2
    run_test(3, [[1,2],[1,3],[2,3]], False)

    # Example 3
    run_test(5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False)

    # Additional test cases
    run_test(1, [], True)
    run_test(2, [], True)
    run_test(2, [[1,2]], True)
    run_test(3, [[1,2]], True)
    run_test(3, [[1,2],[2,3]], True)
    run_test(4, [[1,2],[3,4]], True)
    run_test(4, [[1,2],[1,3],[3,4]], True)
    run_test(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]], False)
    run_test(7, [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True)


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
        (4, [[1,2],[1,3],[3,4]], True),
        (6, [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]], False),
        (7, [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True),
        (4, [[1,2],[3,4],[1,4]], True),
        (4, [[1,2],[3,4],[1,3],[2,4]], False)
    ]

    correct_count = 0
    for i, (N, dislikes, expected_output) in enumerate(test_cases):
        actual_output = can_split_groups(N, dislikes)
        if actual_output == expected_output:
            print('True')
            correct_count += 1
        else:
            print('False')

    print(f"{correct_count}/{len(test_cases)}")

solve()