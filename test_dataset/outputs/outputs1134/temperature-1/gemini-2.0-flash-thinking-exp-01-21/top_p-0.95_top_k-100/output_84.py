def solve():
    def num_provinces(isConnected):
        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                province_count += 1
                dfs(i)
        return province_count

    def run_tests():
        test_cases = [
            ([[1,1,0],[1,1,0],[0,0,1]], 2),
            ([[1,0,0],[0,1,0],[0,0,1]], 3),
            ([[1,1,1],[1,1,1],[1,1,1]], 1),
            ([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]], 1),
            ([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 4),
            ([[1,0],[0,1]], 2),
            ([[1,1],[1,1]], 1),
            ([[1]], 1)
        ]
        correct_count = 0
        for i, (input_matrix, expected_output) in enumerate(test_cases):
            output = num_provinces(input_matrix)
            if output == expected_output:
                print(f'Test {i+1}: True')
                correct_count += 1
            else:
                print(f'Test {i+1}: False')
        print(f'{correct_count}/{len(test_cases)}')

    run_tests()

solve()