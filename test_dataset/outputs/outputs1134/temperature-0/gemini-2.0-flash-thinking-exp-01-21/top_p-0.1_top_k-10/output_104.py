def solve(nodes, parent, value):
    children = [[] for _ in range(nodes)]
    for i in range(1, nodes):
        children[parent[i]].append(i)

    subtree_sum = [0] * nodes
    removed = [False] * nodes

    def remove_subtree_nodes(u):
        removed[u] = True
        for v in children[u]:
            remove_subtree_nodes(v)

    def calculate_subtree_sum(u):
        current_sum = value[u]
        for v in children[u]:
            current_sum += calculate_subtree_sum(v)
        subtree_sum[u] = current_sum
        return current_sum

    calculate_subtree_sum(0)

    for i in range(nodes):
        if subtree_sum[i] == 0:
            remove_subtree_nodes(i)

    count = 0
    for i in range(nodes):
        if not removed[i]:
            count += 1
    return count

def test_solve():
    test_cases = [
        (7, [-1,0,0,1,2,2,2], [1,-2,4,0,-2,-1,-1], 2),
        (7, [-1,0,0,1,2,2,2], [1,-2,4,0,-2,-1,-2], 6),
        (5, [-1,0,1,0,0], [-672,441,18,728,378], 5),
        (5, [-1,0,0,1,1], [-686,-842,616,-739,-746], 5),
        (1, [-1], [0], 0),
        (1, [-1], [1], 1),
        (2, [-1, 0], [1, -1], 1),
        (3, [-1, 0, 0], [1, -1, 0], 1),
        (4, [-1, 0, 0, 0], [1, -1, 0, 0], 1),
        (5, [-1, 0, 0, 0, 0], [1, -1, 0, 0, 0], 1),
        (3, [-1, 0, 0], [1, 2, -3], 3),
        (4, [-1, 0, 0, 0], [1, 2, -3, 4], 4),
        (5, [-1, 0, 0, 0, 0], [1, 2, -3, 4, -4], 4),
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
    test_solve()