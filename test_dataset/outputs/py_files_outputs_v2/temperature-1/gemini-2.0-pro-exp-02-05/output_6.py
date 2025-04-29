def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    row_index = 0
    direction = -1  # Start by going "down" (0 -> 1 -> 2)

    for char in s:
        rows[row_index] += char
        if row_index == 0 or row_index == numRows - 1:
            direction *= -1  # Change direction at top and bottom
        row_index += direction

    return ''.join(rows)