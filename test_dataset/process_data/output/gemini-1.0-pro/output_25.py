def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head
    next = None
    count = 0
    while curr:
        count += 1
        next = curr.next
        if count == k:
            prev = reverse(prev, curr.next)
            curr = next
            count = 0
    return dummy.next
def reverse(prev, next):
    last = prev.next
    curr = last.next
    while curr != next:
        last.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = last.next
    return last