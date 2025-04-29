def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    def largest_component_size(A):
        n = len(A)
        adj = {num: [] for num in A}
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(A[i], A[j]) > 1:
                    adj[A[i]].append(A[j])
                    adj[A[j]].append(A[i])

        visited = {num: False for num in A}
        max_component_size = 0

        def get_connected_component_size(start_node):
            count = 0
            stack = [start_node]
            visited[start_node] = True
            while stack:
                node = stack.pop()
                count += 1
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            return count

        for num in A:
            if not visited[num]:
                component_size = get_connected_component_size(num)
                max_component_size = max(max_component_size, component_size)
        return max_component_size

    test_cases = [
        ([4, 6, 15, 35], 4),
        ([20, 50, 9, 63], 2),
        ([2, 3, 6, 7, 4, 12, 21, 39], 8),
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([1, 2, 3], 1),
        ([2, 4], 2),
        ([2], 1),
        ([1], 1),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 10)
    ]

    correct_count = 0
    for i, (input_arr, expected_output) in enumerate(test_cases):
        output = largest_component_size(input_arr)
        if output == expected_output:
            print(True)
            correct_count += 1
        else:
            print(False)

    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    solve()