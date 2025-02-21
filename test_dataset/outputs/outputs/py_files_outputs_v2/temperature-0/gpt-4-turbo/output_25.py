class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if head is None or k == 1:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur, prev, next = dummy, dummy, dummy
    count = 0
    while cur.next:
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

# Test cases
inputs = [([1,2,3,4,5], 2), ([1,2,3,4,5], 3), ([1,2,3,4,5], 1)]
outputs = [[2,1,4,3,5], [3,2,1,4,5], [1,2,3,4,5]]
for (inp, k), out in zip(inputs, outputs):
    head = ListNode(inp[0])
    current = head
    for value in inp[1:]:
        current.next = ListNode(value)
        current = current.next
    result = reverseKGroup(head, k)
    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    print(result_list == out)