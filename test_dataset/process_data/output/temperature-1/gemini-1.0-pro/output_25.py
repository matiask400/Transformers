class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if not head or k == 1:
        return head

    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr:
        group_prev = prev
        group_next = None
        count = 0

        while curr and count < k:
            group_next = curr.next
            curr.next = prev
            prev = curr
            curr = group_next
            count += 1

        if count == k:
            group_prev.next = prev
            prev = group_next

    return dummy.next     