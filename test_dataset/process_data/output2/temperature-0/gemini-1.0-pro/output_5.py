s = "babad"
print(s == longestPalindrome(s))
s = "cbbd"
print(s == longestPalindrome(s))
s = "a"
print(s == longestPalindrome(s))
s = "ac"
print(s == longestPalindrome(s))

def longestPalindrome(s):
    if len(s) < 2 or s == s[::-1]:
        return s
    for middle in range(1, len(s)):
        for start in range(0, len(s) - middle + 1):
            end = start + middle
            if s[start:end] == s[start:end][::-1]:
                return s[start:end]