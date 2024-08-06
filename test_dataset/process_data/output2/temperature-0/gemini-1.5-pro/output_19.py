class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
inputs = [
    ([1, 2, 3, 4, 5], 2),
    ([1], 1),
    ([1, 2], 1),
]
outputs = [
    [1, 2, 3, 5],
    [],
    [1],
]

for i in range(len(inputs)):
    head = create_linked_list(inputs[i][0])
    n = inputs[i][1]
    result = remove_nth_from_end(head, n)
    result_list = linked_list_to_list(result)
    print(result_list == outputs[i])