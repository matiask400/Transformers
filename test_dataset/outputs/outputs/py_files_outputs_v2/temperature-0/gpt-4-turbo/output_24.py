class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        second.next = first
        current.next = second
        current = first
    return dummy.next

def list_to_nodes(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
inputs = [[1,2,3,4], [], [1]]
expected_outputs = [[2,1,4,3], [], [1]]
for input_list, expected in zip(inputs, expected_outputs):
    input_nodes = list_to_nodes(input_list)
    swapped = swapPairs(input_nodes)
    output_list = nodes_to_list(swapped)
    print(output_list == expected)