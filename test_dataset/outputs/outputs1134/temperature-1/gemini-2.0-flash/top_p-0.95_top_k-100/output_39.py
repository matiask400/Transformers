def shortest_encoding(words):
    """
    Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
    """
    words = sorted(list(set(words)), key=len, reverse=True)
    s = ""
    for word in words:
        if word + "#" in s:
            continue
        is_substring = False
        for other_word in words:
            if word != other_word and word in other_word:
                is_substring = True
                break
        if not is_substring:
            s += word + "#"
    return len(s)

def test_shortest_encoding():
    tests = [
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["time", "me", "time"], 5),
        (["time", "me", "bell", "time"], 10),
        (["time", "me", "bell", "time", "e"], 11),
        (["time", "me", "bell", "time", "e", "m"], 11),
        (["feffeeffee", "ffee"], 11),
    ]
    
    correct_tests = 0
    total_tests = len(tests)

    for i, (input_words, expected_output) in enumerate(tests):
        result = shortest_encoding(input_words)
        if result == expected_output:
            print(f"Test {i+1}: True")
            correct_tests += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_words}")
            print(f"  Expected: {expected_output}")
            print(f"  Got: {result}")
    
    print(f"{correct_tests}/{total_tests}")

if __name__ == "__main__":
    test_shortest_encoding()