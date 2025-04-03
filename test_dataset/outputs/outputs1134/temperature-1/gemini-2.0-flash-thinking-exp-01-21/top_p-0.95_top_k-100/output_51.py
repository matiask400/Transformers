def count_trailing_zeros_factorial(x):
    count = 0
    i = 5
    while x // i >= 1:
        count += x // i
        i *= 5
    return count

def solve():
    k_values = [0, 5]
    expected_outputs = [5, 0]

    num_tests = len(k_values)
    correct_tests = 0

    for i in range(num_tests):
        k = k_values[i]
        expected_output = expected_outputs[i]

        low = 0
        high = max(5 * k + 1, 5)
        x_start = -1

        while low <= high:
            mid = (low + high) // 2
            zeros = count_trailing_zeros_factorial(mid)
            if zeros >= k:
                x_start = mid
                high = mid - 1
            else:
                low = mid + 1

        if x_start != -1 and count_trailing_zeros_factorial(x_start) == k:
            actual_output = 5
        else:
            actual_output = 0

        if actual_output == expected_output:
            print('True')
            correct_tests += 1
        else:
            print('False')

    print(f"{correct_tests}/{num_tests}")

if __name__ == '__main__':
    solve()