def solve():
    def knows(a, b):
        return graph[a][b]

    def findCelebrity(n):
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i):
                return -1
            if not knows(i, candidate):
                return -1
        return candidate

    test_cases = [
        ([[1,1,0],[0,1,0],[1,1,1]], 1),
        ([[1,0,1],[1,1,0],[0,1,1]], -1),
        ([[1,0],[1,1]], 0),
        ([[1,1],[0,1]], 1),
        ([[1]], 0)
    ]

    num_correct = 0
    for i, (graph_input, expected_output) in enumerate(test_cases):
        global graph
        graph = graph_input
        n = len(graph)
        actual_output = findCelebrity(n)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            num_correct += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{num_correct}/{len(test_cases)}")

graph = []
solve()