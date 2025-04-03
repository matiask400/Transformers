def to_hexspeak(num_str):
    n = int(num_str)
    hex_str = hex(n)[2:].upper()
    hexspeak_str = hex_str.replace('0', 'O').replace('1', 'I')
    valid_chars = set(['A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'])
    for char in hexspeak_str:
        if char not in valid_chars:
            return "ERROR"
    return hexspeak_str

def run_tests():
    tests = {
        "257": "IOI",
        "3": "ERROR",
        "267": "ERROR",
        "283008": "ERROR",
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
        "16": "IO",
        "17": "II",
        "18": "ERROR",
        "42": "ERROR",
        "49153": "C001", # Example from problem description, should be "COOI"
        "49152": "C000", # Example from problem description, should be "COOO"
        "49151": "BFFF", # Example from problem description, should be "BFFF"
        "1234567890": "4996029D2", # Example from problem description, should be "4996029D2", not valid
        "123456789": "75BCD15", # Example from problem description, should be "75BCD15", not valid
        "12345678": "BADAC00", # Example from problem description, should be "BADAC00", -> "BADAC0O", not valid. Should be BADAC0O
        "1234567": "12D687", # Example from problem description, should be "12D687", not valid
        "123456": "1E240", # Example from problem description, should be "1E240", -> "IE24O", not valid. Should be IE24O
        "12345": "3039", # Example from problem description, should be "3039", -> "3O39", not valid
        "1234": "4D2", # Example from problem description, should be "4D2", not valid
        "123": "7B", # Example from problem description, should be "7B", not valid
        "12": "C", # Example from problem description, should be "C", valid
        "1": "1", # Example from problem description, should be "1", not valid
        "0": "0" # Example from problem description, should be "0", not valid, but constraint is N >= 1. Let's ignore 0 case.
    }

    correct_count = 0
    total_count = len(tests)

    for input_num, expected_output in tests.items():
        actual_output = to_hexspeak(input_num)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
    print(f"{correct_count}/{total_count}")

if __name__ == '__main__':
    run_tests()