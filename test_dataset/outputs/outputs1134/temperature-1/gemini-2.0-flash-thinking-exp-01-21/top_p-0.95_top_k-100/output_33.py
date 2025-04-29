def solve():
    nums = [int(x) for x in input().split()]
    initial_xor_sum = 0
    for num in nums:
        initial_xor_sum ^= num
    
    if initial_xor_sum == 0:
        print(True)
        return
        
    if len(nums) % 2 == 0:
        print(True)
    else:
        print(False)

def test_example_1():
    nums = [1, 1, 2]
    expected_output = False
    
    current_xor_sum = 0
    for num in nums:
        current_xor_sum ^= num
    if current_xor_sum == 0:
        actual_output = True
    elif len(nums) % 2 == 0:
        actual_output = True
    else:
        actual_output = False
        
    if actual_output == expected_output:
        print('True')
    else:
        print('False')

def test_example_2():
    nums = [2, 3]
    expected_output = True
    
    current_xor_sum = 0
    for num in nums:
        current_xor_sum ^= num
    if current_xor_sum == 0:
        actual_output = True
    elif len(nums) % 2 == 0:
        actual_output = True
    else:
        actual_output = False
        
    if actual_output == expected_output:
        print('True')
    else:
        print('False')

def test_example_3():
    nums = [3, 4, 5]
    expected_output = False
    
    current_xor_sum = 0
    for num in nums:
        current_xor_sum ^= num
    if current_xor_sum == 0:
        actual_output = True
    elif len(nums) % 2 == 0:
        actual_output = True
    else:
        actual_output = False
        
    if actual_output == expected_output:
        print('True')
    else:
        print('False')

def test_case(nums, expected_output):
    current_xor_sum = 0
    for num in nums:
        current_xor_sum ^= num
    if current_xor_sum == 0:
        actual_output = True
    elif len(nums) % 2 == 0:
        actual_output = True
    else:
        actual_output = False
        
    if actual_output == expected_output:
        print('True')
        return True
    else:
        print('False')
        return False

def run_tests():
    tests = [
        ([1, 1, 2], False),
        ([2, 3], True),
        ([3, 4, 5], False),
        ([0], True),
        ([1], False),
        ([0, 0], True),
        ([0, 1], True),
        ([1, 0], True),
        ([1, 1], False),
        ([2, 2], False),
        ([3, 3], False),
        ([1, 2, 3], True),
        ([1, 2, 3, 4], True),
        ([1, 2, 3, 4, 5], False),
        ([0, 0, 0], True),
        ([0, 0, 1], False),
        ([0, 1, 0], False),
        ([1, 0, 0], False),
        ([0, 0, 0, 0], True),
        ([0, 0, 0, 1], True),
        ([0, 0, 1, 0], True),
        ([0, 1, 0, 0], True),
        ([1, 0, 0, 0], True),
        ([1, 1, 1], True),
        ([2, 2, 2], True),
        ([3, 3, 3], True),
        ([1, 1, 1, 1], False),
        ([2, 2, 2, 2], False),
        ([3, 3, 3, 3], False),
    ]
    
    correct_count = 0
    total_count = len(tests)
    for nums, expected in tests:
        if test_case(nums, expected):
            correct_count += 1
            
    print(f"{correct_count}/{total_count}")

if __name__ == '__main__':
    run_tests()