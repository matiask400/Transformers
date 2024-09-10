def swapPairs(head):
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while head and head.next:
        nxt = head.next
        head.next = nxt.next
        nxt.next = head
        prev.next = nxt
        prev = head
        head = head.next
    return dummy.next