class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next

    return dummy.next

def list_to_nodes(lst):
    dummy = ListNode(0)
    cur = dummy
    for number in lst:
        cur.next = ListNode(number)
        cur = cur.next
    return dummy.next

def nodes_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

inputs = [[1,2,3,4], [], [1]]
outputs = [[2,1,4,3], [], [1]]

for i, lst in enumerate(inputs):
    input_head = list_to_nodes(lst)
    expected_output = outputs[i]
    result_head = swapPairs(input_head)
    result_list = nodes_to_list(result_head)
    print(result_list == expected_output)