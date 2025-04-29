import re
from collections import Counter

def mostCommonWord(paragraph, banned):
    """
    Finds the most frequent word that is not banned in a given paragraph.

    Args:
        paragraph (str): The input paragraph.
        banned (list[str]): A list of banned words.

    Returns:
        str: The most frequent non-banned word in lowercase.
    """
    words = re.findall(r'\b\w+\b', paragraph.lower())
    word_counts = Counter(word for word in words if word not in banned)
    return word_counts.most_common(1)[0][0]

def test_mostCommonWord():
    """
    Tests the mostCommonWord function with various test cases.
    """
    test_cases = [
        {
            "paragraph": "Bob hit a ball, the hit BALL flew far after it was hit.",
            "banned": ["hit"],
            "expected": "ball"
        },
        {
            "paragraph": "a.",
            "banned": [],
            "expected": "a"
        },
        {
            "paragraph": "a, a, a, a, b,b,b,c, c",
            "banned": ["a"],
            "expected": "b"
        },
        {
            "paragraph": "Bob",
            "banned": [],
            "expected": "bob"
        },
        {
            "paragraph": "Bob. hIt, baLl",
            "banned": ["bob", "hit"],
            "expected": "ball"
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        paragraph = test_case["paragraph"]
        banned = test_case["banned"]
        expected = test_case["expected"]
        
        result = mostCommonWord(paragraph, banned)
        
        if result == expected:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False (Expected: {expected}, Got: {result})")
    
    print(f"\n{correct_tests}/{total_tests} correct tests")
    
if __name__ == "__main__":
    test_mostCommonWord()