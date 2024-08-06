import unittest

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [[] for _ in range(numRows)]
    row = 0
    direction = 1
    for i in range(len(s)):
        rows[row].append(s[i])
        if row == numRows - 1:
            direction = -1
        elif row == 0:
            direction = 1
        row += direction
    return ''.join([''.join(row) for row in rows])

class TestConvert(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
    def test_example_2(self):
        self.assertEqual(convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
    def test_example_3(self):
        self.assertEqual(convert('A', 1), 'A')

if __name__ == '__main__':
    unittest.main()