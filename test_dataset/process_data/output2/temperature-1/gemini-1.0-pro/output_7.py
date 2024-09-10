import sys

def reverse(x: int) -> int:
    rev = 0
    neg = x < 0
    x = abs(x)
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    rev = -rev if neg else rev
    return rev if -2**31 <= rev <= 2**31 - 1 else 0

if __name__ == '__main__':
    test_cases = [(123, 321), (-123, -321), (120, 21), (0, 0), (-1534236469, 0)]
    for input, expected in test_cases:
        result = reverse(input)
        print(result == expected)