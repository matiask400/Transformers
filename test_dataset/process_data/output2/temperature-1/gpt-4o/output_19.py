class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n + 1):
        first = first.next
    while first is not None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

def list_to_nodes(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def nodes_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Inputs and expected outputs
inputs = [([1,2,3,4,5], 2), ([1], 1), ([1,2], 1)]
expected_outputs = [[1,2,3,5], [], [1]]

# Verify solutions
for (input_list, n), expected in zip(inputs, expected_outputs):
    head = list_to_nodes(input_list)
    output = removeNthFromEnd(head, n)
    output_list = nodes_to_list(output)
    print(output_list == expected)