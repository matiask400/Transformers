class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + carry
        carry = sum // 10

        curr.next = ListNode(sum % 10)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# Example 1
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
output1 = addTwoNumbers(l1, l2)

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)
output2 = addTwoNumbers(l1, l2)

# Example 3
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
output3 = addTwoNumbers(l1, l2)

# Check if the output is correct
print(f"Output 1: {output1.val} -> {output1.next.val} -> {output1.next.next.val}")
print(f"Output 2: {output2.val}")
print(f"Output 3: {output3.val} -> {output3.next.val} -> {output3.next.next.val} -> {output3.next.next.next.val} -> {output3.next.next.next.next.val} -> {output3.next.next.next.next.next.val} -> {output3.next.next.next.next.next.next.val} -> {output3.next.next.next.next.next.next.next.val}")