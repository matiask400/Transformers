# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
test_cases = [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0])
]

solution = Solution()

for i, (l1_list, l2_list, expected_output) in enumerate(test_cases):
    # Create linked lists from input lists
    l1 = ListNode(0)
    current = l1
    for val in l1_list:
        current.next = ListNode(val)
        current = current.next
    l1 = l1.next

    l2 = ListNode(0)
    current = l2
    for val in l2_list:
        current.next = ListNode(val)
        current = current.next
    l2 = l2.next

    # Run the solution and compare the output
    merged_list = solution.mergeTwoLists(l1, l2)
    output = print_linked_list(merged_list)
    is_correct = output == expected_output
    print(f"Test case {i+1}: {is_correct}")