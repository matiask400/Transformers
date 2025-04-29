def is_k_palindrome(s: str, k: int) -> bool:
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
        
    for length in range(2, n+1):
        for i in range(n - length +1):
            j = i + length -1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] +2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                
    lps = dp[0][n-1]
    return (n - lps) <= k

def run_tests():
    test_cases = [
        ("abcdeca", 2, True),
        ("abbababa", 1, True),
        ("abcdef", 3, False),
        ("a", 0, True),
        ("ab", 1, True),
        ("abcba", 0, True),
        ("abccba", 0, True),
        ("abcdba", 1, True),
        ("abcdefdba", 2, True),
        ("abcdefgfedcba", 0, True),
        ("abcdefgfedcba", 1, True),
        ("abcdefgfedcba", 2, True),
        ("abcdefgfedcba", 3, True),
        ("abcdefgfedcba", 6, True),
        ("abcdefgfedcba", 12, True),
        ("abcdefgfedcbad", 1, False),
        ("abcdefgfedcbad", 2, True),
    ]
    
    correct = 0
    total = len(test_cases)
    for idx, (s, k, expected) in enumerate(test_cases, 1):
        result = is_k_palindrome(s, k)
        test_passed = result == expected
        print(test_passed)
        if test_passed:
            correct +=1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()