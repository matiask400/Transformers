def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    result = ''
    for i in range(len(s)):
        odd_pal = expand_around_center(i, i)
        if len(odd_pal) > len(result):
            result = odd_pal
        even_pal = expand_around_center(i, i+1)
        if len(even_pal) > len(result):
            result = even_pal
    return result

# Test cases
inputs = ['babad', 'cbbd', 'a']
outputs = ['bab', 'bb', 'a']
for i, input_val in enumerate(inputs):
    result = longest_palindromic_substring(input_val)
    print('Test', i+1, ':', result in outputs[i])
