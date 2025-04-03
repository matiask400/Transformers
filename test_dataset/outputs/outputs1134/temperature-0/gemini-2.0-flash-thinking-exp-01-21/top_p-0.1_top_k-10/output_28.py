import re

def most_frequent_word(paragraph, banned):
    """
    Given a string paragraph and a string array of the banned words banned,
    return the most frequent word that is not banned.

    Args:
        paragraph (str): The input paragraph.
        banned (list[str]): A list of banned words.

    Returns:
        str: The most frequent word that is not banned.
    """
    paragraph = paragraph.lower()
    words = re.findall(r'\b\w+\b', paragraph)
    banned_set = set(banned)
    word_counts = {}
    for word in words:
        if word not in banned_set:
            word_counts[word] = word_counts.get(word, 0) + 1

    max_count = 0
    most_frequent = ""
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_frequent = word
    return most_frequent

def run_tests():
    test_cases = [
        {
            "paragraph": "Bob hit a ball, the hit BALL flew far after it was hit.",
            "banned": ["hit"],
            "expected_output": "ball"
        },
        {
            "paragraph": "a.",
            "banned": [],
            "expected_output": "a"
        },
        {
            "paragraph": "a, a, a, a, b,b,b,c, c",
            "banned": ["a"],
            "expected_output": "b"
        },
        {
            "paragraph": "Bob. hIt, baLl",
            "banned": ["bob", "ball"],
            "expected_output": "hit"
        }
    ]

    correct_count = 0
    for i, test_case in enumerate(test_cases):
        paragraph = test_case["paragraph"]
        banned = test_case["banned"]
        expected_output = test_case["expected_output"]
        actual_output = most_frequent_word(paragraph, banned)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    print(f"{correct_count}/{len(test_cases)}")

if __name__ == '__main__':
    run_tests()