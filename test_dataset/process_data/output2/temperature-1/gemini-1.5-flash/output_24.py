class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next

# Example 1
head_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
output_1 = swapPairs(head_1)
print(output_1.val, output_1.next.val, output_1.next.next.val, output_1.next.next.next.val)  # Output: 2 1 4 3
print(output_1.val == 2 and output_1.next.val == 1 and output_1.next.next.val == 4 and output_1.next.next.next.val == 3)  # Output: True

# Example 2
head_2 = None
output_2 = swapPairs(head_2)
print(output_2)  # Output: None
print(output_2 is None)  # Output: True

# Example 3
head_3 = ListNode(1)
output_3 = swapPairs(head_3)
print(output_3.val)  # Output: 1
print(output_3.val == 1)  # Output: True