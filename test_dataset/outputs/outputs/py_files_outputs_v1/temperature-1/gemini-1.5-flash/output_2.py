class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
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

# Example usage
# Convert input lists to linked lists
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Call the function to add the linked lists
sum_list = addTwoNumbers(l1, l2)

# Convert the output linked list back to a list
result = []
while sum_list:
    result.append(sum_list.val)
    sum_list = sum_list.next

# Print the result
print(result)