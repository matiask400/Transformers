# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

def create_linked_list(lst):
    head = None
    tail = None
    for val in lst:
        if head is None:
            head = ListNode(val)
            tail = head
        else:
            tail.next = ListNode(val)
            tail = tail.next
    return head

def compare_linked_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

# Test cases
input_1 = create_linked_list([2, 4, 3])
input_2 = create_linked_list([5, 6, 4])
output_1 = create_linked_list([7, 0, 8])
print(compare_linked_lists(addTwoNumbers(input_1, input_2), output_1))  # Expected: True

input_1 = create_linked_list([0])
input_2 = create_linked_list([0])
output_2 = create_linked_list([0])
print(compare_linked_lists(addTwoNumbers(input_1, input_2), output_2))  # Expected: True

input_1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
input_2 = create_linked_list([9, 9, 9, 9])
output_3 = create_linked_list([8, 9, 9, 9, 0, 0, 0, 1])
print(compare_linked_lists(addTwoNumbers(input_1, input_2), output_3))  # Expected: True