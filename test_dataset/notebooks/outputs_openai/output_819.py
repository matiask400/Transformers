import re
from collections import Counter

def most_frequent_word(paragraph, banned):
    # Normalize the paragraph to lowercase
    paragraph = paragraph.lower()
    # Replace punctuation with spaces
    paragraph = re.sub(r'[!?\',;.]', ' ', paragraph)
    # Split into words
    words = paragraph.split()
    # Create a set of banned words for faster lookup
    banned_set = set(banned)
    # Count the frequency of each non-banned word
    counts = Counter(word for word in words if word not in banned_set)
    # Return the most common word
    return counts.most_common(1)[0][0]

def run_tests():
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
            "paragraph": "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food.",
            "banned": ["and", "he", "the", "to", "is", "jack's", "jill's"],
            "expected": "cheese"
        },
        {
            "paragraph": "It was the best of times, it was the worst of times.",
            "banned": ["it", "was", "the", "of"],
            "expected": "times"
        },
        {
            "paragraph": "Hello, hello! HELLO?",
            "banned": [],
            "expected": "hello"
        },
        {
            "paragraph": "a a a b b c",
            "banned": ["a"],
            "expected": "b"
        }
    ]
    
    correct = 0
    total = len(test_cases)
    
    for test in test_cases:
        output = most_frequent_word(test["paragraph"], test["banned"])
        result = output == test["expected"]
        print(result)
        if result:
            correct += 1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()