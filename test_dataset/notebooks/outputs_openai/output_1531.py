def run_length_encoding_min_length(s: str, k: int) -> int:
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, k_left, last, cnt):
        if k_left < 0:
            return float('inf')
        if i == len(s):
            if cnt == 0:
                return 0
            return 1 + (len(str(cnt)) if cnt > 1 else 0)
        # Option 1: delete s[i]
        option1 = dp(i + 1, k_left - 1, last, cnt)
        # Option 2: keep s[i]
        if s[i] == last:
            new_cnt = cnt + 1
            added_length = 0
            if new_cnt == 2 or new_cnt == 10 or new_cnt == 100:
                added_length +=1
            option2 = added_length + dp(i + 1, k_left, last, new_cnt)
        else:
            added_length = 1
            if cnt >1:
                added_length += len(str(cnt))
            option2 = added_length + dp(i + 1, k_left, s[i], 1)
        return min(option1, option2)

    return dp(0, k, '', 0)

def test():
    tests = [
        {"s": "aaabcccd", "k": 2, "expected": 4},
        {"s": "aabbaa", "k": 2, "expected": 2},
        {"s": "aaaaaaaaaaa", "k": 0, "expected": 3},
    ]
    correct = 0
    for test_case in tests:
        s = test_case["s"]
        k = test_case["k"]
        expected = test_case["expected"]
        result = run_length_encoding_min_length(s, k)
        is_correct = result == expected
        print(is_correct)
        if is_correct:
            correct +=1
    print(f"{correct}/{len(tests)}")

test()