class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p, q, current = l1, l2, dummy_head
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum_val = carry + x + y
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
            if p is not None: p = p.next
            if q is not None: q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy_head.next

def create_linked_list(digits):
    head = ListNode(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = ListNode(digit)
        current = current.next
    return head

def get_list_from_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example 1
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
out = solution.addTwoNumbers(l1, l2)
print(get_list_from_linked_list(out) == [7, 0, 8])  # Should output True

# Example 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
out = solution.addTwoNumbers(l1, l2)
print(get_list_from_linked_list(out) == [0])  # Should output True

# Example 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
out = solution.addTwoNumbers(l1, l2)
print(get_list_from_linked_list(out) == [8, 9, 9, 9, 0, 0, 0, 1])  # Should output True
