def run_tests():
    from collections import defaultdict, deque

    def possibleBipartition(N, dislikes):
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}
        for node in range(1, N+1):
            if node not in color:
                queue = deque()
                queue.append(node)
                color[node] = 0
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True

    test_cases = [
        {
            "N": 4,
            "dislikes": [[1,2],[1,3],[2,4]],
            "expected": True
        },
        {
            "N": 3,
            "dislikes": [[1,2],[1,3],[2,3]],
            "expected": False
        },
        {
            "N": 5,
            "dislikes": [[1,2],[2,3],[3,4],[4,5],[1,5]],
            "expected": False
        },
        # Additional test cases can be added here
    ]

    correct = 0
    total = len(test_cases)
    for test in test_cases:
        result = possibleBipartition(test["N"], test["dislikes"])
        is_correct = result == test["expected"]
        print(is_correct)
        if is_correct:
            correct += 1
    print(f"{correct}/{total}")

# Run the tests
run_tests()