class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next

# Testing:
def list_to_linkedlist(elements):
    dummy = ListNode()
    current = dummy
    for el in elements:
        current.next = ListNode(el)
        current = current.next
    return dummy.next

l1 = list_to_linkedlist([1, 2, 4])
l2 = list_to_linkedlist([1, 3, 4])
sol = Solution()
output1 = sol.mergeTwoLists(l1, l2)
expected1 = list_to_linkedlist([1, 1, 2, 3, 4, 4])

result1 = output1
while result1:
    if expected1:
        if result1.val != expected1.val:
            print(False)
            break
        expected1 = expected1.next
    result1 = result1.next
else:
    print(True)

l1 = list_to_linkedlist([])
l2 = list_to_linkedlist([])
output2 = sol.mergeTwoLists(l1, l2)
expected2 = list_to_linkedlist([])

result2 = output2
while result2:
    if expected2:
        if result2.val != expected2.val:
            print(False)
            break
        expected2 = expected2.next
    result2 = result2.next
else:
    print(True)

l1 = list_to_linkedlist([])
l2 = list_to_linkedlist([0])
output3 = sol.mergeTwoLists(l1, l2)
expected3 = list_to_linkedlist([0])

result3 = output3
while result3:
    if expected3:
        if result3.val != expected3.val:
            print(False)
            break
        expected3 = expected3.next
    result3 = result3.next
else:
    print(True)