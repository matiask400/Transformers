def longest_palindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_length = length
    return s[start:start+max_length]

# Test cases
inputs = ["babad", "cbbd", "a"]
outputs = ["bab", "bb", "a"]

for i, input_str in enumerate(inputs):
    result = longest_palindrome(input_str)
    print(result == outputs[i])