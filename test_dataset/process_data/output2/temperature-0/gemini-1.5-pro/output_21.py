# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_solution():
    solution = Solution()

    # Test case 1
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = solution.mergeTwoLists(l1, l2)
    print(print_linked_list(merged_list) == [1, 1, 2, 3, 4, 4])  # Expected output: True

    # Test case 2
    l1 = None
    l2 = None
    merged_list = solution.mergeTwoLists(l1, l2)
    print(print_linked_list(merged_list) == [])  # Expected output: True

    # Test case 3
    l1 = None
    l2 = ListNode(0)
    merged_list = solution.mergeTwoLists(l1, l2)
    print(print_linked_list(merged_list) == [0])  # Expected output: True

test_solution()