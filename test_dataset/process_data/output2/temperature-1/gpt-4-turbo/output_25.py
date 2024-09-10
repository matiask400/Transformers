class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if head is None or k == 1:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur, prev, next = head, dummy, None
    count = 0
    while cur:
        cur = cur.next
        count += 1
    while count >= k:
        cur = prev.next
        next = cur.next
        for i in range(1, k):
            cur.next = next.next
            next.next = prev.next
            prev.next = next
            next = cur.next
        prev = cur
        count -= k
    return dummy.next

# testing expected outputs
example_1 = [1, 2, 3, 4, 5]
k_1 = 2
expected_1 = [2, 1, 4, 3, 5]
example_2 = [1, 2, 3, 4, 5]
k_2 = 3
expected_2 = [3, 2, 1, 4, 5]
example_3 = [1, 2, 3, 4, 5]
k_3 = 1
expected_3 = [1, 2, 3, 4, 5]

print(reverseKGroup(example_1, k_1) == expected_1)
print(reverseKGroup(example_2, k_2) == expected_2)
print(reverseKGroup(example_3, k_3) == expected_3)