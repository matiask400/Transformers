def is_prefix_word(sentence, searchWord):
    words = sentence.split(' ')
    for idx, word in enumerate(words, 1):
        if word.startswith(searchWord):
            return idx
    return -1

tests = [
    {
        'sentence': "i love eating burger",
        'searchWord': "burg",
        'expected': 4
    },
    {
        'sentence': "this problem is an easy problem",
        'searchWord': "pro",
        'expected': 2
    },
    {
        'sentence': "i am tired",
        'searchWord': "you",
        'expected': -1
    },
    {
        'sentence': "i use triple pillow",
        'searchWord': "pill",
        'expected': 4
    },
    {
        'sentence': "hello from the other side",
        'searchWord': "they",
        'expected': -1
    },
]

count_correct = 0
total = len(tests)

for test in tests:
    result = is_prefix_word(test['sentence'], test['searchWord'])
    if result == test['expected']:
        print("True")
        count_correct += 1
    else:
        print("False")

print(f"{count_correct}/{total}")