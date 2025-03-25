def convert(s, numRows):
    """
    The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: `"PAHNAPLSIIGYIR"`
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);
    """
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag = [''] * numRows
    row = 0
    going_down = True

    for char in s:
        zigzag[row] += char

        if row == 0:
            going_down = True
        elif row == numRows - 1:
            going_down = False

        if going_down:
            row += 1
        else:
            row -= 1

    return ''.join(zigzag)