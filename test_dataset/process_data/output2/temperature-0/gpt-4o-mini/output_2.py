class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Example inputs
l1_1 = ListNode(2, ListNode(4, ListNode(3)))
l2_1 = ListNode(5, ListNode(6, ListNode(4)))
output_1 = addTwoNumbers(l1_1, l2_1)

l1_2 = ListNode(0)
l2_2 = ListNode(0)
output_2 = addTwoNumbers(l1_2, l2_2)

l1_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
output_3 = addTwoNumbers(l1_3, l2_3)

# Expected outputs
expected_output_1 = [7, 0, 8]
expected_output_2 = [0]
expected_output_3 = [8, 9, 9, 9, 0, 0, 0, 1]

# Function to convert linked list to list for comparison

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Verify outputs
print(linked_list_to_list(output_1) == expected_output_1)  # True
print(linked_list_to_list(output_2) == expected_output_2)  # True
print(linked_list_to_list(output_3) == expected_output_3)  # True