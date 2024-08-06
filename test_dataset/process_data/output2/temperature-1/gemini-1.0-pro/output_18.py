nums = [1,0,-1,0,-2,2]
target = 0
output = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
assert sorted(find_all_quadruplets(nums, target)) == sorted(output)

nums = []
target = 0
output = []
assert find_all_quadruplets(nums, target) == output

print("True")  # Matches output 1
print("True")  # Matches output 2