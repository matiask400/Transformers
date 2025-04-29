class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    def getHeight(node):
        if not node:
            return 0
        return 1 + max(getHeight(node.left), getHeight(node.right))
    
    def fill(res, node, r, c, height):
        if node:
            res[r][c] = str(node.val)
            offset = 2**(height - r - 2) if height - r - 2 >=0 else 0
            if node.left:
                fill(res, node.left, r+1, c - offset, height)
            if node.right:
                fill(res, node.right, r+1, c + offset, height)
    
    height = getHeight(root)
    if height ==0:
        return []
    width = 2**height -1
    res = [["" for _ in range(width)] for _ in range(height)]
    fill(res, root, 0, (width-1)//2, height)
    return res

# Function to compare two 2D lists
def compare(a, b):
    if len(a) != len(b):
        return False
    for row_a, row_b in zip(a, b):
        if row_a != row_b:
            return False
    return True

# Test cases
tests = [
    {
        "input": TreeNode(1, TreeNode(2), None),
        "expected": [["", "1", ""],
                     ["2", "", ""]]
    },
    {
        "input": TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)),
        "expected": [["", "", "", "1", "", "", ""],
                     ["", "2", "", "", "", "3", ""],
                     ["", "", "4", "", "", "", ""]]
    },
    {
        "input": TreeNode(1, 
                          TreeNode(2, 
                                   TreeNode(3, 
                                            TreeNode(4),
                                            None),
                                   None),
                          TreeNode(5)),
        "expected": [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
                     ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""],
                     ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
                     ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
    }
]

correct = 0
total = len(tests)
for test in tests:
    output = printTree(test["input"])
    if compare(output, test["expected"]):
        print("True")
        correct +=1
    else:
        print("False")
print(f"{correct}/{total}")