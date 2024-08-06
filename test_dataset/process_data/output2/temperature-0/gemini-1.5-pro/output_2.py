# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
test_cases = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
]

solution = Solution()
for i, (l1, l2, expected) in enumerate(test_cases):
    l1 = ListNode(l1[0])
    curr = l1
    for val in l1[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    l2 = ListNode(l2[0])
    curr = l2
    for val in l2[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    result = solution.addTwoNumbers(l1, l2)
    result_list = print_linked_list(result)
    print(f'Test Case {i+1}: {result_list == expected}')