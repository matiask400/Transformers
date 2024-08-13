class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(out)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example 1
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])
expected_output = [7, 0, 8]
solution = Solution()
output = linkedlist_to_list(solution.addTwoNumbers(l1, l2))
print(output == expected_output)

# Example 2
l1 = list_to_linkedlist([0])
l2 = list_to_linkedlist([0])
expected_output = [0]
output = linkedlist_to_list(solution.addTwoNumbers(l1, l2))
print(output == expected_output)

# Example 3
l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linkedlist([9, 9, 9, 9])
expected_output = [8, 9, 9, 9, 0, 0, 0, 1]
output = linkedlist_to_list(solution.addTwoNumbers(l1, l2))
print(output == expected_output)