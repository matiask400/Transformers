class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Converts a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

        Args:
            root: The root of the binary search tree.

        Returns:
            The pointer to the smallest element of the linked list.
        """
        if not root:
            return None

        self.first = None
        self.last = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node

            self.last = node

            inorder(node.right)

        inorder(root)

        self.last.right = self.first
        self.first.left = self.last

        return self.first

def test_cases():
    def create_bst(arr):
        if not arr:
            return None
        root = Node(arr[0])
        for val in arr[1:]:
            node = root
            while True:
                if val < node.val:
                    if node.left is None:
                        node.left = Node(val)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(val)
                        break
                    else:
                        node = node.right
        return root
    
    def linked_list_to_array(head):
        if not head:
            return []
        
        arr = []
        curr = head
        seen = set()
        
        while curr and curr not in seen:
            arr.append(curr.val)
            seen.add(curr)
            curr = curr.right
            
        return arr

    test_cases = [
        ([4,2,5,1,3], [1,2,3,4,5]),
        ([2,1,3], [1,2,3]),
        ([], []),
        ([1], [1])
    ]

    solution = Solution()
    correct_count = 0
    total_count = len(test_cases)
    
    for i, (input_arr, expected_arr) in enumerate(test_cases):
        root = create_bst(input_arr)
        result_head = solution.treeToDoublyList(root)
        result_arr = linked_list_to_array(result_head)
        
        if result_arr == expected_arr:
            print(f"Test {i+1}: True")
            correct_count += 1
        else:
            print(f"Test {i+1}: False")
            print(f"  Input: {input_arr}")
            print(f"  Expected: {expected_arr}")
            print(f"  Got: {result_arr}")
            
    print(f"{correct_count}/{total_count}")

if __name__ == "__main__":
    test_cases()