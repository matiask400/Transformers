import heapq
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(nodes_list):
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes_list:
        return None

    nodes = [(TreeNode(val) if val is not None else None) for val in nodes_list]
    root = nodes[0]
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if node: # Only process if the parent node is not None
            if i < len(nodes) and nodes[i] is not None:
                node.left = nodes[i]
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = nodes[i]
                queue.append(node.right)
            i += 1
    return root

class Solution:
    """
    Solves the K Closest Values in BST problem.
    """

    # Approach 1: In-order traversal + Heap (O(N log K))
    # This approach works for any binary tree, not just BSTs,
    # but doesn't leverage the BST property optimally for the follow-up.
    def closestKValues_heap(self, root: TreeNode, target: float, k: int) -> list[int]:
        """
        Finds the k closest values using in-order traversal and a max-heap.
        Time: O(N log K), where N is the number of nodes.
        Space: O(K + H), where H is the height of the tree (for recursion stack).
        """
        heap = [] # Max-heap storing tuples: (-difference, value)

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            diff = abs(node.val - target)
            # Push onto heap (using negative diff for max-heap behavior with min-heap)
            heapq.heappush(heap, (-diff, node.val))

            # If heap size exceeds k, remove the element with the largest difference
            if len(heap) > k:
                heapq.heappop(heap)

            inorder(node.right)

        inorder(root)

        # Extract values from the heap
        return [val for diff, val in heap]

    # Approach 2: In-order traversal + Sliding Window (O(N))
    # Leverages BST property (in-order gives sorted) but still O(N) time/space.
    def closestKValues_sliding_window(self, root: TreeNode, target: float, k: int) -> list[int]:
        """
        Finds the k closest values using in-order traversal and a sliding window.
        Time: O(N)
        Space: O(N)
        """
        sorted_vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)

        inorder(root)

        n = len(sorted_vals)
        if k >= n:
            return sorted_vals

        # Find the element closest to target to start the window search
        # This part can be optimized with binary search O(log N), but overall is still O(N)
        # due to traversal. Linear scan is sufficient here.
        min_diff = float('inf')
        closest_idx = -1
        for i in range(n):
            diff = abs(sorted_vals[i] - target)
            if diff < min_diff:
                min_diff = diff
                closest_idx = i
            # Optimization: if diff starts increasing, we found the minimum locally
            # This isn't strictly necessary as the window shrinking handles it.

        # Initialize window pointers
        left = 0
        right = n - 1

        # Shrink window until its size is k
        while right - left + 1 > k:
            if target - sorted_vals[left] > sorted_vals[right] - target:
                # Left element is farther away than the right element
                left += 1
            else:
                # Right element is farther or equally far
                right -= 1

        return sorted_vals[left : right + 1]


    # Approach 3: Optimized In-order Traversal with Deque (O(N))
    # Similar to sliding window but builds the window during traversal.
    def closestKValues_deque(self, root: TreeNode, target: float, k: int) -> list[int]:
        """
        Finds the k closest values using in-order traversal and a deque.
        Time: O(N)
        Space: O(K + H)
        """
        window = collections.deque()

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # Add current node value to the window
            window.append(node.val)

            # If window size exceeds k, remove the element farther from target
            if len(window) > k:
                # Compare the oldest element (window[0]) with the newest (node.val)
                if abs(window[0] - target) > abs(node.val - target):
                    # The oldest element is farther, remove it
                    window.popleft()
                else:
                    # The newest element is farther or equally far.
                    # Since the traversal is in-order, all subsequent elements
                    # will be even farther than the current node.val.
                    # Thus, the current window (excluding the last added element)
                    # holds the k closest. We remove the last added element
                    # and can potentially stop further traversal in this branch,
                    # but simply removing and continuing is easier to implement.
                    window.pop() # Remove the last added element (node.val)
                    # We can return here if we are sure no closer elements exist
                    # in the right subtree, but the logic is complex.
                    # Let's just let the traversal continue, the window maintains correctness.
                    # However, a slight optimization: if window[0] is closer,
                    # it means node.val is farther. Since nodes to the right are even larger,
                    # they will also be farther than window[0]. So we don't need to explore
                    # the right subtree of the *current* node if this condition holds.
                    # This optimization is tricky to implement correctly within recursive inorder.
                    # The simpler approach is just to let inorder finish.

            inorder(node.right)

        inorder(root)
        return list(window)


    # Approach 4: Follow-up O(log N + K) for balanced BST
    # Uses two stacks to simulate in-order and reverse in-order traversal
    # starting from the node closest to the target.
    def closestKValues(self, root: TreeNode, target: float, k: int) -> list[int]:
        """
        Finds the k closest values in O(log N + K) time for a balanced BST.
        Time: O(log N + K)
        Space: O(log N + K)
        """
        if not root:
            return []

        # Stacks to store predecessors and successors
        pred_stack = []
        succ_stack = []

        # Initialize stacks by finding the path to the target value
        curr = root
        while curr:
            if curr.val <= target:
                pred_stack.append(curr)
                curr = curr.right
            else:
                succ_stack.append(curr)
                curr = curr.left

        # Helper function to get the next predecessor
        def get_predecessor():
            if not pred_stack:
                return None
            node = pred_stack.pop()
            val = node.val
            # Move to the rightmost node in the left subtree
            curr = node.left
            while curr:
                pred_stack.append(curr)
                curr = curr.right
            return val

        # Helper function to get the next successor
        def get_successor():
            if not succ_stack:
                return None
            node = succ_stack.pop()
            val = node.val
            # Move to the leftmost node in the right subtree
            curr = node.right
            while curr:
                succ_stack.append(curr)
                curr = curr.left
            return val

        result = []
        # Get initial predecessor and successor candidates
        # Note: The stacks might contain the exact target or nodes surrounding it.
        # The get_predecessor/get_successor functions handle finding the *next* one correctly.
        # We need to call them k times.

        # We need the actual predecessor/successor values to start comparison
        # The top of the stacks *after* the initial traversal might not be
        # the immediate pred/succ if the path didn't end exactly there.
        # Let's refine the initialization or the get functions.

        # Alternative stack initialization: Push all nodes on path
        pred_stack = []
        succ_stack = []
        curr = root
        while curr:
            if curr.val == target:
                pred_stack.append(curr)
                succ_stack.append(curr)
                break
            elif curr.val < target:
                pred_stack.append(curr)
                curr = curr.right
            else: # curr.val > target
                succ_stack.append(curr)
                curr = curr.left

        # Now pred_stack's top is the largest node <= target on the path
        # succ_stack's top is the smallest node > target on the path

        # Refined get_predecessor
        def get_next_smaller():
            if not pred_stack: return None
            node = pred_stack.pop()
            val = node.val
            p = node.left
            while p:
                pred_stack.append(p)
                p = p.right
            return val

        # Refined get_successor
        def get_next_larger():
            if not succ_stack: return None
            node = succ_stack.pop()
            val = node.val
            s = node.right
            while s:
                succ_stack.append(s)
                s = s.left
            return val

        # Handle the case where target itself is in the tree and is closest
        # If target exists, both stacks might point to it initially.
        # We need to get the actual predecessor and successor *values*.
        # Let's simplify: Use the get functions repeatedly.

        # Get initial values using the helper functions
        # Need to handle potential None returns if one side is exhausted early.
        next_smaller = get_next_smaller() # Gets the floor(target) or smaller
        next_larger = get_next_larger()   # Gets the ceil(target) or larger

        # If target was found, one of the calls above returned target.
        # We need to call the *other* function again to get the next distinct value.
        if next_smaller is not None and next_larger is not None and next_smaller == next_larger:
             # This happens if target is in the tree. next_smaller is target.
             # We need the actual next larger value.
             next_larger = get_next_larger()


        result = []
        for _ in range(k):
            if next_smaller is None and next_larger is None:
                break # Should not happen if k <= n

            if next_smaller is None:
                result.append(next_larger)
                next_larger = get_next_larger()
            elif next_larger is None:
                result.append(next_smaller)
                next_smaller = get_next_smaller()
            else:
                # Compare distances
                diff_smaller = target - next_smaller # Always non-negative
                diff_larger = next_larger - target   # Always non-negative

                if diff_smaller < diff_larger:
                    result.append(next_smaller)
                    next_smaller = get_next_smaller()
                else: # diff_larger <= diff_smaller (includes equality)
                    result.append(next_larger)
                    next_larger = get_next_larger()

        return result


# --- Test Framework ---

def run_tests():
    """Runs the test cases."""
    solver = Solution()
    # Using the O(log N + K) approach as the primary one for testing
    # Change solver.closestKValues to solver.closestKValues_heap etc. to test others
    solution_func = solver.closestKValues

    test_cases = [
        # Input: (tree_list, target, k), Expected Output: list_of_values
        ([4, 2, 5, 1, 3], 3.714286, 2, [4, 3]),
        ([1], 0.000000, 1, [1]),
        ([5, 3, 7, 2, 4, 6, 8], 3.5, 3, [3, 4, 2]), # Note: |2-3.5|=1.5, |3-3.5|=0.5, |4-3.5|=0.5. Closest are 3, 4. Next is 2.
        ([5, 3, 7, 2, 4, 6, 8], 6.1, 4, [6, 7, 5, 8]), # |6-6.1|=0.1, |7-6.1|=0.9, |5-6.1|=1.1, |8-6.1|=1.9, |4-6.1|=2.1
        ([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8], 7.2, 3, [7, 6, 8]), # |7-7.2|=0.2, |6-7.2|=1.2, |8-7.2|=0.8. Closest: 7, 8, 6
        ([100, 50, 150, 25, 75, 125, 175], 110.0, 5, [100, 125, 75, 150, 50]), # |100-110|=10, |125-110|=15, |75-110|=35, |150-110|=40, |50-110|=60. Order: 100, 125, 75, 150, 50
        ([2, 1, 3], 5.5, 2, [3, 2]), # |3-5.5|=2.5, |2-5.5|=3.5, |1-5.5|=4.5
        ([0], 0.0, 1, [0]),
        ([3,1,4,None,2], 2.0, 1, [2]), # Tree: 3 / \ 1 4 \ 2
    ]

    correct_count = 0
    total_tests = len(test_cases)

    for i, (tree_list, target, k, expected_raw) in enumerate(test_cases):
        root = build_tree_from_list(tree_list)
        result_raw = solution_func(root, target, k)

        # Sort both lists for comparison as order doesn't matter
        result_sorted = sorted(result_raw)
        expected_sorted = sorted(expected_raw)

        passed = (result_sorted == expected_sorted)
        print(f"Test Case {i + 1}: {passed}")
        # Optional: Print details on failure
        # if not passed:
        #     print(f"  Input Tree: {tree_list}")
        #     print(f"  Target: {target}, k: {k}")
        #     print(f"  Expected: {expected_sorted}")
        #     print(f"  Got: {result_sorted}")

        if passed:
            correct_count += 1

    print(f"\nResult: {correct_count} / {total_tests} tests passed.")

# Execute the tests
if __name__ == "__main__":
    run_tests()