class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
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

# Example 1: Input
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Example 1: Output
output1 = addTwoNumbers(l1, l2)
print(output1.val == 7 and output1.next.val == 0 and output1.next.next.val == 8)

# Example 2: Input
l1 = ListNode(0)
l2 = ListNode(0)

# Example 2: Output
output2 = addTwoNumbers(l1, l2)
print(output2.val == 0)

# Example 3: Input
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

# Example 3: Output
output3 = addTwoNumbers(l1, l2)
print(output3.val == 8 and output3.next.val == 9 and output3.next.next.val == 9 and output3.next.next.next.val == 9 and output3.next.next.next.next.val == 0 and output3.next.next.next.next.next.val == 0 and output3.next.next.next.next.next.next.val == 0 and output3.next.next.next.next.next.next.next.val == 1)