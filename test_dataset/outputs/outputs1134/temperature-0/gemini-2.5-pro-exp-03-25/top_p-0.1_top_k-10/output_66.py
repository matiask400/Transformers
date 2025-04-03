import sys
import io

def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    Counts how many stones are also jewels.

    Args:
        jewels: A string representing the types of stones that are jewels.
        stones: A string representing the stones you have.

    Returns:
        The number of stones you have that are also jewels.
    """
    # Create a set of jewels for efficient O(1) average time lookup.
    jewel_set = set(jewels)
    
    count = 0
    # Iterate through each stone you have.
    for stone in stones:
        # If the stone is present in the set of jewels, increment the count.
        if stone in jewel_set:
            count += 1
            
    return count

# --- Testing Framework ---

def run_tests():
    """
    Runs predefined test cases against the numJewelsInStones function.
    """
    test_cases = [
        # Example 1
        {"input": {"jewels": "aA", "stones": "aAAbbbb"}, "expected": 3},
        # Example 2
        {"input": {"jewels": "z", "stones": "ZZ"}, "expected": 0},
        # Additional Test Cases
        {"input": {"jewels": "abc", "stones": "aabbccddeeff"}, "expected": 6},
        {"input": {"jewels": "Xy", "stones": "xYxYxY"}, "expected": 0}, # Case sensitivity
        {"input": {"jewels": "Jewels", "stones": "Stones"}, "expected": 2}, # 'e', 's'
        {"input": {"jewels": "", "stones": "abc"}, "expected": 0}, # No jewels
        {"input": {"jewels": "abc", "stones": ""}, "expected": 0}, # No stones
        {"input": {"jewels": "a", "stones": "aaaaaaaaaa"}, "expected": 10}, # All stones are jewels
        {"input": {"jewels": "b", "stones": "aaaaaaaaaa"}, "expected": 0}, # No stones are jewels
        {"input": {"jewels": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "stones": "AbCdEfGhIjKlMnOpQrStUvWxYz"}, "expected": 26}, # All uppercase stones are jewels
    ]

    correct_count = 0
    total_tests = len(test_cases)

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    for i, test in enumerate(test_cases):
        jewels_input = test["input"]["jewels"]
        stones_input = test["input"]["stones"]
        expected_output = test["expected"]
        
        # Run the function with the test input
        actual_output = numJewelsInStones(jewels_input, stones_input)
        
        # Compare the actual output with the expected output
        is_correct = (actual_output == expected_output)
        
        # Print True or False for the test result
        print(f"{is_correct}")
        
        if is_correct:
            correct_count += 1

    # Restore stdout
    sys.stdout = old_stdout
    
    # Print the captured output (True/False for each test)
    print(captured_output.getvalue(), end="")

    # Print the final summary
    print(f"\n{correct_count}/{total_tests}")

# Execute the tests when the script is run
if __name__ == "__main__":
    run_tests()