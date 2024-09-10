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
        next_node = current.next
        current.next = next_node.next
        next_node.next = current
        if prev:
            prev.next = next_node
        prev = current
        current = current.next
    return new_head

# Example usage
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head2 = None
head3 = ListNode(1)

result1 = swapPairs(head1)

# Convert ListNode to list for easier comparison
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

output1 = to_list(result1)
output2 = to_list(swapPairs(head2))
output3 = to_list(swapPairs(head3))

print(output1 == [2, 1, 4, 3])
print(output2 == [])
print(output3 == [1])