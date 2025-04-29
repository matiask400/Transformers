def lengthOfLongestSubstring(s):
    """
    Finds the length of the longest substring without repeating characters.
    """
    longest_substring = 0
    current_substring = ""
    seen_characters = set()

    for char in s:
        while char in seen_characters:
            seen_characters.remove(s[0])
            current_substring = current_substring[1:]
            s = s[1:]  # Remove the first character from s
        
        seen_characters.add(char)
        current_substring += char
        longest_substring = max(longest_substring, len(current_substring))
    
    return longest_substring


def test_lengthOfLongestSubstring():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
    ]

    passed_tests = 0

    for case in test_cases:
        result = lengthOfLongestSubstring(case[0])
        print(f"True: {result == case[1]}")
        if result == case[1]:
            passed_tests += 1

    print(f"Passed {passed_tests}/{len(test_cases)} tests")

test_lengthOfLongestSubstring()