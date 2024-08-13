class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    current = head
    while current and current.next:
        next_pair = current.next.next
        second = current.next
        second.next = current
        current.next = next_pair
        if prev:
            prev.next = second
        prev = current
        current = next_pair
    return new_head

# Test cases
inputs = [
    [1, 2, 3, 4],
    [],
    [1]
]
outputs = [
    [2, 1, 4, 3],
    [],
    [1]
]

for i in range(len(inputs)):
    head = ListNode(inputs[i][0]) if inputs[i] else None
    current = head
    for value in inputs[i][1:]:
        current.next = ListNode(value)
        current = current.next
    result = swapPairs(head)
    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    print(result_list == outputs[i])