def solve():
    def num_jewels_in_stones(jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count

    test_cases = [
        {
            "jewels": "aA",
            "stones": "aAAbbbb",
            "expected": 3
        },
        {
            "jewels": "z",
            "stones": "ZZ",
            "expected": 0
        }
    ]
    
    num_correct = 0
    for i, test_case in enumerate(test_cases):
        jewels = test_case["jewels"]
        stones = test_case["stones"]
        expected = test_case["expected"]
        
        actual = num_jewels_in_stones(jewels, stones)
        
        if actual == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
    
    print(f"{num_correct}/{len(test_cases)}")
    

solve()