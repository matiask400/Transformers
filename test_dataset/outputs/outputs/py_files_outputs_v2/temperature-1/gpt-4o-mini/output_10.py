def isMatch(s: str, p: str) -> bool:
    # Initialize a 2D array to store results of subproblems
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # Empty pattern matches empty string

    # Fill the first row for patterns that can match an empty string
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the dp table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]  # If characters match
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Consider '*' as matching 0 characters
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # Consider '*' matching one or more characters

    return dp[-1][-1]

# Testing the function with given examples
inputs = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True)
]

for s, p, expected in inputs:
    result = isMatch(s, p)
    print(f'Input: s = {s}, p = {p} => Output: {result}, Expected: {expected}, Correct: {result == expected}')