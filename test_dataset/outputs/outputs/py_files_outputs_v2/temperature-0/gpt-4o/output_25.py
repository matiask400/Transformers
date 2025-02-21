def reverseKGroup(head, k):
    def reverseLinkedList(head, k):
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head

    count = 0
    ptr = head
    while count < k and ptr:
        ptr = ptr.next
        count += 1

    if count == k:
        reversed_head = reverseLinkedList(head, k)
        head.next = reverseKGroup(ptr, k)
        return reversed_head
    return head

# Helper function to convert list to linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Helper function to create linked list from list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Test cases
input_1 = ([1, 2, 3, 4, 5], 2)
output_1 = [2, 1, 4, 3, 5]
input_2 = ([1, 2, 3, 4, 5], 3)
output_2 = [3, 2, 1, 4, 5]
input_3 = ([1, 2, 3, 4, 5], 1)
output_3 = [1, 2, 3, 4, 5]

# Convert inputs to linked lists
head_1 = list_to_linked_list(input_1[0])
head_2 = list_to_linked_list(input_2[0])
head_3 = list_to_linked_list(input_3[0])

# Apply function
result_1 = linked_list_to_list(reverseKGroup(head_1, input_1[1]))
result_2 = linked_list_to_list(reverseKGroup(head_2, input_2[1]))
result_3 = linked_list_to_list(reverseKGroup(head_3, input_3[1]))

# Verify results
print(result_1 == output_1)
print(result_2 == output_2)
print(result_3 == output_3)