def reverseKGroup(head, k):
    # Function to reverse k nodes in the linked list
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

# Helper function to create linked list from Python list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to convert linked list to Python list
def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

# Helper function to create linked list from Python list

def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test cases
input_1_head = list_to_linked_list([1, 2, 3, 4, 5])
input_1_k = 2
expected_output_1 = [2, 1, 4, 3, 5]

input_2_head = list_to_linked_list([1, 2, 3, 4, 5])
input_2_k = 3
expected_output_2 = [3, 2, 1, 4, 5]

input_3_head = list_to_linked_list([1, 2, 3, 4, 5])
input_3_k = 1
expected_output_3 = [1, 2, 3, 4, 5]

# Validate outputs
output_1 = linked_list_to_list(reverseKGroup(input_1_head, input_1_k))
output_2 = linked_list_to_list(reverseKGroup(input_2_head, input_2_k))
output_3 = linked_list_to_list(reverseKGroup(input_3_head, input_3_k))

print(output_1 == expected_output_1)  # True
print(output_2 == expected_output_2)  # True
print(output_3 == expected_output_3)  # True
