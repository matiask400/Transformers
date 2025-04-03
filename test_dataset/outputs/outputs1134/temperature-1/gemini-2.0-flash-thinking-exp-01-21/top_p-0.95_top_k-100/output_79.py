def get_smallest_string(n: int, k: int) -> str:
    result = ['a'] * n
    remaining_value = k - n
    for i in range(n - 1, -1, -1):
        add_value = min(25, remaining_value)
        result[i] = chr(ord('a') + add_value)
        remaining_value -= add_value
        if remaining_value == 0:
            break
    return "".join(result)

def test_get_smallest_string():
    test_cases = [
        ((3, 27), "aay"),
        ((5, 73), "aaszz"),
        ((1, 1), "a"),
        ((2, 26), "ay"),
        ((2, 52), "zz"),
        ((4, 4), "aaaa"),
        ((4, 104), "zzzz"),
        ((10, 260), "zzzzzzzzzz"),
        ((10, 10), "aaaaaaaaaa"),
        ((6, 60), "aaaafo"),
        ((6, 156), "zzzzzz"),
    ]
    correct_count = 0
    for input_val, expected_output in test_cases:
        n, k = input_val
        output = get_smallest_string(n, k)
        if output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    test_get_smallest_string()