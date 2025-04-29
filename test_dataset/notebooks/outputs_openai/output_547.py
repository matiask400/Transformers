def run_tests():
    def find_num_provinces(isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for adjacent, connected in enumerate(isConnected[city]):
                if connected and not visited[adjacent]:
                    visited[adjacent] = True
                    dfs(adjacent)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces += 1
        return provinces

    test_cases = [
        (
            [[1,1,0],[1,1,0],[0,0,1]],
            2
        ),
        (
            [[1,0,0],[0,1,0],[0,0,1]],
            3
        ),
        (
            [[1,1,1],[1,1,1],[1,1,1]],
            1
        ),
        (
            [[1]],
            1
        ),
        (
            [[1,0,1],[0,1,0],[1,0,1]],
            2
        ),
    ]

    correct = 0
    total = len(test_cases)
    for idx, (isConnected, expected) in enumerate(test_cases):
        result = find_num_provinces(isConnected)
        if result == expected:
            print(True)
            correct += 1
        else:
            print(False)
    print(f"{correct}/{total}")

# Run the tests
run_tests()