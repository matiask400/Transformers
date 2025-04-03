def min_length_after_removals(s):
    i, j = 0, len(s) - 1
    while i <= j and s[i] == s[j]:
        c = s[i]
        # Count prefix
        count_i = 1
        while i + count_i <= j and s[i + count_i] == c:
            count_i += 1
        # Count suffix
        count_j = 1
        while j - count_j >= i and s[j - count_j] == c:
            count_j += 1
        # Remove the counted prefix and suffix
        i += count_i
        j -= count_j
    return max(0, j - i + 1)

# Define test cases as tuples of (input, expected_output)
tests = [
    ("ca", 2),
    ("cabaabac", 0),
    ("aabccabba", 3),
    ("a", 1),
    ("aaaa", 0),
    ("abccba", 0),
    ("abcde", 5),
    ("aabbcc", 6),
    ("abbacadd", 3),
    ("ababa", 1)
]

correct = 0
for s, expected in tests:
    result = min_length_after_removals(s)
    is_correct = result == expected
    print(is_correct)
    if is_correct:
        correct += 1
print(f"{correct}/{len(tests)}")