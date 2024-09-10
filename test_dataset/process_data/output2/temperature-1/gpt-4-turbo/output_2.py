class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1 + val2 + carry, 10)

        current.next = ListNode(out)
        current = current.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return dummy.next

def list_to_nodes(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Test cases
inputs = [([2,4,3], [5,6,4]), ([0], [0]), ([9,9,9,9,9,9,9], [9,9,9,9])]
expected_outputs = [[7,0,8], [0], [8,9,9,9,0,0,0,1]]
results = []

for input_pair, expected in zip(inputs, expected_outputs):
    l1, l2 = map(list_to_nodes, input_pair)
    result = addTwoNumbers(l1, l2)
    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    results.append(result_list == expected)

for result in results:
    print(result)