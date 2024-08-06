# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next

def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Test cases
inputs = [([1,2,4], [1,3,4]), ([], []), ([], [0])]
outputs = [[1,1,2,3,4,4], [], [0]]

# Run tests
for i in range(len(inputs)):
    l1 = list_to_linked_list(inputs[i][0])
    l2 = list_to_linked_list(inputs[i][1])
    result = Solution().mergeTwoLists(l1, l2)
    output = linked_list_to_list(result)
    print(output == outputs[i])