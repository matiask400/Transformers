def solve():
    def count_remaining_nodes(nodes, parent, value):
        adj = [[] for _ in range(nodes)]
        for i in range(1, nodes):
            adj[parent[i]].append(i)

        subtree_sums = [0] * nodes
        remaining_nodes = set(range(nodes))

        def calculate_subtree_sum(node):
            subtree_sums[node] = value[node]
            for child in adj[node]:
                subtree_sums[node] += calculate_subtree_sum(child)
            return subtree_sums[node]

        calculate_subtree_sum(0)

        def remove_zero_sum_subtrees(node):
            if subtree_sums[node] == 0:
                if node in remaining_nodes:
                    remaining_nodes.remove(node)
                for child in adj[node]:
                    remove_zero_sum_subtrees(child)

                return

            for child in adj[node]:
                remove_zero_sum_subtrees(child)


        remove_zero_sum_subtrees(0)

        return len(remaining_nodes)

    test_cases = [
        (7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -1], 2),
        (7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -2], 6),
        (5, [-1, 0, 1, 0, 0], [-672, 441, 18, 728, 378], 5),
        (5, [-1, 0, 0, 1, 1], [-686, -842, 616, -739, -746], 5),
        (4, [-1, 0, 1, 0], [0,1,2,0], 2),
        (4, [-1, 0, 0, 1], [0, 1, 2, 0], 2),
        (4, [-1,0,1,0], [0,1,-1,0], 1)
    ]

    num_correct = 0
    for i, (nodes, parent, value, expected) in enumerate(test_cases):
        result = count_remaining_nodes(nodes, parent, value)
        if result == expected:
            print(f"True")
            num_correct += 1
        else:
            print(f"False")
    print(f"{num_correct}/{len(test_cases)}")

solve()