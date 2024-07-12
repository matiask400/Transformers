class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
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
result1 = addTwoNumbers(l1, l2)

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)
result2 = addTwoNumbers(l1, l2)

# Example 3
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result3 = addTwoNumbers(l1, l2)

# Check if the results match the expected outputs
output1 = [7, 0, 8]
output2 = [0]
output3 = [8, 9, 9, 9, 0, 0, 0, 1]

print(f"Example 1: {result1 == output1}")
print(f"Example 2: {result2 == output2}")
print(f"Example 3: {result3 == output3}")