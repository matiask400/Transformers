import math
from collections import deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def largest_component_size(A):
    adj = {}
    nodes = list(A)
    for u in nodes:
        adj[u] = []

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if gcd(nodes[i], nodes[j]) > 1:
                adj[nodes[i]].append(nodes[j])
                adj[nodes[j]].append(nodes[i])

    visited = set()
    max_component_size = 0
    for node in nodes:
        if node not in visited:
            current_component_size = 0
            q = deque([node])
            visited.add(node)
            current_component_size += 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        current_component_size += 1
                        q.append(v)
            max_component_size = max(max_component_size, current_component_size)
    return max_component_size

def run_tests():
    test_cases = [
        ([4, 6, 15, 35], 4),
        ([20, 50, 9, 63], 2),
        ([2, 3, 6, 7, 4, 12, 21, 39], 8),
        ([2], 1),
        ([2, 3], 1),
        ([6, 12], 2),
        ([2, 4, 8, 16], 4),
        ([3, 9, 27, 81], 4),
        ([2, 3, 5, 7, 11], 1),
        ([2, 4, 6, 8, 3, 9, 27], 7)
    ]

    num_correct = 0
    for i, (input_array, expected_output) in enumerate(test_cases):
        actual_output = largest_component_size(input_array)
        if actual_output == expected_output:
            print(True)
            num_correct += 1
        else:
            print(False)
        # print(f"Test case {i+1}: Input={input_array}, Expected={expected_output}, Actual={actual_output}, Result={'Passed' if actual_output == expected_output else 'Failed'}")

    print(f"{num_correct}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()