def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(n + 1):
        first = first.next
    while first is not None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

# Test the solution with example inputs
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5)))
print(removeNthFromEnd(head1, 2) == output1)

head2 = ListNode(1)
output2 = None
print(removeNthFromEnd(head2, 1) == output2)

head3 = ListNode(1, ListNode(2))
output3 = ListNode(1)
print(removeNthFromEnd(head3, 1) == output3)