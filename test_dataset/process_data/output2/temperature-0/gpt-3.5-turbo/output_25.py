def reverseKGroup(head, k):
    def reverseLinkedList(head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    while True:
        start = prev_group_end.next
        end = prev_group_end
        for _ in range(k):
            end = end.next
            if not end:
                return dummy.next
        next_group_start = end.next
        end.next = None
        prev_group_end.next = reverseLinkedList(start)
        start.next = next_group_start
        prev_group_end = start
    return dummy.next

# Test Cases
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output1 = reverseKGroup(head1, 2)
print(output1 == ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5))))))

head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output2 = reverseKGroup(head2, 3)
print(output2 == ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))))

head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output3 = reverseKGroup(head3, 1)
print(output3 == ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))