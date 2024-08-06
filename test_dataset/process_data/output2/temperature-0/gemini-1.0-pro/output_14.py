import unittest

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other_str in strs:
            if other_str[i] != char:
                return shortest_str[:i]
    return shortest_str


class TestLongestCommonPrefix(unittest.TestCase):

    def test_example_1(self):
        input1 = ["flower", "flow", "flight"]
        output1 = "fl"
        self.assertEqual(longest_common_prefix(input1), output1)

    def test_example_2(self):
        input2 = ["dog", "racecar", "car"]
        output2 = ""
        self.assertEqual(longest_common_prefix(input2), output2)

    def test_empty_array(self):
        input3 = []
        output3 = ""
        self.assertEqual(longest_common_prefix(input3), output3)

if __name__ == '__main__':
    unittest.main()