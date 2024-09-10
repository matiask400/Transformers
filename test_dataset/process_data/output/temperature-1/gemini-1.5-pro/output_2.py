# Definition for singly-linked list.
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

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)

        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

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

# Example usage
input1_l1 = list_to_linked_list([2, 4, 3])
input1_l2 = list_to_linked_list([5, 6, 4])
output1 = linked_list_to_list(addTwoNumbers(input1_l1, input1_l2))  # Output: [7, 0, 8]

input2_l1 = list_to_linked_list([0])
input2_l2 = list_to_linked_list([0])
output2 = linked_list_to_list(addTwoNumbers(input2_l1, input2_l2))  # Output: [0]

input3_l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
input3_l2 = list_to_linked_list([9, 9, 9, 9])
output3 = linked_list_to_list(addTwoNumbers(input3_l1, input3_l2))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]

print([7, 0, 8] == output1)
print([0] == output2)
print([8, 9, 9, 9, 0, 0, 0, 1] == output3)