if __name__ == "__main__":
    # Example 1: Test Input
    num1 = 3
    result1 = int_to_roman(num1)
    print("Input: num = {}".format(num1))
    print("Output: {}".format(result1))
    print("Expected: III")
    print("Correct? {}".format(result1 == "III"))

    # Example 2: Test Input
    num2 = 4
    result2 = int_to_roman(num2)
    print("Input: num = {}".format(num2))
    print("Output: {}".format(result2))
    print("Expected: IV")
    print("Correct? {}".format(result2 == "IV"))

    # Example 3: Test Input
    num3 = 9
    result3 = int_to_roman(num3)
    print("Input: num = {}".format(num3))
    print("Output: {}".format(result3))
    print("Expected: IX")
    print("Correct? {}".format(result3 == "IX"))

    # Example 4: Test Input
    num4 = 58
    result4 = int_to_roman(num4)
    print("Input: num = {}".format(num4))
    print("Output: {}".format(result4))
    print("Expected: LVIII")
    print("Correct? {}".format(result4 == "LVIII"))

    # Example 5: Test Input
    num5 = 1994
    result5 = int_to_roman(num5)
    print("Input: num = {}".format(num5))
    print("Output: {}".format(result5))
    print("Expected: MCMXCIV")