def hexspeak(num: str) -> str:
    n = int(num)
    hex_str = hex(n)[2:].upper()
    hex_str = hex_str.replace('0', 'O').replace('1', 'I')
    valid_chars = set("ABCDEFIO")
    if all(c in valid_chars for c in hex_str):
        return hex_str
    else:
        return "ERROR"

def run_tests():
    tests = [
        ("257", "IOI"),
        ("3", "ERROR"),
        ("16", "IO"),
        ("15", "F"),
        ("31", "IF"),
        ("4096", "IOOO"),
        ("43690", "AAAA"),
        ("4660", "ERROR"),
        ("11259375", "ABCDEF"),
        ("11111111", "IOOIIIIOI"),
    ]
    correct = 0
    total = len(tests)
    for i, (inp, expected) in enumerate(tests, 1):
        output = hexspeak(inp)
        result = output == expected
        print(result)
        if result:
            correct +=1
    print(f"{correct}/{total}")

if __name__ == "__main__":
    run_tests()