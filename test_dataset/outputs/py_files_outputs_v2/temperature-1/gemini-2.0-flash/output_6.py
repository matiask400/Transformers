def convert(s, numRows):
    """
    The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: `"PAHNAPLSIIGYIR"`
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    row_index = 0
    going_down = True

    for char in s:
        rows[row_index] += char

        if row_index == 0:
            going_down = True
        elif row_index == numRows - 1:
            going_down = False

        row_index += 1 if going_down else -1

    return ''.join(rows)