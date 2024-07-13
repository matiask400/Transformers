def longestPalindrome(s: str) -> str:
    if not s:
        return""
    start = 0
    end = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > end - start:
                start, end = l, r
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > end - start:
                start, end = l, r