class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

# Example 1
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
output_1 = addTwoNumbers(l1, l2)
print(output_1 == ListNode(7, ListNode(0, ListNode(8))))  # True

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)
output_2 = addTwoNumbers(l1, l2)
print(output_2 == ListNode(0))  # True

# Example 3
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
output_3 = addTwoNumbers(l1, l2)
print(output_3 == ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))))))  # True