def num_times_all_blue(light):
    """
    Calculates the number of moments in which all turned on bulbs are blue.

    Args:
        light: A list of integers representing the order in which bulbs are turned on.

    Returns:
        The number of moments in which all turned on bulbs are blue.
    """
    n = len(light)
    rightmost = 0
    on = [False] * n
    count = 0
    for i in range(n):
        on[light[i] - 1] = True
        rightmost = max(rightmost, light[i])
        all_blue = True
        for j in range(rightmost):
            if not on[j]:
                all_blue = False
                break
        if all_blue and rightmost == i + 1:
            count += 1
    return count

def test_num_times_all_blue():
    test_cases = [
        ([2, 1, 3, 5, 4], 3),
        ([3, 2, 4, 1, 5], 2),
        ([4, 1, 2, 3], 1),
        ([2, 1, 4, 3, 6, 5], 3),
        ([1, 2, 3, 4, 5, 6], 6),
        ([1], 1),
        ([2,1], 1),
        ([3,1,2], 2)
    ]

    correct_count = 0
    total_count = len(test_cases)

    for i, (light, expected) in enumerate(test_cases):
        result = num_times_all_blue(light)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False (Input: {light}, Expected: {expected}, Got: {result})")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_num_times_all_blue()