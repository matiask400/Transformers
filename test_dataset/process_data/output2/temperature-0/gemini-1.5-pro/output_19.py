# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # Delete the node
        left.next = left.next.next

        return dummy.next

def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    return values

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
]

solution = Solution()

for i, (head_values, n, expected_output) in enumerate(test_cases):
    # Create the linked list from the input values
    head = ListNode(head_values[0])
    current = head
    for val in head_values[1:]:
        current.next = ListNode(val)
        current = current.next

    result_head = solution.removeNthFromEnd(head, n)
    result = print_linked_list(result_head)
    print(f"Test case {i+1}: {result == expected_output}")