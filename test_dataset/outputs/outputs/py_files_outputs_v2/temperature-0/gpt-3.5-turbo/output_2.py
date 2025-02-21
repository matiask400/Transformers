def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        carry, val = divmod(sum_val, 10)
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test the solution with example inputs
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