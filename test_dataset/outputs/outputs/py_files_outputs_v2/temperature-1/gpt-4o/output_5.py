# Function to find the longest palindromic substring
def longestPalindrome(s):
    n = len(s)
    if n == 0:
        return ''
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    for i in range(n):
        dp[i][i] = True
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                if cl == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if cl > max_length:
                        start = i
                        max_length = cl
    return s[start:start + max_length]

# Example inputs
inputs = ['babad', 'cbbd', 'a']
# Expected outputs
expected_outputs = ['bab', 'bb', 'a']
# Check and print if outputs match the expected results
for i, input_str in enumerate(inputs):
    result = longestPalindrome(input_str)
    print(result == expected_outputs[i])
