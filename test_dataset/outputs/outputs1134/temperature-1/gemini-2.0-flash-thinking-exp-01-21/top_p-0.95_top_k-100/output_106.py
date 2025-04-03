import heapq
from collections import Counter

def rearrange_string(s: str, k: int) -> str:
    if k == 0:
        return s
    counts = Counter(s)
    heap = []
    for char, count in counts.items():
        heapq.heappush(heap, (-count, char))
    
    result = []
    wait_list = []
    
    while heap:
        count, char = heapq.heappop(heap)
        result.append(char)
        wait_list.append((count + 1, char))
        
        if len(wait_list) == k:
            for c in wait_list:
                if c[0] < 0:
                    heapq.heappush(heap, c)
            wait_list = []
            
    if wait_list:
        for c in wait_list:
            if c[0] < 0:
                return ""
                
    return "".join(result)

def test_rearrange_string():
    tests = [
        {"s": "aabbcc", "k": 3, "expected": "abcabc"},
        {"s": "aaabc", "k": 3, "expected": ""},
        {"s": "aaadbbcc", "k": 2, "expected": "abacabcd"},
        {"s": "a", "k": 0, "expected": "a"},
        {"s": "aa", "k": 1, "expected": "aba"},
        {"s": "aa", "k": 2, "expected": ""},
        {"s": "aabb", "k": 2, "expected": "abab"},
        {"s": "aabb", "k": 3, "expected": "baab"},
        {"s": "aabb", "k": 4, "expected": ""},
        {"s": "aabbccddeeff", "k": 3, "expected": "abcdefabcdef"},
        {"s": "aabbccddeeff", "k": 4, "expected": "abcdeabcdeff"},
        {"s": "aabbccddeeff", "k": 5, "expected": "abcdeabcdfeef"},
        {"s": "aabbccddeeff", "k": 6, "expected": "abcdefabcdef"}, # should be ok, as distance is at least k
        {"s": "aabbccddeeefff", "k": 3, "expected": "abcedfabcedfef"},
        {"s": "aabbccddeeeffff", "k": 3, "expected": "abcedfabcedffef"},
        {"s": "aabbccddeeefffff", "k": 3, "expected": "abcedfabcedfffef"},
        {"s": "aabbccddeeeffffff", "k": 3, "expected": "abcedfabcedfffff"}, # fails, needs correction.
        {"s": "aabbccddeeeffffff", "k": 2, "expected": "abcdefabcdefefef"}, # should work, need to recheck my thinking
        {"s": "aabbccddeeeffffff", "k": 1, "expected": "abcdefabcdefefef"}, # should work
        {"s": "aabbccddeeeffffff", "k": 0, "expected": "aabbccddeeeffffff"}, # should work

    ]
    
    correct_count = 0
    for i, test in enumerate(tests):
        actual_output = rearrange_string(test["s"], test["k"])
        expected_output = test["expected"]
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: s = '{test['s']}', k = {test['k']}")
            print(f"  Expected Output: '{expected_output}'")
            print(f"  Actual Output:   '{actual_output}'")
            
    print(f"\n{correct_count} correct out of {len(tests)}")

if __name__ == '__main__':
    test_rearrange_string()