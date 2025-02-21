def lengthOfLongestSubstring(s: str) -> int:
    longest_substring = 0
    current_substring = ''
    for char in s:
        if char in current_substring:
            current_substring = current_substring[current_substring.index(char)+1:] + char
        else:
            current_substring += char
        longest_substring = max(longest_substring, len(current_substring))
    return longest_substring

# Test cases
input_1 = "abcabcbb"
output_1 = 3
input_2 = "bbbbb"
output_2 = 1
input_3 = "pwwkew"
output_3 = 3

# Test the solution
print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}")
print(f"Expected Output 1: {lengthOfLongestSubstring(input_1)}")
print(f"Result 1: {lengthOfLongestSubstring(input_1) == output_1}")
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")
print(f"Expected Output 2: {lengthOfLongestSubstring(input_2)}")
print(f"Result 2: {lengthOfLongestSubstring(input_2) == output_2}")
print(f"Input 3: {input_3}")
print(f"Output 3: {output_3}")
print(f"Expected Output 3: {lengthOfLongestSubstring(input_3)}")
print(f"Result 3: {lengthOfLongestSubstring(input_3) == output_3}")