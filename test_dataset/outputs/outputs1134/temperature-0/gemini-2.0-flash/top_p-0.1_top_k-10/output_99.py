class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    if not s:
        return None

    def parse(s):
        if not s:
            return None, ""

        i = 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        root = TreeNode(sign * num)

        if i < len(s) and s[i] == '(':
            i += 1
            left, remaining = parse(s[i:])
            root.left = left
            i += len(s[i:]) - len(remaining)

            if remaining and remaining[0] == ')':
                i += 1
                remaining = remaining[1:]
            else:
                return None, ""

            if i < len(s) and s[i] == '(':
                i += 1
                right, remaining = parse(s[i:])
                root.right = right
                i += len(s[i:]) - len(remaining)

                if remaining and remaining[0] == ')':
                    i += 1
                    remaining = remaining[1:]
                else:
                    return None, ""

        return root, s[i:]

    root, _ = parse(s)
    return root

def tree_to_list(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

def test_str2tree():
    test_cases = [
        ("4(2(3)(1))(6(5))", [4, 2, 6, 3, 1, 5]),
        ("4(2(3)(1))(6(5)(7))", [4, 2, 6, 3, 1, 5, 7]),
        ("-4(2(3)(1))(6(5)(7))", [-4, 2, 6, 3, 1, 5, 7]),
        ("1", [1]),
        ("1(2)", [1, 2]),
        ("1(2)(3)", [1, 2, 3]),
        ("", []),
        ("10(5(1)(2))(6)", [10, 5, 6, 1, 2]),
        ("1(2(4))(3)", [1, 2, 3, 4])
    ]

    correct_count = 0
    total_count = len(test_cases)

    for s, expected in test_cases:
        root = str2tree(s)
        actual = tree_to_list(root)
        
        if actual == expected:
            print("True")
            correct_count += 1
        else:
            print("False")
            print(f"Input: {s}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")

    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_str2tree()