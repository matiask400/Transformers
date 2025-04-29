import re
from collections import Counter

def mostCommonWord(paragraph, banned):
    """
    Given a string `paragraph` and a string array of the banned words `banned`,
    return the most frequent word that is not banned.
    It is guaranteed there is at least one word that is not banned, and that the answer is unique.

    The words in `paragraph` are case-insensitive and the answer should be returned in lowercase.
    """
    words = re.findall(r'\b\w+\b', paragraph.lower())
    word_counts = Counter(w for w in words if w not in banned)
    return word_counts.most_common(1)[0][0]

def test_mostCommonWord():
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
            "paragraph": "Bob. hit, ball",
            "banned": ["hit"],
            "expected": "ball"
        },
        {
            "paragraph": "a, a, a, a, b,b,b,c, c",
            "banned": ["a"],
            "expected": "b"
        },
        {
            "paragraph": "abc abc? abcd the jeff!",
            "banned": ["abc","abcd","jeff"],
            "expected": "the"
        }
    ]

    num_correct = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        paragraph = test_case["paragraph"]
        banned = test_case["banned"]
        expected = test_case["expected"]
        
        result = mostCommonWord(paragraph, banned)
        
        if result == expected:
            print("True")
            num_correct += 1
        else:
            print("False")
            print(f"Test case {i+1} failed:")
            print(f"  Input: paragraph = '{paragraph}', banned = {banned}")
            print(f"  Expected: '{expected}'")
            print(f"  Got: '{result}'")

    print(f"{num_correct}/{total_tests}")

if __name__ == "__main__":
    test_mostCommonWord()