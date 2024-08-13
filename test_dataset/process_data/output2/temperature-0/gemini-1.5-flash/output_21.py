class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
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
    if l2:
        tail.next = l2

    return dummy.next

# Example 1
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
output_1 = mergeTwoLists(l1, l2)
print(output_1 == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))))  # True

# Example 2
l1 = None
l2 = None
output_2 = mergeTwoLists(l1, l2)
print(output_2 == None)  # True

# Example 3
l1 = None
l2 = ListNode(0)
output_3 = mergeTwoLists(l1, l2)
print(output_3 == ListNode(0))  # True