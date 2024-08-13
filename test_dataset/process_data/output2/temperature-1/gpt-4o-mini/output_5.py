def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest

# Example inputs
inputs = ["babad", "cbbd", "a"]
outputs = ["bab", "bb", "a"]
for i in range(len(inputs)):
    result = longest_palindrome(inputs[i])
    print(f'Input: {inputs[i]}, Output: {result}, Correct: {result in outputs}')