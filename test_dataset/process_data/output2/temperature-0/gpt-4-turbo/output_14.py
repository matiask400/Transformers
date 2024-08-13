def longest_common_prefix(strs):
    if not strs:
        return ''
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

# Test cases
strs1 = ['flower', 'flow', 'flight']
expected1 = 'fl'
print(longest_common_prefix(strs1) == expected1)

strs2 = ['dog', 'racecar', 'car']
expected2 = ''
print(longest_common_prefix(strs2) == expected2)