import collections

# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def parse_helper(s: str, i: int) -> tuple[TreeNode | None, int]:
    """
    Recursively parses a substring starting at index i to build a subtree.

    Args:
        s: The input string representation of the tree.
        i: The current starting index in the string s.

    Returns:
        A tuple containing:
        - The root node of the constructed subtree (or None if no node).
        - The index in s immediately after the parsed subtree.
    """
    if i >= len(s) or s[i] == ')':
        # Base case: end of string or end of current subtree scope
        return None, i

    # --- Parse the root value ---
    start = i
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
        start = i # Update start index after potential sign

    # Read digits for the value
    while i < len(s) and s[i].isdigit():
        i += 1

    # Should always find a number if the format is correct
    if start == i and sign == 1: # Check if any digits were read after potential sign
         # This case handles scenarios like "()" or "(())" within a larger structure,
         # or if the string starts with '('. It indicates no number here.
         # However, the problem description implies a number always precedes parentheses.
         # If the input guarantees a number first, this check might be redundant
         # for the initial call, but useful for recursive calls finding empty subtrees like ()
         # Let's assume valid input structure where a number is expected if not at end or ')'.
         # If the input can be just "()", this needs adjustment.
         # Given examples, assume a number is always present when a node is expected.
         pass # Continue, assuming valid number was parsed

    value = sign * int(s[start:i])
    node = TreeNode(value)

    # --- Parse left child ---
    if i < len(s) and s[i] == '(':
        i += 1 # Skip '('
        node.left, i = parse_helper(s, i)
        # After parsing the left subtree, we must be at the closing ')'
        if i < len(s) and s[i] == ')':
            i += 1 # Skip ')'
        else:
            # This would indicate a malformed string if parse_helper returned
            # without reaching the expected ')'
            # For simplicity, assume valid input format.
            pass


    # --- Parse right child ---
    # Note: Right child only exists if a left child was specified (even if empty)
    # The problem statement implies left comes first. If there's a second '(', it's the right child.
    if i < len(s) and s[i] == '(':
        i += 1 # Skip '('
        node.right, i = parse_helper(s, i)
        # After parsing the right subtree, we must be at the closing ')'
        if i < len(s) and s[i] == ')':
            i += 1 # Skip ')'
        else:
            # Malformed string indication
            pass

    return node, i


def level_order_traversal(root: TreeNode | None) -> list[int]:
    """
    Performs a level-order (BFS) traversal of the binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of node values in level order.
    """
    if not root:
        return []

    result = []
    queue = collections.deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result

def str2tree_and_traverse(s: str) -> list[int]:
    """
    Constructs a binary tree from the string representation and returns
    its level-order traversal.

    Args:
        s: The string representation of the binary tree.

    Returns:
        A list of node values from the level-order traversal.
    """
    if not s:
        return []

    # Start parsing from the beginning of the string
    root, _ = parse_helper(s, 0)

    # Perform level-order traversal on the constructed tree
    return level_order_traversal(root)


# --- Test Framework ---
def run_tests():
    """
    Runs predefined test cases against the str2tree_and_traverse function.
    """
    test_cases = [
        ("4(2(3)(1))(6(5))", [4, 2, 6, 3, 1, 5]),
        ("4(2(3)(1))(6(5)(7))", [4, 2, 6, 3, 1, 5, 7]),
        ("-4(2(3)(1))(6(5)(7))", [-4, 2, 6, 3, 1, 5, 7]),
        ("1", [1]),
        ("1(2)", [1, 2]),
        ("1()(3)", [1, 3]), # Test case with empty left child parenthesis
        ("1(2(4)(5))(3)", [1, 2, 3, 4, 5]),
        ("", []), # Test empty string
        ("-100(-200)(-300)", [-100, -200, -300]), # Test negative numbers
        ("5(3(1)(2))(8(6)(9))", [5, 3, 8, 1, 2, 6, 9]), # Another standard case
        ("0", [0]), # Test zero value
        ("10(20)", [10, 20]), # Test multi-digit numbers
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_s, expected_output) in enumerate(test_cases):
        try:
            actual_output = str2tree_and_traverse(input_s)
            passed = actual_output == expected_output
            print(f"{passed}")
            if passed:
                correct_count += 1
            # Optional: Print details on failure
            # else:
            #     print(f"Test {i+1} Failed:")
            #     print(f"  Input: '{input_s}'")
            #     print(f"  Expected: {expected_output}")
            #     print(f"  Actual:   {actual_output}")
        except Exception as e:
            print(f"False") # Indicate failure due to exception
            # print(f"Test {i+1} Failed with exception:")
            # print(f"  Input: '{input_s}'")
            # print(f"  Exception: {e}")


    print(f"\n{correct_count}/{total_tests}")

# --- Main execution ---
if __name__ == "__main__":
    run_tests()