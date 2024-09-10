# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next

def list_to_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Test

# Example 1
l1 = list_to_linked_list([1, 2, 4])
l2 = list_to_linked_list([1, 3, 4])
expected_output1 = [1, 1, 2, 3, 4, 4]

# Example 2
l1 = list_to_linked_list([])
l2 = list_to_linked_list([])
expected_output2 = []

# Example 3
l1 = list_to_linked_list([])
l2 = list_to_linked_list([0])
expected_output3 = [0]

solution = Solution()
output1 = linked_list_to_list(solution.mergeTwoLists(l1, l2))
output2 = linked_list_to_list(solution.mergeTwoLists(l1, l2))
output3 = linked_list_to_list(solution.mergeTwoLists(l1, l2))

print(output1 == expected_output1, output2 == expected_output2, output3 == expected_output3)