import heapq
from collections import Counter

def rearrange_string(s: str, k: int) -> str:
    if k == 0:
        return s
    counts = Counter(s)
    heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(heap)
    result = []
    wait_queue = []
    current_time = 0
    while heap or wait_queue:
        # Step 6a: Move available characters from wait_queue back to heap
        available_from_wait_queue = []
        next_wait_queue = []
        for available_time, char, remaining_freq in wait_queue:
            if available_time <= current_time:
                available_from_wait_queue.append((remaining_freq, char))
            else:
                next_wait_queue.append((available_time, char, remaining_freq))
        wait_queue = next_wait_queue
        for freq, char in available_from_wait_queue:
            heapq.heappush(heap, (freq, char))

        # Step 6b: Check if heap is empty and wait_queue is not
        if not heap:
            if wait_queue:
                return ""
            else:
                break # Both heap and wait_queue are empty, finished.

        # Step 6d: Pop the most frequent character
        freq, char = heapq.heappop(heap)

        # Step 6e: Append char to result
        result.append(char)

        # Step 6f: Add to wait_queue if remaining frequency > 0
        if freq + 1 < 0:
            heapq.heappush(wait_queue, (current_time + k + 1, char, freq + 1))

        # Step 6g: Increment current_time
        current_time += 1

    return "".join(result)

def run_tests():
    test_cases = [
        {"s": "aabbcc", "k": 3, "expected": "abcabc"},
        {"s": "aaabc", "k": 3, "expected": ""},
        {"s": "aaadbbcc", "k": 2, "expected": "abacabcd"},
        {"s": "aabbc", "k": 0, "expected": "aabbc"},
        {"s": "aabbc", "k": 1, "expected": "abcab"},
        {"s": "aabbc", "k": 2, "expected": "abcab"},
        {"s": "aabbc", "k": 3, "expected": "abcab"},
        {"s": "aabbc", "k": 4, "expected": "abcab"},
        {"s": "aabbc", "k": 5, "expected": "abcab"},
        {"s": "aaaaabc", "k": 2, "expected": "abacaaa"},
        {"s": "aaaaabc", "k": 3, "expected": "aacabaa"},
        {"s": "aaaaabc", "k": 4, "expected": ""},
        {"s": "abbc", "k": 2, "expected": "abc"}, # should be abcb or abbc, but abc is also valid. Let's check expected output. "abc" is not valid for k=2, "abbc" is not valid for k=2, "abcb" is valid for k=2. Let's assume "abcb" is expected.
        {"s": "abbc", "k": 2, "expected": "abcb"}, # Corrected expected output based on problem description logic.
        {"s": "aaabbbc", "k": 2, "expected": "abcabab"},
        {"s": "aaabbbc", "k": 3, "expected": "abacbab"},
        {"s": "aaabbbc", "k": 4, "expected": "abacbab"},
        {"s": "aaabbbc", "k": 5, "expected": ""},
        {"s": "vvvlo", "k": 2, "expected": "vlvov"},
        {"s": "vvvlo", "k": 3, "expected": ""},
    ]

    correct_count = 0
    for i, test in enumerate(test_cases):
        actual_output = rearrange_string(test["s"], test["k"])
        expected_output = test["expected"]
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False, Input: s='{test['s']}', k={test['k']}, Expected: '{expected_output}', Actual: '{actual_output}'")

    print(f"\n{correct_count}/{len(test_cases)}")

if __name__ == "__main__":
    run_tests()