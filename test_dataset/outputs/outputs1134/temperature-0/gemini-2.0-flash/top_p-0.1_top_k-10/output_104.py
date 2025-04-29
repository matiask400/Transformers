def solve():
    def count_remaining_nodes(nodes, parent, value):
        adj = [[] for _ in range(nodes)]
        for i in range(1, nodes):
            adj[parent[i]].append(i)

        subtree_sums = [0] * nodes
        remaining_nodes = set(range(nodes))

        def dfs(node):
            subtree_sums[node] = value[node]
            for child in adj[node]:
                dfs(child)
                subtree_sums[node] += subtree_sums[child]

            if subtree_sums[node] == 0:
                remove_subtree(node)

        def remove_subtree(node):
            if node in remaining_nodes:
                remaining_nodes.remove(node)
                for child in adj[node]:
                    remove_subtree(child)

        dfs(0)
        return len(remaining_nodes)

    def run_test(nodes, parent, value, expected):
        result = count_remaining_nodes(nodes, parent, value)
        if result == expected:
            print("True")
        else:
            print("False")
        return result == expected

    test_cases = [
        (7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -1], 2),
        (7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -2], 6),
        (5, [-1, 0, 1, 0, 0], [-672, 441, 18, 728, 378], 5),
        (5, [-1, 0, 0, 1, 1], [-686, -842, 616, -739, -746], 5)
    ]

    correct_count = 0
    for nodes, parent, value, expected in test_cases:
        if run_test(nodes, parent, value, expected):
            correct_count += 1

    print(f"{correct_count}/{len(test_cases)}")

solve()