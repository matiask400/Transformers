class WordFilter:
    def __init__(self, words):
        self.words = words

    def f(self, prefix, suffix):
        indices = []
        for i, word in enumerate(self.words):
            if word.startswith(prefix) and word.endswith(suffix):
                indices.append(i)
        if not indices:
            return -1
        else:
            return max(indices)

def test_word_filter():
    tests = [
        ((["apple"], "a", "e"), 0),
        ((["apple", "banana"], "a", "a"), 0),
        ((["apple", "banana"], "b", "a"), 1),
        ((["apple", "banana"], "ap", "e"), 0),
        ((["apple", "banana"], "ban", "a"), 1),
        ((["apple", "banana"], "app", "e"), 0),
        ((["apple", "banana"], "bana", "a"), 1),
        ((["apple", "banana"], "appl", "e"), 0),
        ((["apple", "banana"], "banaa", "a"), 1),
        ((["apple", "banana"], "apple", "e"), -1),
        ((["apple", "banana"], "banana", "a"), -1),
        ((["apple", "banana"], "apple", "apple"), -1),
        ((["apple", "banana"], "banana", "banana"), -1),
        ((["apple", "banana", "apple"], "a", "e"), 2),
        ((["apple", "banana", "apple"], "app", "e"), 2),
    ]
    
    correct_count = 0
    for i, ((words, prefix, suffix), expected) in enumerate(tests):
        wf = WordFilter(words)
        result = wf.f(prefix, suffix)
        if result == expected:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
    
    print(f"{correct_count}/{len(tests)}")

if __name__ == "__main__":
    test_word_filter()