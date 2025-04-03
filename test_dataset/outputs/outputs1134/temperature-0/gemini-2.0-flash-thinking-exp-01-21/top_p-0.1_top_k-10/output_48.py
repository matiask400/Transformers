def solve():
    def test_solution(n, expected_output):
        output = magicalString(n)
        if output == expected_output:
            print("True")
            return 1
        else:
            print("False")
            return 0

    def magicalString(n):
        if n == 0:
            return 0
        s = [1, 2, 2]
        count_pointer = 2
        while len(s) < n:
            count = s[count_pointer]
            last_digit = s[-1]
            next_digit = 1 if last_digit == 2 else 2
            for _ in range(count):
                s.append(next_digit)
            count_pointer += 1

        ones_count = 0
        for i in range(n):
            if s[i] == 1:
                ones_count += 1
        return ones_count

    correct_tests = 0
    total_tests = 0

    # Example 1
    total_tests += 1
    correct_tests += test_solution(6, 3)

    # Test case 1
    total_tests += 1
    correct_tests += test_solution(1, 1)

    # Test case 2
    total_tests += 1
    correct_tests += test_solution(2, 1)

    # Test case 3
    total_tests += 1
    correct_tests += test_solution(3, 2)

    # Test case 4
    total_tests += 1
    correct_tests += test_solution(4, 2)

    # Test case 5
    total_tests += 1
    correct_tests += test_solution(5, 2)

    # Test case 6
    total_tests += 1
    correct_tests += test_solution(7, 4)

    # Test case 7
    total_tests += 1
    correct_tests += test_solution(8, 4)

    # Test case 8
    total_tests += 1
    correct_tests += test_solution(9, 4)

    # Test case 9
    total_tests += 1
    correct_tests += test_solution(10, 5)

    # Test case 10
    total_tests += 1
    correct_tests += test_solution(20, 9)

    # Test case 11
    total_tests += 1
    correct_tests += test_solution(50, 21)

    # Test case 12
    total_tests += 1
    correct_tests += test_solution(100, 48)

    # Test case 13
    total_tests += 1
    correct_tests += test_solution(1000, 499)

    # Test case 14
    total_tests += 1
    correct_tests += test_solution(10000, 4999)

    # Test case 15
    total_tests += 1
    correct_tests += test_solution(100000, 49999)


    print(f"{correct_tests}/{total_tests}")

solve()