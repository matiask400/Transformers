import statistics
def find_median_sorted_arrays(nums1, nums2):
    merged_array = sorted(nums1 + nums2)
    return statistics.median(merged_array)

# Test Cases
input_1 = ([1, 3], [2])
output_1 = 2.00000
input_2 = ([1, 2], [3, 4])
output_2 = 2.50000
input_3 = ([0, 0], [0, 0])
output_3 = 0.00000

print(find_median_sorted_arrays(*input_1) == output_1)  # True
print(find_median_sorted_arrays(*input_2) == output_2)  # True
print(find_median_sorted_arrays(*input_3) == output_3)  # True