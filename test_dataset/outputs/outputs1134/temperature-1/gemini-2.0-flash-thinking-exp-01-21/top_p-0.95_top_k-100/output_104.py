def solve(nodes, parent, value):
    children = [[] for _ in range(nodes)]
    for i in range(1, nodes):
        children[parent[i]].append(i)

    subtree_sum = [0] * nodes

    def dfs_sum(u):
        subtree_sum[u] = value[u]
        for v in children[u]:
            dfs_sum(v)
            subtree_sum[u] += subtree_sum[v]

    dfs_sum(0)

    def remove_zero_subtree(u):
        new_children = []
        for v in children[u]:
            remove_zero_subtree(v)
            if subtree_sum[v] != 0:
                new_children.append(v)
        children[u] = new_children

    remove_zero_subtree(0)

    def count_nodes(u):
        count = 1
        for v in children[u]:
            count += count_nodes(v)
        return count

    return count_nodes(0)

def test_solution():
    test_cases = [
        (7, [-1,0,0,1,2,2,2], [1,-2,4,0,-2,-1,-1], 2),
        (7, [-1,0,0,1,2,2,2], [1,-2,4,0,-2,-1,-2], 6),
        (5, [-1,0,1,0,0], [-672,441,18,728,378], 5),
        (5, [-1,0,0,1,1], [-686,-842,616,-739,-746], 5)
    ]
    correct_tests = 0
    for nodes, parent, value, expected_output in test_cases:
        output = solve(nodes, parent, value)
        if output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')
    print(f"{correct_tests}/{len(test_cases)}")

if __name__ == '__main__':
    test_solution()