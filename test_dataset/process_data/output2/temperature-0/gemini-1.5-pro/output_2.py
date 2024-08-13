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

def create_linked_list(nums):
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head

def compare_linked_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

# Example test cases
input_1 = create_linked_list([2, 4, 3])
input_2 = create_linked_list([5, 6, 4])
expected_output_1 = create_linked_list([7, 0, 8])
print(compare_linked_lists(Solution().addTwoNumbers(input_1, input_2), expected_output_1))  # True

input_3 = create_linked_list([0])
input_4 = create_linked_list([0])
expected_output_2 = create_linked_list([0])
print(compare_linked_lists(Solution().addTwoNumbers(input_3, input_4), expected_output_2))  # True

input_5 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
input_6 = create_linked_list([9, 9, 9, 9])
expected_output_3 = create_linked_list([8, 9, 9, 9, 0, 0, 0, 1])
print(compare_linked_lists(Solution().addTwoNumbers(input_5, input_6), expected_output_3))  # True