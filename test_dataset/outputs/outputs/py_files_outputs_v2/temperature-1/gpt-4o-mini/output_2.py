class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    p, q, current = l1, l2, dummy_head
    carry = 0

    while p is not None or q is not None:
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0
        total = carry + x + y
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

# Test examples
l1_1 = ListNode(2, ListNode(4, ListNode(3)))
l2_1 = ListNode(5, ListNode(6, ListNode(4)))
result_1 = addTwoNumbers(l1_1, l2_1)
print(result_1.val, end=' ')
while result_1:
    print(result_1.val, end=' ')
    result_1 = result_1.next
print('\nExpected: [7,0,8]')

l1_2 = ListNode(0)
l2_2 = ListNode(0)
result_2 = addTwoNumbers(l1_2, l2_2)
print(result_2.val, end=' ')
while result_2:
    print(result_2.val, end=' ')
    result_2 = result_2.next
print('\nExpected: [0]')

l1_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result_3 = addTwoNumbers(l1_3, l2_3)
print(result_3.val, end=' ')
while result_3:
    print(result_3.val, end=' ')
    result_3 = result_3.next
print('\nExpected: [8,9,9,9,0,0,0,1]')