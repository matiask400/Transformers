def solution(nums, target):
    hash_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], index]
        hash_map[num] = index


input_1 = [2, 7, 11, 15]
output_1 = [0, 1]
target_1 = 9
print(solution(input_1, target_1) == output_1)

input_2 = [3, 2, 4]
output_2 = [1, 2]
target_2 = 6
print(solution(input_2, target_2) == output_2)

input_3 = [3, 3]
output_3 = [0, 1]
target_3 = 6
print(solution(input_3, target_3) == output_3)