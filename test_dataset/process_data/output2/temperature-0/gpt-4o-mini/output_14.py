def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix

# Example inputs
input_1 = ["flower", "flow", "flight"]
output_1 = longest_common_prefix(input_1)
print(output_1 == "fl")  # True

input_2 = ["dog", "racecar", "car"]
output_2 = longest_common_prefix(input_2)
print(output_2 == "")  # True

input_3 = []
output_3 = longest_common_prefix(input_3)
print(output_3 == "")  # True