def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example inputs
input_1 = ["flower", "flow", "flight"]
output_1 = "fl"
result_1 = longest_common_prefix(input_1)
print(result_1 == output_1)

input_2 = ["dog", "racecar", "car"]
output_2 = ""
result_2 = longest_common_prefix(input_2)
print(result_2 == output_2)

input_3 = []  # Additional input case
output_3 = ""
result_3 = longest_common_prefix(input_3)
print(result_3 == output_3)