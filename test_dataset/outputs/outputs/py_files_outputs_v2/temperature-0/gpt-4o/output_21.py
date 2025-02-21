def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next

# Helper function to create linked list from list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to convert list to linked list
def to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
inputs = [([1,2,4], [1,3,4]), ([], []), ([], [0])]
expected_outputs = [[1,1,2,3,4,4], [], [0]]

for i, (l1, l2) in enumerate(inputs):
    l1 = to_linked_list(l1)
    l2 = to_linked_list(l2)
    merged_list = mergeTwoLists(l1, l2)
    output = to_list(merged_list)
    print(output == expected_outputs[i])