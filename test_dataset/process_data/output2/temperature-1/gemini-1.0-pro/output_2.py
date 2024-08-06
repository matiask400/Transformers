class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = addTwoNumbers(l1, l2)
print(result.val == 7 and result.next.val == 0 and result.next.next.val == 8)

l1 = ListNode(0)
l2 = ListNode(0)
result = addTwoNumbers(l1, l2)
print(result.val == 0)

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
result = addTwoNumbers(l1, l2)
print(result.val == 8 and result.next.val == 9 and result.next.next.val == 9 and result.next.next.next.val == 9 and result.next.next.next.next.val == 0 and result.next.next.next.next.next.val == 0 and result.next.next.next.next.next.next.val == 0 and result.next.next.next.next.next.next.next.val == 1)