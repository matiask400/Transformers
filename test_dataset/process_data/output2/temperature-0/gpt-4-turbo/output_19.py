class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

def list_to_array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array

# Test cases
inputs = [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
    (ListNode(1), 1),
    (ListNode(1, ListNode(2)), 1)
]
outputs = [
    [1,2,3,5],
    [],
    [1]
]

for inp, expected in zip(inputs, outputs):
    result = list_to_array(removeNthFromEnd(inp[0], inp[1]))
    print(result == expected)