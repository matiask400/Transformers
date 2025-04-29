def solve():
    def game(nums):
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        if xor_sum == 0:
            return True
        if len(nums) % 2 == 1:
            return False
        else:
            return True

    def test_case(nums, expected_output):
        output = game(nums)
        if output == expected_output:
            print("True")
            return 1
        else:
            print("False")
            return 0

    correct_count = 0
    total_count = 0

    # Example 1
    nums1 = [1, 1, 2]
    expected_output1 = False
    correct_count += test_case(nums1, expected_output1)
    total_count += 1

    # Example 2: [0]
    nums2 = [0]
    expected_output2 = True
    correct_count += test_case(nums2, expected_output2)
    total_count += 1

    # Example 3: [2, 2]
    nums3 = [2, 2]
    expected_output3 = True
    correct_count += test_case(nums3, expected_output3)
    total_count += 1

    # Example 4: [1, 2]
    nums4 = [1, 2]
    expected_output4 = True
    correct_count += test_case(nums4, expected_output4)
    total_count += 1

    # Example 5: [1]
    nums5 = [1]
    expected_output5 = False
    correct_count += test_case(nums5, expected_output5)
    total_count += 1

    # Example 6: [2, 3]
    nums6 = [2, 3]
    expected_output6 = True
    correct_count += test_case(nums6, expected_output6)
    total_count += 1

    # Example 7: [1, 1]
    nums7 = [1, 1]
    expected_output7 = True
    correct_count += test_case(nums7, expected_output7)
    total_count += 1

    print(f"{correct_count}/{total_count}")

    return game

if __name__ == '__main__':
    solve()