import heapq
from collections import Counter, deque

def rearrangeString(s, k):
    if k <= 1:
        return s
    freq = Counter(s)
    max_heap = [(-cnt, char) for char, cnt in freq.items()]
    heapq.heapify(max_heap)
    wait_queue = deque()
    result = []
    
    while max_heap or wait_queue:
        if max_heap:
            cnt, char = heapq.heappop(max_heap)
            result.append(char)
            cnt += 1  # decrement the count since it's a max heap using negative
            wait_queue.append((cnt, char))
            if len(wait_queue) >= k:
                front_cnt, front_char = wait_queue.popleft()
                if front_cnt < 0:
                    heapq.heappush(max_heap, (front_cnt, front_char))
        else:
            # If heap is empty but wait_queue still has items, it's impossible to rearrange
            return ""
    return ''.join(result)

def run_tests():
    tests = [
        # Example tests
        {"s": "aabbcc", "k": 3, "expected": "abcabc"},
        {"s": "aaabc", "k": 3, "expected": ""},
        {"s": "aaadbbcc", "k": 2, "expected": "abacabcd"},
        # Additional tests
        {"s": "aa", "k": 0, "expected": "aa"},
        {"s": "aa", "k": 1, "expected": "aa"},
        {"s": "aab", "k": 2, "expected": "aba"},
        {"s": "aabbccddeeff", "k": 2, "expected": "abcdefabcdef"},
        {"s": "aaaaa", "k": 2, "expected": ""},
        {"s": "a", "k": 2, "expected": "a"},
        {"s": "aaabbb", "k": 2, "expected": "ababab"},
    ]
    
    correct = 0
    total = len(tests)
    for test in tests:
        output = rearrangeString(test["s"], test["k"])
        if output == test["expected"]:
            print("True")
            correct += 1
        else:
            print("False")
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()