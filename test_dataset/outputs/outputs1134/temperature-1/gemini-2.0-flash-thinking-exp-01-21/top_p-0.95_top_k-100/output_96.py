def solve():
    def findCelebrity(n, graph):
        def knows(a, b):
            return graph[a][b] == 1

        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i != candidate:
                if knows(candidate, i):
                    return -1
                if not knows(i, candidate):
                    return -1
        return candidate

    def run_test(graph, expected_output):
        n = len(graph)
         knows_calls_count = [0]  # To track knows calls, not needed for this problem though

        def knows_api(a, b):
            knows_calls_count[0] += 1
            return graph[a][b] == 1

        def find_celebrity_wrapper(n_people):
            # Using the provided knows API instead of the graph directly
            def knows_func(a, b):
                return knows_api(a, b)

            # Modified findCelebrity function to use knows_func
            candidate = 0
            for i in range(1, n_people):
                if knows_func(candidate, i):
                    candidate = i

            for i in range(n_people):
                if i != candidate:
                    if knows_func(candidate, i):
                        return -1
                    if not knows_func(i, candidate):
                        return -1
            return candidate

        output = find_celebrity_wrapper(n)
        if output == expected_output:
            print("True")
            return True
        else:
            print("False")
            return False

    test_cases = [
        ([[1,1,0],[0,1,0],[1,1,1]], 1),
        ([[1,0,1],[1,1,0],[0,1,1]], -1),
        ([[1,0],[1,1]], 0),
        ([[1,1],[0,1]], 1),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 1]], 2),
        ([[1, 1, 1, 1, 1], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 1),
        ([[1, 1], [1, 1]], -1),
        ([[1, 0], [0, 1]], -1)
    ]

    correct_tests = 0
    for graph, expected_output in test_cases:
        if run_test(graph, expected_output):
            correct_tests += 1

    print(f"{correct_tests}/{len(test_cases)}")

solve()