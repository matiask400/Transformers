import heapq
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_bst(nums):
    """Helper function to build a BST from a list (level-order)."""
    if not nums:
        return None
    
    nodes = [(TreeNode(val) if val is not None else None) for val in nums]
    kids = collections.deque(nodes[1:])
    root = nodes[0]
    q = collections.deque([root])

    while q:
        parent = q.popleft()
        if parent is None:
            continue
            
        if kids:
            left_child = kids.popleft()
            if left_child:
                parent.left = left_child
                q.append(left_child)
        if kids:
            right_child = kids.popleft()
            if right_child:
                parent.right = right_child
                q.append(right_child)
                
    return root

# --------------------------------------------------------------------------
# Solution implementation
# --------------------------------------------------------------------------

def closestKValues(root: TreeNode, target: float, k: int) -> list[int]:
    """
    Finds the k values in the BST closest to the target.

    Args:
        root: The root of the Binary Search Tree.
        target: The target value.
        k: The number of closest values to find.

    Returns:
        A list containing the k closest values.
    """
    
    # Approach: Use a max-heap to keep track of the k closest elements found so far.
    # The heap stores tuples of (-difference, value). We use negative difference
    # because heapq implements a min-heap, and we want to easily pop the element
    # with the largest difference (i.e., the farthest among the current k closest).

    max_heap = [] # Stores (-abs(node.val - target), node.val)

    def dfs(node):
        if not node:
            return

        diff = abs(node.val - target)

        if len(max_heap) < k:
            # If heap has less than k elements, just add the current node
            heapq.heappush(max_heap, (-diff, node.val))
        else:
            # If heap is full, compare current node's difference with the largest 
            # difference currently in the heap (which is at the root, index 0).
            # The stored value is -largest_diff, so we compare diff < -max_heap[0][0].
            if diff < -max_heap[0][0]:
                # Current node is closer than the farthest node in the heap.
                # Replace the farthest node with the current node.
                # heapreplace pops the smallest item (-largest_diff) and pushes the new item.
                heapq.heapreplace(max_heap, (-diff, node.val))
        
        # Recursively traverse the tree
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    
    # Extract the values from the heap
    result = [val for diff, val in max_heap]
    return result

# --------------------------------------------------------------------------
# Follow-up Solution (O(log n + k) for balanced BST)
# --------------------------------------------------------------------------
def closestKValues_optimized(root: TreeNode, target: float, k: int) -> list[int]:
    """
    Optimized solution using two stacks (simulating inorder iterators).
    Achieves O(h + k) time complexity, which is O(log n + k) for balanced BST.
    Space complexity is O(h).
    """
    if not root:
        return []

    pred_stack = []
    succ_stack = []
    
    # Initialize stacks: traverse towards target
    curr = root
    while curr:
        if curr.val <= target:
            pred_stack.append(curr)
            curr = curr.right
        else:
            succ_stack.append(curr)
            curr = curr.left

    def get_predecessor(stack):
        if not stack: return None
        node = stack.pop()
        val = node.val
        # Go left once, then right as far as possible to find next predecessor's path
        curr = node.left
        while curr:
            stack.append(curr)
            curr = curr.right
        return val

    def get_successor(stack):
        if not stack: return None
        node = stack.pop()
        val = node.val
        # Go right once, then left as far as possible to find next successor's path
        curr = node.right
        while curr:
            stack.append(curr)
            curr = curr.left
        return val
    
    result = []
    for _ in range(k):
        pred_val = pred_stack[-1].val if pred_stack else float('-inf')
        succ_val = succ_stack[-1].val if succ_stack else float('inf')

        if target - pred_val <= succ_val - target: # Predecessor is closer or equally close (or successor doesn't exist)
            if pred_val == float('-inf'): break # No more predecessors
            result.append(get_predecessor(pred_stack))
        else: # Successor is closer (or predecessor doesn't exist)
             if succ_val == float('inf'): break # No more successors
             result.append(get_successor(succ_stack))
             
    return result


# --------------------------------------------------------------------------
# Test framework
# --------------------------------------------------------------------------
def run_tests():
    test_cases = [
        # Example 1
        ([4, 2, 5, 1, 3], 3.714286, 2, [3, 4]), # Note: output order doesn't matter, testing checks sorted lists
        # Example 2
        ([1], 0.000000, 1, [1]),
        # Additional test cases
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3.1, 3, [3, 4, 2]),
        ([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8], 7.5, 4, [7, 8, 6, 10]),
        ([100], 50.0, 1, [100]),
        ([50, 30, 70, 20, 40, 60, 80], 68.0, 3, [70, 60, 80]),
        ([50, 30, 70, 20, 40, 60, 80], 32.0, 3, [30, 40, 20]),
        ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13], 9.0, 5, [8, 10, 7, 6, 13]), # Requires careful diff comparison
        ([], 5.0, 3, []), # Empty tree
        ([2,1,3], 5.5, 2, [3,2]), # Target outside range
        ([2,1], 0.0, 1, [1]), # Target less than min
    ]

    correct_count = 0
    print("Running tests with standard heap approach (O(n log k)):")
    for i, (tree_list, target, k, expected) in enumerate(test_cases):
        root = list_to_bst(tree_list)
        # Use the standard heap-based solution for the main testing
        result = closestKValues(root, target, k)
        # Sort both lists for comparison as order doesn't matter
        passed = sorted(result) == sorted(expected)
        print(f"Test {i+1}: {passed}")
        if passed:
            correct_count += 1
            
    print("\nRunning tests with optimized stack approach (O(h + k)):")
    correct_count_optimized = 0
    for i, (tree_list, target, k, expected) in enumerate(test_cases):
        root = list_to_bst(tree_list)
        # Use the optimized stack-based solution
        result_optimized = closestKValues_optimized(root, target, k)
        # Sort both lists for comparison
        passed_optimized = sorted(result_optimized) == sorted(expected)
        print(f"Test {i+1} (Optimized): {passed_optimized}")
        if passed_optimized:
             correct_count_optimized += 1

    print(f"\nStandard Heap Approach Results: {correct_count}/{len(test_cases)} tests passed.")
    print(f"Optimized Stack Approach Results: {correct_count_optimized}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()