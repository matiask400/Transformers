def get_smallest_string(n: int, k: int) -> str:
    """
    Given two integers n and k, return the lexicographically smallest string with length equal to n and numeric value equal to k.

    Args:
        n (int): The length of the string.
        k (int): The numeric value of the string.

    Returns:
        str: The lexicographically smallest string with length equal to n and numeric value equal to k.
    """
    result = ['a'] * n
    k -= n
    for i in range(n - 1, -1, -1):
        if k == 0:
            break
        add = min(k, 25)
        result[i] = chr(ord('a') + add)
        k -= add
    return ''.join(result)


def test_get_smallest_string():
    test_cases = [
        (3, 27, "aay"),
        (5, 73, "aaszz"),
        (1, 1, "a"),
        (2, 26, "az"),
        (2, 52, "zz"),
        (4, 104, "zzzz"),
        (4, 4, "aaaa"),
        (10, 260, "zzzzzzzzzz"),
        (10, 10, "aaaaaaaaaa"),
        (10, 11, "aaaaaaaaab"),
        (5, 70, "aasyy"),
        (5, 71, "aasyz"),
        (5, 72, "aaszx"),
        (5, 74, "aatzz"),
        (5, 75, "auzzz"),
        (5, 76, "bvzzz"),
        (5, 77, "cwzzz"),
        (5, 60, "aaaao"),
    ]
    correct_count = 0
    total_count = len(test_cases)

    for n, k, expected in test_cases:
        actual = get_smallest_string(n, k)
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: n={n}, k={k}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")
    print(f"{correct_count}/{total_count}")


if __name__ == "__main__":
    test_get_smallest_string()