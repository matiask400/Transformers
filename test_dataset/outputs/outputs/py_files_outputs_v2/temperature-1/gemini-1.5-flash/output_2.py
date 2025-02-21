class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        sum = x + y + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# Example 1
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
output_1 = addTwoNumbers(l1, l2)
print(f'Example 1: Output: {output_1.val} -> {output_1.next.val} -> {output_1.next.next.val} (True if matches expected output)')
print(f'Expected: {7} -> {0} -> {8}')
print(f'Output matches expected: {output_1.val == 7 and output_1.next.val == 0 and output_1.next.next.val == 8}

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)
output_2 = addTwoNumbers(l1, l2)
print(f'Example 2: Output: {output_2.val} (True if matches expected output)')
print(f'Expected: {0}')
print(f'Output matches expected: {output_2.val == 0}

# Example 3
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
output_3 = addTwoNumbers(l1, l2)
print(f'Example 3: Output: {output_3.val} -> {output_3.next.val} -> {output_3.next.next.val} -> {output_3.next.next.next.val} -> {output_3.next.next.next.next.val} -> {output_3.next.next.next.next.next.val} -> {output_3.next.next.next.next.next.next.val} -> {output_3.next.next.next.next.next.next.next.val} (True if matches expected output)')
print(f'Expected: {8} -> {9} -> {9} -> {9} -> {0} -> {0} -> {0} -> {1}')
print(f'Output matches expected: {output_3.val == 8 and output_3.next.val == 9 and output_3.next.next.val == 9 and output_3.next.next.next.val == 9 and output_3.next.next.next.next.val == 0 and output_3.next.next.next.next.next.val == 0 and output_3.next.next.next.next.next.next.val == 0 and output_3.next.next.next.next.next.next.next.val == 1}')