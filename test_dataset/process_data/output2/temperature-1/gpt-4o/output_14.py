def longest_common_prefix(strs):
    if not strs:
        return ""
    # Start with the first string in the array as the prefix
    prefix = strs[0]
    for string in strs[1:]:
        # Adjust the prefix with each string in the array
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test cases
input_1 = ["flower","flow","flight"]
output_1 = "fl"
result_1 = longest_common_prefix(input_1)
print(result_1 == output_1)

input_2 = ["dog","racecar","car"]
output_2 = ""
result_2 = longest_common_prefix(input_2)
print(result_2 == output_2)

# No third input given in examples
input_3 = []
output_3 = None
# As there is no concrete example for input_3 and output_3, they can't be tested meaningfully

# The solution above correctly handles the given test cases and constraints as per the problem description.