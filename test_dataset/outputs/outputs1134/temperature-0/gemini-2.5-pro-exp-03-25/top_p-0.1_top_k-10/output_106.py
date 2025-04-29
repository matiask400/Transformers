import collections
import heapq
import io
import sys

class Solution:
    """
    Solves the problem of rearranging a string such that the same characters
    are at least distance k from each other.
    """
    def rearrangeString(self, s: str, k: int) -> str:
        """
        Rearranges the string s such that the same characters are at least
        distance k apart.

        Args:
            s: The input string.
            k: The minimum distance between identical characters.

        Returns:
            The rearranged string if possible, otherwise an empty string "".
        """
        n = len(s)
        if k <= 1:
            # If k is 0 or 1, any arrangement is valid, including the original.
            # k=0 means distance >= 0, always true.
            # k=1 means distance >= 1, always true for distinct positions.
            return s

        counts = collections.Counter(s)
        # Max heap storing tuples of (-frequency, character).
        # We use negative frequency because heapq implements a min-heap.
        max_heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(max_heap)

        result = []
        # Wait queue stores tuples of (available_index, count, char).
        # It holds characters that have been recently used and cannot be used
        # again until they reach their 'available_index'.
        wait_q = collections.deque()

        for i in range(n):
            # Check the wait queue. If the character at the front is now
            # available (its available_index is the current index i),
            # move it back to the max_heap.
            while wait_q and wait_q[0][0] == i:
                _, count, char = wait_q.popleft()
                heapq.heappush(max_heap, (-count, char))

            # If the max_heap is empty at this point, it means we cannot find
            # a valid character to place at the current position i that
            # satisfies the k-distance constraint. All remaining characters
            # are still in the wait_q.
            if not max_heap:
                return ""

            # Get the most frequent available character from the max_heap.
            neg_count, char = heapq.heappop(max_heap)
            count = -neg_count

            # Append the chosen character to the result.
            result.append(char)

            # Decrement the count of the chosen character.
            new_count = count - 1
            # If the character still needs to be placed more times,
            # add it to the wait queue with its next available index (i + k).
            if new_count > 0:
                wait_q.append((i + k, new_count, char))

        # If the loop completes, we have successfully built the rearranged string.
        return "".join(result)

# --- Testing Framework ---

def run_tests():
    """
    Runs the test cases against the Solution.rearrangeString method.
    """
    sol = Solution()
    tests = [
        # Example 1
        {"s": "aabbcc", "k": 3, "expected": ["abcabc", "acbacb", "bacabc", "bcabca", "cabacb", "cbabca"]}, # Multiple valid outputs possible
        # Example 2
        {"s": "aaabc", "k": 3, "expected": [""]},
        # Example 3
        {"s": "aaadbbcc", "k": 2, "expected": ["abacabcd", "abcabacd", "acabcabd", "acbacabd", "bacabcda", "bcabcada", "cabacabd", "cbacabda"]}, # Multiple valid outputs possible
        # Additional Test Cases
        {"s": "a", "k": 0, "expected": ["a"]},
        {"s": "a", "k": 1, "expected": ["a"]},
        {"s": "a", "k": 2, "expected": ["a"]},
        {"s": "aa", "k": 0, "expected": ["aa"]},
        {"s": "aa", "k": 1, "expected": ["aa"]},
        {"s": "aa", "k": 2, "expected": [""]},
        {"s": "ab", "k": 0, "expected": ["ab"]},
        {"s": "ab", "k": 1, "expected": ["ab"]},
        {"s": "ab", "k": 2, "expected": ["ab", "ba"]},
        {"s": "aaa", "k": 2, "expected": [""]},
        {"s": "aabb", "k": 2, "expected": ["abab", "baba"]},
        {"s": "aaabb", "k": 3, "expected": ["ababa"]},
        {"s": "aaabc", "k": 2, "expected": ["abaca", "acaba"]},
        {"s": "abcdefg", "k": 2, "expected": ["abcdefg"]}, # Any order works
        {"s": "zzzaac", "k": 3, "expected": ["zacza", "zcaza"]},
        {"s": "bbabcaca", "k": 3, "expected": ["abcabcab", "acbacbac", "bacbacba", "bcabcabc", "cabacbac", "cbacbaca"]}, # Multiple valid outputs
        {"s": "aaaaabbbbbccccc", "k": 3, "expected": ["abcabcabcabcabc"]}, # Multiple valid outputs
        {"s": "aaaaabbbbbccccc", "k": 4, "expected": [""]},
        {"s": "aaaaabbbbbcccccddddd", "k": 5, "expected": ["abcdabcdabcdabcdabcd"]}, # Multiple valid outputs
        {"s": "aaaaabbbbbcccccddddd", "k": 6, "expected": [""]},
        {"s": "programming", "k": 3, "expected": ["pgmirornga", "pgroirmnga", "rgmoprinag", "rgmopirang"]}, # Multiple valid outputs
        {"s": "aabbccddeeff", "k": 2, "expected": ["abcdefabcdef", "acebdfacebdf"]}, # Multiple valid outputs
    ]

    correct_count = 0
    total_tests = len(tests)

    # Capture stdout to prevent interference with test results
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    for i, test in enumerate(tests):
        s_input = test["s"]
        k_input = test["k"]
        expected_outputs = test["expected"]

        # Run the solution
        actual_output = sol.rearrangeString(s_input, k_input)

        # Restore stdout
        sys.stdout = original_stdout

        # Validate the output
        passed = False
        if actual_output in expected_outputs:
             # If the output is one of the expected valid outputs, check constraints
            if actual_output == "":
                 passed = True # Correctly identified impossibility
            else:
                # Check length
                if len(actual_output) != len(s_input):
                    print(f"Test {i+1} Failed: Length mismatch. Input: s='{s_input}', k={k_input}. Got: '{actual_output}', Expected one of: {expected_outputs}")
                    continue # Skip further checks for this test

                # Check character counts
                if collections.Counter(actual_output) != collections.Counter(s_input):
                     print(f"Test {i+1} Failed: Character count mismatch. Input: s='{s_input}', k={k_input}. Got: '{actual_output}', Expected one of: {expected_outputs}")
                     continue # Skip further checks for this test

                # Check k-distance constraint
                valid_distance = True
                last_pos = {}
                for idx, char in enumerate(actual_output):
                    if char in last_pos:
                        if idx - last_pos[char] < k_input:
                            valid_distance = False
                            break
                    last_pos[char] = idx

                if valid_distance:
                    passed = True
                else:
                     print(f"Test {i+1} Failed: k-distance constraint violated. Input: s='{s_input}', k={k_input}. Got: '{actual_output}', Expected one of: {expected_outputs}")
                     continue # Skip further checks for this test

        # Print result for the current test
        print(passed)
        if passed:
            correct_count +=
        else:
             # Print failure details only if validation failed above or output not in expected list
             if actual_output not in expected_outputs:
                 print(f"Test {i+1} Failed: Output mismatch. Input: s='{s_input}', k={k_input}. Got: '{actual_output}', Expected one of: {expected_outputs}")


        # Capture stdout again for the next iteration
        sys.stdout = io.StringIO()

    # Restore stdout finally
    sys.stdout = original_stdout

    # Print summary
    print(f"{correct_count}/{total_tests}")

if __name__ == "__main__":
    run_tests()