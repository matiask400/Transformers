def total_money(n: int) -> int:
    """
    Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

    He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday. 
    Given `n`, return the total amount of money he will have in the Leetcode bank at the end of the `nth` day.
    """
    weeks = n // 7
    days = n % 7
    
    total = 0
    
    for i in range(weeks):
        total += 7 * (i + 1) + 21
    
    for i in range(days):
        total += weeks + 1 + i
    
    return total

def test_total_money():
    test_cases = [
        (4, 10),
        (10, 37),
        (20, 96),
        (7, 28),
        (1, 1),
        (14, 70),
        (21, 147),
        (28, 252)
    ]
    
    correct_count = 0
    total_count = len(test_cases)
    
    for i, (input_n, expected_output) in enumerate(test_cases):
        actual_output = total_money(input_n)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"Input: {input_n}, Expected: {expected_output}, Actual: {actual_output}")
    
    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_total_money()