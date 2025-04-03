import collections

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a BST from a list (level-order traversal with None for missing nodes)
def build_bst(arr):
    if not arr:
        return None
    
    root = Node(arr[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        
        # Process left child
        if i < len(arr) and arr[i] is not None:
            node.left = Node(arr[i])
            queue.append(node.left)
        i += 1
        
        # Process right child
        if i < len(arr) and arr[i] is not None:
            node.right = Node(arr[i])
            queue.append(node.right)
        i += 1
            
    return root

# Helper function to verify the Circular Doubly Linked List
def verify_cdll(head, expected_arr):
    if not head and not expected_arr:
        return True
    if not head or not expected_arr:
        return False
    if head.val != expected_arr[0]:
         print(f"Verification failed: Head value mismatch. Expected {expected_arr[0]}, Got {head.val}")
         return False

    # Forward traversal
    current = head
    result_forward = []
    for _ in range(len(expected_arr) + 1): # Traverse one extra step to check circularity
        if not current:
             print(f"Verification failed: Forward traversal encountered None unexpectedly.")
             return False
        result_forward.append(current.val)
        if len(result_forward) > len(expected_arr): # Should have looped back
            break
        # Check predecessor link during forward traversal
        if current.left:
            expected_prev_val = expected_arr[(expected_arr.index(current.val) - 1 + len(expected_arr)) % len(expected_arr)]
            if current.left.val != expected_prev_val:
                 print(f"Verification failed: Predecessor link incorrect for node {current.val}. Expected {expected_prev_val}, Got {current.left.val}")
                 return False
        elif len(expected_arr) > 1: # Only head's predecessor can be None initially if not circular yet
             print(f"Verification failed: Node {current.val} has None predecessor unexpectedly.")
             return False

        current = current.right

    if result_forward[:-1] != expected_arr:
        print(f"Verification failed: Forward traversal mismatch. Expected {expected_arr}, Got {result_forward[:-1]}")
        return False
    if result_forward[-1] != head.val:
        print(f"Verification failed: Forward circularity check failed. Expected last.right to be head ({head.val}), Got {result_forward[-1]}")
        return False

    # Backward traversal (starting from head's predecessor, which should be the last element)
    if not head.left:
         print(f"Verification failed: Head's predecessor is None.")
         return False
    if head.left.val != expected_arr[-1]:
         print(f"Verification failed: Head's predecessor value mismatch. Expected {expected_arr[-1]}, Got {head.left.val}")
         return False

    current = head.left # Start from the last element
    result_backward = []
    for _ in range(len(expected_arr) + 1):
        if not current:
            print(f"Verification failed: Backward traversal encountered None unexpectedly.")
            return False
        result_backward.append(current.val)
        if len(result_backward) > len(expected_arr):
            break
        # Check successor link during backward traversal
        if current.right:
             expected_next_val = expected_arr[(expected_arr.index(current.val) + 1) % len(expected_arr)]
             if current.right.val != expected_next_val:
                 print(f"Verification failed: Successor link incorrect for node {current.val}. Expected {expected_next_val}, Got {current.right.val}")
                 return False
        elif len(expected_arr) > 1:
             print(f"Verification failed: Node {current.val} has None successor unexpectedly.")
             return False

        current = current.left

    # The backward list should be the reverse of expected, excluding the wrap-around element
    expected_backward = list(reversed(expected_arr))
    if result_backward[:-1] != expected_backward:
        print(f"Verification failed: Backward traversal mismatch. Expected {expected_backward}, Got {result_backward[:-1]}")
        return False
    if result_backward[-1] != head.left.val: # Should loop back to the last element
        print(f"Verification failed: Backward circularity check failed. Expected first.left to be last ({head.left.val}), Got {result_backward[-1]}")
        return False

    return True


class Solution:
    """
    Converts a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
    """
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Performs the in-place conversion.

        Args:
            root: The root node of the Binary Search Tree.

        Returns:
            The head node (smallest element) of the Circular Doubly Linked List,
            or None if the input tree is empty.
        """
        if not root:
            return None

        # Use instance variables to keep track of the first (smallest)
        # and last (most recently visited) nodes during the in-order traversal.
        self.first = None
        self.last = None

        def inorder_connect(node):
            """
            Recursive helper function to perform in-order traversal
            and connect nodes.
            """
            if not node:
                return

            # 1. Recurse on the left subtree
            inorder_connect(node.left)

            # 2. Process the current node
            if self.last:
                # Link the previous node (last) with the current node
                self.last.right = node # last's successor is current node
                node.left = self.last   # current node's predecessor is last
            else:
                # This is the first node visited (the smallest element)
                self.first = node

            # Update the last visited node to be the current node
            self.last = node

            # 3. Recurse on the right subtree
            inorder_connect(node.right)

        # Start the in-order traversal from the root
        inorder_connect(root)

        # After traversal, self.first points to the head (smallest)
        # and self.last points to the tail (largest).
        # Make the list circular by connecting the tail back to the head.
        if self.first and self.last: # Ensure list is not empty
             self.last.right = self.first
             self.first.left = self.last

        return self.first

# --- Test Runner ---

def run_tests():
    solution = Solution()
    test_cases = [
        # Input BST (list format), Expected CDLL (list format)
        ([4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),
        ([2, 1, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([5, 3, 7, 2, 4, 6, 8], [2, 3, 4, 5, 6, 7, 8]),
        ([3, 1, None, None, 2], [1, 2, 3]), # Right leaning
        ([3, None, 5, 4, None], [3, 4, 5]), # Left leaning
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (input_list, expected_list) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Input BST (list): {input_list}")
        print(f"Expected CDLL (list): {expected_list}")

        root = build_bst(input_list)
        
        # It's good practice to visualize the tree structure if needed
        # print_tree(root) # You might want a tree printing function for debugging

        head_cdll = solution.treeToDoublyList(root)

        # Reset solution's state if it uses instance variables for next test
        # (In this implementation, treeToDoublyList resets self.first/last anyway)

        # Verify the result
        passed = verify_cdll(head_cdll, expected_list)
        print(f"Test Passed: {passed}")

        if passed:
            correct_count += 1
        else:
            # Optional: Print the actual list if verification fails
            if head_cdll:
                actual_list = []
                curr = head_cdll
                for _ in range(len(expected_list) + 1): # Limit traversal
                     actual_list.append(curr.val)
                     curr = curr.right
                     if curr == head_cdll:
                         break
                print(f"Actual CDLL (forward): {actual_list}")


    print("\n--- Summary ---")
    print(f"{correct_count} out of {total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()