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
