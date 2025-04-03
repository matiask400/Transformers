#!/usr/bin/env python3
import sys # Although not strictly necessary for Python 3 int, good practice

def solve():
    """
    Contains the main logic for solving the Hexspeak problem and the testing harness.
    """

    def toHexspeak(num: str) -> str:
        """
        Converts a decimal number string to its Hexspeak representation.

        A decimal number can be converted to its Hexspeak representation by
        first converting it to an uppercase hexadecimal string, then replacing
        all occurrences of the digit `0` with the letter `O`, and the digit `1`
        with the letter `I`. Such a representation is valid if and only if it
        consists only of the letters in the set `{"A", "B", "C", "D", "E", "F", "I", "O"}`.

        Args:
            num: A string representing a decimal integer N (1 <= N <= 10^12).

        Returns:
            The valid Hexspeak representation in uppercase, or "ERROR" if invalid.
        """
        try:
            N = int(num)
        except ValueError:
            # This case should not be reachable given the problem constraints
            # (input is always a valid decimal integer string).
            # However, it's robust to handle it.
            return "ERROR"

        # Constraint check N >= 1 is guaranteed by the problem statement.
        # if N < 1:
        #      return "ERROR"

        # 1. Convert integer N to its hexadecimal representation string
        #    hex(N) returns "0x..." format. We slice off the "0x".
        hex_str = hex(N)[2:]

        # 2. Convert the hexadecimal string to uppercase
        hex_upper = hex_str.upper()

        # 3. Replace '0' with 'O' and '1' with 'I'
        #    We can build the string character by character or use replace.
        #    Using replace is generally more efficient and concise in Python.
        hexspeak_candidate = ""
        for digit in hex_upper:
            if digit == '0':
                hexspeak_candidate += 'O'
            elif digit == '1':
                hexspeak_candidate += 'I'
            else:
                hexspeak_candidate += digit # Keep other hex digits (A-F, 2-9)

        # 4. Validate the resulting string
        #    Check if all characters are in the allowed set {"A", "B", "C", "D", "E", "F", "I", "O"}
        #    Any character that is not one of these (i.e., digits '2' through '9') makes it invalid.
        allowed_chars = set("ABCDEFIO")
        for char in hexspeak_candidate:
            if char not in allowed_chars:
                # Found a character not allowed (must be '2' through '9')
                return "ERROR"

        # 5. If all characters are valid, return the Hexspeak representation
        return hexspeak_candidate

    # --- Testing Harness ---

    test_cases = [
        # Provided Examples
        {"input": "257", "expected": "IOI"},      # 257 -> 0x101 -> 101 -> IOI (Valid)
        {"input": "3", "expected": "ERROR"},      # 3 -> 0x3 -> 3 (Invalid char '3')

        # Additional Test Cases
        {"input": "1", "expected": "I"},          # 1 -> 0x1 -> 1 -> I (Valid)
        {"input": "10", "expected": "A"},         # 10 -> 0xA -> A (Valid)
        {"input": "15", "expected": "F"},         # 15 -> 0xF -> F (Valid)
        {"input": "16", "expected": "IO"},        # 16 -> 0x10 -> 10 -> IO (Valid)
        {"input": "17", "expected": "II"},        # 17 -> 0x11 -> 11 -> II (Valid)
        {"input": "2", "expected": "ERROR"},      # 2 -> 0x2 -> 2 (Invalid char '2')
        {"input": "9", "expected": "ERROR"},      # 9 -> 0x9 -> 9 (Invalid char '9')
        {"input": "26", "expected": "IA"},        # 26 -> 0x1A -> 1A -> IA (Valid)