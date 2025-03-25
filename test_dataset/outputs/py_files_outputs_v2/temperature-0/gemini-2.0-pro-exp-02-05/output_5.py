def longestPalindrome(s):
    if not s:
        return ""

    n = len(s)
    start = 0
    max_len = 1

    def expand_around_center(left, right):
        nonlocal start, max_len
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > max_len:
            max_len = right - left - 1
            start = left + 1

    for i in range(n):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)

    return s[start:start + max_len]