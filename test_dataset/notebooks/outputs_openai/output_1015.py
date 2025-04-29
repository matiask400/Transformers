from collections import deque

def smallest_length(K):
    if K == 0:
        return -1
    visited = set()
    q = deque()
    q.append((1 % K, 1))
    visited.add(1 % K)
    
    while q:
        remainder, length = q.popleft()
        if remainder == 0:
            return length
        next_remainder = (remainder * 10 + 1) % K
        if next_remainder not in visited:
            visited.add(next_remainder)
            q.append((next_remainder, length + 1))
    return -1

# Test cases: list of tuples (K, expected_output)
test_cases = [
    (1, 1),
    (2, -1),
    (3, 3),
    (7, 6),
    (9, 9),
    (10, -1),
    (13, 6),
    (17, 16),
    (19, 18),
    (23, 22),
    (99991, 99991),  # A large prime
    (99999, -1),     # Divisible by 3 and 9 but not by 2 or 5
]

correct = 0
total = len(test_cases)

for K, expected in test_cases:
    result = smallest_length(K)
    is_correct = result == expected
    print(is_correct)
    if is_correct:
        correct += 1

print(f"{correct} / {total}")