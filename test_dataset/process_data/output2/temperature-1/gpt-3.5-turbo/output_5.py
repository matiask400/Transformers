def longestPalindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 1:
        return ""

    longest_palindrome = ""
    for i in range(len(s)):
        # for odd case
        palindrome1 = expand_around_center(i, i)
        # for even case
        palindrome2 = expand_around_center(i, i + 1)

        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome

# Example Inputs
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("ac"))