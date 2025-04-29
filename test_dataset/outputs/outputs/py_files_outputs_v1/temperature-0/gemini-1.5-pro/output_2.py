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

# Test the solution
l1 = [2,4,3]
l2 = [5,6,4]
output1 = [7,0,8]

l12 = [0]
l22 = [0]
output2 = [0]

l13 = [9,9,9,9,9,9,9]
l23 = [9,9,9,9]
output3 = [8,9,9,9,0,0,0,1]

def list_to_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

solution = Solution()
result1 = solution.addTwoNumbers(list_to_linked_list(l1), list_to_linked_list(l2))
result2 = solution.addTwoNumbers(list_to_linked_list(l12), list_to_linked_list(l22))
result3 = solution.addTwoNumbers(list_to_linked_list(l13), list_to_linked_list(l23))

print(linked_list_to_list(result1) == output1)  # True
print(linked_list_to_list(result2) == output2)  # True
print(linked_list_to_list(result3) == output3)  # True