import sys

def solve():
    """
    Solves the Hexspeak problem and runs tests.
    """

    def toHexspeak(num: str) -> str:
        """
        Converts a decimal number string to its Hexspeak representation.

        Args:
            num: A string representing a decimal integer N (1 <= N <= 10^12).

        Returns:
            The Hexspeak representation if valid, otherwise "ERROR".
        """
        try:
            n = int(num)
        except ValueError:
            # Should not happen based on constraints, but good practice
            return "ERROR"

        # 1. Convert to uppercase hexadecimal string
        hex_n = hex(n)[2:].upper() # [2:] removes the "0x" prefix

        # 2. Replace '0' with 'O' and '1' with 'I'
        hexspeak_candidate = hex_n.replace('0', 'O').replace('1', 'I')

        # 3. Validate the result
        allowed_chars = set("ABCDEFIO")
        for char in hexspeak_candidate:
            if char not in allowed_chars:
                # Found a character not in the allowed set (e.g., 2-9)
                return "ERROR"

        # 4. Return the valid Hexspeak string
        return hexspeak_candidate

    # --- Test Runner ---
    tests = [
        # Input num_str, Expected Output
        ("257", "IOI"),          # Example 1: 257 -> 101 -> IOI
        ("3", "ERROR"),          # Example 2: 3 -> 3 -> ERROR
        ("619879596177", "ERROR"), # Large number: hex 90ABCDEF121 -> 9OABCDEFII2I -> ERROR (9, 2)
        ("10", "A"),             # 10 -> A
        ("16", "IO"),            # 16 -> 10 -> IO
        ("17", "II"),            # 17 -> 11 -> II
        ("2730", "ABC"),         # 2730 -> ABC
        ("48879", "BEEF"),       # 48879 -> BEEF
        ("747823", "ERROR"),     # 747823 -> B692F -> ERROR (6, 9, 2)
        ("1", "I"),              # 1 -> 1 -> I
        ("4096", "IOOO"),        # 4096 -> 1000 -> IOOO
        ("4369", "IIII"),        # 4369 -> 1111 -> IIII
        ("69905", "IIIII"),      # 69905 -> 11111 -> IIIII
        ("99", "ERROR"),         # 99 -> 63 -> ERROR (6, 3)
        (str(10**12), "ERROR"),  # Max constraint: 10^12 -> E8D4A51000 -> E8D4A5IOOO -> ERROR (8, 4, 5)
        ("26", "IA"),            # 26 -> 1A -> IA
        ("27", "IB"),            # 27 -> 1B -> IB
        ("28", "IC"),            # 28 -> 1C -> IC
        ("29", "ID"),            # 29 -> 1D -> ID
        ("30", "IE"),            # 30 -> 1E -> IE
        ("31", "IF"),            # 31 -> 1F -> IF
        ("256", "IOO"),          # 256 -> 100 -> IOO
    ]

    correct_count = 0
    total_tests = len(tests)

    # Run tests and print results
    for i, (num_input, expected_output) in enumerate(tests):
        result = toHexspeak(num_input)
        passed = result == expected_output
        print(f"{passed}") # Print True/False for the current test
        if passed:
            correct_count += 1
        # Optional: Print details on failure
        # else:
        #     print(f"  Input: {num_input}")
        #     print(f"  Expected: {expected_output}")
        #     print(f"  Got: {result}")


    # Print the final summary
    print(f"{correct_count}/{total_tests}")

# Execute the solve function when the script is run
if __name__ == "__main__":
    solve()