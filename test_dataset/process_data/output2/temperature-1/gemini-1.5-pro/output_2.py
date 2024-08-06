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

def test_solution(l1_vals, l2_vals, expected_output):
    l1 = ListNode(0)
    curr = l1
    for val in l1_vals:
        curr.next = ListNode(val)
        curr = curr.next
    l1 = l1.next

    l2 = ListNode(0)
    curr = l2
    for val in l2_vals:
        curr.next = ListNode(val)
        curr = curr.next
    l2 = l2.next

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    output = print_linked_list(result)
    return output == expected_output

# Test cases
input_1 = [2, 4, 3]
input_2 = [5, 6, 4]
output_1 = [7, 0, 8]
print(f"Input 1: True" if test_solution(input_1, input_2, output_1) else f"Input 1: False")

input_1 = [0]
input_2 = [0]
output_2 = [0]
print(f"Input 2: True" if test_solution(input_1, input_2, output_2) else f"Input 2: False")

input_1 = [9,9,9,9,9,9,9]
input_2 = [9,9,9,9]
output_3 = [8,9,9,9,0,0,0,1]
print(f"Input 3: True" if test_solution(input_1, input_2, output_3) else f"Input 3: False")