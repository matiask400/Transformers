import re

def most_frequent_word(paragraph, banned):
    """
    Given a string paragraph and a string array of the banned words banned,
    return the most frequent word that is not banned.
    It is guaranteed there is at least one word that is not banned,
    and that the answer is unique.

    The words in paragraph are case-insensitive and the answer should be returned in lowercase.
    """
    paragraph = paragraph.lower()
    words = re.findall(r'\b\w+\b', paragraph)
    banned_words = set(banned)
    word_counts = {}
    for word in words:
        if word not in banned_words:
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
            "paragraph": "Jack and Jill went up the hill to fetch a pail of water. Jack fell down and broke his crown and Jill came tumbling after.",
            "banned": ["jack", "jill", "hill", "water"],
            "expected_output": "and"
        },
        {
            "paragraph": "Luffy is still joyboy joyboy",
            "banned": ["joyboy"],
            "expected_output": "luffy"
        }
    ]

    correct_tests = 0
    total_tests = len(test_cases)

    for i, test_case in enumerate(test_cases):
        paragraph = test_case["paragraph"]
        banned = test_case["banned"]
        expected_output = test_case["expected_output"]
        actual_output = most_frequent_word(paragraph, banned)
        if actual_output == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")

    print(f"{correct_tests}/{total_tests}")

if __name__ == '__main__':
    run_tests()