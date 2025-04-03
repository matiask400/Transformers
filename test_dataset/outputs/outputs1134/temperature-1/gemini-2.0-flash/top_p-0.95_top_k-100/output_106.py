import heapq
from collections import Counter

def rearrange_string(s, k):
    """
    Rearranges string s such that the same characters are at least distance k from each other.

    Args:
        s (str): The input string.
        k (int): The minimum distance between the same characters.

    Returns:
        str: The rearranged string, or an empty string if it's not possible.
    """

    if k == 0:
        return s

    counts = Counter(s)
    max_heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_heap)

    result = []
    queue = []  # Store characters that are currently blocked

    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)

        count += 1  # Decrement the count (as it was negated)
        queue.append((char, count))

        if len(queue) >= k:
            char, count = queue.pop(0)
            if count < 0:
                heapq.heappush(max_heap, (count, char))

    if len(result) == len(s):
        return "".join(result)
    else:
        return ""

def test_rearrange_string():
    """Tests the rearrange_string function with several test cases."""

    test_cases = [
        ("aabbcc", 3, "abcabc"),
        ("aaabc", 3, ""),
        ("aaadbbcc", 2, "abacabcd"),
        ("a", 0, "a"),
        ("a", 1, "a"),
        ("abc", 0, "abc"),
        ("abc", 1, "abc"),
        ("aabb", 2, "abab"),
        ("aaabbc", 2, "abcaba"),
        ("aaaa", 2, ""),
        ("abbba", 2, ""),
        ("aaaaabc", 2, ""),
        ("aaaaaaaaaaaaabc", 2, ""),

    ]

    correct_count = 0
    total_tests = len(test_cases)

    for s, k, expected in test_cases:
        actual = rearrange_string(s, k)
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: s='{s}', k={k}")
            print(f"Expected: '{expected}'")
            print(f"Actual: '{actual}'")

    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    test_rearrange_string()