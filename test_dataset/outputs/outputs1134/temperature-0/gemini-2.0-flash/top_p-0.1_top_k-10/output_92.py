def toHexspeak(num):
    """
    Converts a decimal number to its Hexspeak representation.

    Args:
        num: A string representing a decimal integer N.

    Returns:
        The Hexspeak representation of N if it is valid, otherwise "ERROR".
    """
    n = int(num)
    hex_str = hex(n)[2:].upper()
    hexspeak = hex_str.replace('0', 'O').replace('1', 'I')
    valid_chars = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}
    for char in hexspeak:
        if char not in valid_chars:
            return "ERROR"
    return hexspeak

def test_toHexspeak():
    """
    Tests the toHexspeak function with various inputs.
    """
    test_cases = [
        ("257", "IOI"),
        ("3", "ERROR"),
        ("3000000000000", "A00000000000"),
        ("1000000000000", "ERROR"),
        ("1000000000001", "ERROR"),
        ("42", "2A"),
        ("65535", "FFFF"),
        ("65536", "10000"),
        ("10", "A"),
        ("11", "B"),
        ("12", "C"),
        ("13", "D"),
        ("14", "E"),
        ("15", "F"),
        ("16", "10"),
        ("17", "11"),
        ("18", "12"),
        ("19", "13"),
        ("20", "14"),
        ("21", "15"),
        ("22", "16"),
        ("23", "17"),
        ("24", "18"),
        ("25", "19"),
        ("26", "1A"),
        ("27", "1B"),
        ("28", "1C"),
        ("29", "1D"),
        ("30", "1E"),
        ("31", "1F"),
        ("32", "20"),
        ("33", "21"),
        ("34", "22"),
        ("35", "23"),
        ("36", "24"),
        ("37", "25"),
        ("38", "26"),
        ("39", "27"),
        ("40", "28"),
        ("41", "29"),
    ]

    correct_count = 0
    total_count = len(test_cases)

    for input_num, expected_output in test_cases:
        actual_output = toHexspeak(input_num)
        if actual_output == expected_output:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {input_num}, Expected: {expected_output}, Actual: {actual_output}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_toHexspeak()