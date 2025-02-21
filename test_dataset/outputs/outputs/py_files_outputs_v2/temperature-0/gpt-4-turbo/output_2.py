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
        carry, out = divmod(val1 + val2 + carry, 10)

        current.next = ListNode(out)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

def list_to_linked(lst):
    head = ListNode(lst[0])
    current = head
    for number in lst[1:]:
        current.next = ListNode(number)
        current = current.next
    return head

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
inputs = [([2,4,3], [5,6,4]), ([0], [0]), ([9,9,9,9,9,9,9], [9,9,9,9])]
outputs = [[7,0,8], [0], [8,9,9,9,0,0,0,1]]

for i, (inp, out) in enumerate(zip(inputs, outputs)):
    l1, l2 = map(list_to_linked, inp)
    result = addTwoNumbers(l1, l2)
    result_list = linked_to_list(result)
    print(f'Test {i+1}:', result_list == out)