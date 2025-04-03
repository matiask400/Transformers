class WordFilter:
    def __init__(self, words):
        self.mapping = {}
        for index, word in enumerate(words):
            length = len(word)
            prefixes = [word[:i] for i in range(1, length + 1)]
            prefixes.append('')
            suffixes = [word[i:] for i in range(length)]
            suffixes.append('')
            for prefix in prefixes:
                for suffix in suffixes:
                    self.mapping[(prefix, suffix)] = index

    def f(self, prefix, suffix):
        return self.mapping.get((prefix, suffix), -1)

def solve():
    # Define test cases
    test_cases = [
        {
            "commands": ["WordFilter", "f"],
            "params": [[["apple"]], ["a", "e"]],
            "expected": [None, 0]
        },
        {
            "commands": ["WordFilter","f","f"],
            "params": [[["banana","bandana","band"]], ["ban", "ana"], ["ba", "d"]],
            "expected": [None, 1, 2]
        },
        {
            "commands": ["WordFilter","f","f","f"],
            "params": [[["test","tester","testing","tested"]], ["test", "ing"], ["te", "ed"], ["tes", "er"]],
            "expected": [None, 2, 3, 1]
        },
        {
            "commands": ["WordFilter", "f", "f", "f"],
            "params": [[["apple","apply","appetite"]], ["app", "le"], ["ap", "y"], ["apple", "etite"]],
            "expected": [None, 0, 1, 2]
        },
        {
            "commands": ["WordFilter", "f"],
            "params": [[["hello","helium"]], ["he", "lo"]],
            "expected": [None, 0]
        },
        {
            "commands": ["WordFilter", "f"],
            "params": [[["cat","dog","caterpillar"]], ["ca", "pillar"]],
            "expected": [None, 2]
        },
        {
            "commands": ["WordFilter", "f"],
            "params": [[["prefix","suffix","preface","suffice"]], ["pre", "fix"]],
            "expected": [None, 0]
        },
        {
            "commands": ["WordFilter", "f"],
            "params": [[["abcd","abef","abgh","ijk"]], ["ab", "ef"]],
            "expected": [None, 1]
        },
        {
            "commands": ["WordFilter", "f"],
            "params": [[["single"]], ["s", "e"]],
            "expected": [None, 0]
        },
        {
            "commands": ["WordFilter", "f"],
            "params": [[["multiple","multiplex","multiply"]], ["multi", "ply"]],
            "expected": [None, 2]
        }
    ]
    
    total = 0
    correct = 0
    for case in test_cases:
        commands = case["commands"]
        params = case["params"]
        expected = case["expected"]
        obj = None
        for i, cmd in enumerate(commands):
            if cmd == "WordFilter":
                obj = WordFilter(*params[i])
                output = None
            elif cmd == "f":
                output = obj.f(*params[i])
            else:
                output = None
            if output == expected[i]:
                print("True")
                correct +=1
            else:
                print("False")
            total +=1
    print(f"{correct}/{total}")

solve()