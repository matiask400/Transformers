def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 1:
        return ""
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
    return longest

# Test Cases
print(longest_palindromic_substring("babad") == "bab")
print(longest_palindromic_substring("cbbd") == "bb")
print(longest_palindromic_substring("a") == "a")